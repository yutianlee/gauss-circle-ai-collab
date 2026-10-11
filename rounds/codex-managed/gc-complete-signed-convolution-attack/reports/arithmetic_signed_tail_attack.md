# Round 203: complete signed tail through the divisor identity

Campaign: `gc-complete-signed-convolution-attack`. Task: `arithmetic_signed_tail_attack`. Role: discovery, selected-context access. Generated: 2026-09-23. Starting graph SHA-256: `abc88f6cd29d757b880037b6f600b802a22ac4b57fcce40662205150f3ed8ceb`. Candidate evidence only. This report was completed before reading any sibling or conductor calculation. Effort: 100 percent analytical/algebraic; no experiment or external theorem import.

## 1. Result: a complete arithmetic transformation, with a classical return

The exact divisor identity and one-dimensional Poisson summation transform each smooth product box into an explicit signed sum near integer products at height (R^2). The character remains present. The leading transformed phase is

\[
 e\left(\frac{R^2d}{4k}\right),
 \qquad k\asymp\frac{RD}{\sqrt N},\quad d\asymp D,
 \qquad N=DM.
 \tag{1}
\]

The two character branches detect (R^2\) near products (k(4\ell\pm1)). Summing their geometric cancellation and then using the elementary divisor bound gives, uniformly on the physical window,

\[
 |H_{D,M}(R)|\ll_\varepsilon T^\varepsilon
 \min\{N^{1/4},T^{1/2}N^{-1/2}\}.
 \tag{2}
\]

All upper tails, the sharp lower endpoint and the Poisson/stationary-phase error are restored below. The balance in (2) is (N=T^{2/3}), and summing gives (T^{1/6+\varepsilon}) for the normalized oscillation, the classical circle exponent (1/3) after amplitude restoration. Combining (2) with its actual second moment gives

\[
 \int\chi(R/T)^2|H_{T,>U}(R)|^{12}dR
 \ll_\varepsilon T^{7/3+\varepsilon},
 \qquad
 \|K_T*\mu_{T,>U}^{*6}\|_2\ll_\varepsilon T^{7/6+\varepsilon}.
 \tag{3}
\]

This is an explicit complete bound, but is weaker than the inherited benchmark and far weaker than the target. The new transformation supplies **no exponent improvement**. The restricted stopping point is taking the absolute sum over the dual (k)-packets after using the character within each packet. It does not show that further cancellation in the complete signed packet sum is impossible.

## 2. Exact statement and hypotheses

Let (T\ge2) be real, (U=\lfloor T^{1/2047}\rfloor), and use the fixed real even Schwartz function (\Psi) and fixed nonnegative (\chi\in C_c^\infty((0,\infty))) in the frozen strategy. Write (w=\chi^2), so (R\asymp T) on its support. Put

\[
 H_{T,>U}(R)=\sum_{n>U}r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
                 \cos(2\pi R\sqrt n-3\pi/4).
 \tag{4}
\]

No positivity of (\Psi) is assumed. We use (e(t)=\exp(2\pi it)) and exactly

\[
 r_2(n)=4\sum_{d\mid n}\chi_4(d),\qquad
 \chi_4(d)=\frac{e(d/4)-e(-d/4)}{2i}.
 \tag{5}
\]

Take fixed smooth (\eta,\zeta\) on the positive axis with (\eta(t)=0) for (t\le1), (\eta(t)=1) for (t\ge2), (\zeta(t)=1) for (t\le1), and (\zeta(t)=0) for (t\ge2). Values can be chosen in ([0,1]). Put (V=T^{3/2}). Let (\{b_D\}), indexed by dyadic (D\ge1), be a smooth partition of unity at all positive integers, with support (d\asymp D) and (j)-th derivative (O_j(D^{-j})). Use an independent copy (b_M) for (m). Lower-end partition functions are included; neither (d=1) nor (m=1) is removed.

Define the actual box

\[
 S_{D,M}(R)=4\sum_{d,m\ge1}\chi_4(d)b_D(d)b_M(m)
 (dm)^{-3/4}\Psi(\sqrt{dm/T})\eta(dm/U)\zeta(dm/V)e(R\sqrt{dm}),
 \tag{6}
\]
\[
 H_{D,M}(R)=\operatorname{Re}\{e(-3/8)S_{D,M}(R)\}.
 \tag{7}
\]

