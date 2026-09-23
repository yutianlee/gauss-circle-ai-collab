# Round 168 claimant mathematical endpoint/power review

- Campaign: `m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate`
- Reviewed claimant: `reports/literal_pre_mobius_mellin_attack.md`
- Role: independent mathematical seam reviewer
- Verdict: **REVISE**

## 1. Result

The claimant has a correct core, but it is not passable without three repairs.

The following parts pass:

1. the intact local Euler factors, the factorization
   \(D=L(s_1,\chi_4)\zeta(s_2)G\), the larger factorization through
   \(\mathcal H\), and the pole ledger for a shift to
   \(\Re s_j=1/2+\eta\);
2. the disjoint-cardinal-cell interpolation, its exact Mellin identity,
   and the target-safe cardinal realization of the \(s_2=1\) residue;
3. the substantive distinction between that cardinal residue and the
   discrete Perron--Stieltjes residue, which is not automatically small;
4. the smooth radial stationary scale
   \(L^{1+2\eta}(JL)^{-1/2}\), the radial length \(JL\), and the
   resulting \(\sqrt J\) deficit under unweighted pointwise absolute or
   fixed-angular mean-square-plus-Cauchy control;
5. the fixed-\(B\) polylogarithmic-\(L\) full-scalar sector; and
6. the exact algebraic connector obtained by defining
   \(\mathcal S^{\rm rem}_{L,1}=\mathcal S_{L,1}-\mathcal S^{\rm cp}_{L,1}\).

Three claims require revision:

1. The claimed “natural continuous profile plus \(O(LX^\varepsilon)\)
   atoms” is not actually constructed or enumerated.  The count is
   plausible for the displayed finite family of codimension-one faces,
   and the accepted exchange kernel separately counts several exact
   faces, but neither fact supplies the missing literal decomposition in
   this report.  Target-safety of that realization is therefore not yet
   proved.  The cardinal-cell realization remains valid independently.
2. The statement that the factorwise functional equations, or
   approximate functional equations, return *exactly* to the accepted
   Round-162 opening is overclaimed.  The accepted kernel starts from the
   explicit projector opening and then applies physical Poisson.  The
   claimant does not identify the Dirichlet coefficients of \(G\) with
   the \((a,b,c;Q,R)\) opening, track the \(p=2\) branch, gamma factors,
   pole/main terms, AFE truncations and remainders, or recover the literal
   \(q_X,H+1\), floor, star, and endpoint profiles.  What is presently
   justified is only the conditional statement that **if one deliberately
   reopens the original projector as in the accepted kernel and then uses
   its Poisson calculation**, positive collar control has the accepted
   \(\sqrt{JL}\) capacity.
3. The exact hypothesis \(H=\sqrt J\) is false for the accepted literal
   scalar.  The correct definitions are
   \[
   y=\lfloor J\rfloor,\qquad q_X=\frac{X}{y^2},\qquad
   H=\left\lfloor yX^{-1/4}\right\rfloor
    =\sqrt J+O(1).
   \]
   Consequently
   \[
   \frac{\sqrt J}{L}=\frac HL+O(L^{-1}),
   \]
   not \(H/L\) identically.  This does not change the adverse power in
   \(1\ll L\ll H\), but it matters in a report advertised as literal and
   endpoint-exact.

Thus the absolute Mellin-capacity no-go survives after narrowing its
wording, but the claimed functional-equation/AFE self-return and the
continuous-plus-atoms residue cannot yet be retained as proved seams.

## 2. Exact statement and hypotheses

For comparison with the accepted kernels, the literal parameters are

\[
J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
q_X=X/y^2,\qquad
H=\lfloor yX^{-1/4}\rfloor,\qquad 1\ll L\ll H.
\tag{168.V1}
\]

Let

\[
W(n,m)=a_{n,m}e(J\sqrt{nm})
\]

be the already evaluated literal array, including the normalization,
\(q_X\)-ratio profile, \(H+1\)-profile, real-centre floors, stars,
half-open faces, and zero extension.  The arithmetic series is

\[
D(s_1,s_2)=
\sum_{\substack{n,m\ge1\\n\ \mathrm{odd}\\nm\ \mathrm{squarefree}}}
\frac{\chi_4(n)}{n^{s_1}m^{s_2}},
\qquad \Re s_1,\Re s_2>1.
\tag{168.V2}
\]

This review distinguishes four logically separate assertions:

