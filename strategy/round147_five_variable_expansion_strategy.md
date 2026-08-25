# Round 147 strategy report: five-variable coefficient expansion

- Role: bounded strategy evaluation
- Authoritative graph SHA-256: `1dc79cf41e0dea8888341e944c5d0bf025d87f22cfaa282da34fcd10eecd04f5`
- Allocation: 100% analytic and algebraic; 0% numerical

## 1. Result

The Round-145 coefficient can be opened exactly into five positive
variables \((\gamma,a,b,d,e)\).  On this lift the phase is

\[
 f(\gamma,a,b,d,e)=\sqrt N\,\gamma ab\sqrt{de},
\]

and its five-dimensional relative-coordinate Hessian is nondegenerate,
with determinant \(3/4\).  This determinant is algebraically correct but
does **not** define a genuinely new proof interface.  The lift is
multiplicity one and is exactly inverted by

\[
 h=\gamma da^2,\qquad r=\gamma eb^2.
\]

Consequently the five-variable scalar is the old signed
\((h,r)\)-product wave, with the accepted small-square-factor condition
written in factor coordinates.  It is not overparameterized in the
counting sense, but it is an invertible over-resolution of the same
incidences.  Its box capacity is still

\[
 \ll_{\varepsilon,V}X^\varepsilon\frac{M^{1/4}}{T},
 \qquad T\asymp \gamma ab,
\]

and the mandatory face \(\gamma=a=b=1\), namely \(t=1\), is precisely
the owner-sized rank-one \((d,e)\) cone left open by Round 146.

This gives a rigorous strategy no-go for the proposal

\[
 \text{``open }\kappa_t(d,e)\text{, invoke the nonzero five-Hessian,
 and gain by a coefficient-blind transform or modulus.''}
\]

It is not a no-go for a new theorem that uses the literal
\(\chi_4\)-signs and all arithmetic correlations.  In particular, the
\(t=1\) face has a potentially genuinely new multiplicative interface:
after ratio Mellin inversion its exact Dirichlet series is
\(\zeta(w+z)L(w-z,\chi_4)H(w,z)\), with an absolutely convergent
squarefree correction in the initial shifted critical region.  A
uniform generalized-divisor Voronoi formula for this exact product
would use arithmetic structure that the five-Hessian does not see.
The recommended Round-147 objective is therefore a \(t=1\)
ratio-Mellin/Voronoi feasibility gate, not a full five-variable Hessian
campaign.

## 2. Exact statement and hypotheses

Retain the accepted notation

\[
 R=X^{1/4},\qquad N=\lfloor X\rfloor,\qquad
 \mathcal I_M=\mathbb N\cap[M,B_M),\quad B_M\leq 2M,
\]

with the literal terminal truncation, disjoint half-open blocks, fixed
positive direction, and the inherited profile \(V_{\rm low}\).  Put
\(T_M=\lceil M^{1/4}\rceil\).  The exact unmasked Round-146 scalar is

\[
\boxed{
\begin{aligned}
 \mathfrak U_N^<=
 \sum_M\ \sum_{\substack{\gamma,a,b,d,e\geq1\\
          \mu^2(\gamma de)=1\\
          2\nmid \gamma eb\\
          \gamma ab<T_M\\
          \gamma^2a^2b^2de\in\mathcal I_M\\
          eb^2>4da^2}}
 &(\gamma^2a^2b^2de)^{-3/4}
 V_{\rm low}\!\left(\frac{R^2\gamma^2a^2b^2de}{N}\right)\\
 &\times\chi_4(\gamma e)
 e\!\left(+\sqrt N\,\gamma ab\sqrt{de}\right).
\end{aligned}}
\tag{147.S1}
\]

Every condition in (147.S1) is literal.

- \(\mu^2(\gamma de)=1\) says simultaneously that
  \(\gamma,d,e\) are squarefree and pairwise coprime.  An exact
  expanded version is

  \[
  \mu^2(\gamma)\mu^2(d)\mu^2(e)
  \sum_{u\mid(\gamma,d)}\mu(u)
  \sum_{v\mid(\gamma,e)}\mu(v)
  \sum_{w\mid(d,e)}\mu(w).
  \tag{147.S2}
  \]

  Equivalently, the compact squarefree projector is
  \(\mu^2(\gamma de)=\sum_{q^2\mid\gamma de}\mu(q)\).  This latter
  divisor condition is joint; it is not a one-variable tensor
  decomposition without a further prime-allocation argument.