Only (O((\log T)^2)) boxes are nonzero; their products satisfy (N=DM\asymp n\), with (N\ll V). Constants depend only on fixed windows, partition functions, Schwartz seminorms and (\varepsilon). The bounds are uniform in real (T,R), including (R^2\) an integer or arbitrarily near an integer. The statements about the strongest inherited benchmark retain the evidence status assigned by the supplied Round-202 audit; they do not promote its source input.

## 3. Derivation and all costs

### Exact endpoints and the complete infinite tail

At every positive integer (n),

\[
 {\bf1}_{n>U}=\eta(n/U)\zeta(n/V)
 +({\bf1}_{n>U}-\eta(n/U))
 +\eta(n/U)(1-\zeta(n/V)).
 \tag{8}
\]

The second term produces a finite correction (E_U), supported on (U<n<2U), including the exact hard-cutoff convention. The third gives the actual upper-tail correction (Q_V). Thus exactly

\[
 H_{T,>U}=\sum_{D,M}H_{D,M}+E_U+Q_V.
 \tag{9}
\]

The elementary divisor bound and Schwartz decay give, for every fixed (B), after selecting a sufficiently high fixed seminorm of (\Psi),

\[
 |E_U|\ll_\varepsilon U^{1/4+\varepsilon},\qquad
 |Q_V|\le\sum_{n>V}|a_n(T)|\ll_B T^{-B}.
 \tag{10}
\]

In detail, the latter sum is at most (C_{L,\varepsilon}T^{L/2}V^{1/4+\varepsilon-L/2}), equal to (T^{3/8+(3/2)\varepsilon-L/4}). Therefore

\[
 \int w|E_U|^{12}\ll_\varepsilon T^{1+3/2047+\varepsilon},
 \tag{11}
\]

which is safely below (T^{29/25+\varepsilon}). This crude estimate suffices for the auxiliary smoothing collar; it does not replace the inherited sharper low-head theorem. Upper-tail products, if expanded, are bounded by

\[
 T\Big(\sum_n|a_n|\Big)^{11}\sum_{n>V}|a_n|
 \ll T^{15/4+\varepsilon-B}.
 \tag{12}
\]

Hence all omitted upper indices and every cross term are restored. Equivalently, the (L^{12}(w\,dR)) triangle inequality handles (9) before raising to power twelve.

### Poisson summation with the character intact

Fix a box and (d\asymp D). Poisson summation is applied only in the smooth (m)-variable. This is exact; extend its compactly supported integrand by zero to the real line. The (k\)-th integral has phase

\[
 f(m)=R\sqrt{dm}-km.
 \tag{13}
\]

A stationary point exists only for (k>0), and

\[
 m_0=\frac{R^2d}{4k^2},\qquad
 f(m_0)=\frac{R^2d}{4k},\qquad
 f''(m_0)=-\frac{2k^3}{R^2d}.
 \tag{14}
\]

Its scale is (k\asymp K:=RD/\sqrt N). Throughout the nonzero boxes, (K\gg T^{1/4}) up to fixed constants for sufficiently large (T), and (F:=R\sqrt N\gg T). On putting (m=Mt), the phase has large parameter comparable to (F), its stationary second derivative is bounded away from zero in normalized variables, and all normalized amplitude derivatives are bounded by a fixed multiple of (N^{-3/4}). This remains uniform at cutoff supports because the partition functions are smooth and flat where extended by zero.

The leading stationary amplitude is particularly simple:

\[
 (dm_0)^{-3/4}|f''(m_0)|^{-1/2}
 =\frac{2}{\sqrt R\,d}.
 \tag{15}
\]

The negative second derivative contributes (e(-1/8)). Define the real weight

\[
 W_{D,M}(R,d,k)=b_D(d)b_M(m_0)
 \Psi\left(\frac{Rd}{2k\sqrt T}\right)
 \eta\left(\frac{R^2d^2}{4k^2U}\right)
 \zeta\left(\frac{R^2d^2}{4k^2V}\right)
 \tag{16}
\]

and retain the entire signed packet