1. an exact cardinal interpolation of the literal lattice array;
2. a proposed natural continuous interpolation plus exceptional lattice
   atoms;
3. the exact discrete mixed-difference/Perron--Stieltjes realization; and
4. a smooth radial-angular capacity model used only to test absolute
   contour estimates.

Only the first and third are exact from the formulas currently displayed.
The fourth is a valid optimistic capacity test.  The second needs the
literal decomposition and face audit described below.

## 3. Proof/derivation

### 3.1 Euler continuation algebra

For odd \(p\), put

\[
x=\chi_4(p)p^{-s_1},\qquad y=p^{-s_2}.
\]

Then

\[
G_p=(1+x+y)(1-x)(1-y)
=1-x^2-y^2-xy+x^2y+xy^2.
\tag{168.V3}
\]

With

\[
P_p=(1-x^2)(1-y^2)(1-xy),
\]

direct subtraction gives

\[
G_p-P_p
=x^2y+xy^2-x^3y-xy^3-x^2y^2+x^3y^3.
\tag{168.V4}
\]

Thus \(\prod_{p\ \mathrm{odd}}G_p/P_p\) converges absolutely in

\[
\Omega=\{\sigma_1,\sigma_2>0:
2\sigma_1+\sigma_2>1,\ \sigma_1+2\sigma_2>1\}.
\]

The two-adic cancellation is also correct.  Indeed,

\[
\prod_{p\ \mathrm{odd}}P_p
=\frac{1}{(1-2^{-2s_1})(1-2^{-2s_2})
\zeta(2s_1)\zeta(2s_2)L(s_1+s_2,\chi_4)},
\]

and multiplication by \(G_2=1-2^{-2s_2}\) cancels the second local
factor.  Hence

\[
G(s_1,s_2)=
\frac{\mathcal H(s_1,s_2)}
{(1-2^{-2s_1})\zeta(2s_1)\zeta(2s_2)
L(s_1+s_2,\chi_4)}.
\tag{168.V5}
\]

Equation (168.V5) is meromorphic in \(\Omega\); denominator zeros are
only possible poles and may be cancelled.  On
\(\sigma_j\ge1/2+\eta\), the direct product for \(G\) is already
absolutely convergent and holomorphic, while all denominator arguments
in (168.V5) have real part greater than one.  Therefore a shift from
\(c_j>1\) to \(1/2+\eta\) crosses only the pole of \(\zeta(s_2)\) at
\(s_2=1\).  This seam passes.

### 3.2 Cardinal, continuous, and Stieltjes residues

For \(\psi\in C_c^\infty((-1/3,1/3))\) with \(\psi(0)=1\), the claimant's

\[
\mathcal B(x,y)=e(J\sqrt{xy})
\sum_{n,m}a_{n,m}\psi(x-n)\psi(y-m)
\tag{168.V6}
\]

is smooth and compactly supported away from the coordinate axes.  The
cell supports are disjoint, so \(\mathcal B(n,m)=W(n,m)\) exactly.  Its
Mellin transform is entire and rapidly decreasing on every fixed vertical
strip.  Absolute convergence of \(D\) on the initial contours and ordinary
Mellin inversion therefore give the claimed exact identity.  These facts
also justify the rectangular contour shift and its single residue

\[
R_\zeta^{\rm card}
=\frac1{2\pi i}\int_{(1/2+\eta)}
\widehat{\mathcal B}(s_1,1)L(s_1,\chi_4)G(s_1,1)\,ds_1.
\tag{168.V7}
\]

On each cardinal cell,

\[
\partial_y(2\pi J\sqrt{xy})=\pi J\sqrt{x/y}\asymp J.
\]

There is no \(y\)-stationary point.  Arbitrarily many integrations by
parts in \(y\), followed by enough \(x\)-integrations to dominate the
polynomial vertical growth of \(L(s_1,\chi_4)\), give a negative power of
\(J\) after paying the finite \(O(L^2)\) cell and derivative costs.
Because \(L\le J^{1/2}\), the cardinal residue is target-safe.  This
argument is legitimate, but the saving is representation-dependent; the
remaining critical-line integral inherits the complexity created by the
chosen interpolation.

The discrete Stieltjes residue is different.  If

\[
\sum_{n\ge1}\rho(n)n^{-s}=L(s,\chi_4)G(s,1)
\]

on an initial line and the mixed difference is the one in the blind
rederivation, then exact telescoping gives, for support away from \(m=1\),

