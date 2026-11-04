#!/usr/bin/env python3
"""Original, CPU-only masked-EMA contract example; requires PyTorch.

This is not I-JEPA/V-JEPA reproduction code. No datasets, downloads, files,
distributed collectives, AMP, or statistical anti-collapse claims are involved.
"""

from copy import deepcopy
import json

import torch
from torch import nn
from torch.nn import functional as F


def gather_tokens(tokens, ids):
    """Gather original positions: [B,N,D] and long [B,K] -> [B,K,D]."""
    if tokens.ndim != 3 or ids.ndim != 2 or ids.shape[0] != tokens.shape[0]:
        raise ValueError("Expected tokens[B,N,D] and ids[B,K].")
    if ids.dtype != torch.long or ids.device != tokens.device:
        raise ValueError("IDs must be long tensors on the token device.")
    if ids.numel() == 0 or ids.min().item() < 0 or ids.max().item() >= tokens.shape[1]:
        raise ValueError("IDs must select nonempty, in-range token positions.")
    return tokens.gather(1, ids.unsqueeze(-1).expand(-1, -1, tokens.shape[-1]))


def validate_pair(context_ids, target_ids, batch_size, n_tokens):
    for ids in (context_ids, target_ids):
        if ids.ndim != 2 or ids.shape[0] != batch_size or ids.dtype != torch.long:
            raise ValueError("Each index tensor must have shape [B,K] and dtype long.")
        if ids.numel() == 0 or ids.min().item() < 0 or ids.max().item() >= n_tokens:
            raise ValueError("Masks must be nonempty and in range.")
        ordered = ids.sort(dim=1).values
        if (ordered[:, 1:] == ordered[:, :-1]).any().item():
            raise ValueError("A mask must not duplicate token IDs.")
    if context_ids.device != target_ids.device:
        raise ValueError("Context and target IDs must share a device.")
    if (context_ids.unsqueeze(-1) == target_ids.unsqueeze(-2)).any().item():
        raise ValueError("This masked-prediction example requires disjoint masks.")


class TinyEncoder(nn.Module):
    def __init__(self, n_tokens=8, patch_dim=4, dim=12):
        super().__init__()
        self.patch = nn.Linear(patch_dim, dim)
        self.position = nn.Embedding(n_tokens, dim)
        self.block = nn.TransformerEncoderLayer(
            dim, nhead=3, dim_feedforward=24, dropout=0.0, batch_first=True
        )
        self.norm = nn.LayerNorm(dim)

    def forward(self, patches, ids):
        # Content is gathered BEFORE any token mixing; positions stay original.
        x = self.patch(gather_tokens(patches, ids)) + self.position(ids)
        return self.norm(self.block(x))


class TinyPredictor(nn.Module):
    def __init__(self, n_tokens=8, dim=12):
        super().__init__()
        self.query = nn.Embedding(n_tokens, dim)
        self.attention = nn.MultiheadAttention(dim, 3, dropout=0.0, batch_first=True)
        self.output = nn.Linear(dim, dim)

    def forward(self, context, target_ids):
        query = self.query(target_ids)
        prediction, _ = self.attention(query, context, context, need_weights=False)
        return self.output(prediction + query)


class TinyJEPA(nn.Module):
    def __init__(self):
        super().__init__()
        self.online = TinyEncoder()
        self.predictor = TinyPredictor()
        self.teacher = deepcopy(self.online).requires_grad_(False).eval()

    def predict(self, patches, context_ids, target_ids):
        validate_pair(context_ids, target_ids, patches.shape[0], patches.shape[1])
        return self.predictor(self.online(patches, context_ids), target_ids)

    def loss(self, patches, context_ids, target_ids):
        prediction = self.predict(patches, context_ids, target_ids)
        # Explicit policy for this example: deterministic teacher, no mutable BN.
        self.teacher.eval()
        with torch.no_grad():
            all_ids = torch.arange(patches.shape[1]).expand(patches.shape[0], -1)
            full_target = self.teacher(patches, all_ids).float()
            full_target = F.layer_norm(full_target, (full_target.shape[-1],))
            target = gather_tokens(full_target, target_ids)
        if prediction.shape != target.shape:
            raise ValueError("Prediction and target shapes differ.")
        return F.smooth_l1_loss(prediction.float(), target)


@torch.no_grad()
def update_ema(online, teacher, momentum, did_step):
    """Update complete, unwrapped modules; copy buffers by explicit toy policy."""
    if not 0.0 <= momentum <= 1.0:
        raise ValueError("Momentum must be in [0,1].")
    if not did_step:
        return
    source = dict(online.named_parameters())
    target = dict(teacher.named_parameters())
    if source.keys() != target.keys():
        raise ValueError("EMA parameter names differ.")
    for name, weight in target.items():
        if weight.shape != source[name].shape:
            raise ValueError("EMA parameter shapes differ: " + name)
        weight.lerp_(source[name], 1.0 - momentum)
    source_buffers = dict(online.named_buffers())
    target_buffers = dict(teacher.named_buffers())
    if source_buffers.keys() != target_buffers.keys():
        raise ValueError("EMA buffer names differ.")
    for name, value in target_buffers.items():
        value.copy_(source_buffers[name])


