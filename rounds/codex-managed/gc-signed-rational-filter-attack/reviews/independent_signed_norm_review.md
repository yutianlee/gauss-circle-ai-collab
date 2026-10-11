# Round207: independent signed reciprocal and rational norm review

## 1. Result

Campaign: `gc-signed-rational-filter-attack`. Task: `independent_signed_norm_review`. Role: independent, unmasked post-report seam reviewer. Date: 2026-09-27. Starting graph hash reported by the claimants: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`; the graph was not inspected in this assignment. Effort: 100 percent analytical; file hashing is provenance work, not a mathematical experiment.

**GREEN for the assigned signed-reciprocal, rational-coefficient, variable-multiplier, moving-prefix, and restored-power seams of both final claimant files.** No mathematical defect was found in these scopes. The precise reviewed versions are bound by SHA-256 in section 6.

The two Fourier conventions agree exactly, including the quotient Gauss sign. The elementary second-derivative proof is valid for all the actual reciprocal phases and all their partial intervals. Every amplitude and every supported harmonic is paid. It gives the asserted pointwise estimate, but no new physical supremum.

The direct rational variance proof is also correct. In particular, after exact collision grouping, the varying width costs a bounded Fourier integral, and the actual prefix mask costs only logarithms. An explicit bound supplied by the printed argument is

\[
\int_J |A(x)|^2dx\ll XH\log^2(2X),\qquad
\int_J |B(x)|^2dx\ll XH\log^6(2X).
\tag{R1}
\]

Adding the separately assigned threshold-error interface yields the complete (\int_J|Z|^2\ll_\epsilon X^{1+\epsilon}H\). Neither (R1), the signed pointwise estimate, nor their lawful interpolation supplies the missing sixth moment. All displayed (K_6\), (p=12\), and complete-band comparisons are correct.

This review does **not** independently validate the reviewer's original isolated threshold report or the even-(D\) seam. Those are expressly outside this post-report assignment's independent GREEN scope and are assigned to another reviewer. Here their norm bounds are treated as separately checked interfaces when combining the rational arms with the full (Z\). The original isolated report is frozen and unchanged.

## 2. Exact scope and hypotheses

The primary files are `reports/periodic_hyperbola_attack.md` (notation P) and `controls/conductor_rational_norm_ledger.md` (notation C), in this campaign. The review covers P7--P19, the signs and coefficients in P8--P10/C4--C7, the full proof of P11--P13, C6--C10, and their stated inherited moment interfaces. Threshold estimates P1/P6/C3 are interfaces for combination only, not a self-review.

Keep (X=T^2\), (J=[X/2,3X]\), (I=[T/\sqrt2,\sqrt3T]\), and every dyadic middle block

\[
T^{52/125}<N=T^\alpha<T^{99/125},\qquad
h(x)=2\sqrt{x}/\sqrt N,quad H=T/\sqrt N.
\]

Thus (h(x)=Hs(x/X)\), (s(y)=2\sqrt y\), and (h\asymp H\) uniformly on (J\). The filters are those of the actual fixed Round205 mollifier and partition. With

\[
a_{N,T}(t)=t^{-1}\Psi(\sqrt{N/T}\,t)v(t^2),
\quad K(u)=\int_1^2a_{N,T}(t)\sin(2\pi tu)\,dt,
\quad F=-K,
\]

the two definitions of the centered physical quantity agree:

\[
F((m-x)/h)=K((x-m)/h).
\tag{R2}
\]

Both kernels are real odd, uniformly Schwartz, with smooth Fourier support in the two closed bands. Uniformity follows directly because \(\sqrt{N/T}\leq1\) in the whole band, (t\) stays in ([1,2]\), and the fixed (v(t^2)\) vanishes smoothly at both endpoints. All required derivatives of the compact amplitudes are bounded. Implicit constants depend only on fixed windows, filters and, when indicated, epsilon.

The conductor's rational calculation uses either stated cutoff, with its own (L\); the assigned coefficient/norm seams require only (D,L\asymp\sqrt X\), the exact two-arm identity, and (Q=\max(D,4L)=O(\sqrt X)\). This review does not certify the separate claim about choosing an even cutoff.

For the inherited power comparison,

\[
\beta=2\theta_{LY}-\tfrac12,quad \tfrac18<\beta<\tfrac{27}{208},
\quad W_0=T^{\omega(\alpha)},\quad
\omega(\alpha)=\min\{\alpha/4,\beta,(1-\alpha)/2\}.
\]

The accepted distribution and physical shell interfaces are used only with their previously stated fixed-filter, fixed-window, real-endpoint and coefficient-energy qualifications. No new external theorem or unrestricted coefficient sixth-moment theorem is being invoked.

## 3. Independent derivation of the assigned seams

### Fourier orientation, both hyperbola arms, and exact collisions

Use \(\widehat f(\xi)=\int f(u)e(-u\xi)du\). Directly,

\[
\widehat F(\xi)=\frac{i}{2}\operatorname{sgn}(\xi)a_{N,T}(|\xi|),
\qquad \widehat K=-\widehat F.
\]

Poisson summation on (m=a+q\mathbb Z\) gives

\[
\sum_{m\equiv a(q)}F((m-x)/h)
=\frac hq\sum_k\widehat F(hk/q)e(k(a-x)/q),
\]

whereas the (K((x-m)/h)\) convention has (e(k(x-a)/q)\). For the quotient residues (a=\ell,3\ell\), the respective character factors are

\[
e(k/4)-e(3k/4)=2i\chi_4(k),\qquad
e(-k/4)-e(-3k/4)=-2i\chi_4(k).
\tag{R3}
\]

Therefore P8 and C4--C5 have precisely the printed signs and factors. Algebraically, substitute \(\widehat F=-\widehat K\) in P8 and then change (k\mapsto-k\). Oddness of \(\widehat K\) converts the first arm to C4. In the quotient arm the additional identity \(\chi_4(-k)=-\chi_4(k)\) converts the (+2i\) prefactor to the (-2i\) in C5. No arm or negative harmonic is lost. The zero mode vanishes. At (q=h/2\), possible modes meet (\pm2\), where the smooth transform is zero; equality causes no exception.

For the first arm, write the nonzero rational frequency (k/d=a/q\) in lowest terms with (q>0\). Since (\chi_4(d)\ne0\), (q\) is odd and (d=qj,k=aj\), with nonzero terms having (j\) odd. Complete multiplicativity gives the coefficient before (h\widehat K(h\lambda)\):

\[
c^A_{a/q}=\frac{4\chi_4(q)}q
\sum_{j\leq D/q}\frac{\chi_4(j)}j.
\tag{R4}
\]

For a fixed quotient label set (U\), reducing (k/(4\ell)=a/q\), the condition (k\) odd forces (4\mid q\), (a\) odd, and \(\ell=qj/4,k=aj\), with (j\) odd. Hence

\[
c^B_{a/q,U}=\frac{-8i\chi_4(a)}q
\sum_{qj/4\in U}\frac{\chi_4(j)}j.
\tag{R5}
\]

Even (j\) can be included because their character is zero. These are exactly C6--C7; the opposite orientation gives P9--P10. For the prefix in P10 the cutoff remains strictly (Dqj/4<x\), including real (x\). The character harmonic sum for an initial interval is the alternating sum (1-1/3+1/5-\cdots\), between (2/3\) and (1\) whenever nonempty. It is not zero. Distinct denominator classes exclude exact cross-arm coincidence only; they do not exclude mixed higher relations.

### Complete second-derivative argument and amplitude accounting

Here is an independent detailed proof of the lemma used in P11. Suppose (f\in C^2\) on a one-unit enlargement, and (c\lambda\leq |f''|\leq C\lambda\) with a constant sign. When (\lambda\) is bounded below by a fixed positive constant, the trivial number-of-terms bound proves the asserted estimate. For sufficiently small (\lambda\), set \(\delta=\sqrt\lambda<1/4\), and let

\[
\Delta_n=f(n+1)-f(n).
\]

After reversing signs if needed, these differences increase, and

\[
\Delta_{n+1}-\Delta_n
=\int_0^1\int_0^1 f''(n+s+t)\,ds\,dt\asymp\lambda.
\]

Their total range is (O((U+1)\lambda)\). Consequently only (O(U\lambda+1)\) integer levels can be approached. The indices for which \(\operatorname{dist}(\Delta_n,\mathbb Z)<\delta\) number at most

\[
O((U\lambda+1)(\delta/\lambda+1))
=O(U\sqrt\lambda+\lambda^{-1/2}+1).
\]

The remaining indices split into (O(U\lambda+1)\) consecutive pieces, each having monotone differences in one interval \([j+\delta,j+1-\delta]\). On such an interval the reciprocal \(g(t)=(e(t)-1)^{-1}\) has both supremum and total variation (O(\delta^{-1})\); for example its derivative has magnitude (O(\sin^{-2}(\pi t))\), whose integral away from the two endpoints is (O(\delta^{-1})\). Summation by parts in

\[
e(f(n))=g(\Delta_n)\{e(f(n+1))-e(f(n))\}
\]

therefore bounds each good piece by (O(\delta^{-1})\), including both endpoint terms. Adding all pieces and the bad indices proves

\[
\left|\sum_{n\in\mathbb Z\cap\mathcal I}e(f(n))\right|
\ll U\sqrt\lambda+\lambda^{-1/2}+1.
\tag{R6}
\]

The proof applies to all partial real-ended intervals. A bounded number of boundary integers can alternatively be removed, which is paid by the (+1\). There is no omitted monotonicity-of-(f''\) assumption: only its sign and two-sided size were used.

At fixed (x\), (h=h(x)\) is a parameter. In the first arm, resolve the character exactly as

\[
\chi_4(d)=\{e(d/4)-e(-d/4)\}/(2i).
\]

For each positive harmonic (k\), the phases are \(\pm d/4-kx/d\), and the supported interval is \([hk/2,hk]\cap[1,D]\). Their second derivatives are (-2kx/d^3\), so their magnitudes are comparable to

\[
\lambda_k=x/(h^3k^2).
\]

The interval has length (O(hk)\), including when it is truncated. The weight \(w(d)=4h\widehat F(hk/d)/d\) satisfies

\[
\|w\|_\infty\ll k^{-1},\qquad
|w'(d)|\ll (hk^2)^{-1},\qquad
\operatorname{Var}(w)\ll k^{-1}.
\]

These follow by differentiating both (h/d\) and \(\widehat F(hk/d)\); the latter contributes (h^2k/d^3\), of the same order as (h/d^2\) on the support. Endpoint weights are (O(1/k)\). Abel summation with (R6) gives the full (k\)-contribution

\[
\ll \frac{\sqrt{x/h}}k+\frac{h^{3/2}}{\sqrt x}+\frac1k.
\tag{R7}
\]

For the quotient arm, (k\) is odd and the phase is \(-kx/(4\ell)\). The support and actual mask make the one interval

\[
[hk/8,hk/4]\cap[1,L]\cap\{\ell:D\ell<x\}.
\]

The second derivative is \(-kx/(2\ell^3)\), again comparable in magnitude to \(\lambda_k\). Its weight \(2ih\chi_4(k)\widehat F(hk/(4\ell))/\ell\) has supremum and variation (O(1/k)\). The strict truncated endpoint adds only its endpoint weight, already paid by partial summation. Thus (R7) holds here too. No derivative in (x\), no derivative of the moving mask, and no replacement of (h(x)\) is used.

All positive harmonics satisfy (k\leq CT/h\), and all negative ones are included by conjugation. Summing every harmonic in (R7) gives

\[
|A_N|+|Q_N|
\ll\sqrt{x/h}\log(2T/h)
 +(T/h)h^{3/2}/\sqrt x+\log(2T/h)
\]

\[
\ll T^{1/2}N^{1/4}\log(2T)
 +T^{1/2}N^{-1/4}+\log(2T).
\tag{R8}
\]

If some \(\lambda_k\geq1\), (R6)'s trivial branch remains valid and (R7) is still a lawful upper bound. All middle scales have (h\to\infty\), so the reciprocal supports and their fixed enlargements stay away from zero. The separately supplied (O(1)\) boundary norm turns (R8) into P2. Its normalization by (T^{-1/2}\) recovers the existing (N^{1/4}\) physical supremum.

### Rational spacing and variable-width multiplier

Choose a fixed envelope \(c/H\leq|\lambda|\leq C/H\) containing the support for every (x\in J\). Every reduced denominator obeys (q\leq Q=O(\sqrt X)\), and distinct fractions satisfy

\[
|a/q-a'/q'|\geq(qq')^{-1}\gg X^{-1}.
\tag{R9}
\]

Since (a\ne0\), the envelope also implies (q\gg H\). For a fixed (q\), the number of possible numerators, with both signs and without imposing coprimality, is (O(q/H)\). There are (O(Q^2/H)=O(X)\) frequencies in total.

On any interval of length (O(X)\), the integrated Gram entry for two frequencies is bounded by \(\min(CX,C/|\lambda-\mu|)\). Ordering the frequencies and applying (R9) bounds every absolute row sum by (CX\log(2X)\). The elementary Schur bound therefore proves

\[
\int_J\left|\sum_\lambda b_\lambda e(x\lambda)\right|^2dx
\ll X\log(2X)\sum_\lambda|b_\lambda|^2.
\tag{R10}
\]

It is uniform under translating (J\) and multiplying the polynomial by a common unit-modulus function. The diagonal is retained. Exact fractions have already been grouped before applying this estimate.

To justify the varying multiplier, choose fixed smooth cutoffs in (y\) and (z\), equal to one on (J/X\) and the frequency envelope in (z=H\lambda\). Their product with

\[
A_0(y,z)=s(y)\widehat K(s(y)z),\qquad s(y)=2\sqrt y,
\]

defines a compact smooth extension with uniformly bounded derivatives. In particular, derivatives up to order two in each coordinate give, by integration by parts,

\[
|\widehat A_0(u,v)|\ll(1+u^2)^{-1}(1+v^2)^{-1},
\quad \|\widehat A_0\|_{L^1(\mathbb R^2)}\ll1.
\tag{R11}
\]

Fourier inversion expresses (A_0(x/X,H\lambda)\) as the integral of \(e(ux/X)e(vH\lambda)\) against \(\widehat A_0\). The first factor has common modulus one, and the second is either a unit phase in the coefficient vector or translation of the frequency polynomial by (vH\). Hence (R10) is uniform in both integration variables. Minkowski proves

\[
\left\|\sum_\lambda Hc_\lambda
A_0(x/X,H\lambda)e(x\lambda)\right\|_{L^2(J)}^2
\ll X\log(2X)H^2\sum_\lambda|c_\lambda|^2.
\tag{R12}
\]

Exactly the same argument works in (L^2(J;\ell^2(U))\) for a family of interval labels (U\). This establishes the conductor's mixed-multiplier separation without assuming that arbitrary two-variable coefficients factor.

For arm A, (R4), the bounded alternating partial sum, and numerator counting yield

\[
H^2\sum_\lambda|c^A_\lambda|^2
\ll H^2\sum_{cH\leq q\leq Q}\frac{q/H}{q^2}
\ll H\log(2X).
\tag{R13}
\]

Equations (R12)--(R13) prove the first part of (R1).

### Joint dyadic-prefix coefficient energy and complete variance

For every real (x\), let (n(x)\) be the number of integers \(\ell\in[1,L]\) satisfying \(D\ell<x\). The frozen quotient labels are exactly the integer prefix \([1,n(x)]\). Its canonical binary decomposition has at most one interval at each dyadic scale, using (O(\log(2X))\) scales. Padding the label universe to a power of two does not add labels to this prefix.

At a fixed scale, the dyadic intervals (U\) are disjoint. The sets of (x\) that select different such intervals are also disjoint, since each (x\) selects at most one. Cauchy over scales followed by dropping these selecting-set restrictions bounds the squared norm of the moving prefix by

\[
O(\log(2X))\sum_{\text{scales}}\sum_U\|B_U\|_{L^2(J)}^2.
\tag{R14}
\]

Crucially, for fixed (a/q\) at one scale, the corresponding sets of (j\) are disjoint. Thus

\[
\sum_U\left|\sum_{qj/4\in U}\frac{\chi_4(j)}j\right|^2
\leq\sum_U\left(\sum_{qj/4\in U}\frac1j\right)^2
\leq\left(\sum_{j\leq4L/q}\frac1j\right)^2
\ll\log^2(2X).
\tag{R15}
\]

No number-of-intervals factor appears in this joint estimate. From (R5), numerator counting and (R15),

\[
\sum_U H^2\sum_\lambda|c^B_{\lambda,U}|^2
\ll H\log^2(2X)\sum_{cH\leq q\leq Q}\frac1q
\ll H\log^3(2X).
\tag{R16}
\]

Use the Hilbert-direct-sum form of (R12) at that scale. It gives (\sum_U\|B_U\|_2^2\ll XH\log^4(2X)\). Summing scales and applying the outside Cauchy factor in (R14) gives (XH\log^6(2X)\), proving the second part of (R1). The strict prefix at integer thresholds is retained by the definition of (n(x)\); no endpoint convention or variation assumption on the selecting sets is needed.

The separate threshold interface contributes squared norm (O(\sqrt XH)\), smaller than (XH\), and the completed-localization tails are rapid. Applying the finite-sum norm inequality to the two arms and these errors proves the claimed complete C1. This combination is conditional only on the separately assigned threshold/tail seam, not on the signed reciprocal estimate. Conversely, (R8) does not use the rational variance proof.

### Restored sixth and twelfth powers

The grouped pointwise absolute coefficient mass is (O(Q)\) up to logarithms: at denominator (q\), (O(q/H)\) numerators times an amplitude (H/q\) cost (O(1)\), with a harmless logarithm if the duplicate character sum is bounded absolutely. Both arms remain. Consequently C1 gives

\[
K_6\ll_\epsilon X^{1+\epsilon}HQ^4
\ll X^{3+\epsilon}H=T^{7+\epsilon}N^{-1/2},
\tag{R17}
\]

which is C10. Directly raising (R8) would give (T^{5+\epsilon}N^{3/2}\). Combining its fourth power with C1 is stronger:

\[
K_6\ll_\epsilon(T^{1/2}N^{1/4})^4
(T^3N^{-1/2})T^\epsilon
=T^{5+\epsilon}N^{1/2}.
\tag{R18}
\]

The inherited additive bridge is \(S_N(R)=R^{-1/2}Z(R^2)+e_N(R)\), with \(e_N\ll T^{-1/2+\epsilon}N^{-1}\) plus rapid tails. Its exact sixth-power Jacobian is

\[
\int_I|R^{-1/2}Z(R^2)|^6dR
=\tfrac12\int_Jx^{-2}|Z(x)|^6dx\asymp T^{-4}K_6.
\tag{R19}
\]

Multiplying by the legal physical supremum (W_0^6T^\epsilon\) proves P14. The algebraic bridge error contributes

\[
W_0^6\,T\,(T^{-1/2}N^{-1})^6T^\epsilon
\leq T^{-2+\epsilon}N^{-9/2}.
\]

Using the separately assigned boundary sixth norm (TH\), its physical twelfth certificate costs at most

\[
W_0^6T^{-4}TH\leq T^{-2}N<T^{-151/125},
\]

exactly P15. This is a power check of an input, not independent validation of that input.

Substitution of (R18) gives (T^{1+\epsilon}N^{1/2}W_0^6\). Retaining all suprema instead gives

\[
K_6\ll_\epsilon T^{5+\epsilon}N^{-1/2}W_0^4,
\qquad M_{12}(S_N)\ll_\epsilon T^{1+\epsilon}N^{-1/2}W_0^{10}.
\tag{R20}
\]

The sufficient sixth threshold is exactly (T^{129/25-6\omega+\epsilon}\). The respective excess exponents of these upper certificates are

\[
6\omega+\alpha/2-4/25,
\qquad 10\omega-\alpha/2-4/25.
\]

On the three pieces of (\omega\), the first is (2\alpha-4/25\), (6\beta+\alpha/2-4/25\), (71/25-5\alpha/2\), all positive; the end values cited in P are (84/125\) and (43/50\). The second has pieces (2\alpha-4/25\), (10\beta-\alpha/2-4/25\), (121/25-11\alpha/2\), with positive global lower bound (121/250\). The claimed insufficiency therefore holds on every middle scale.

Finally, the inherited distribution (D(V)\ll T^\epsilon(V^{-2}+TV^{-136/13})\), together with block variance (TN^{-1/2}\), gives the claimed sharper sixth input. To check its powers directly, split sixth layer cake at (V_0=N^{13/220}\). The low Chebyshev integral and high (TV^{-136/13}\) integral are both (TN^{-29/110}\); the high (V^{-2}\) term gives (W_0^4\), which is smaller throughout the stated band. The low integral is integrable at zero. This gives physical sixth norm (T^{1+\epsilon}N^{-29/110}\), hence additive

\[
K_6\ll_\epsilon T^{5+\epsilon}N^{-29/110}.
\tag{R21}
\]

Its excess over the sufficient sixth threshold is

\[
g(\alpha)=6\omega(\alpha)-4/25-(29/110)\alpha.
\]

The first piece increases, and both subsequent pieces decrease. The lower and upper endpoint values are respectively (2436/6875\) and (3509/13750\), both positive. The maximum occurs at (4\beta\). The corresponding complete twelfth exponent is

\[
\max_\alpha\{1-(29/110)\alpha+6\omega(\alpha)\}
=1+(272/55)\beta>10\beta,
\]

where the difference is (1-(278/55)\beta>0\). Both breakpoints (4\beta\) and (1-2\beta\) lie inside the complete middle range. Minkowski over all (O(\log T)\) blocks pays only logarithms and retains all mixed terms. The accepted complete (10\beta\) exponent remains stronger; the already estimated outside band has exponent (29/25<10\beta\). No pointwise exponent or parent obligation is improved.

## 4. First doubtful or unproved step

No defect remains in the exact scopes reviewed above. The conductor corrected the odd-denominator TeX phrase and subsequently clarified that, at a threshold, agreement of the two strict indicators concerns the atom at that threshold. The latter wording belongs to the separately assigned threshold seam; neither correction changes the signed or norm sections reviewed here. The final corrected file is the version bound here.

The first missing mathematical input remains a complete signed sixth-order correlation estimate for the actual rational sum with both arms and the real variable-width coefficients, or a direct twelfth-moment estimate bypassing this certificate. None of rational spacing, pairwise denominator disjointness, recovered variance, or the separate-harmonic second-derivative bound establishes such an input.

This GREEN review must not be cited as independent review of the threshold/even-(D\) calculation. Completing C1 from (R1) uses that separately assigned norm interface; its independent evidence must come from the other reviewer.

## 5. Controls and outcomes

| Assigned control | Outcome |
|---|---|
| Two spatial/Fourier orientations | GREEN: (F=-K\), (k\mapsto-k\), odd transform and odd character reproduce both signs exactly. |
| Quotient (k=1\) Gauss sign | GREEN: (e(1/4)-e(3/4)=2i\); the opposite orientation is (-2i\). The external divisor factor four is retained. |
| Repeated first-arm fraction | GREEN: at cutoff (D=9\), the coefficient of (1/3\) is (-4/3+4/9=-8/9\), matching ((4\chi_4(3)/3)(1-1/3)\). This is a finite algebraic control, not numerical evidence. |
| Repeated quotient fraction | GREEN: with quotient labels (1,2,3\), the coefficient of (1/4\) is (-2i+2i/3=-4i/3\); the even label has zero character, and (R5) gives the same answer. |
| Partial intervals and large second derivative | GREEN: real-ended truncations, endpoint weights, bounded boundary removals and the trivial large-(\lambda\) branch are included in (R6)--(R8). |
| Amplitude and all harmonics | GREEN: both differentiated factors cost (O((hk^2)^{-1})\), total variation is (O(1/k)\), and (O(T/h)\) harmonics of both signs are retained. |
| Spacing after collisions | GREEN: the spacing estimate applies to reduced distinct fractions only; repeated labels are summed into (R4)--(R5) first. |
| Mixed variable-width multiplier | GREEN: a compact two-variable extension has bounded Fourier (L^1\), and the integrated polynomial norm is uniform under both generated modulations. |
| Prefix energy | GREEN: (R15) bounds the energy jointly over disjoint intervals; no multiplication by their number occurs. Scale and Cauchy costs give at most the explicit sixth logarithmic power. |
| Complete variance | GREEN for rational arms; adding the separately reviewed threshold/tail interface gives the full (Z\) variance. No higher moment is inferred from it. |
| Sixth/twelfth ledger | GREEN: exact (T^{-4}\) conversion, every algebraic error, sufficient threshold, piecewise excesses, and complete interior maximum checked. |
| Threshold/even-(D\) independent review | OUTSIDE THIS REVIEW: expressly assigned elsewhere; the original isolated author does not independently validate their own result here. |
| Scope controls | GREEN: no positive lower bound for the signed moment, no Gaussian inference, no deletion of one arm, no claim that the sufficient certificate is necessary. |

All mathematical controls are analytical. No new source theorem, web lookup or mathematical numerical experiment was used.

## 6. Exact artifacts, provenance, and final hashes

Primary final reviewed versions:

| Claimant file | SHA-256 |
|---|---|
| `rounds/codex-managed/gc-signed-rational-filter-attack/reports/periodic_hyperbola_attack.md` | `79a1ec2efb8430a72cb3b14cc49a2533795c8ec013d725b5240b719a5749e8ab` |
| `rounds/codex-managed/gc-signed-rational-filter-attack/controls/conductor_rational_norm_ledger.md` | `be115ee27206a429c9480594969aa9e9fddd7963569e3f635e8c3ce9085029d4` |

Both hashes were recomputed after the conductor's announced format correction and final threshold-wording clarification; the corrected sentence was read. The second agrees with its announced final hash, and the discovery file remained unchanged. The mathematical audit applies only to these exact versions.

Other files actually read for this post-report assignment:

- `protocol.md`.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/reports/actual_divisor_shell_attack.md`: the exact filter, physical bridge, divisor identity and legal block norms cited by P.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/controls/conductor_sixth_moment_power_ledger.md`: the complete second moment, legitimate suprema, inherited sixth bound and sufficient threshold.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/reviews/independent_bridge_power_review.md`: the precise previously reviewed bridge and power interfaces.
- `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md`: the actual partition, complete middle interval, outside-band scope and fixed physical shell interface.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`: the coefficient-uniform distribution interface and accepted complete moment scope.

This task began only after the statement-only report was completed and frozen. Its earlier isolation is not claimed for this unmasked review, and this review is not represented as an independent review of that author's own isolated threshold proof. No current graph, current manifest, current strategy, sibling discovery report or unrelated interface was inspected in this assignment. No authoritative state was changed.

## 7. Recommended state effect

**GREEN as reviewed analytical evidence for the expressly assigned seams; no graph or proof-draft change.** Retain the complete rational representation, its direct variance proof, the signed reciprocal estimate, and the fully priced failure of these estimates to improve the complete twelfth moment.

Use the separate reviewer's threshold/even-(D\) findings for that seam before campaign closure. Do not count this review twice as independent evidence for the original isolated threshold result. Preserve the actual signed sixth target, complete (p=12\) target, accepted (10\beta\) exponent and every open parent obligation.

Only this assigned review file was written. Both claimant files, the isolated report, graph, proof draft, validation matrices, synthesis and all other files remain unchanged. This assignment stops here and initiates no next round.