- The parity condition is exactly that \(\gamma,e,b\) are odd.
  The variable \(d\) may be even, \(a\) is unrestricted, and the
  entire \(2\)-adic valuation of \(t=\gamma ab\) lies in \(a\).
- There is no condition \((a,b)=1\), no condition between \(a\) or
  \(b\) and \(\gamma de\), and no additional full-gcd condition.
- The character is
  \(\chi_4(\gamma e)=\chi_4(\gamma)\chi_4(e)\), because \(b\) is
  odd and \(\chi_4(b^2)=1\).
- The cone is the strict inequality \(eb^2>4da^2\).  Equality is
  impossible because its left side is odd and its right side is
  divisible by four.
- The product, small-square-factor, and phase identities are

  \[
  m=\gamma^2a^2b^2de,\qquad s=de,\qquad
  t=\gamma ab<T_M,qquad
  e(t\sqrt{Ns})=e(\sqrt N\,\gamma ab\sqrt{de}).
  \tag{147.S3}
  \]

No nearest-square mask remains.  The profile, product staircase,
clipped endpoints, squarefree projector, parity, character, cone,
fixed centre, and individual positive complex direction do remain.

## 3. Proof or derivation

### 3.1 Multiplicity-one derivation and exact return to \((h,r)\)

For one ordered incidence \(hr=st^2\), let \({\rm sf}(n)\) denote
the squarefree kernel and set

\[
 \gamma=(\operatorname{sf}(h),\operatorname{sf}(r)),\qquad
 d=\frac{\operatorname{sf}(h)}\gamma,\qquad
 e=\frac{\operatorname{sf}(r)}\gamma.
\]

Then \(\gamma,d,e\) are pairwise coprime and squarefree.  There are
unique positive \(a,b\) for which

\[
 h=\gamma da^2,\qquad r=\gamma eb^2.
\tag{147.S4}
\]

Conversely, every tuple satisfying the squarefree and coprimality
conditions in (147.S1) reconstructs exactly one ordered pair by
(147.S4).  Moreover

\[
 hr=de(\gamma ab)^2,qquad
 \operatorname{sf}(hr)=de,qquad
 \sqrt{\frac{hr}{\operatorname{sf}(hr)}}=\gamma ab.
\tag{147.S5}
\]

The parity, character, and cone identities are

\[
 r\text{ odd}\iff 2\nmid\gamma eb,qquad
 \chi_4(r)=\chi_4(\gamma e),\qquad
 r>4h\iff eb^2>4da^2.
\tag{147.S6}
\]

Thus (147.S1) is equivalently

\[
\boxed{
 \sum_M\ \sum_{\substack{h,r\geq1\\hr\in\mathcal I_M\\
        r\ \operatorname{odd},\ r>4h\\
        \sqrt{hr/\operatorname{sf}(hr)}<T_M}}
 (hr)^{-3/4}V_{\rm low}(R^2hr/N)\chi_4(r)
 e(+\sqrt{Nhr}).}
\tag{147.S7}
\]

Equation (147.S7) proves the exact strategy diagnosis: opening
\(\gamma,a,b,d,e\) removes the factor-count notation
\(\kappa_t(d,e)\), but it simply returns to the original signed
divisor incidence.  The Round-145 complement with
\(\sqrt{hr/\operatorname{sf}(hr)}\geq T_M\) is already target-safe;
no further scalar has been reduced.

### 3.2 Aspect-ratio capacity and short faces

On a dyadic five-box write

\[
 \gamma\asymp G,\quad a\asymp A,\quad b\asymp B,
 \quad d\asymp D,\quad e\asymp E,
 \qquad T=GAB.
\]

Nonempty support requires

\[
 G^2A^2B^2DE\asymp M,qquad T^2DE\asymp M,qquad
 EB^2\gg DA^2.
\tag{147.S8}
\]

