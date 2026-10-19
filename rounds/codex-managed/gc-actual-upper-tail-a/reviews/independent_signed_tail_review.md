# Independent review of the signed upper-tail attempt

Round 231; campaign `gc-actual-upper-tail-a`; reviewer `resonance_hostile_controls`, acting as a nonauthor of the discovery report. Generated 2026-10-11. Claimant artifact: `rounds/codex-managed/gc-actual-upper-tail-a/reports/signed_upper_tail_attack.md`, SHA256 `ccd6592b215eecd1c38909fb088d40de2f0ea0b1916b1e568a58d54ba3c94e20`, independently checked on read. Starting graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

## 1. Result and precise verdict

**Pass as a conditional reduction and an explicitly unsuccessful bounded attempt.** No mathematical error was found in the reviewed second-Poisson identity, the full-band summation and error, the exceptional-set quadratic sufficient condition, the change of radius variable, or the two-tail and complementary-owner ledger.

The report proves neither target A nor its integrated alternative. Its new exact representation and quadratic sufficient target must remain candidate evidence. The stated first unproved step, a saving for the signed covariance restricted to the actual exceptional set, is indeed unproved by the displayed first-average or unrestricted mean-square arguments.

Two scope conditions are essential and are already respected by the claimant: (Q) is a sufficient condition, not an asserted equivalent formulation of the full twelfth-moment target; and (P) uses the exceptional set selected by the entire original F, not one rectangle or a smooth replacement for its indicator. No repair to the frozen claimant artifact is required for these points.

## 2. Exact statement and hypotheses reviewed

The actual fixed full band is

    F(R)=sum_n phi(n)r2(n)n^(-3/4)Psi(sqrt(n/T))
                      cos(2pi R sqrt(n)-3pi/4),
    phi(n)=eta(n/T^(64/125))-eta(n/T^(93/125)),
    dmu_T=w(R/T)dR, gamma=16/125, V0=T^gamma.

Use only the separately justified actual ceiling `||F||infinity<<T^(beta+delta)`, the accepted generic distribution, and the reviewed exact restoration `B=L+F+H`, with L,H paid at `32/25`. Define

    a*=10beta-32/25>0,
    E={R in supp(w(R/T)): |F(R)|>V0}.

The reviewed sufficient statement is

    Q_tail=integral_E |F|^2 dmu_T << T^(-a*+epsilon).     (R1)

For the claimant's exact second-Poisson leading representation,

    F(R)=T^(-1/2)S_T(R^2)+E_T(R),
    ||E_T||infinity<<T^(-1/2+epsilon),                  (R2)

the proposed sufficient covariance target is

    integral_(E_s) w(sqrt(s)/T)|S_T(s)|^2 ds
                    <<T^(2-a*+epsilon),
    E_s={s: sqrt(s) in E}.                             (R3)

Both (R1) and (R3) are open. The review checks their conditional implication and the exact mathematical objects, not their truth.

## 3. Independent derivation and seam checks

### 3.1 Second Poisson, sign, multiplicity, and exact resonance

Fix one smooth rectangle and one positive stationary h. Write `alpha=s/(4h)` and `hat b(xi)=integral b(d)e(-xi d)dd`. Directly from

    chi4(d)=(e(d/4)-e(-d/4))/(2i)

and ordinary Poisson summation,

    sum_d chi4(d)b(d)e(alpha d)
     =1/(2i) [sum_k hat b(k-alpha-1/4)
                          -sum_k hat b(k-alpha+1/4)].

The first sum has `q=4k-1`, hence `chi4(q)=-1`; the second has `q=4k+1`, hence `chi4(q)=1`. These disjoint residue classes give

    sum_d chi4(d)b(d)e(alpha d)
       =(i/2)sum_(q odd)chi4(q)hat b(q/4-alpha).        (R4)

Since `q/4-alpha=-(s-hq)/(4h)`, the imaginary part of the transform in (R4) is

    integral b(d) sin(pi(s-hq)d/(2h))dd.

The original two phase shifts multiply to `e(-1/2)=-1`. Consequently taking minus the real part of (R4) gives **plus** one half of this sine integral, exactly as claimed. The definition `K=(sqrt(T)/2) integral b sin` therefore gives the factor `T^(-1/2)K` with the correct sign and normalization.

Each odd q is a distinct Fourier index and occurs once in (R4). Distinct pairs (h,q) with the same product hq are distinct genuine summands; the representation does not authorize deleting their covariance. This all-q summation is valid because it comes from a second Poisson identity. It is different from summing the elementary nearest-q identity repeatedly.

There is also an exact control at `s=hq0`, with q0 odd. The central K vanishes. The remaining q are `q0+2k`; the terms indexed by k and -k have equal characters `chi4(q0)(-1)^k` and opposite odd-kernel arguments. They cancel pairwise in the absolutely convergent sum. Thus the all-q representation preserves the exact real-resonance zero, not merely the central term's zero.

The negative cosine branch is the conjugate already represented by the real part. No extra branch factor or cancellation is missing.