\[
 Z_{D,M}(R)=\sum_{k\ge1}\sum_{d\ge1}
 \frac{\chi_4(d)}d W_{D,M}(R,d,k)e\left(\frac{R^2d}{4k}\right).
 \tag{17}
\]

Both sums are finite by the weights. The leading transformation is

\[
 S_{D,M}=8R^{-1/2}e(-1/8)Z_{D,M}+O_\varepsilon(T^{-1/2+\varepsilon}).
 \tag{18}
\]

Here the error is priced directly, without assuming cancellation. For each of (O(K)) possibly stationary integrals, the first stationary remainder is (O(MN^{-3/4}F^{-3/2})). Summing the (O(D)) choices of (d) yields

\[
 O(N^{1/4}KF^{-3/2})
 =O(R^{-1/2}D/N)\ll T^{-1/2},
 \tag{19}
\]

since (M\ge1). On the enlarged (k\asymp K) range, the same uniform estimate includes stationary points outside the amplitude support, whose leading weight is zero. Outside that range, including all (k\le0) and arbitrarily large (|k|), repeated integration by parts gives a total

\[
 O_A\{N^{1/4}(1+K)F^{-A}\}.
 \tag{20}
\]

Taking (A\ge2) makes (20) at most (O(T^{-1/2})) in the stated range. Thus neither (k=0), negative dual frequencies nor the infinite dual tail is dropped. Higher asymptotic terms are already covered by (19); no unpriced stationary correction remains.

Combining the original cosine phase with the stationary phase gives

\[
 e(-3/8)e(-1/8)=e(-1/2)=-1.
 \tag{21}
\]

Consequently the complete main term in physical space is

\[
 \mathfrak A_T(R)=-8R^{-1/2}\operatorname{Re}
                         \sum_{D,M}Z_{D,M}(R),
 \qquad
 H_{T,>U}=\mathfrak A_T+E_U+O_\varepsilon(T^{-1/2+\varepsilon}).
 \tag{22}
\]

The arbitrarily small (Q_V) is included in this last error. Equation (22), together with (16)-(17), is a complete arithmetic approximation, not merely a transform of one favorable band. The negative sign and the real part are essential. Replacing (22) by a positive shell count changes the object.

### What the character cancellation actually yields

For fixed (R,k), the weight (d^{-1}W_{D,M}) has size (O(D^{-1})) and total variation (O(D^{-1})). Its differentiated bounds are uniform since (k\asymp K) and all saddle ratios in (16) are at their natural scales. Expanding only the exact character in (5), and summing each smooth geometric progression, gives

\[
 |Z_{D,M}(R)|\ll D^{-1}\sum_{k\asymp K}\sum_{\pm}
 \min\left(D,\left\|\frac{R^2}{4k}\pm\frac14\right\|^{-1}\right).
 \tag{23}
\]

This is the precise step that takes a modulus over separate (k)-packets and the two character branches. The identity before it retains their relative signs.

If the distance in (23) is at most (0<\delta\le1/2), there is an integer (\ell) such that

\[
 |R^2-k(4\ell\mp1)|\ll K\delta.
 \tag{24}
\]

For sufficiently large (T), (K\ll T^{7/4}=o(R^2)), so the integer product in (24) is positive and comparable to (T^2). There are (O(K\delta+1)) possible integers in the real-centered interval (24), and each has (O_\varepsilon(T^\varepsilon)) positive divisor pairs. The parity restriction on the second factor can only reduce their number. Thus

\[
 \#\left\{k\asymp K:\left\|\frac{R^2}{4k}\pm\frac14\right\|\le\delta\right\}
 \ll_\varepsilon T^\varepsilon(K\delta+1).
 \tag{25}
\]

This includes exact product coincidences; an exact zero distance is assigned its finite cost (D), never (1/0). Summing dyadic distance ranges from (D^{-1}) to (1/2), including the range below (D^{-1}), yields

\[
 \sum_{k\asymp K}\min(D,\|R^2/(4k)\pm1/4\|^{-1})
 \ll_\varepsilon T^\varepsilon(K\log(2D)+D).
 \tag{26}
\]