The number of lattice points before the squarefree and cone cuts is at
most \(O(GABDE)=O(M/T)\).  Since the physical weight is
\(M^{-3/4}\), a fixed box has the lawful coefficient-envelope price

\[
 \boxed{
 |\mathfrak U_{M;G,A,B,D,E}|
 \ll_{\varepsilon,V}X^\varepsilon\frac{M^{1/4}}T.}
\tag{147.S9}
\]

Summing the factor boxes costs only divisor/logarithmic powers, already
absorbed by \(X^\varepsilon\).  Therefore the five-variable lift has
exactly the Round-145/146 capacity; it does not bank a factorization
saving.

Put \(H=GDA^2\) and \(Q=GEB^2\), the scales of \(h\) and \(r\).
The cone gives \(Q>4H\) and \(HQ\asymp M\), hence

\[
 H\ll\sqrt M,\qquad Q\gg\sqrt M,qquad
 D\ll\sqrt M,qquad E\gg\frac{\sqrt M}{T^2}.
\tag{147.S10}
\]

The mandatory faces are not lower-order consequences of (147.S9).

- \(G=A=B=1\) is exactly \(t=1\), with scalar

  \[
  \sum_M\sum_{\substack{d,e\geq1\\
       \mu^2(de)=1,\ e\ \operatorname{odd},\ e>4d\\de\in\mathcal I_M}}
  (de)^{-3/4}V_{\rm low}(R^2de/N)\chi_4(e)e(+\sqrt{Nde}).
  \tag{147.S11}
  \]

  Its available top-block capacity is \(M^{1/4+o(1)}\), or
  \(R^{1/2+o(1)}\).  The five-dimensional Hessian is unavailable on
  this singleton three-coordinate face.
- Each of \(G=1\), \(A=1\), and \(B=1\) occurs on genuine support;
  a theorem requiring five growing side lengths misses mandatory
  arithmetic strata.
- \(D=1\) is structurally present.  In particular
  \(G=A=B=D=1\), \(e=p>4\) prime, has coefficient
  \(\chi_4(p)\neq0\).
- \(E=1\) is empty in the strict small-\(t\) range.  Indeed
  \(e^2>4m/t^4\), whereas \(t^4<M\leq m\).  Fixed bounded \(E\)
  forces \(T\) into the already target-safe terminal shell, but this
  does not remove growing short-\(E\) boxes.

### 3.3 The genuinely different fixed-face multiplicative interface

The \(t=1\) face has more structure than its rank-one Hessian records.
Before imposing the cone, introduce product and ratio Mellin variables
by assigning \(d\) the exponent \(w+z\) and \(e\) the exponent
\(w-z\).  The exact arithmetic Dirichlet series is

\[
 \mathcal D_1(w,z):=
 \sum_{\substack{d,e\geq1\\\mu^2(de)=1\\e\ \operatorname{odd}}}
 \frac{\chi_4(e)}{d^{w+z}e^{w-z}}.
\tag{147.S12}
\]

For an odd prime \(p\), put

\[
 x_p=p^{-(w+z)},\qquad
 y_p=\chi_4(p)p^{-(w-z)}.
\]

Because \(de\) is squarefree, the local choices are exactly: put
\(p\) in neither variable, in \(d\), or in \(e\).  Hence the local
factor is \(1+x_p+y_p\).  It follows identically that

\[
\boxed{
 \mathcal D_1(w,z)=\zeta(w+z)L(w-z,\chi_4)H(w,z),}
\tag{147.S13}
\]

where

\[
\begin{aligned}
 H_2(w,z)&=(1+2^{-(w+z)})(1-2^{-(w+z)})
          =1-2^{-2(w+z)},\\
 H_p(w,z)&=(1+x_p+y_p)(1-x_p)(1-y_p),\qquad p>2,\\
 H(w,z)&=H_2(w,z)\prod_{p>2}H_p(w,z).
\end{aligned}
\tag{147.S14}
\]

For \(p>2\),

\[
 H_p=1-x_p^2-y_p^2-x_py_p+x_p^2y_p+x_py_p^2.
\tag{147.S15}
\]

Thus \(H\) converges absolutely whenever
\(\Re(w+z)>1/2\) and \(\Re(w-z)>1/2\).  The sharp cone has the exact
Perron representation, initially for \(\Re z>0\),

