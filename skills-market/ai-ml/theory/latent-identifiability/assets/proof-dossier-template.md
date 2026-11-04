# Identifiability dossier: [research model]

Status: [proved under stated assumptions / proof sketch / open gap / disproved as stated / not assessed]

Verification: [self-review / independent review / machine-checked, with scope]

## Scientific target and observable information

State the scientific mechanism, the mathematical claim, and the proposed contribution separately. Specify observed and latent variables, known design/graph, sampling unit, and the exact observable law. Distinguish the population question from a finite-data objective.

## Model class

Give the generative factorization, noise kernel and nuisance parameters, dimensions, supports, function classes, regularity, and parameter restrictions. State how the model induces the observable law. Record checks of normalizers, compatibility, and any valid nondegenerate example.

## Symmetries and target equivalence

Define admissible transformations and the target equivalence relation or invariant functional. State which semantic interpretations survive those transformations. Record at least the relevant symmetry checks, including rejected transformations and why they are inadmissible.

## Assumption ledger

| ID | Mathematical statement and quantifiers | Why scientifically plausible | Lemma using it | Enforced, encouraged, or assumed | Failure mode |
|---|---|---|---|---|---|

Distinguish necessary conditions from sufficient conditions selected for this proof. Identify any assumptions involving both true and candidate representations.

## Candidate theorem

State the admissible class, quantified observational equality, conclusion, and whether it is global, local, generic, or almost everywhere. Make the direction and strength of every transformation explicit.

## Dependency graph and proof

List lemmas in dependency order. For each: statement; actual assumptions; proof; external theorem used with locator; and status. Explain the difficult cancellations or rank arguments. Mark unresolved steps locally rather than hiding them in a final disclaimer.

## Attempts to falsify the claim

| Attack | Model satisfying retained assumptions | Observable-law comparison | Target comparison | Result |
|---|---|---|---|---|

Separate analytic counterexamples from numerical checks and unsuccessful searches. If the theorem changed, retain the reason for the narrower statement.

## Connection to the implemented estimator

| Theoretical requirement | Actual implementation/data condition | Evidence | Gap or implication |
|---|---|---|---|

Assess only relevant bridges: variational inference, optimizer, noise specification, sample dependence, dimension choice, posterior means, and downstream invariance. If causal effects are claimed, define interventions, adjustment, support, and the estimand computed by the actual formula.

## Strongest justified statement and open work

State what is established, what remains unproved, and the next lemma or counterexample that would change the conclusion. Do not replace an unresolved theorem with an empirical result.

## Source ledger

| Source | Exact result used and locator | Statement inspected? | Conditions matched | Remaining uncertainty |
|---|---|---|---|---|