def make_optimizer(model):
    return torch.optim.AdamW(
        list(model.online.parameters()) + list(model.predictor.parameters()),
        lr=1e-3, weight_decay=0.01
    )


def random_step(model, optimizer):
    patches = torch.randn(3, 8, 4)
    ids = torch.stack([torch.randperm(8) for _ in range(3)])
    context_ids, target_ids = ids[:, :4], ids[:, 4:]
    optimizer.zero_grad(set_to_none=True)
    loss = model.loss(patches, context_ids, target_ids)
    if not torch.isfinite(loss).item():
        raise AssertionError("Loss is not finite.")
    loss.backward()
    optimizer.step()
    update_ema(model.online, model.teacher, momentum=0.9, did_step=True)
    return loss.detach(), context_ids, target_ids


def expect_value_error(callback):
    try:
        callback()
    except ValueError:
        return
    raise AssertionError("Invalid input was accepted.")


def main():
    torch.set_num_threads(1)
    torch.manual_seed(17)
    model = TinyJEPA()
    optimizer = make_optimizer(model)
    checks = []

    tags = torch.arange(16).reshape(2, 8, 1)
    picked = gather_tokens(tags, torch.tensor([[6, 2], [4, 0]]))
    torch.testing.assert_close(picked.squeeze(-1), torch.tensor([[6, 2], [12, 8]]))
    expect_value_error(lambda: gather_tokens(tags, torch.tensor([[8], [0]])))
    expect_value_error(lambda: gather_tokens(tags, torch.empty(2, 0, dtype=torch.long)))
    expect_value_error(lambda: validate_pair(
        torch.tensor([[0, 0]]), torch.tensor([[1]]), 1, 8))
    expect_value_error(lambda: validate_pair(
        torch.tensor([[0, 1]]), torch.tensor([[1, 2]]), 1, 8))
    checks.append("gather identity and mask rejection")

    for name, source in model.online.state_dict().items():
        torch.testing.assert_close(source, model.teacher.state_dict()[name])
    optimizer_ids = {id(p) for group in optimizer.param_groups for p in group["params"]}
    assert all(not p.requires_grad and id(p) not in optimizer_ids for p in model.teacher.parameters())
    checks.append("teacher copy, freeze, and optimizer exclusion")

    patches = torch.randn(2, 8, 4)
    context_ids = torch.tensor([[6, 0, 2], [1, 7, 3]])
    target_ids = torch.tensor([[1, 7, 4], [0, 2, 6]])
    changed = patches.clone()
    hidden = torch.ones(2, 8, dtype=torch.bool)
    hidden.scatter_(1, context_ids, False)
    changed[hidden] = 100.0
    with torch.no_grad():
        torch.testing.assert_close(
            model.predict(patches, context_ids, target_ids),
            model.predict(changed, context_ids, target_ids), rtol=0, atol=0
        )
    checks.append("hidden-content counterfactual")

    optimizer.zero_grad(set_to_none=True)
    model.loss(patches, context_ids, target_ids).backward()
    assert all(p.grad is None for p in model.teacher.parameters())
    for module in (model.online, model.predictor):
        grads = [p.grad for p in module.parameters() if p.requires_grad]
        assert all(g is not None and torch.isfinite(g).all().item() for g in grads)
        assert sum(g.abs().sum().item() for g in grads) > 0
    checks.append("online/predictor gradients and teacher isolation")

    before = deepcopy(model.teacher.state_dict())
    optimizer.step()
    update_ema(model.online, model.teacher, 0.9, did_step=True)
    for name, updated in model.teacher.state_dict().items():
        expected = 0.9 * before[name] + 0.1 * model.online.state_dict()[name]
        torch.testing.assert_close(updated, expected)
    before = deepcopy(model.teacher.state_dict())
    update_ema(model.online, model.teacher, 0.9, did_step=False)
    for name, weight in model.teacher.state_dict().items():
        torch.testing.assert_close(weight, before[name], rtol=0, atol=0)
    checks.append("EMA formula and explicit skipped-step policy")

    # In-memory boundary after an update; no disk/dataloader guarantee implied.
    snapshot = deepcopy({"model": model.state_dict(), "optimizer": optimizer.state_dict(),
                         "rng": torch.get_rng_state()})
    expected_loss, expected_context, expected_target = random_step(model, optimizer)
    resumed = TinyJEPA()
    resumed.load_state_dict(snapshot["model"], strict=True)
    resumed_optimizer = make_optimizer(resumed)
    resumed_optimizer.load_state_dict(snapshot["optimizer"])
    torch.set_rng_state(snapshot["rng"])
    actual_loss, actual_context, actual_target = random_step(resumed, resumed_optimizer)
    for actual, expected in [(actual_loss, expected_loss), (actual_context, expected_context),
                             (actual_target, expected_target)]:
        torch.testing.assert_close(actual, expected, rtol=0, atol=0)
    for name, actual in resumed.state_dict().items():
        torch.testing.assert_close(actual, model.state_dict()[name], rtol=0, atol=0)
    checks.append("randomized next-update resume equivalence")
    print(json.dumps({"status": "passed", "torch": torch.__version__, "device": "cpu",
                      "checks": checks}, indent=2))


if __name__ == "__main__":
    main()
