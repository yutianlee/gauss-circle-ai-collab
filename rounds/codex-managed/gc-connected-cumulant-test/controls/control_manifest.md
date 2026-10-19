# Round234 exact controls

All mathematical computations in this round are **diagnostic_only**. Analytical/algebraic reasoning received at least95% of effort; no numerical radius scan or asymptotic fit was run.

The user selected Wolfram. A semantic context call was used for tool orientation, and its generated topic summaries were not mathematical premises. The [Wolfram MomentConvert documentation](https://reference.wolfram.com/language/ref/MomentConvert.html) identifies the symbolic conversion checked here. No external analytic theorem is imported.

- `wolfram_checks.wl`: exact integer-partition multiplicities and cumulants at orders2..12; all eight proper partitions of12 with block sizes>=3; balanced constant-family controls; zero cumulants for deterministic variables.
- `wolfram_result.json`: complete Wolfram evaluator response, time constraint30 seconds, no formatted result URL returned. All11 coefficient comparisons and11 constant-cumulant checks pass; the maximum disconnected absolute exponent is9/4, at shape(9,3).
- `exact_local_controls.py`: independent Python integer-polynomial cumulant recurrence versus partition formula, exact rational budget and balanced-family reproduction, plus direct permutation sums versus independent equality-partition expansions on two six-position/two-radius cases.
- `exact_local_controls.json`: local output. Both multiradius tests pass, with signed values-560 and-23120; each checks all203 partitions of six positions. The three balanced12 controls at N=12,24,48 match Wolfram exactly.

Reproduction command: `python rounds/codex-managed/gc-connected-cumulant-test/controls/exact_local_controls.py`. This uses standard-library integer and rational arithmetic; there is no floating precision or random seed. Run2026-10-12 Asia/Shanghai, exit0.

Pass criterion: all independent polynomial dictionaries agree exactly; all control sums and rational exponents agree; constants have zero cumulants above first order. Outcome: PASS. These finite checks do not establish(C1), the infinite-harmonic lower bound, or any complete improved circle estimate. Those require the proofs and independent seam reviews.

The isolated report's Walsh-character counterfamily is proved analytically and is not claimed to be an actual circle-coefficient example. Its proof is reviewed separately; no finite experiment is substituted for its uniform statement.

The actual-certificate analyst additionally made one exact Wolfram call and a local rational reproduction, both fully archived as code and output inside its frozen report. It checks the common-harmonic rational bound, the23/24 squarefree-removal budget, all eight partition shapes, and the conditional102/325 restoration. The conductor's local script independently reproduces these newly supplied rational checks as well. This second computation remains within the same5% diagnostic budget; it imports no asymptotic theorem.

The signed-remainder analyst's frozen report archives a separate six-position mixed-radius control on seven labels: all5040 distinct assignments and the203-term partition expression equal-68112. Its first Wolfram expression had a syntax/binding error; the report discloses this and archives the repaired code and successful output. The conductor independently reproduced the final exact value in the local script. The failed expression supplied no mathematical evidence. These brief finite calls, including the repair, remain within the5% overall computation allocation.
