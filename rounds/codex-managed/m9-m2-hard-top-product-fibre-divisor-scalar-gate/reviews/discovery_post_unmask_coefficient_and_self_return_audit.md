# Discovery post-unmask audit of the coefficient bounds and canonical self-return

## 1. Result and verdict

**Verdict: green.**  The revised conductor candidate's two positive
upper bounds are mathematically sound:

\[
 \sum_n |C_L(n)|^2\ll L^2\log(2L)
 \tag{137.R1}
\]

and, for each squarefree \(D>1\),

\[
 \sum_{\substack{n\asymp L^2\\ \operatorname{sf}(n)=D}}
 |B_L(n)|
 \ll_\varepsilon
 \left(1+\frac{L}{\sqrt D}\right)L^\varepsilon.
 \tag{137.R2}
\]

The exact-cone energy parametrization and the candidate's
maximum-shell count are compatible descriptions of the same
multiplicative energy.  Its revised squarefree-kernel proof now states
\(\sqrt D\ll A\ll L\), controls every shell cross term, records the
parity restrictions, and passes from a bounded contribution per
incidence to (137.R2) lawfully.

The divisibility-completed \(n\)-B-process and the direct \(m\)-B-process
also agree exactly at the stationary-principal level.  The residue
factor \(1/h\), the Hessian Jacobian, the universal phase, and all
literal profiles combine to give

\[
 \frac{2e(-1/8)L^{3/2}}{\sqrt J}
 \sum_{\substack{h\ {\rm odd}}}
 \frac{\chi_4(h)\eta_L(h)\Phi(h/(H+1))}{h}
 \sum_r^\star W(r/y)e\!\left(\frac{Xh}{4r}\right),
 \tag{137.R3}
\]

with positive stationary \(r\) in the inherited range
\(J/2\le r\le J\).  This is the returned reciprocal stationary
principal family, not by itself an exact finite-sum equality.

The revised candidate also gives the complete phase-one classification:
if \(J\sqrt D=p/q\) in lowest terms, the phase-one points in the
\(D\)-channel are exactly \(q\mid t\); an irrational \(J\sqrt D\)
gives none; and the whole channel is phase one exactly when
\(J\sqrt D\in\mathbb Z\), equivalently \(XD\) is an integer square.
At one fixed centre, exact nonsquare phase-one points lie in at most
one squarefree channel.  The candidate correctly treats this as a
target-safe upper capacity, not a lower bound.

All previously requested scope corrections are present: (137.R1) is
called an upper energy envelope, the formal mode ledger is
coefficient-free, the returned expression is explicitly only a
stationary principal family with every correction owner retained, and
the full-divisor statement distinguishes circular import from a new
independent radial estimate.  The closure product_fibre_no_go is
therefore green with no residual defect.

## 2. Exact statement and hypotheses

Retain

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=\frac{X}{y^2},\qquad
 H=\lfloor yX^{-1/4}\rfloor,
 \tag{137.R4}
\]

one literal half-open polynomial intermediate block \(1\ll L\ll H\),
odd \(h\), and

\[
 \left\lceil\frac h4\right\rceil\le m\le h.
 \tag{137.R5}
\]

Write

\[
 w_{L,X}(h,m)=
 \eta_L(h)\Phi\!\left(\frac h{H+1}\right)
 W\!\left(\sqrt{\frac{q_Xh}{4m}}\right)
 \tag{137.R6}
\]

on the hard cone and extend it by zero elsewhere.  The coefficient and
normalized nonsquare coefficient are

\[
 C_L(n)=
 \sum_{\substack{hm=n,\ h\ {\rm odd}\\
                  \lceil h/4\rceil\le m\le h}}
 \chi_4(h)w_{L,X}(h,m),
 \qquad
 B_L(n)=L^{3/2}n^{-3/4}C_L(n)1_{n\ne\square}.
 \tag{137.R7}
\]

Only uniform boundedness of the three fixed profiles is used in
(137.R1)--(137.R2).  No positivity, lower envelope, multiplicativity,
smoothness in \(n\), bounded variation, or additive-twist estimate is
assumed.  The square sector is removed or restored only through its
existing norm-triangle owner.