\[
 \mathbf1_{e>4d}
 =\frac1{2\pi i}\int_{(c)}\left(\frac e{4d}\right)^z\frac{dz}{z},
\tag{147.S16}
\]

with its principal-value/boundary convention retained when contours are
moved.  Product Mellin inversion supplies \(w\).  Consequently the
full cone factor is
\(4^{-z}\zeta(w+z)L(w-z,\chi_4)H(w,z)\): a shifted degree-two
product convolved with the absolutely convergent coefficients of
\(H\).

This is analytically different from the five-dimensional curvature
claim.  It compresses the exact \(t=1\) signs into two functional
equations and remains meaningful when \(G=A=B=1\), precisely where the
five-Hessian disappears.  A generalized-divisor Voronoi formula uniform
in the ratio shift \(z\), followed by a signed estimate for the
positive square-root kernel, could therefore be a genuinely new route.
However, factorization alone is not new enough: Round 141 already
exposed the related unsquarefree factor
\(4^{-z}\zeta(w+z)L(w-z,\chi_4)\), and its canonical transforms did not
close the owner.  Any Round-147 novelty must come from a source-legal
uniform shifted Voronoi theorem for the exact \(H\)-convolution and a
strictly favorable power ledger, not from restating (147.S13).

### 3.4 Hessian and why its determinant is coordinate-induced

For a monomial \(f=c\prod_{i=1}^n x_i^{\alpha_i}\), one has

\[
 f^{-1}\operatorname{diag}(x_i)\nabla^2f
 \operatorname{diag}(x_i)
 =\alpha\alpha^{\!T}-\operatorname{diag}(\alpha),
\tag{147.S17}
\]

and the matrix determinant lemma gives

\[
 \det\bigl(\alpha\alpha^{\!T}-\operatorname{diag}(\alpha)\bigr)
 =(-1)^n\left(1-\sum_i\alpha_i\right)\prod_i\alpha_i.
\tag{147.S18}
\]

For (147.S1), in the order \((\gamma,a,b,d,e)\),
\(\alpha=(1,1,1,1/2,1/2)\).  Therefore

\[
 K_5=
 \begin{pmatrix}
 0&1&1&1/2&1/2\\
 1&0&1&1/2&1/2\\
 1&1&0&1/2&1/2\\
 1/2&1/2&1/2&-1/4&1/4\\
 1/2&1/2&1/2&1/4&-1/4
 \end{pmatrix},
 \qquad \boxed{\det K_5=\frac34},
\tag{147.S19}
\]

and

\[
 \det\nabla^2f
 =\frac{3f^5}{4\gamma^2a^2b^2d^2e^2}.
\tag{147.S20}
\]

The same formula exposes the coordinate artifact:

\[
\begin{array}{c|c|c}
\text{coordinates}&\alpha&\det K\\ \hline
(h,r)&(1/2,1/2)&0\\
(t,d,e)&(1,1/2,1/2)&1/4\\
(\gamma,a,b,d,e)&(1,1,1,1/2,1/2)&3/4.
\end{array}
\tag{147.S21}
\]

All three rows describe the same phase values after exact grouping or
ungrouping.  Splitting a product can therefore manufacture a nonzero
ordinary Hessian without manufacturing arithmetic oscillation.  In
particular, every pure second derivative in \(\gamma,a,b\) vanishes;
the determinant is carried entirely by mixed derivatives.

For completeness, the ideal smooth five-variable stationary transform
also supplies no modulus saving.  Let
\(F=\sqrt{NM}\) and \(V_5=GABDE\asymp M/T\).  The gradient image has
upper lattice capacity \(O(F^5/V_5)\), while one stationary integral
has size \(O(V_5/F^{5/2})\).  Aliaswise triangle inequality therefore
costs \(F^{5/2}\), or

\[
 M^{-3/4}F^{5/2}=N^{5/4}M^{1/2}
\tag{147.S22}
\]

after the physical weight.  This is an adverse upper ledger, not a
lower bound.  The ideal critical phase for aliases
\((u_\gamma,u_a,u_b,u_d,u_e)\) is

