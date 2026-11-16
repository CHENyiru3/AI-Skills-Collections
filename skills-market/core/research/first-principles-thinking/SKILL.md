---
name: first-principles-thinking
description: Reason from first principles (第一性原理, 从根本分析) when explicitly requested, or when a research or design decision depends on a disputed premise, what the data can identify, or whether a proposed component is necessary. For routine factual explanations, use the ordinary response unless the user asks for a first-principles derivation.
metadata:
  version: "0.3.0"
---

# First Principles Thinking

1. **Define the target.** For a concept, identify what must be present for it to apply
   and test the definition against a nearby case. For research or design, name the claim
   or decision, the unit and setting, and what would count as success. If a metric is a
   proxy, state which part of the claim it tests. For prediction, specify the
   information available at use time. For intervention, specify what changes, the
   comparison, and the outcome.
2. **Separate premises by status.** Distinguish definitions and logical or mathematical
   consequences, directly supported observations, binding constraints, and modeling
   assumptions or hypotheses. State the scope of an observation. Trace the conclusion to
   the few premises that could change it. Use prior work to check empirical premises and
   generate alternatives. Treat an analogy as a candidate explanation that needs its own
   evidence.
3. **Check what the evidence can distinguish.** Seek two plausible explanations that fit
   the same observations yet imply different answers. If both fit, name the assumption,
   independent measurement, or comparison that would separate them. For modeling,
   inspect which shortcuts the measurement process, available inputs, or split permits.
   If the data support prediction and the desired conclusion is causal, report the
   predictive result and state what would identify the causal effect.
4. **Derive a minimal solution under the stated premises.** Start with the strongest
   simple baseline that addresses the same target. For each proposed component, name the
   role it serves, whether another component could serve that role, and what should
   happen when the component is removed or replaced. Distinguish the mathematical role
   from one implementation and from a convenient default. Add complexity when a baseline
   fails a relevant requirement or a controlled comparison shows a gain worth its cost.
5. **Specify what would change the conclusion.** Choose a feasible, discriminating check
   and state how its outcomes would affect the decision. Match the check to the claim.
   An ablation can test a component’s contribution under a matched evaluation. A causal
   claim needs assumptions or a design that identifies the specified effect. When
   evidence is missing, give the strongest conditional conclusion and identify the next
   observation that would resolve the decision.

Lead with the answer and show the reasoning the user needs to verify it. For a small
conceptual question, a short derivation and a boundary case can suffice. For a
consequential research choice, state the decisive premise, the strongest alternative,
and the result that would change the recommendation. Scale the depth to the decision and
avoid a fixed report template.