### 3.2 Actual amplitude, radius dependence, all q tails, and stationary errors

For a rectangle `DM asymp N`, `h asymp H=TD/sqrt(N)`, the stationary symbol has

    b_h(d,R) << T^(-1/2)D^(-1),
    partial_d^j b_h << T^(-1/2)D^(-1-j).

This follows by substituting H into the exact factor `N^(-3/4)R sqrt(D)h^(-3/2)`. The change `d=Dt` in K gives a smooth compactly supported function of t, with total scale O(1) and phase frequency a fixed positive constant times u, because `WD/h asymp1`. Differentiating in u preserves uniform bounds; integration by parts in t gives arbitrary polynomial decay. K is therefore a real odd Schwartz function with uniformly bounded fixed seminorms.

At fixed u and h, each R derivative of b costs `T^(-1)`: the explicit R factor and `a(d,R^2d/(4h^2))` have this scale on `R asymp T`, using the m derivative bounds. Higher derivatives obey the corresponding bounds. The h range may be chosen as one fixed enlarged interval using T and the fixed support ratios; stationary points outside the smooth support give zero leading amplitude. No discontinuous R-dependent h selection is needed.

The all-q series is absolutely convergent by these Schwartz bounds, including negative and far q. For fixed T there are finitely many rectangles and relevant h, so finite expansion of the squared sum followed by absolutely convergent q summation is lawful on the compact radius range. No quantitative saving is implied by that justification.

The inherited stationary error per d,h is

    O(N^(-3/4)M(R sqrt(N))^(-3/2)).

Multiplying by O(DH) gives `O(D R^(-1/2)N^(-1))`. Since `D/N asymp1/M=O(1)`, each rectangle contributes `O(T^(-1/2))`. The nonstationary h tail is paid by repeated integration by parts. Summing O(log^2 T) smooth rectangles proves the stated bound in (R2). The second Poisson transform adds no approximation error.

The full F band is finite and includes singleton factor scales and both norm transitions. The infinite H tail remains an exact complementary owner. F is already the cosine series, so there is no new Bessel error in (R2); the accepted sharp-discrepancy reconstruction retains its separate Bessel and smoothing errors.

### 3.3 The actual exceptional set and the two powers of T

The exact change of variables in the leading quadratic term is

    integral_E |T^(-1/2)S_T(R^2)|^2 dmu_T
      =T^(-1) integral_(E_s)
           w(sqrt(s)/T)|S_T(s)|^2 ds/(2sqrt(s)).        (R5)

On the support of w, `sqrt(s) asymp T`. Therefore (R5) is comparable, with fixed constants, to `T^(-2)` times the integral in (R3). The claimant's normalization `2-a*` is correct. This comparison uses no averaging assumption about E_s and no symmetry of that set.

At V0 the accepted distribution gives

    mu_T(E)<<T^epsilon[T^(-2gamma)+T^(1-(136/13)gamma)]
            <<T^(-2gamma+epsilon),

because the second exponent is `-551/1625`, smaller than `-2gamma=-416/1625`. Hence

    integral_E |E_T|^2 dmu_T<<T^(-1-2gamma+epsilon),    (R6)

far smaller than `T^(-a*)`. The inequality `|x+y|^2<=2|x|^2+2|y|^2` pays the cross term and proves that (R3) implies (R1). Conversely, (R2), (R5), and the accepted `Q_tail<<T^epsilon` yield only `T^(2+epsilon)` for (R3). The claimed missing power a* has not been manufactured or hidden by a normalization change.

Using the entire interval to pay E_T would give only a zero-power upper bound for its quadratic energy and would be too weak for the negative-power target. The claimant correctly uses the actual E and its already known measure. No level-set transfer from one rectangle to F is asserted.

### 3.4 Quadratic layer cake, both tails, and complete restoration

For strict E as above, the identity

    Q_tail=V0^2 D_F(V0)+2 integral_(V0)^infinity V D_F(V)dV

is exact, even if a level set at V0 has positive measure. Its first generic tail contributes at most a logarithm between V0 and the actual polynomial ceiling. Its second tail, including the boundary, has power

    1+(2-136/13)gamma
       =1-(110/13)(16/125)=-27/325.

Thus the accepted distribution yields only `Q_tail<<T^epsilon`. Target A would yield `T^(-1/100+epsilon)` because `27/325>1/100`. These calculations check the claimant's signs and both tail terms.

Assuming (R1), the separately proved actual ceiling gives

    integral_E |F|^12 dmu_T
       <=||F||infinity^10 Q_tail
       <<T^(10beta-a*+epsilon)=T^(32/25+epsilon).

Choose the ceiling input delta sufficiently small after specifying the output epsilon. Below V0 the old distribution pays `max(1,10gamma,1+20gamma/13)=32/25`; the threshold boundary is paid at the same budget. The L,H norm bounds and exact `B=L+F+H` restore the complete B moment at `32/25`. U is contained in F and does not become an omitted error. If one changes representation to C+U later, its separately paid budget must still be restored.