The approved scope is:

1. (137.R1) and (137.R2) are upper bounds only;
2. the mode count \(J/L\) and capacity \(\sqrt{JL}\) concern the
   coefficient-free stationary geometry;
3. (137.R3) is a stationary principal family with inherited endpoint,
   support-crossing, nonstationary, remainder, and square owners; and
4. completion to \(r_2(n)/4\) is an exact algebraic split, not an
   equivalence between the truncated scalar and a proved Gauss-circle
   estimate.

## 3. Proof and reconciliation

**Compatibility of the two energy counts.**  Boundedness of
\(w_{L,X}\), expansion of the square, and deletion of signs give

\[
 \sum_n|C_L(n)|^2
 \ll
 \#\{(h_1,m_1,h_2,m_2):h_1m_1=h_2m_2,
                         h_i,m_i\asymp L\}.
 \tag{137.R8}
\]

Put \(g=(h_1,h_2)\) and

\[
 h_1=ga,\qquad h_2=gb,\qquad
 m_1=bt,\qquad m_2=at,\qquad (a,b)=1.
 \tag{137.R9}
\]

The two literal cone conditions imply

\[
 \max\!\left(\frac a{4b},\frac b{4a}\right)
 \le\frac tg\le
 \min\!\left(\frac ab,\frac ba\right),
 \qquad \frac12\le\frac ab\le2.
 \tag{137.R10}
\]

Thus \(a\asymp b\), and for fixed \(a,b\) there are
\(O((1+L/a)^2)\) choices of \(g,t\).  Summing over the \(O(a)\)
eligible values of \(b\) gives

\[
 \sum_{a\ll L}O(a)(1+L/a)^2
 \ll L^2\log(2L).
 \tag{137.R11}
\]

The candidate instead groups by \(M=\max(a,b)\), counts \(O(M)\)
ordered pairs, and bounds both \(g\) and \(t\) by \(O(L/M+1)\).
Equation (137.R10) shows that \(M\asymp a\asymp b\), so its sum is
exactly the same envelope as (137.R11).  Oddness, the exact ceiling,
the profiles, and nonsquare deletion only restrict this absolute
count.  Hence (137.R1) is green.  It gives
\(\|B_L\|_2\ll L\sqrt{\log(2L)}\), and Cauchy over \(O(L^2)\)
products still gives \(O(L^2\sqrt{\log(2L)})\), not the target.

**Fixed squarefree-kernel count.**  Taking absolute values before the
fibre sum and using \(L^{3/2}n^{-3/4}\asymp1\) gives

\[
 \sum_{\substack{n\asymp L^2\\\operatorname{sf}(n)=D}}|B_L(n)|
 \ll
 \#\{(h,m): (h,m)\text{ lies in (137.R5)},\
             \operatorname{sf}(hm)=D\}.
 \tag{137.R12}
\]

For one such pair put \(g=(h,m)\), \(h=ga\), \(m=gb\), and
\((a,b)=1\).  Since \(hm=g^2ab\),
\(\operatorname{sf}(ab)=D\), and there is a unique decomposition

\[
 a=d_1u^2,\qquad b=d_2v^2,\qquad
 d_1d_2=D,
 \tag{137.R13}
\]

where \(d_1,d_2\) are coprime squarefree factors.  Coprimality
conditions on \(u,v,d_1,d_2\) may be dropped for an upper bound.  The
cone gives \(b/a\in[1/4,1]\), so a bounded number of dyadic
decompositions reduces to \(a,b\asymp A\).  For a fixed ordered
factorization \(d_1d_2=D\), the number of triples \(u,v,g\) on that
shell is at most

\[
 \left(\sqrt{\frac A{d_1}}+1\right)
 \left(\sqrt{\frac A{d_2}}+1\right)
 \left(\frac LA+1\right).
 \tag{137.R14}
\]