\[
 -3\left(
 \frac{2u_\gamma u_a u_b\sqrt{u_du_e}}{\sqrt N}
 \right)^{1/3}.
\tag{147.S23}
\]

It again depends only on products of alias variables, and a second
Legendre transform returns the primal phase only at the smooth
phase level.  Arithmetic coefficients, cone boundaries, squarefree
cuts, and short faces do not follow this formal involution.

## 4. First doubtful or unproved step

The first unproved step for the five-variable proposal is an
owner-complete, sign-sensitive estimate for the literal amplitude in
(147.S1), not the Hessian calculation.
On a box with \(T=GAB\), a boxwise route would need the unweighted
estimate

\[
 \sum_{\text{literal }G,A,B,D,E\text{ box}}
 \mu^2(\gamma de)\mathbf1_{2\nmid\gamma eb}
 \chi_4(\gamma e)\mathbf1_{eb^2>4da^2}
 e(\sqrt N\,\gamma ab\sqrt{de})
 \ll_{\varepsilon,V}M^{3/4}X^\varepsilon,
\tag{147.S24}
\]

or a stronger aggregate theorem that proves the required cancellation
between boxes.  Relative to raw capacity, (147.S24) asks for a factor
\(M^{1/4}/T\).  At \(t=1\) this is the full factor \(M^{1/4}\).

Neither (147.S2), the nonzero determinant (147.S19), nor a smooth
Mellin treatment of the radial profile proves (147.S24).  A lawful
tensor reduction would still have to prove a subpolynomial nuclear
norm after jointly separating the squarefree/coprimality projector,
the strict cone, clipped product prefixes, and every short face.  Even
such a decomposition would only repair a coefficient hypothesis; it
would not supply the missing target-power exponential-sum theorem.

For the more promising fixed-face interface, the first unproved step is
sharper: derive or source-audit a generalized-divisor Voronoi formula
for

\[
 \zeta(w+z)L(w-z,\chi_4)H(w,z)
\tag{147.S25}
\]

that is uniform over the full ratio-Mellin height required by the sharp
cone or by a separately proved target-safe smoothing.  It must retain
the \(H\)-convolution, clipped radial prefixes, fixed real centre, and
individual positive square-root direction.  One must then show that
the transformed main term and every polar, boundary, and dual term have
total weighted size \(O(X^\varepsilon)\).  No accepted theorem currently
supplies this statement, and the Round-141 self-return control must be
retested rather than assumed absent.

The sharpest first face statement is the inherited prefix estimate

\[
 \sup_{M\leq U\leq B_M}
 \left|
 \sum_{\substack{M\leq de<U\\
       \mu^2(de)=1,\ e\ \operatorname{odd},\ e>4d}}
 \chi_4(e)e(+\sqrt{Nde})
 \right|
 \ll_{\varepsilon,V}M^{3/4}X^\varepsilon.
\tag{147.S26}
\]

The smooth weight in (147.S11) then follows by partial summation.  No
accepted argument or audited source proves (147.S26).

## 5. Required control tests and outcomes

1. **Multiplicity and inverse map: GREEN.**  Prime valuations prove
   (147.S4)--(147.S6), with exactly one tuple per ordered \((h,r)\)
   incidence.
2. **Möbius and coprimality: GREEN.**  Equations (147.S1)--(147.S2)
   retain squarefreeness and all three pairwise gcd conditions.  No
   illegal gcd involving \(a,b\) is inserted.
3. **Parity and character: GREEN.**  Exactly \(\gamma,e,b\) are odd;
   \(d,a\) retain their legal even cases, and the sign is
   \(\chi_4(\gamma e)=\chi_4(r)\).
4. **Cone, product, profile, and endpoints: GREEN.**  The strict cone,
   exact small-\(t\) ceiling, literal product block, clipped endpoint,
   profile, fixed centre, and positive direction all occur in
   (147.S1).
5. **Aspect ratio and capacity: GREEN as an upper ledger.**
   Equations (147.S8)--(147.S10) reproduce
   \(M^{1/4}/T\); no factorization gain is present.
6. **Five-dimensional Hessian: GREEN algebraically, ADVERSE
   strategically.**  The determinant is \(3/4\), but (147.S21) proves
   that it changes under an exact multiplicity-one product split.
