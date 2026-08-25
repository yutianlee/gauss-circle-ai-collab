# Hostile post-unmask audit of completion, radical channels, and self-return

## 1. Result

**Verdict: green.**  The revised conductor candidate's two positive estimates

\[
 \sum_n |C_L(n)|^2\ll L^2\log(2L)
 \tag{137.U1}
\]

and, for squarefree \(D>1\),

\[
 \sum_{\substack{n\asymp L^2\\ \operatorname{sf}(n)=D}}
 |B_L(n)|
 \ll_\varepsilon
 \left(1+\frac{L}{\sqrt D}\right)L^\varepsilon
 \tag{137.U2}
\]

are correct upper bounds for the literal coefficient.  The product-energy parametrization, squarefree-channel parametrization, target-safe exact resonance, formal B-process ledger, divisibility-completion critical map, complementary-divisor involution, and full-divisor circularity diagnosis all survive recomputation.  They do not prove the target scalar or a strict product-fibre reduction, so `product_fibre_no_go` remains the correct round closure.

Final verification finds every requested repair in the revised candidate: (137.C2) is called only an upper energy envelope; (137.C10a)--(137.C10b) supply the radical-shell inequalities; (137.C13)--(137.C14) are expressly coefficient-free and formal; (137.C15)--(137.C17a) give the bijective residue-to-dual map, surviving \(1/h\), universal phase, exact profile, mode range, and owner caveats; (137.C17b) is the literal divisor switch; and the paragraph after (137.C18) distinguishes circular import of the desired Gauss-circle conclusion from a genuinely independent localized \(r_2\)-estimate.  No residual equation-level defect remains.

## 2. Exact statement and hypotheses

Retain exactly

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=\frac{X}{y^2},\qquad
 H=\lfloor yX^{-1/4}\rfloor,
 \tag{137.U3}
\]

one half-open polynomial intermediate block \(1\ll L\ll H\), and the literal hard cone \(\lceil h/4\rceil\le m\le h\).  Put

\[
 w_L(h,m)=
 \eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xh}{4m}}\right),
 \tag{137.U4}
\]

with zero extension outside the cone, and

\[
 C_L(n)=
 \sum_{\substack{hm=n,\ h\ \mathrm{odd}\\
                  \lceil h/4\rceil\le m\le h}}
 \chi_4(h)w_L(h,m),
 \qquad
 B_L(n)=L^{3/2}n^{-3/4}C_L(n)1_{n\ne\square}.
 \tag{137.U5}
\]

The fixed profiles are used only through their literal occurrence and uniform boundedness in the counting estimates.  No lower envelope, positivity, smoothness in \(n\), bounded variation, additive-twist bound, or fibre mean is assumed.  The square sector may be added or removed only through its existing target-safe owner.  All B-process statements below concern the smooth phase geometry or the stationary principal family after a lawful expansion; they are not estimates for the rough actual coefficient without a new transform theorem.

The review tests only the candidate's displayed product-energy and radical lemmas and the proposed one-dimensional continuations.  A no-go for those interfaces is not a lower bound for the physical scalar and does not exclude a new fixed-actual-coefficient theorem.

## 3. Proof and equation-by-equation recomputation

**Product energy.**  On the literal support, \(h\asymp m\asymp L\).  Boundedness of (137.U4) and expansion of the square give

\[
 \sum_n|C_L(n)|^2
 \ll Q_L,
 \qquad
 Q_L:=\#\{h_1m_1=h_2m_2:\ h_i,m_i\asymp L\}.
 \tag{137.U6}
\]

Write \(g=(h_1,h_2)\), \(h_1=ga\), \(h_2=gb\), \((a,b)=1\).  The equality forces

\[
 m_1=bt,\qquad m_2=at.
 \tag{137.U7}
\]