A nonempty shell has \(d_1,d_2\ll A\), hence
\(\sqrt D\ll A\); it also has \(A\ll L\) because \(g\ge1\) and
\(ga,gb\asymp L\).  These are the decisive shell inequalities, now
explicit in (137.C10b).  They give

\[
 \left(\sqrt{\frac A{d_1}}+1\right)
 \left(\sqrt{\frac A{d_2}}+1\right)
 \ll 1+\frac A{\sqrt D},
\]

and then

\[
 \left(1+\frac A{\sqrt D}\right)
 \left(1+\frac LA\right)
 \ll 1+\frac L{\sqrt D}.
 \tag{137.R15}
\]

There are \(O(\log L)\) shells and
\(2^{\omega(D)}\ll_\varepsilon D^\varepsilon\) ordered
factorizations.  Active \(D\) satisfy \(D\ll L^2\), so the logarithm
and factorization count are absorbed after the standard rescaling of
\(\varepsilon\).  Odd \(h=gd_1u^2\) forces \(g,d_1,u\) odd.  If
\(D\) is even its factor \(2\) must lie in \(d_2\); if \(D\) is odd,
an even \(v\) contributes only an even square factor to \(m\).
Dropping these parity restrictions enlarges the count.  Since the
normalized literal weight attached to each incidence is bounded, the
pair count proves (137.R2).

For the complete exact-phase audit, put
\(\alpha_D=J\sqrt D\).  On \(n=Dt^2\),

\[
 e(J\sqrt n)=1
 \quad\Longleftrightarrow\quad
 \alpha_Dt\in\mathbb Z.
\]

If \(\alpha_D=p/q\) in lowest terms, the exact points are precisely
\(q\mid t\); if \(\alpha_D\) is irrational, there are none.  Every
point in the \(D\)-channel is phase one exactly when \(q=1\), or
equivalently

\[
 J\sqrt D\in\mathbb Z
 \quad\Longleftrightarrow\quad
 XD\text{ is an integer square}.
\]

The family \(X=Ds^2\) is a sufficient subfamily, not the full
classification.  If phase-one points \(D_1t_1^2\) and \(D_2t_2^2\)
occur at one fixed centre, their ratio is a rational square.  Since
\(D_1,D_2\) are squarefree, this forces \(D_1=D_2\).  Thus a fixed
centre has at most one exact nonsquare phase-one radical.  Equation
(137.R2) makes all of its exact points target-safe in absolute upper
capacity, but proves neither nonzero mass nor a physical lower bound:
the profiles may vanish and the literal \(\chi_4\)-terms may cancel.
Near resonances remain outside this classification.  Summing
(137.R2) over all \(D\ll L^2\) gives \(L^{2+\varepsilon}\), so the
radical decomposition does not close the target.

**Reconciliation of the two B-processes.**  Resolve divisibility by

\[
 1_{h\mid n}=\frac1h\sum_{c\bmod h}e(cn/h).
 \tag{137.R16}
\]

After Poisson summation in \(n\), let \(k\in\mathbb Z\) and
\(r=kh-c\).  The map \((c,k)\mapsto r\) is bijective for
\(0\le c<h\), so the factor \(1/h\) survives.  With

\[
 \phi_{h,r}(x)=J\sqrt x-\frac rhx,
\]

the positive stationary point, phase, and Hessian are

\[
 x_{h,r}=\frac{Xh^2}{4r^2},\qquad
 \phi_{h,r}(x_{h,r})=\frac{Xh}{4r},\qquad
 \phi''_{h,r}(x_{h,r})=-\frac{2r^3}{Xh^3}.
 \tag{137.R17}
\]

At that point,

\[
 W\!\left(\sqrt{\frac{q_Xh^2}{4x_{h,r}}}\right)=W(r/y),
 \qquad
 x_{h,r}^{-3/4}|\phi''_{h,r}(x_{h,r})|^{-1/2}
 =2J^{-1/2}.
 \tag{137.R18}
\]

