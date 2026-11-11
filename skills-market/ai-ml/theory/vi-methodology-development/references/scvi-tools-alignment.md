# scvi-tools implementation and community alignment

Use for a scvi-tools-based method or community-facing package. The mathematical specification remains authoritative for scientific meaning; the framework supplies data, training, persistence, and interface conventions. The engineering recommendations below are this skill's synthesis unless explicitly labeled upstream requirements.

## Version and ownership first

Evidence checked **2026-10-22**:

- Latest release returned by the official release endpoint was [scvi-tools 1.5.1](https://github.com/scverse/scvi-tools/releases/tag/1.5.1), published 2026-09-10.
- Source inspection used main commit `d85bb10e5a8cba6cf8e32ed56a2433b855f325cc`, not an asserted release-tag commit. Its [metadata](https://github.com/scverse/scvi-tools/blob/d85bb10e5a8cba6cf8e32ed56a2433b855f325cc/pyproject.toml) declares Python >=3.12 and ordinary tests on 3.12–3.14. Recheck these when creating an environment.
- [ResolVI's migration notice](https://docs.scvi-tools.org/en/stable/user_guide/models/resolvi.html) says it moved to scVIVA-Tools starting with scvi-tools 1.5 and is no longer maintained in scvi-tools. The latest checked scVIVA release was [0.1.7](https://github.com/YosefLab/scviva-tools/releases/tag/v0.1.7); its inspected main commit was `b7e3cb21cb04496b9f9d516f863b07ecd9df120c`.

For implementation, inspect the selected environment's package versions and installed source, then use matching documentation/source tags. Record which APIs are verified. Do not silently mix a paper's configuration, a legacy implementation, a current main branch, and stable docs. A class still present in `scvi.external` can be a legacy entry point. Resolve actual ownership before extending it.

## Choose the distribution route

An independently distributed package using scvi-tools is a supported architecture; the official [development index](https://github.com/scverse/scvi-tools/blob/d85bb10e5a8cba6cf8e32ed56a2433b855f325cc/docs/tutorials/index_dev.md) links [simple-scvi](https://github.com/scverse/simple-scvi) as an example. Use its architecture rather than old dependency pins.

For an evolving method, an independent package can keep dependencies and maintenance with its authors. A contribution to `scvi.external` or shared core components is a separate upstream choice, with maintainer-dependent scope and acceptance. “External package” and the upstream `scvi.external` namespace are not interchangeable. No universal rule requires every VI method to join either scvi-tools or scVIVA-Tools.

## Map mathematical responsibilities to the framework

| Method layer | Typical scvi-tools mechanism | Model-specific obligation |
|---|---|---|
| Data schema | `setup_anndata`, `AnnDataManager`, registered fields; MuData setup when supported | Correct measurement layer, masks, categories, covariates, feature order and observation identity |
| Probabilistic module | `BaseModuleClass` and distribution/network components | `_get_inference_input`, `inference`, `_get_generative_input`, `generative`, `loss` consistent with p and q |
| Objective reporting | `LossOutput` | Correct scalar `loss`, per-unit reconstruction/local KL, global KL and named extra metrics |
| User interface | `BaseModelClass` plus appropriate mixins | Setup validation, constructor state, training, persistence and explicit posterior queries |
| Optimization | Appropriate training plan and training mixin | Optimizer groups, schedules, auxiliary/adversarial updates and scaling |
| Pyro alternative | `PyroBaseModuleClass`, model/guide, matching Pyro training plan/mixins | Sample/parameter sites, plates, enumeration, subsampling and guide semantics |

These API roles are documented in [data handling](https://docs.scvi-tools.org/en/stable/tutorials/notebooks/dev/data_tutorial.html), [probabilistic modules](https://docs.scvi-tools.org/en/stable/tutorials/notebooks/dev/module_user_guide.html), and [high-level models](https://docs.scvi-tools.org/en/stable/tutorials/notebooks/dev/model_user_guide.html). Confirm exact signatures against the selected version.

For a conventional amortized model, the direct module route often makes the objective easiest to inspect. Use Pyro when its probabilistic machinery helps express the actual hierarchy or inference algorithm; it is an alternative route, not an extra required layer. Do not mix their training conventions without an explicit design.

### Data and persistence contract

Register the measurements matching the likelihood: raw counts for a count model, an explicitly declared transformed scale for a continuous model. Registration does not replace preprocessing design. Avoid generalized “all models use counts” assumptions. Persist feature order, category encodings, preprocessing parameters, masks/panel definitions and graph construction settings where required.

Use manager-based validation and loader access rather than private hard-coded AnnData keys. Handle multiple models/data objects without silently reusing a stale registry. For unseen categories specify whether to reject, initialize, or adapt them; never silently map a new category to a known one. Separate ordinary inference on new data from query-time model adaptation.

Save constructor/setup arguments and learned state through the target framework's supported mechanisms. If local MAP/variational parameters are indexed by observations, explicitly serialize their ID mapping and define behavior for reordered or new observations. Save/load success alone does not establish that a posterior query is unchanged: test that output contract.

### Module and training contract

Return the output keys and dimensions required by the mixins actually used. A custom decoder need not support a stock normalized-expression or differential-expression mixin; inherited methods can impose incompatible likelihood semantics.

The supplied scalar `LossOutput.loss` drives optimization; its other fields serve reporting and monitoring. Ensure reported ELBO components correspond to the intended unweighted/weighted quantities. Do not assume populating a KL field adds it to the optimization loss. Verify local/global scaling and the training plan's dataset-size handling. See the [pinned base module](https://github.com/scverse/scvi-tools/blob/d85bb10e5a8cba6cf8e32ed56a2433b855f325cc/src/scvi/module/base/_base_module.py).

For Pyro, verify plates, batch-size scale factors and parameter-store ownership. Delta guide sites describe point estimates; they do not establish fully Bayesian uncertainty. Models with neighbor reuse, multiple optimizers, or asymmetric gradients need an explicit training plan rather than assuming a standard plan expresses the algorithm.

Current source offers optional `plan_config` and `trainer_config`; legacy kwargs override corresponding config values. Match the config class to the plan (ordinary, semi-supervised, adversarial, or Pyro) and log the resolved settings. This avoids reporting a configuration different from the one executed. See [training configuration](https://github.com/scverse/scvi-tools/blob/d85bb10e5a8cba6cf8e32ed56a2433b855f325cc/docs/user_guide/use_case/training_configuration.md).

## Modern features: choose and verify

Maintain a small capability table: **needed / inherited / implemented / verified / unsupported**, with evidence and limits. Inheritance is not verification. Choose features for the research and deployment setting, not for a checklist score.

| Capability | When useful | Verification that matters |
|---|---|---|
| CPU/GPU, mixed precision, compile | Demonstrated compute bottleneck | Eager correctness first; finite gradients, stable probabilities, equivalent query behavior and measured total cost |
| Distributed training | Data throughput warrants multiple devices | Sampling, local/global reduction, shared/global state, graph context, checkpoint and validation equivalence |
| Sparse/backed/custom streaming loaders | Input size or I/O exceeds practical memory | Registry, feature/category order, IDs, split semantics and equivalence to in-memory loading |
| scArches/reference mapping | New conditions should adapt while retaining a reference | Architecture compatibility, parameter freeze mask, category expansion and reference stability |
| Minification/cached inference | Storage or repeated-query costs matter | Which observations/posterior summaries remain, supported queries, and agreement with full data |
| Autotuning and tracking | Several justified model choices need comparison | Fixed selection metric, validation data, label access, search budget, resolved configuration |
| Posterior criticism/reporting | Diagnostics match the observation model | Correct predictive sampler, measurement support and claim-relevant summaries |
| Model hub/sharing | Reuse by others is requested | Reconstructable software/schema, output definitions, limitations and separate authorization for upload |

Official starting points: [custom loaders](https://github.com/scverse/scvi-tools/blob/d85bb10e5a8cba6cf8e32ed56a2433b855f325cc/docs/user_guide/use_case/custom_dataloaders.md), [training configuration including compile](https://github.com/scverse/scvi-tools/blob/d85bb10e5a8cba6cf8e32ed56a2433b855f325cc/src/scvi/train/_config.py), [transfer learning](https://github.com/scverse/scvi-tools/blob/d85bb10e5a8cba6cf8e32ed56a2433b855f325cc/docs/user_guide/background/transfer_learning.md), [saving/loading](https://github.com/scverse/scvi-tools/blob/d85bb10e5a8cba6cf8e32ed56a2433b855f325cc/docs/user_guide/use_case/saving_and_loading_models.md), [tuning](https://github.com/scverse/scvi-tools/blob/d85bb10e5a8cba6cf8e32ed56a2433b855f325cc/docs/user_guide/use_case/hyper_parameters_tuning.md), [criticism](https://github.com/scverse/scvi-tools/blob/d85bb10e5a8cba6cf8e32ed56a2433b855f325cc/docs/user_guide/use_case/scvi_criticism.md).

Custom loader and backend support varies by model. Ordinary distributed data parallel training replicates model parameters; it does not pool GPU parameter memory ([PyTorch DDP documentation](https://docs.pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html)). Do not promise compile, DDP, minification, or transfer support for custom guides or indexed local state without checking them. Preserve the scientific objective when adding performance features.

## Community requirements versus recommendations

The checked [upstream contribution guide](https://github.com/scverse/scvi-tools/blob/d85bb10e5a8cba6cf8e32ed56a2433b855f325cc/docs/developer/code.md) accepts code through PRs, requires tests for new features/fixes, and requires public functions/classes to have NumPy-style docstrings. It asks for API-reference updates, changelog entries and informative PR descriptions. Follow repository lint/format rules. Type hints, prior issue discussion, Hatch, and local hooks are recommendations; they are not extra permission gates. These are upstream conventions, not a claim that every standalone package must use identical tooling.

Current tooling uses Hatch/uv environments, Ruff (line length 99), pytest, Sphinx with warnings treated as errors, and pre-commit-compatible checks runnable with `prek`. Read the target's metadata and CI before adopting commands. For the inspected source, examples are `hatch test tests/test_my_change.py`, `hatch run docs:build`, and `prek run --all-files`. Run focused tests first and then relevant required checks; hardware, internet, and optional suites are selected according to supported behavior. Do not impose a new universal mypy or all-hardware gate.

For a reusable method, prepare these concrete deliverables as appropriate:

- A minimal setup → train → query → save/load example with a small fixture or public data reference.
- A mathematical specification, input-scale contract, query semantics, uncertainty limits, and supported capabilities.
- Tests for the actual scientific and software invariants: masks, feature/category identity, local parameter IDs, finite training, save/load, and new-data behavior; claim-specific scientific evaluation remains separate.
- Reproducible configuration and dependencies; focused API docs; expected runtime/memory; known failure cases and limitations.

Tutorials are linked through the separate [scvi-tutorials repository](https://github.com/scverse/scvi-tutorials); editing a tutorial and updating a submodule reference are distinct changes. Prepare reviewable local work within the user's scope. Community alignment does not itself authorize issue messages, PR publication, uploads, or external contact.