\[
R_\zeta^{\rm St}
=\sum_{n,m}\rho(n)W(n,m).
\tag{168.V8}
\]

If the lower endpoint can meet \(m=1\), its explicit half-threshold
correction must be added.  In the assigned \(m\asymp L\), \(1\ll L\)
range it is absent.  Formula (168.V8), rather than an undefined schematic
\(\omega_m\), should be stated in the claimant.  It has no continuous
\(y\)-variable and has \(L^2X^\varepsilon\) absolute capacity.  The
claimant's conclusion that this residue is not automatically target-safe
is therefore correct.

The proposed natural continuous realization is not comparably complete.
The claimant does not define a piecewise smooth function
\(\mathcal B_{\rm nat}\), an exceptional set \(E\), or coefficients
\(c_{n,m}\) such that

\[
W(n,m)=\mathcal B_{\rm nat}(n,m)
+c_{n,m}\mathbf 1_E(n,m)
\tag{168.V9}
\]

with \(\#E\ll LX^\varepsilon\).  To prove (168.V9), it must list every
product-shell, cone, dyadic, ratio, \(H+1\)-profile, real-centre floor,
star, zero-extension, and even-branch face, and show that each equality
set contributes \(O(L)\), or the appropriate divisor-type
\(O(LX^\varepsilon)\), lattice points.  Continuous boundary integrals
created by the jumps must then be kept separate from exceptional lattice
atoms and bounded by nonstationary phase.  The accepted exchange kernel's
\(O(L)\) count for several exact ties supports this program, but it is not
the missing all-face decomposition.  This seam remains open.

### 3.3 Stationary scale and the absolute/mean-square deficit

For a smooth radial-angular component, the change of variables

\[
x=rw,\qquad y=r/w
\]

gives

\[
dx\,dy=2r\,dr\,\frac{dw}{w}
\]

and radial phase

\[
2\pi Jr+t_+\log r,qquad t_+=t_1+t_2.
\]

The stationary equation is \(t_+=-2\pi Jr\), so the stationary band has
size and length \(T=JL\).  On
\(\Re s_1=\Re s_2=1/2+\eta\), stationary phase gives

\[
\left|\widehat{\mathcal B}\right|
\asymp L^{1+2\eta}(JL)^{-1/2}
=\sqrt{L/J}\,L^{2\eta}
\tag{168.V10}
\]

times the angular transform and profile seminorms.  With an optimistic
\(O(1)\) angular range and an \(X^\varepsilon\) pointwise arithmetic
majorant, absolute integration costs

\[
\sqrt{L/J}\,(JL)X^\varepsilon
=\sqrt J\,L^{3/2}X^\varepsilon.
\tag{168.V11}
\]

Likewise, the radial transform has \(L^2\)-norm of order \(L\), while a
granted fixed-angular arithmetic mean square of size
\(TX^\varepsilon\) has square-root norm \(T^{1/2}X^\varepsilon\).
Cauchy therefore gives

\[
L\sqrt{JL}\,X^\varepsilon
=\sqrt J\,L^{3/2}X^\varepsilon.
\tag{168.V12}
\]

The powers and the missing factor \(\sqrt J\) are correct.  The claimant
should say explicitly that (168.V10)--(168.V12) concern the recombined
smooth/BV continuous component, not an individual unit cardinal cell.
A cardinal cell has different radial and angular bandwidths, and the
exact cardinal sum has \(O(L^2)\) such cells.  Also, the no-go should be
worded for unweighted pointwise control or the stated one-dimensional
mean square followed by Cauchy, not for every conceivable weighted hybrid
estimate.

### 3.4 Functional equations and the Round-162 kernel

The character transform quoted by the claimant is exactly the accepted
identity

\[
\sum_m\chi_4(m)g(m)
=\frac i2\sum_{s\ \mathrm{odd}}\chi_4(s)\widehat g(s/4).
\tag{168.V13}
\]

The accepted Round-162 kernel also proves that **after** the exact opening

\[
\mu^2(d_1)\mu^2(d_2)\mathbf1_{(d_1,d_2)=1}
=\sum_{a^2\mid d_1}\mu(a)
 \sum_{b^2\mid d_2}\mu(b)
 \sum_{c\mid(d_1,d_2)}\mu(c),
\tag{168.V14}
\]

with \(Q=[a^2,c]\), \(R=[b^2,c]\), physical Poisson gives

\[
J\sqrt{QRmn}-sm/4-\ell n,
\quad s\ell=XQR,
\quad |s\ell-XQR|\ll QRJ/L,
\tag{168.V15}
\]

and positive capacity \(\sqrt{JL}X^\varepsilon\).  Those accepted facts
may be cited.

They do not by themselves prove that applying the functional equations
to \(L(s_1,\chi_4)\zeta(s_2)G(s_1,s_2)\) returns coefficientwise to
(168.V14)--(168.V15).  The claimant never writes the two-variable
Dirichlet coefficients of \(G\), identifies their multiplicities and
signs with \((a,b,c;Q,R)\), or shows that the infinite expansion can be
interchanged with both transformed integrals.  It also omits the zeta
main term, gamma factors, dual test-function normalizations, the even
\(d_2\) branch, and the exact returned profiles, including
\(W(XQ/(ys))\), \(q_X\), and \(H+1\).  No approximate functional equation,
its conductor, its two lengths, or its remainder is displayed at all.

Accordingly, “functional-equation/AFE self-return” is not proved.  There
are two lawful repairs:

1. delete the exact-equivalence language and state only that choosing the
   already accepted Möbius opening plus positive Poisson control invokes
   the Round-162 obstruction; or
2. add a complete coefficient bridge from \(G\) to (168.V14), including
   \(p=2\), all gamma/main terms, AFE truncations and errors, literal
   profiles, and the coefficient normalization
   \(L^{3/2}/(QR\sqrt J)\).

Until one repair is made, the Round-168 no-go cannot include bare
factorwise functional equations or approximate functional equations as a
newly proved branch.  The already accepted Round-162 positive-opening
obstruction itself remains valid.

### 3.5 Polylogarithmic sector, normalization, and connector

The normalization \((L^2/(nm))^{3/4}\) is \(O(1)\) on \(n,m\asymp L\),
and the fixed profiles are bounded.  Hence the literal support has at most
\(O(L^2)\) entries and

\[
|\mathcal S_{L,1}|\ll L^2X^{\varepsilon/2}.
\]

For each fixed \(B\), if \(L\le(\log X)^B\), then

\[
L^{1/2}\le(\log X)^{B/2}\ll_{B,\varepsilon}X^{\varepsilon/2},
\]

so

\[
|\mathcal S_{L,1}|\ll_{B,\varepsilon}L^{3/2}X^\varepsilon.
\tag{168.V16}
\]

This is uniform in all literal endpoints because it is an absolute bound.
It is a complete strict sector for fixed \(B\), not a polynomial-range
result.

The accepted opposite-prime kernel gives, for fixed \(\kappa\),

\[
\mathcal S^{\rm cp}_{L,1}\ll_\kappa L^{3/2}.
\]

Defining the remainder as the exact complementary incidence set gives

\[
\mathcal S_{L,1}
=\mathcal S^{\rm cp}_{L,1}+\mathcal S^{\rm rem}_{L,1}.
\tag{168.V17}
\]

Thus full and residual \(L^{3/2}X^\varepsilon\) estimates imply one
another by addition/subtraction, with the accepted close-prime term.  In
particular, (168.V16) also yields the residual bound in the same fixed
polylogarithmic sector.  It does not close the general residual node, full
hard TOP, M9--M2, M9, the bridge, the quarter theorem, or an exponent.

Finally, every occurrence of \(H=\sqrt J\) must be replaced using
(168.V1).  The accepted collar ratio is

\[
\frac{\sqrt{JL}}{L^{3/2}}
=\frac{\sqrt J}{L}
=\frac HL+O(L^{-1}).
\tag{168.V18}
\]

This repair preserves the power comparison but restores literal floor
normalization.

## 4. First doubtful or unproved step

The earliest unsupported substantive claim is the Result-section sentence
that a “natural continuous interpolation” is lawful after splitting off
finitely many boundary atoms, followed by the assertion that those atoms
cost \(O(LX^\varepsilon)\).  No exact continuous extension, exceptional
set, or all-face count appears in the derivation.  The cardinal
interpolation should not be conflated with this unproved second model.

The first literal false equality is the Section 2 hypothesis
\(H=\sqrt J\); the exact relation is (168.V1).  The most consequential
later overstatement is the exact functional-equation/AFE return to
Round 162.  The accepted kernel proves (168.V15) only after (168.V14), and
the missing coefficient/gamma/profile seam is not supplied by citing the
one-variable functional equations.

## 5. Required controls and outcomes

| Required control | Outcome |
|---|---|
| Odd-prime and two-adic Euler factors | **PASS.** The local factors and \(G_2=1-2^{-2s_2}\) are exact. |
| Larger Euler continuation | **PASS.** Equations (168.V4)--(168.V5) and the region \(\Omega\) are correct; denominator-zero poles are only possible poles. |
| Critical contour shift | **PASS.** On \(\Re s_j\ge1/2+\eta\), only \(s_2=1\) is crossed. |
| Cardinal interpolation | **PASS.** Disjoint supports reproduce every literal lattice value exactly. |
| Cardinal residue | **PASS.** Nonstationary \(y\)-integration makes this representation's residue target-safe. |
| Stieltjes residue | **PASS AFTER FORMULA REPAIR.** Replace the schematic \(\omega_m\) statement by (168.V8); it is not automatically small. |
| Natural continuous-plus-atoms model | **OPEN / REVISE.** Define it, enumerate every face, and separate boundary integrals from lattice atoms. |
| \(O(LX^\varepsilon)\) atom cost | **NOT YET PROVED.** The finite-face geometry suggests it, but the claimant gives no complete count. |
| Smooth stationary scale and radial length | **PASS.** Scale \(\sqrt{L/J}\,L^{2\eta}\), length \(JL\). |
| Absolute and stated mean-square power ledger | **PASS WITH NARROW SCOPE.** Each stated treatment loses \(\sqrt J\); this is not a no-go for every weighted hybrid estimate. |
| Functional-equation return | **REVISE.** Only the conditional return through the already accepted projector opening is established. |
| Approximate functional equation | **FAIL AS WRITTEN.** No gamma factors, conductor, lengths, truncations, or errors are derived. |
| Round-162 collar powers | **PASS WHEN IMPORTED FROM THE ACCEPTED KERNEL.** The positive capacity is \(\sqrt{JL}X^\varepsilon\). |
| \(H,y,q_X\) and floor normalization | **FAIL AS WRITTEN.** Use (168.V1) and (168.V18). |
| Fixed-\(B\) polylog full scalar | **PASS.** The \(\varepsilon/2\mapsto\varepsilon\) relabelling is correct and endpoint-complete. |
| Close-prime/remainder connector | **PASS.** Exact addition/subtraction gives only the corresponding full/residual statement. |
| Downstream scope | **PASS AFTER QUALIFICATION.** No general K17a, hard-TOP, M9--M2, M9, bridge, theorem, or exponent follows. |

No numerical experiment is needed: all decisive checks are algebraic or
analytic.

## 6. Dependencies/exact artifacts used

Only the following authorized artifacts were used:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/reports/literal_pre_mobius_mellin_attack.md`;
3. `rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/reports/blind_mellin_euler_rederivation.md`;
4. `proofs/kernels/m9_m2_hard_top_t1_character_poisson_product_collar_obstruction.md`;
5. `proofs/kernels/m9_m2_hard_top_t1_close_opposite_prime_exchange_sector.md`.

No proof graph, active campaign, strategy, barrier packet, sibling report,
source, candidate, synthesis, or shared-state file was inspected or edited.

## 7. Recommended state effect

**REVISE; do not promote the claimant as a whole.**

Retain as candidate facts after editorial tightening:

1. the exact Euler products and continuation algebra;
2. the exact cardinal Mellin identity and its representation-specific
   target-safe \(\zeta\)-residue;
3. the exact discrete Stieltjes warning, preferably in the form
   (168.V8);
4. the smooth absolute/standard-mean-square \(\sqrt J\)-deficit ledger;
5. the fixed-polylogarithmic-\(L\) full-scalar sector and, by the accepted
   connector, the same strict residual sector.

Before acceptance, require the claimant to:

1. restore \(y,q_X,H\) and every floor-dependent occurrence exactly;
2. either construct and count the natural continuous-plus-atoms
   decomposition or delete its target-safe claim;
3. distinguish the cardinal transform from the smooth global transform in
   the stationary analysis;
4. replace the functional-equation/AFE self-return by the narrower
   conditional citation to the accepted Round-162 opening, or prove the
   full coefficient/gamma/profile bridge; and
5. narrow the no-go label to unweighted absolute control, the stated
   fixed-angular mean square plus Cauchy, and the already accepted
   Möbius-opened positive collar route.

Make no general K17a, residual, hard-TOP, M9--M2, M9, bridge,
quarter-theorem, or exponent promotion from the present claimant.