Multiplying (137.R18) by \(L^{3/2}/h\), the character, and the
two height profiles gives exactly (137.R3).  Negative curvature gives
the factor \(e(-1/8)\), and the continuous hard face
\(h^2/4\le x\le h^2\) gives positive modes
\(J/2\le r\le J\), with the inherited endpoint convention.

For the direct process, put
\[
 F_h(m)=J\sqrt{hm}.
\]
Then

\[
 F_h'(m_r)=r
 \quad\Longleftrightarrow\quad
 m_r=\frac{Xh}{4r^2},\qquad
 F_h(m_r)-rm_r=\frac{Xh}{4r}.
 \tag{137.R19}
\]

Since \(x=hm\),

\[
 \phi_{h,r}(hm)=F_h(m)-rm,\qquad
 F_h''(m)=h^2\phi_{h,r}''(hm),
\]

and therefore

\[
 \frac1h|\phi_{h,r}''(x_{h,r})|^{-1/2}
 =|F_h''(m_r)|^{-1/2}.
 \tag{137.R20}
\]

Together with

\[
 W\!\left(\sqrt{\frac{q_Xh}{4m_r}}\right)=W(r/y),
\]

equation (137.R20) proves that the \(n\)-completion and direct
\(m\)-process have the same phase, factor
\(2L^{3/2}/(\sqrt J\,h)\), profile, and stationary range.  There is no
missing residue multiplicity, \(h\)-power, \(J\)-power, \(q_X\)-factor,
or Jacobian.

This agreement certifies only the canonical stationary principal
family.  It does not identify the original finite sum with (137.R3)
without the hard endpoint samples, Poisson zero and nonstationary
modes, stationary remainders, support crossings, and square
subtraction.

## 4. First doubtful or unproved step

No residual defect remains in the candidate's two positive lemmas or
its stationary-principal self-return.  Equations
(137.C10a)--(137.C10b) now supply the formerly omitted shell
inequalities and cross-term estimate; the following parity paragraph
supplies the literal odd-height ledger and the bounded-per-incidence
passage to (137.C3).  Equation (137.C12) gives the full rational,
irrational, whole-channel, and fixed-centre one-radical
classification.  Equations (137.C15)--(137.C17a) display the complete
principal coefficient and retain all nonprincipal owners.

The first genuinely unproved mathematical seam, correctly identified
by the candidate, remains the
fixed-centre signed estimate

\[
 \left|\sum_nB_L(n)e(J\sqrt n)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
 \tag{137.R21}
\]

Neither the upper energy envelope (137.R1), the channelwise upper bound
(137.R2), nor the coefficient-free stationary capacity controls the
actual direction of \(C_L(n)\).  Re-expanding divisibility returns
(137.R3), and a second canonical process returns the original
square-root phase.  This is a phase/profile self-return, not a proof of
(137.R21).

The following stronger readings remain forbidden, and the revised
candidate now avoids all three:

1. “near-minimal energy” is not proved, because (137.R1) has no matching
   lower bound; the revised candidate now says “upper
   multiplicative-energy envelope”;
2. an exactly phase-one radical family is not an actual lower bound,
   because its literal coefficient can vanish or cancel; the candidate
   expressly makes this upper-bound qualification; and
3. the formal \(J/L\) stationary modes and \(\sqrt{JL}\) capacity do not
   assert that every mode carries physical coefficient mass; the
   candidate now states this explicitly.

These are retained scope barriers, not residual defects.

## 5. Required controls and outcomes

