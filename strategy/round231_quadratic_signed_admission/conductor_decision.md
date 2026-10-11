# Round231 signed polynomial admission decision

Conductor, 11 October 2026. Starting and retained graph SHA256: a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b. This closes a bounded prelaunch test for Round231, not an analytic campaign or a successor round. The final closure timestamp, evidence hashes and mechanical checks are in controls/closure_validation.json and controls/final_evidence_hashes.json.

## Decision

Retain two actual signed inputs and a newly paid complete component. Do not admit a claim of improved complete moments from them. The best accepted full bound remains

    M12(B_T) <<_epsilon T^(10beta+epsilon),
    10beta=1.289663519481...,

against the still open target29/25=1.16. No pointwise exponent, quarter theorem, M1/M2/M9 obligation or endpoint is improved. The graph and proof draft are unchanged; no State Patch is applied.

## The useful advance

The primary source Matomaki--Shao--Tao--Teravainen, *Higher uniformity I*, arXiv2204.03754v4, Theorem1.1(iii) and PropositionA.3, explicitly controls the actual difference r2-r2sharp against arbitrary fixed-degree polynomial phases, with a positive power saving. This is a valid arithmetic input, not a multiplicative-character analogy or merely a logarithmic estimate. Source and full application audit: reports/quadratic_source_audit.md; primary https://arxiv.org/html/2204.03754v4 .

Quadratic Taylor patches miss its positive short-interval margin at and below N~T^(2/3). Quartic patches of length H4~N^(9/10)T^(-1/5) repair that premise over the entire complement of the affordable norm head X0=T^(52/125). At its first shell, the length exponent is109/260, exceeding1/3 by67/780. A fixed source margin1/25 is legal up to the Schwartz truncation T^(3/2). The exact phase residual has bounded variation; it is retained.

The explicit patch-dependent approximant is now paid. Regrouping its sums by divisor across each full shell makes both cutoff supports single intervals. The logarithmic multiplier has bounded total variation including every patch jump. The accepted exponent-pair input on each complete divisor fibre then yields

    |S_N^sharp(R)| << T^epsilon (1+N/T)^(-L)
                     [T^(13/84)N^(-103/840)+T^-1 N^(-1/4)].

There is no factor equal to the number of patches. Summing all retained shells gives

    sup_R |S^sharp(R)| << T^(5447/52500+epsilon),
    M12(S^sharp) << T^(3044/2625+epsilon)
                 = T^(29/25-1/2625+epsilon).

This complete component includes both divisor ranges, chi4(n/d), the varying local cutoffs, partial endpoints and the prescribed cosine projection. Its coefficients are fixed as R varies; the generic distribution proof applies to them with their own proved supremum. The infinite actual tail is paid separately and all mixed terms are preserved by the norm inequality. The independent review proves the same main estimate without reading this derivation. See conductor_type_i_main.md and reviews/type_i_main_and_resonance_review.md.

## What remains unproved

For the exact decomposition

    B_T = H_X0 + S^sharp + V + actual far tail,

the norm head costs29/25, the explicit main costs3044/2625, and the tail is negligible. The remaining V contains the actual signed arithmetic residual on every retained norm. Consequently, at any exponent b>=29/25, an upper bound M12(V)<<T^(b+epsilon) is equivalent to the same complete-wave upper bound, through two applications of the L12 triangle inequality. This is a useful ownership statement; equivalence is not an estimate for V.

The audited source supplies a fixed kappa>0 and a residual ceiling T^(1/4-kappa+epsilon). Its numerical value is not specified sufficiently to restore a gain. The resulting certificate has exponents

    1, 10(1/4-kappa), 1+(20/13)(1/4-kappa).

That certificate needs kappa>1/4-beta=0.121033648... for strict improvement over10beta, and kappa>=73/500 for29/25. These are requirements of this particular ceiling/distribution restoration, not necessary conditions on every possible signed moment argument. No value of kappa is guessed from the existence of a positive source constant.

The independent source review also records a lawful fallback: V=B_T-H_X0-S^sharp-tail inherits the actual ceiling T^(beta+epsilon), because the explicitly paid head and main have smaller supremum exponents. Thus use min(beta,1/4-kappa) as the residual ceiling. This justifies retaining the old complete bound; it supplies no new gain when the source's numerical saving is insufficiently known. It does not transfer an actual supremum to an arbitrary coefficient mask.

The almost-all sequel, arXiv2411.05770v2 Theorem1.1(v), does not directly supply an r2 theorem or the needed power and exceptional-set payment. Its interval-start exceptions cannot be reinterpreted as exceptional physical radii. This is the second and final audited source application; no exhaustive literature claim is made.

## Separate exact estimates and controls

The arithmetic analyst proved, for actual r2, any odd primitive conductor and arbitrary real linear coefficient,

    |sum_(n in I) r2(n)e(an²/q+lambda n)|
       << tau(q)log²(2Nq)[H/sqrt(q)+sqrt(Nq)],

where I is a half-open subinterval of (N,2N] of length at most H. Its finite hyperbola decomposition, real-slope completion, degenerate fibre conductors and rational main are independently reviewed. On quadratic Taylor patches with N<=T, H<=sqrt(N), so the completion cost in this bound does not certify a useful improvement. This is not a lower bound on the signed sum.

An isolated analyst proved the complete finite quadratic Gram formulas. The centered norm-density rows remain almost parallel; their orthogonal common component carries the fraction(p-1)/p of each row's energy. The residual chirps decorrelate only after explicitly removing that component, which must be separately restored. This does not obstruct the higher-uniformity decomposition that now pays its own main.

The conductor's actual-r2 resonance lemma independently passes: for any fixed2/5<sigma<2/3, some integer-centered patch has mass comparable to its length, and a real radius R=8k m^(3/2) makes its quadratic Taylor phase integral at integer norms. Its physical cosine sum has coherent negative sign. This refutes a uniform uncentered local square-root bound. It makes no claim about a prescribed partition, the complement, overlap of exceptional radii, or the full moment.

All finite diagnostics were independently reproduced:3354 transforms and3354 Gram entries over ten primes, plus a70-digit actual resonant-patch phase check. These are diagnostic_only; every asymptotic conclusion rests on analysis. The numerical allocation stayed below5 percent.

## Review and preservation

Three initial reports are frozen. The important finite lemma was derived with statement-only isolation; the Type-I main received an additional independent derivation. Nonauthor reviews cover the Type-I/phase/source seam, the source and residual restoration, the elementary quadratic bound, and the finite Gram algebra. A bibliographic author-list slip in the main review was corrected before closure; the bounded-T approximant convention was made explicit. No mathematical claim was accepted by vote.

The required reviews are:

- reviews/conductor_finite_row_review.md;
- reviews/type_i_main_and_resonance_review.md;
- reviews/source_restoration_seam_review.md;
- reviews/quadratic_bound_seam_review.md.

Closure requires their final PASS verdicts, unchanged protected evidence, valid graph/campaign checks and final hashes. Only the five research-status metadata files listed in the closure record are updated. The401-node graph, proof draft, validation matrix, closed230 manifest, round ledger, accepted kernels, earlier admission packets and legacy archives remain unchanged.

## Next admission boundary

Analytic231 remains pending_design. A useful next input must quantitatively improve the actual residual V using joint or averaged cancellation, a sufficiently strong audited source exponent, or another fully restored arithmetic estimate. Reproving the local identity, polynomial length repair, paid Type-I main, or raw finite-row decorrelation alone does not satisfy that gate. No automatic successor or new numbered round is launched.