Equations (18), (23), and (26) give (T^\varepsilon(R^{1/2}N^{-1/2}+R^{-1/2})). Since (N\ll T^{3/2}\ll R^2), the second term is dominated by the first. The original box (6) also has the trivial bound (O(N^{1/4})). This proves (2). In particular, retaining (\chi_4) through a geometric progression has produced a genuine improvement over the trivial bound in the range (N>T^{2/3}), but the low-frequency balance prevents a global improvement.

### Twelfth power, dyadic recombination and comparison

For each actual box, regrouping by (n=dm) gives real cosine coefficients supported on (n\asymp N), bounded in modulus by (4d(n)n^{-3/4}). Their squared sum is (O_\varepsilon(N^{-1/2+\varepsilon})). For (n,m\ll V), distinct frequencies obey

\[
 T|\sqrt n-\sqrt m|\gg T^{1/4}|n-m|.
 \tag{27}
\]

Fourier decay of the fixed smooth weight therefore bounds the offdiagonal by an arbitrarily small multiple of the diagonal after the standard inequality (2|a_na_m|\le|a_n|^2+|a_m|^2). Sum frequencies are bounded away from zero. It follows directly, with no independent-phase substitution, that

\[
 \int w|H_{D,M}|^2\ll_\varepsilon T^{1+\varepsilon}N^{-1/2}.
 \tag{28}
\]

Multiplying (28) by the tenth power of (2),

\[
 \int w|H_{D,M}|^{12}
 \ll_\varepsilon T^\varepsilon
 \min\{TN^2,\ T^6N^{-11/2}\}.
 \tag{29}
\]

Both envelopes meet at (N=T^{2/3}), where they are (T^{7/3}). Taking the (L^{12}(w\,dR)) triangle inequality over all (O((\log T)^2)) boxes, then restoring (10)-(11), proves (3). Every mixed box product, every sign, and every head/collar/tail cross term is covered by this physical-space inequality. It is not a termwise absolute estimate of the twelfth Fourier expansion.

The complete signed convolution identity gives the square root in (3). Its power (7/6) exceeds the requested (29/50) by (44/75). Thus the arithmetic procedure is quantitatively inadequate, even though its high-(N) cancellation was real. The supremum bound from (2) is (T^{1/6+\varepsilon}), weaker than the inherited (T^{\beta+\varepsilon}), where (\beta=2\theta_{LY}-1/2<1/6).

Using the supplied (q_0=262/27) benchmark and inherited supremum instead leaves the stronger existing full-tail bound

\[
 \|K_T*\mu_{T,>U}^{*6}\|_2
 \ll_\varepsilon T^{1/2+(12-q_0)\beta/2+\varepsilon}
 =T^{0.648072478\ldots+\varepsilon}.
 \tag{30}
\]

No step above strengthens that evidence-level benchmark. Its missing norm saving is (0.068072478\ldots), exactly the strategy's gap. The elementary box estimates (2) and (28) alone cannot force a stronger moment than their combination: at (N=T^{2/3}), an abstract function of height (T^{1/6}) on a set of measure (T^{1/3}) saturates both and has twelfth moment (T^{7/3}). This is only a norm-information control, not an example with the actual arithmetic coefficients.

## 4. First doubtful or unproved step

There is no asserted gain beyond the proved bounds above. The first new inequality needed for the frozen target, expressed in the actual arithmetic packets, is

\[
 \boxed{\int\chi(R/T)^2
 \left|8R^{-1/2}\operatorname{Re}\sum_{D,M}
 \sum_{k,d\ge1}\frac{\chi_4(d)}d
 W_{D,M}(R,d,k)e\left(\frac{R^2d}{4k}\right)\right|^{12}dR
 \ll_\varepsilon T^{29/25+\varepsilon}.}
 \tag{31}
\]

The weights in (31) are exactly (16), not independently chosen packet coefficients. Because (11) has exponent (1+3/2047<29/25) and the entire stationary/tail error has twelfth moment (O(T^{-5+\varepsilon})), (22) and the two directions of the physical (L^{12}) triangle inequality make (31) equivalent to the requested estimate at its stated exponent. This equivalence is a completed remainder interface, not a proof of (31).