Under A the direct twelfth-tail powers are `10beta-1/100=1.279663519481...` and `1+20beta/13=1.198409772228...`, both below `32/25`. Under the unproved weaker sufficient condition (R1), the first high contribution is exactly at the target power; the epsilon convention covers it. The persistence consequence `207/650` does not improve the current pointwise bound. This is a conditional moment gain only.

### 3.5 First-average control versus unrestricted energy

The interval first-average estimate follows term by term by dividing the actual cosine coefficient by `2pi sqrt(n)`. A smooth radius window gives further powers `(T sqrt(N))^(-1)` by integration by parts. These estimates are correct for the stated original radius-independent coefficients.

For the positive interior shell used for the mean-square control, a nonzero fixed smooth shell is bounded below on a fixed smaller annulus. Covering its boundary by unit lattice squares gives the elementary lattice-area count with O(sqrt(N)) error. Thus the weighted r2 mass is at least cN, and Cauchy yields coefficient energy at least `cN^(-1/2)`. The difference-frequency off-diagonal is at most `C sqrt(N)log(2N) sum|a_n|^2`; the sum-frequency term is `O(N^epsilon)`. Since `N` is in the stated band and `sqrt(N)log N=o(T)`, the diagonal proves the claimed `integral F_N^2 >> T N^(-1/2)`.

This verifies an unrestricted mean-square control only. It does not place that energy on E and cannot refute (R1). The report draws this distinction correctly.

## 4. First doubtful or unproved step

The first unproved step remains (R3), with the **same actual full-wave indicator** `1_(E_s)` throughout its signed expansion. None of the established first-average bounds gives a bound for that indicator's variation, Fourier content, or correlation with the wave. The square of one odd kernel is even and has positive integral; oddness alone cannot delete even the elementary covariance diagonal.

Whole-line, smooth-test, rectangle-level, and actual-exceptional-set covariance statements are different interfaces. The claim must not be promoted unless a proved estimate bridges the relevant one to (R3), including the actual amplitudes, all products, all rectangles, and the radius weight. The frozen report does not attempt to pass through this gap silently.

No discovered error requires a correction. The unproved inequality is a substantive analytic gap and remains one after the exact representation is accepted.

## 5. Required controls and outcomes

* **Phase and factor:** pass by the independent residue-class derivation (R4); sine sign and factor one half are correct.
* **q ownership:** pass; two disjoint congruence classes parametrize every odd Fourier index once. Same-product collisions across h are retained.
* **Exact resonance and detuning:** pass; the q0-centered pairing above gives an exact zero at resonance, while a physical detuning need not vanish.
* **Actual amplitude and radius:** pass; fixed coefficient partitions, uniform smooth symbols, fixed enlarged h ranges, and R derivative costs are preserved.
* **Errors and far q:** pass; the second transform is exact, its all-q sum converges, and the first-transform error is summed before use.
* **Exceptional measure and normalization:** pass; (R5) accounts for both powers of T, and (R6) pays the error on the actual E.
* **Full-band scope:** pass; no rectangle event or radius mask is substituted for E, no U owner is deleted, and the full H tail remains paid.
* **Both tails and complete consequence:** pass conditionally, with `-27/325`, `a*`, the threshold boundary, the ceiling epsilon, and complementary `32/25` budgets verified.
* **Mean-square control:** pass as an unrestricted-energy statement only; no high-tail lower bound follows.
* **Resources and state:** analytical review only, with no numerical experiment or external source import. Claimant and initial reports are unchanged; no shared state was edited.

## 6. Dependencies and artifacts used

The sole newly authorized read was the frozen claimant report identified above. The review also used the original named context already read for the hostile-controls assignment: protocol, graph, active campaign, actual interface, upper-tail strategy, accepted complete large-value kernel, combined owner, seam repairs, and the inherited reciprocal report. No other sibling report or review was read.

The reviewer is the author of `reports/resonance_hostile_controls.md`, frozen SHA256 `89693f8519e735dbdd9582850e5465c85fef30835aeab50e398b16fe34f837e8`, and is not the author of the present claimant. The derivations in Section 3 of this review recheck the claimant's formulas directly; the review does not depend on promotion of the reviewer's own candidate report.

Dependencies retain their original scope: the accepted generic distribution and actual ceiling provide baseline input; the reviewed complementary owners pay L,H; the inherited one-variable stationary formula provides its leading symbol and total error. Exact character algebra, ordinary Poisson on a smooth compact symbol, layer cake, and the displayed change of variables establish the reviewed reductions. No fresh external theorem is claimed.

## 7. Recommended state effect

Retain the discovery report as reviewed candidate evidence for the exact product representation and the sufficient exceptional-set quadratic interface. Record this seam review as pass, conditional on (R1)/(R3), with the analytic gap explicitly open. Do not promote A, a complete `32/25` moment, a pointwise result, any M1/M2 parent, or the quarter target.

No claimant repair, shared-state change, or next round is requested. Freeze this review and stop.
