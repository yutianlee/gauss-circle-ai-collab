# Round235 shared exact controls

Campaign gc-signed-sixth-dispersion; conductor; diagnostic_only. Starting graph dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306. The bounded shared controls supplement analytical proofs and never certify S6 or any asymptotic estimate. No numerical sweep, fitting or extrapolation was performed.

## Code, execution and pass rule

Wolfram Language evaluator ran wolfram_primary.wl (30-second bound), wolfram_correction.wl (20-second bound), wolfram_phase.wl (15-second bound), and wolfram_grouping.wl (20-second bound). Exact returned text is archived in the corresponding *_response.json files. Actual calls each completed in about8 seconds. No external formatted-result link was returned. The initial Wolfram context request failed with MCP -32603 Internal error; it supplied no evidence. Evaluator computations succeeded.

Local independent reproduction: `python rounds/codex-managed/gc-signed-sixth-dispersion/controls/exact_local_controls.py`. Code uses integer arithmetic and Python Fraction, including an integer-square-root rational enclosure with denominator10^20. The pass rule is that every explicitly named assertion in exact_local_controls.json is true; the script exits on failure. All passed. Decimal output is display only, not the inequality certificate.

## Results and disclosed corrections

1. beta<129/1000 exactly, so 6beta+193/500<29/25. The positive margin is 387/500-6beta=0.000201888311263119...; a strict rational enclosure is archived locally. The sixth exponent is47/125+1/100=193/500 and the moving-width endpoints are151/250 and99/125.
2. The first Wolfram query accidentally included an unrelated rational expression `(1+1/(29/25))/(4+2/(29/25))`; its output27/83 is correct arithmetic for that expression but is NOT the sharp-restoration formula. The correction explicitly checks the relevant formula `(29/25+7)/26=102/325`. Both queries and outputs are retained. No argument uses27/83.
3. The exact r2 divisor-hyperbola identity holds for all integers1..256 against a direct independent sum-of-two-squares count locally. Omitting the quotient-character branch fails at n=3 (actual0, truncated4). Omitting the square correction fails at n=9 (actual4, uncorrected0). Finite success is a control of the separately proved algebraic identity only.
4. chi4(j)=(e(j/4)-e(-j/4))/(2i) agrees on all four residues. Both leading and second Bessel product-to-sum phase identities return0 exactly. The analytical reports rederive these identities without numerical input.
5. Exact reciprocal-fraction grouping uses H=3, D=19 and a flat Fourier packet on[1,2] purely to test coefficients. The direct and grouped expressions agree at136 nonzero positive frequencies; no reduced denominator is2 mod4. Wolfram emitted a pre-evaluation `Symbol::undefined2` warning about the assigned globals HH/DD, but completed with `{True,136,{}}`; independent local rational arithmetic confirms all three results. This warning is retained in the raw output. The flat packet is not claimed to satisfy the smooth asymptotic theorem hypotheses.
6. The local ordered-distinct-six Newton polynomial agrees with explicit enumeration on five fixed real signed/zero/constant test vectors. This is a regression control for accepted233, not a new proof of its infinite-family application.

## Analytical controls and limits

The isolated report must prove the exact progression cutoffs, positive-index tails and signed-versus-absolute countercontrol. The actual bridge report must pay all harmonics, repeated classes, two-term Bessel remainder, zero and sum phases, moving width and endpoints. The arithmetic report must retain both character branches, moving hyperbola cutoff and the square packet. Independent reviews bind their final hashes. None of these computational checks supplies the unproved nonpaired signed sixth-order arithmetic estimate.

The blind brief was sanitized before the isolated agent was spawned: it contains only its task identifier, read restrictions and output contract. The general template's application text was removed before any blind access. The isolated statement is the sole mathematical input to that task. Initial reports will be frozen before expanded-context nonauthor reviews.