Equation (25) is a counting estimate for the number of possible divisor products near the moving real center. It gives no cancellation among their actual signed, complex packet contributions. Replacing the signed sum by (23) leads precisely to (29), and the (q_0\)-plus-supremum interpolation remains (30). A new signed packet moment estimate or correspondingly stronger distribution estimate is therefore needed before claiming the gain. Exact product coincidences in (24) are not the same notion as exact twelve-radical resonances; neither is silently deleted.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| `actual_coefficients` | PASS: (5)-(7) are exact for (r_2), including even divisors where the character vanishes and all multiplicities. (\Psi) is real and may change sign. |
| `complete_tail_and_cross_terms` | PASS: (8)-(12) restore the sharp lower endpoint and every upper coefficient; physical (L^{12}) recombination covers all cross terms without deleting mixed strata. |
| `signed_filter_preserved` | PASS at identity level: the original two cosine frequencies enter through (7), and the final complete real packet sum is (22). (w=\chi^2) and the exact signed Plancherel interface remain in force. The lossy bound is explicitly identified at (23). |
| `all_errors_priced` | PASS: the first stationary remainder is (19), the entire nonstationary dual sum is (20), the upper arithmetic tail is (10)-(12), and the lower smoothing collar is (11). |
| `real_uniformity` | PASS: (25) counts integers in an interval with real center (R^2); it includes zero distances and near-integer endpoints. No averaging over (T), integer-radius restriction or endpoint exclusion is imposed. Bounded (T) is absorbed in constants. |
| `net_exponent` | PASS: direct moment (7/3), direct convolution norm (7/6), classical supremum (1/6); best inherited norm remains (1/2+(12-q_0)\beta/2). Target (29/50) is not reached. |
| `independent_statement_only_control` | NOT CLAIMED by this selected-context task. The derivation is independent of sibling work; the campaign's separate statement-only audit and any conductor seam review remain required. |
| `no_parent_overclaim` | PASS: the actual target, quarter theorem, M1, M2 and all parent obligations remain open. No lower bound for the complete signed moment is asserted. |

Analytical edge controls: (d=1) or (m=1) is allowed in (19); (D=1) is covered by (\log(2D)); exact (R^2=k(4\ell\pm1)) receives weight (D) in (26); smooth stationary support boundaries use zero extension; nonpositive (k) is included in the remainder. No numerical control was used.

## 6. Dependencies and exact artifacts used

Read-only context, and no other research artifact, before completing this report:

- `protocol.md`.
- `state/proof_obligations.yml`, particularly `GC-target`, `GC-external-Li-Yang-theta-star`, `GC-weighted-square-root-exact-resonance-mass`, and `GC-physical-twelfth-moment-absolute-majorant-obstruction`.
- `state/active_campaign.yml`, Round 203.
- `strategy/round203_complete_signed_convolution_attack.md`.
- `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/candidates/conductor_signed_convolution_interface.md`.
- `rounds/codex-managed/gc-strategy-signed-moment-majorant-review/reports/signed_cutoff_tail_moment_audit.md`.
- This task's assigned brief, `rounds/codex-managed/gc-complete-signed-convolution-attack/briefs/arithmetic_signed_tail_attack.md`.

The analytic tools are the elementary divisor identity/bound, Poisson summation for smooth compact support, elementary one-variable stationary phase with its first remainder, geometric summation by parts, Fourier decay and Hölder/Minkowski. Their applicable scales and remainders are derived explicitly above. No new literature theorem or numerical result is used. Equation (30) is a comparison with the exact inherited evidence; it is not an external theorem independently source-audited here.

## 7. Recommended state effect

**No change** to accepted mathematical state or exponents. Retain the full signed target as open. Retain (22), with (16)-(20) and (31), as candidate arithmetic-interface evidence, subject to independent review. Retain the quantitative diagnosis that this particular character-geometric-sum and product-count route returns the classical scale and no new global moment estimate.

Reject claiming a new exponent from the transform alone, dropping either character branch, omitting the hard-cutoff collar or upper tail, or interpreting the product count as cancellation in the complete signed twelfth moment. This is not a universal no-go for arithmetic methods and does not refute (31).

Only this assigned report was written. No graph, proof draft, validation matrix, synthesis, source card or successor plan was edited. The discovery task stops here.