With \(M=\max(a,b)\), the simultaneous dyadic restrictions give \(\#g,\#t\ll L/M+1\), and there are \(O(M)\) ordered pairs \((a,b)\) with maximum \(M\).  Therefore

\[
 Q_L
 \ll \sum_{M\ll L}M\left(\frac LM+1\right)^2
 \ll L^2\log(2L).
 \tag{137.U8}
\]

The cone, oddness, profiles, and nonsquare deletion can only decrease this absolute envelope, proving (137.U1).  Since \(L^{3/2}n^{-3/4}\asymp1\) and there are \(O(L^2)\) active \(n\), Cauchy gives only

\[
 \left|\sum_nB_L(n)e(J\sqrt n)\right|
 \ll L^2\sqrt{\log(2L)},
 \tag{137.U9}
\]

up to fixed profile constants.  This misses the target by \(L^{1/2-o(1)}\).  Nothing in (137.U6)--(137.U8) proves a matching lower bound for \(\sum|C_L|^2\), so "near-minimal" must not be used as a literal two-sided claim.

**Squarefree-radical channels.**  Fix squarefree \(D>1\) and impose \(hm=Dt^2\).  With \(g=(h,m)\), \(h=ga\), \(m=gb\), and \((a,b)=1\), one has \(\operatorname{sf}(ab)=D\).  There is a unique ordered factorization

\[
 a=d_1u^2,\qquad b=d_2v^2,qquad
 d_1d_2=D,qquad (d_1,d_2)=1,
 \tag{137.U10}
\]

with squarefree \(d_1,d_2\).  The cone makes \(a\asymp b\), so on a shell \(a,b\asymp A\), for a fixed \((d_1,d_2)\),

\[
 \#(u,v,g)
 \ll
 \left(\sqrt{\frac A{d_1}}+1\right)
 \left(\sqrt{\frac A{d_2}}+1\right)
 \left(\frac LA+1\right).
 \tag{137.U11}
\]

On a nonempty shell \(d_i\ll A\), hence \(\sqrt D\ll A\ll L\).  Consequently

\[
 \left(\sqrt{\frac A{d_1}}+1\right)
 \left(\sqrt{\frac A{d_2}}+1\right)
 \ll \frac A{\sqrt D}+1,
 \]

and

\[
 \left(\frac A{\sqrt D}+1\right)
 \left(\frac LA+1\right)
 \ll \frac L{\sqrt D}+1.
 \tag{137.U12}
\]

There are \(O(\log L)\) shells and \(2^{\omega(D)}\ll_\varepsilon D^\varepsilon\) ordered factorizations; active channels have \(D\ll L^2\).  This proves the pair count and hence (137.U2), because the normalized contribution of each \((h,m)\) is \(O(1)\).  If \(X=Ds^2\) and \(n=Dt^2\), then

\[
 e(J\sqrt n)=e(Dst)=1.
 \tag{137.U13}
\]

This is an exact nonsquare resonance, conditional on that centre, but its whole fixed-\(D\) absolute capacity is \(O_\varepsilon(L^{1+\varepsilon})\), below \(L^{3/2}X^\varepsilon\).  It is not an actual lower asymptotic because profiles and character signs remain.  Summing the upper bounds over all active radicals loses the gain:

\[
 \sum_{\substack{D\ll L^2\\D\ \mathrm{squarefree}}}
 \left(1+\frac L{\sqrt D}\right)L^\varepsilon
 \ll L^{2+\varepsilon}.
 \tag{137.U14}
\]

**Formal B-process geometry.**  For \(f(x)=J\sqrt x\),

\[
 f'(x)=\frac J{2\sqrt x},\qquad
 f''(x)=-\frac J{4x^{3/2}}.
 \]

Across a fixed-ratio interval \(x\asymp L^2\), the derivative range has length \(\asymp J/L\).  Thus the geometric dual range contains \(\asymp J/L\) integers, while a stationary integer \(r\) has

\[
 x_r=\frac X{4r^2},\qquad
 f(x_r)-rx_r=\frac X{4r},\qquad
 |f''(x_r)|^{-1/2}\asymp\frac{L^{3/2}}{\sqrt J}.
 \tag{137.U15}
\]

The absolute coefficient-free stationary capacity is therefore

\[
 \frac JL\frac{L^{3/2}}{\sqrt J}
 =\sqrt{JL}
 =L^{3/2}\frac{\sqrt J}{L}
 \asymp L^{3/2}\frac HL.
 \tag{137.U16}
\]

This exceeds the target because \(L\ll H\).  It is neither a physical lower bound nor a lawful transform estimate for \(C_L\): some formal stationary points may carry zero actual coefficient, and no variation or additive-partial-sum hypothesis has been proved.  Exact centre tuning is nevertheless a valid separation control: \(X=4r^2n_0\) gives \(f'(n_0)=r\) and \(f(n_0)=2rn_0\in\mathbb Z\), so a uniform first-derivative gap is false.

**Divisibility completion and stationary return.**  Temporarily restore the square terms through their owner and keep the exact hard interval \(I_h=[h^2/4,h^2]\) with its inherited endpoint convention.  Insert

\[
 1_{h\mid n}=\frac1h\sum_{a\bmod h}e(an/h).
 \tag{137.U17}
\]

With the Poisson dual integer \(k\), let \(r=kh-a\).  For representatives \(0\le a<h\), the map

\[
 (a,k)\longmapsto r=kh-a
 \tag{137.U18}
\]

is a bijection from \((\mathbb Z/h\mathbb Z)\times\mathbb Z\) to \(\mathbb Z\): for a given \(r\), take \(a\equiv-r\pmod h\) and \(k=(r+a)/h\).  Hence no extra factor \(h\) appears, and the \(1/h\) in (137.U17) survives.  The phase

\[
 \phi_{h,r}(x)=J\sqrt x-\frac rhx
\]

has a positive stationary point precisely at

\[
 x_{h,r}=\frac{Xh^2}{4r^2},\qquad
 \phi_{h,r}(x_{h,r})=\frac{Xh}{4r},\qquad
 \phi''_{h,r}(x_{h,r})=-\frac{2r^3}{Xh^3}.
 \tag{137.U19}
\]

Moreover,

\[
 W\!\left(\sqrt{\frac{q_Xh^2}{4x_{h,r}}}\right)
 =W(r/y),
 \qquad
 x_{h,r}^{-3/4}|\phi''_{h,r}(x_{h,r})|^{-1/2}
 =2J^{-1/2}.
 \tag{137.U20}
\]

Since \(x_{h,r}\in I_h\) is equivalent to \(J/2\le r\le J\), with inherited endpoint conventions, the full stationary principal family is

\[
 \begin{aligned}
 \mathcal M_L={}&
 2e(-1/8)L^{3/2}J^{-1/2}
 \sum_{h\ \mathrm{odd}}
 \frac{\chi_4(h)\eta_L(h)\Phi(h/(H+1))}{h}\\
 &\times
 \sum_{\substack{r\in\mathbb Z_{>0}\\J/2\le r\le J}}
 W(r/y)e\!\left(\frac{Xh}{4r}\right).
 \end{aligned}
 \tag{137.U21}
\]

This is the canonical inverse of the earlier endpoint transform and restores the reciprocal hard-TOP phase and exact real-centre profile.  Equation (137.U21) is a stationary principal term, not an exact finite-sum identity by itself.  Hard endpoint samples, support crossings, zero and nonstationary modes, stationary remainders, and square subtraction retain their pre-existing owners.  The candidate's self-return conclusion is correct only with these qualifications.

**Complementary divisor and full divisor.**  Write \(n=2^\nu n_{\rm o}\), \(n_{\rm o}\) odd, and put \(d=n_{\rm o}/h\).  Then

\[
 \frac12\sqrt{\frac{n_{\rm o}}{2^\nu}}
 \le d\le
 \sqrt{\frac{n_{\rm o}}{2^\nu}},
 \qquad
 \chi_4(h)=\chi_4(n_{\rm o})\chi_4(d),
 \tag{137.U22}
\]

and the literal switch is

\[
 \begin{aligned}
 C_L(2^\nu n_{\rm o})={}&\chi_4(n_{\rm o})
 \sum_{\substack{d\mid n_{\rm o}\\
 \frac12\sqrt{n_{\rm o}/2^\nu}\le d\le
 \sqrt{n_{\rm o}/2^\nu}}}
 \chi_4(d)\eta_L(n_{\rm o}/d)
 \Phi\!\left(\frac{n_{\rm o}}{d(H+1)}\right)\\
 &\times W\!\left(
 \sqrt{\frac{q_Xn_{\rm o}}{2^{\nu+2}d^2}}
 \right).
 \end{aligned}
 \tag{137.U23}
\]

The incidence map is bijective and involutive, but the transformed height profile is not a free dyadic profile in \(d\).  Thus (137.U23) is exact and supplies no contraction.

Finally define

\[
 D(n)=\sum_{d\mid n}\chi_4(d)=\frac{r_2(n)}4,
 \qquad R_L(n)=D(n)-C_L(n).
 \tag{137.U24}
\]

The identity \(\mathcal T[C_L]=\mathcal T[D]-\mathcal T[R_L]\) is exact only with the same radial cutoffs and normalization in all three terms.  A prime \(p\equiv1\pmod4\) has \(C_L(p)=0\) but \(D(p)=2\); conversely \(D(3^{2j+1})=0\) while a literal near-square term of \(C_L(3^{2j+1})\) may survive.  Thus \(R_L\) is not a proved boundary error.  The full term is

\[
 \mathcal H_L(J)=\frac{L^{3/2}}4
 \sum_{n\asymp L^2}r_2(n)n^{-3/4}e(J\sqrt n).
 \tag{137.U25}
\]

Its square subseries has only \(O_\varepsilon(L^{1+\varepsilon})\) absolute capacity.  The remaining nonsquare radial block is the localized Hardy--Gauss interface at the target scale.  Estimating it by importing the desired Gauss-circle conclusion is circular; proving a genuinely independent estimate for (137.U25) would instead be new mathematics.  In either case, the uncontrolled \(R_L\) term prevents the displayed completion from being a strict reduction.

## 4. First doubtful or unproved step

The first failed affirmative seam remains the passage

\[
 \text{exact product-fibre regrouping plus }|C_L(n)|\le\tau(n)
 \quad\Longrightarrow\quad
 \text{a smooth-amplitude derivative or B-process estimate}.
 \tag{137.U26}
\]

Neither the pointwise divisor bound nor the valid energy estimate (137.U1) supplies bounded variation, additive partial sums, or a fixed-frequency signed transform estimate for the literal \(C_L\).  Cauchy stops at (137.U9), and the coefficient-free geometric ledger stops at (137.U16).  A phase-adapted array with the same support, pointwise scale, and admissible \(\ell^2\) envelope refutes a coefficient-uniform theorem, but it is not the physical coefficient and gives no physical lower bound.

If one repairs legality by expanding divisibility, the next seam is not an algebraic error: (137.U17)--(137.U21) restore the original reciprocal hard-TOP principal family.  No strict reduction exists until every owner correction is controlled and the returned main term is bounded by a genuinely new signed theorem.  Divisor switching and full-divisor completion do not bypass that seam by (137.U23)--(137.U25).

## 5. Required controls and outcomes

| Control | Equation-specific outcome |
|---|---|
| product energy | **Pass, revision verified.**  Equations (137.C6)--(137.C8) prove the upper bound (137.C2), now described only as an upper envelope; they prove no two-sided or positive mass statement. |
| Cauchy scalar capacity | **No closure.**  Equation (137.U9) remains \(L^{1/2-o(1)}\) above target. |
| radical parametrization | **Pass, revision verified.**  Equations (137.C10a)--(137.C10b) now include the required \(\sqrt D\ll A\ll L\) shell constraints and factorization count. |
| exact nonsquare resonance | **Pass with scope.**  Equation (137.U13) is phase one when \(X=Ds^2\); (137.U2) makes one fixed channel target-safe but gives no actual lower mass. |
| summation over radicals | **No closure.**  Equation (137.U14) restores \(L^{2+o(1)}\) absolute capacity. |
| B-process modes | **Pass as formal geometry only.**  Equations (137.U15)--(137.U16) count the full derivative range and absolute stationary capacity, not nonzero physical modes or a bound for \(C_L\). |
| residue-to-dual map | **Pass.**  Equation (137.U18) is one-to-one and onto, so the factor \(1/h\) survives. |
| stationary point, phase, and Hessian | **Pass.**  Equation (137.U19) has the correct sign, positive-mode restriction, and powers of \(X,h,r\). |
| profile and Jacobian | **Pass.**  Equation (137.U20) exactly restores \(W(r/y)\) and gives \(2J^{-1/2}\). |
| completion/self-return | **Pass, revision verified.**  Equation (137.C17a) includes \(2e(-1/8)\), \(1/h\), the starred inherited \(r\)-endpoint convention, and is explicitly only the stationary principal family, not an owner-complete finite identity. |
| boundary and square owners | **Retain.**  Endpoints, crossings, nonstationary modes, remainders, and square subtraction cannot be silently included in (137.U21). |
| divisor switch | **Pass.**  Equation (137.U23) is an involution with a transformed literal profile and unchanged incidence count, not a smaller dyadic sum. |
| full-divisor continuation | **Pass, revision verified.**  The paragraph after (137.C18) leaves the complement uncontrolled and says only importing the desired theorem is circular; an independent localized estimate remains admissible. |
| coefficient directionality | **Retain as a method control only.**  Arbitrary phase alignment rules out coefficient-uniform reasoning but is neither a physical obstruction nor a lower bound. |

## 6. Dependencies and exact artifacts used

This post-unmask review used:

1. `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/candidates/conductor_round137_product_fibre_energy_and_self_return.md`;
2. `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reports/blind_truncated_chi4_divisor_phase_feasibility.md`;
3. `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reports/product_fibre_bprocess_circularity_hostile_audit.md` for comparison of the already derived owner-preserving completion formula.

Every displayed calculation above was recomputed analytically.  No numerical experiment, symbolic experiment, web source, external theorem import, shared-state edit, or sibling-file edit was used.

## 7. Recommended state effect

Return **green** for the revised candidate.  The six requested repairs are all present and equation-consistent:

1. (137.C2) is an \(L^2\log L\) upper energy envelope, with no lower-energy claim.
2. (137.C10a)--(137.C10b) give the complete radical-shell ledger, while (137.C12) is correctly a conditional, target-safe phase-one channel.
3. (137.C13)--(137.C14) call the \(J/L\) modes and \(\sqrt{JL}\) ledger coefficient-free and formal and deny nonzero actual mass at every mode.
4. (137.C15)--(137.C17a) preserve the bijection \((a,k)\mapsto r\), \(1/h\), \(2e(-1/8)L^{3/2}J^{-1/2}\), positive starred mode range, \(W(r/y)\), and every boundary, remainder, and square owner.
5. (137.C17b) records the exact involutive divisor switch with the transformed literal height profile.
6. (137.C18) and its following paragraph scope circularity only to importing the desired Gauss-circle conclusion and explicitly allow a genuinely independent localized radial estimate, while retaining the uncontrolled complement.

Recommend retaining the two positive structural lemmas and the scoped transform self-return as candidate evidence, and closing the audited route under `product_fibre_no_go`.  Do not promote a target bound, strict product-fibre reduction, arbitrary-coefficient derivative theorem, physical resonance lower bound, divisor-switch contraction, or full-divisor replacement.  The next required input remains a fixed-centre signed estimate for the exact truncated coefficient that saves \(L^{1/2-o(1)}\) and does not prove itself through (137.C17a) or the desired Gauss-circle bound.