| Item audited | Verdict | Precise outcome or correction |
|---|---|---|
| Exact product-fibre dictionary | **green** | The ceiling/cone equivalence and normalized coefficient are termwise exact. |
| Multiplicative energy | **green** | The candidate's \(M\)-shell proof and (137.R9)--(137.R11) agree, and the revised candidate calls it an upper energy envelope. |
| Cone compatibility | **green** | The literal inequalities give (137.R10); the candidate's broader dyadic count only overcounts impossible noncomparable pairs. |
| Squarefree decomposition | **green** | Equation (137.R13) is unique after taking \(g=(h,m)\); omitted coprimality restrictions may safely be dropped for an upper bound. |
| Dyadic \(A\)-shell and parity proof | **green** | Equations (137.C10a)--(137.C10b) include \(\sqrt D\ll A\ll L\), every cross term, \(2^{\omega(D)}\), parity, and the bounded per-incidence passage to (137.C3). |
| Exact phase-one classification | **green** | Equation (137.C12) classifies rational and irrational \(J\sqrt D\), whole-channel alignment, and the fixed-centre one-radical consequence; it asserts upper capacity only. |
| Sum over radical channels | **green no-go** | Summation over all \(D\ll L^2\) restores \(L^{2+\varepsilon}\) absolute capacity. |
| Formal dual-mode ledger | **green** | The revised candidate expressly scopes \(J/L\) and \(\sqrt{JL}\) as coefficient-free geometry, not actual mass or a lawful rough-coefficient estimate. |
| Residue-to-dual map | **green** | \((c,k)\mapsto kh-c\) is bijective; no factor \(h\) is gained or lost. |
| Stationary phase and Hessian | **green** | Equations (137.R17)--(137.R18) have the correct sign and all powers of \(X,h,r,J\). |
| Profile restoration | **green** | Both routes give exactly \(W(r/y)\); the height taper and \(\chi_4(h)\) remain unchanged. |
| \(n\)- versus \(m\)-B-process | **green at principal level** | Equation (137.R20) explains the surviving \(1/h\) and matches the factor \(2L^{3/2}/(\sqrt J\,h)\). |
| Full self-return claim | **green at principal level** | Equation (137.C17a) displays (137.R3), calls it the stationary principal family, and retains every endpoint, remainder, crossing, and square owner. |
| Complementary-divisor switch | **green no-go** | It is an exact incidence involution with transformed literal profiles, not a contraction or independent smooth divisor sum. |
| Full-divisor completion | **green** | The revised candidate distinguishes circular import from a genuinely independent localized radial theorem and keeps the complement uncontrolled. |
| Phase-adapted arrays | **reject as physical evidence** | They refute coefficient-uniform arguments only and prove no lower bound for the literal scalar. |
| Target or strict reduction | **reject** | No audited estimate proves (137.R21) or produces a smaller owner-complete survivor. |

## 6. Dependencies and exact artifacts used

This review used:

1. rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/candidates/conductor_round137_product_fibre_energy_and_self_return.md;
2. rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reports/blind_truncated_chi4_divisor_phase_feasibility.md;
3. rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reports/product_fibre_bprocess_circularity_hostile_audit.md;
4. rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reports/literal_product_fibre_divisor_scalar_attack.md; and
5. rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reviews/hostile_post_unmask_completion_and_radical_audit.md.

The energy, radical-shell, residue, Hessian, profile, and Jacobian
calculations were independently recomputed.  No numerical or symbolic
experiment, web source, external theorem, or unlisted artifact was
used.  No candidate, report, shared-state, plan, synthesis, or sibling
review was edited.

## 7. Recommended state effect

Return **green**, preserving product_fibre_no_go.  The current candidate
has implemented every requested correction and is suitable for the
two scoped state effects it recommends:

1. retain (137.C2)--(137.C3), including the complete exact-phase
   classification and the fixed-centre one-radical consequence, as
   upper-bound structural lemmas; and
2. retain (137.C13)--(137.C18) as the coefficient-free curvature
   ledger, stationary-principal self-return, complementary-divisor
   involution, and scoped full-divisor no-go.

No residual correction is required in the audited interfaces.  The
green verdict does not promote a target bound or strict scalar
reduction.  In particular, it licenses no lower energy claim, actual
resonant lower bound, arbitrary-coefficient derivative theorem,
owner-complete finite-sum B-process equivalence, divisor-switch
contraction, or full-\(r_2\) replacement.

The next open input remains a fixed-centre signed theorem for the
literal \(C_L(n)\) that saves \(L^{1/2-o(1)}\) without proving itself
through the returned reciprocal block or by importing the desired
Gauss-circle estimate.  All downstream obligations and the global
exponent remain unchanged.