7. **Short faces: ADVERSE and mandatory.**  The \(t=1\), \(D=1\),
   and one-or-more of \(G,A,B=1\) faces survive.  Only \(E=1\) and
   fixed bounded \(E\) are already disposed of as in Round 146.
8. **Slow-frequency control: ADVERSE to derivative-gap arguments.**
   The accepted family \(N=sL^2+1\) still makes
   \(e(\gamma ab\sqrt{Ns})\) slowly rotating over legal factor ranges.
   This is not a signed lower bound.
9. **Full transform followed by modulus: ADVERSE.**  The upper price
   (147.S22) is far above target, and (147.S23) preserves product-fibre
   structure at phase level.
10. **Ratio-Mellin Euler product: GREEN algebraically, OPEN
    analytically.**  Equations (147.S12)--(147.S16) give the exact
    \(\zeta L H\) factorization.  A uniform generalized-divisor
    Voronoi formula, its transformed coefficient, and its complete
    target-power ledger are not proved.
11. **Comparison with five-variable curvature: DECISIVE.**  The
    \(\zeta L H\) interface survives on \(t=1\) and uses the exact
    signs; the five-Hessian vanishes there and adds no information to
    this multiplicative factorization.
12. **Owner scope: GREEN.**  The analysis proves no bound for
    \(\mathfrak U_N^<\), lower GAR, either direct M1 parent, M9-M1,
    any M2 owner, endpoint uniformity, M9, the bridge, the quarter
    theorem, or a better global exponent.

## 6. Dependencies and exact artifacts used

This report uses only the following accepted or round-closing artifacts:

- `protocol.md`;
- `state/proof_obligations.yml` at graph SHA-256
  `1dc79cf41e0dea8888341e944c5d0bf025d87f22cfaa282da34fcd10eecd04f5`;
- `state/active_campaign.yml` recording completed Round 146;
- `rounds/codex-managed/m9-m1-lower-cone-squarefree-kernel-linearization-gate/candidates/conductor_round145_squarefree_kernel_reduction.md`;
- `rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/candidates/conductor_round146_three_variable_unmasking_and_dispersion_no_go.md`;
- `rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/reviews/conductor_round146_three_variable_adjudication.md`;
- `rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/controls/conductor_round146_controls.md`;
- `rounds/codex-managed/m9-m1-lower-cone-three-variable-hessian-dispersion-gate/synthesis.md`.

No external theorem is invoked, no numerical experiment is used, and
no claim is decided by analogy or vote.

## 7. Recommended state effect and frozen Round-147 objective

Recommended state effect: **no graph mutation from this strategy
report**.  Retain (147.S1) as a literal diagnostic expansion, and reject
only the inference that its larger Hessian determinant or simpler
pointwise sign automatically creates a new cancellation theorem.  Do
not record a global impossibility: a future exact-coefficient theorem
could still exploit these factor coordinates.

Recommended frozen Round-147 objective:

\[
\boxed{
\begin{minipage}{0.88\linewidth}
Starting from the exact factorization
\(\mathcal D_1(w,z)=\zeta(w+z)L(w-z,\chi_4)H(w,z)\), determine whether a
source-legal generalized-divisor Voronoi formula, uniform in the full
ratio shift and every clipped radial prefix, proves the mandatory
unmasked \(t=1\) squarefree-cone estimate (147.S26).  Retain the exact
\(\chi_4(e)\) sign, \(H\)-convolution, squarefree/coprimality support,
strict cone or a proved target-safe smoothing, all aspect ratios
including \(D=1\), fixed centre, positive complex direction, polar and
boundary terms, and the complete primal/dual power ledger.  Prove the
face bound, produce an owner-complete strict reduction, or identify the
first exact Voronoi-hypothesis, self-return, or power obstruction.
\end{minipage}}
\tag{147.S27}
\]

The appropriate terminal labels are
`t1_voronoi_bound`, `strict_t1_voronoi_reduction`, and
`t1_voronoi_no_go`.
Only after the \(t=1\) face is owned should the program test bounded
\(t>1\) or a genuinely sign-sensitive five-variable interior theorem.
This ordering attacks the face that every five-dimensional theorem
requiring growing \(G,A,B\) necessarily omits.
