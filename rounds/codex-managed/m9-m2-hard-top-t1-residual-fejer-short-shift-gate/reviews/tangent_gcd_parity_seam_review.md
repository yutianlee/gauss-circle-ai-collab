# Round 165 seam review: tangent, dual-gcd, parity, and phase

## 1. Result

The main algebraic seams pass, with two presentation repairs and one scope
restriction on the Poisson claim.

The following statements are verified and are suitable for promotion after
the conductor normalizes notation:

1. the literal tangent map is multiplicity one,
   \(d'=d+a\), \(m'=m+b\),
   \[
     db+am+ab=db+a m'=r,
     \qquad \chi_4(d')\chi_4(d)=(-1)^{a/2};
   \]
2. the complete monotone displacement sector \(a,b\ge0\) has
   \(O(L^2)\) literal atoms and is therefore
   \(O(L^2X^\varepsilon)\) under the exact normalized atom weight;
   the sector \(a,b\le0\), except \((0,0)\), is empty, and every remaining
   nonempty sector has \(ab<0\);
3. both the divisor-gcd and cofactor-gcd progression maps are bijective
   after a canonical base solution is fixed, and their geometric row
   lengths are respectively \(O(1+g)\) and \(O(1+s)\);
4. the cofactor-gcd character is constant on even-shift rows and
   alternating on odd-shift rows, including the squarefree even-even
   branch;
5. the phase derivatives and their \(J,L,g,s,h\) scales are correct once
   the symbol \(K\) is defined to mean the *actual product increment* of
   the chosen integer row parameter; and
6. the parity-window connector
   \[
      \mathfrak E_R\le2\mathfrak E_R^{(2)}
   \]
   is endpoint-exact and reduces the complete residual target to the
   even-shift sector without invoking XOR energy equivalence.

Combining items 2 and 6 gives a sharper exact frontier than any of the
three artifacts states alone.  It is enough to prove

\[
 \boxed{
 \Re\mathfrak C_{2,\mathrm{opp}}^{\rm rem}
 \ll_\varepsilon L^2X^\varepsilon,}
\tag{165.SR1}
\]

where \(\mathfrak C_{2,\mathrm{opp}}^{\rm rem}\) is the complete literal
Fejer aggregate restricted simultaneously to even shifts and
\((d'-d)(m'-m)<0\).  No modulus is placed around a shift or tuple.  On
this frontier the character is frozen along each cofactor-gcd row.

The full estimate (165.SR1) is open.  The classical first-derivative,
second-derivative, shiftwise-modulus, and absolute-dual-mode routes do not
prove it with the available ledger.  The last assertion is route-scoped:
it is not a lower bound and not an impossibility theorem for a coupled
Poisson or arithmetic treatment.

## 2. Exact statement and hypotheses

Use the literal residual atom

\[
 \lambda_N(d)=
 {\bf1}_{\mathcal I_L^{\rm lit}}(N)\mu^2(N)
 \left(\frac{L^2}{N}\right)^{3/4}
 \rho_N(d)A_N(d),
\qquad
 c_N^{\rm rem}=\sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)\lambda_N(d),
\tag{165.SR2}
\]

with the literal profile, selector, parity, hard value, endpoint, and zero
extension retained in \(A_N\) and \(\rho_N\).  On the fixed product shell,

\[
 N\asymp L^2,\qquad d,m=N/d\asymp L,\qquad
 |\lambda_N(d)|\ll1.
\tag{165.SR3}
\]

The last bound is not an extra hypothesis: the outer normalization is
\(\asymp1\), \(\rho_N\in\{0,1\}\), and the accepted fixed profiles and
literal point values are uniformly bounded.  Squarefree and selector
conditions delete atoms and never create multiplicity or a positive power
of \(L\).

Write

\[
 \mathfrak C^{\rm rem}
 =\sum_{1\le r<R}\left(1-\frac rR\right)
 \sum_{d'm'-dm=r}\chi_4(d')\chi_4(d)
 \lambda_{d'm'}(d')\overline{\lambda_{dm}(d)}
 e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right),
\tag{165.SR4}
\]

where all variables are positive, \(d,d'\) are odd, and the zero-extended
atoms impose every remaining literal restriction.

Define \(a=d'-d\), \(b=m'-m\).  Let
\(\mathfrak C_{2,\mathrm{mon}}^{\rm rem}\) and
\(\mathfrak C_{2,\mathrm{opp}}^{\rm rem}\) denote the subaggregates of
(165.SR4) with, respectively,

\[
 2\mid r,\ a,b\ge0,
 \qquad\text{and}\qquad
 2\mid r,\ ab<0.
\tag{165.SR5}
\]

There are no other nonempty even-shift displacement sectors.  With
\(z_N=c_N^{\rm rem}e(J\sqrt N)\), put

\[
 D=\sum_N|c_N^{\rm rem}|^2,
 \quad
 \mathfrak E_R=D+2\Re\mathfrak C^{\rm rem},
\]

and let \(\mathfrak E_R^{(2)}\) keep only even gaps.  The exact implication
to be certified is

\[
 \Re\mathfrak C_{2,\mathrm{opp}}^{\rm rem}ll L^2X^\varepsilon
 \Longrightarrow
 \mathfrak E_R\ll L^2X^\varepsilon
 \Longrightarrow
 |\mathcal S_{L,1}^{\rm rem}|\ll L^{3/2}X^\varepsilon.
\tag{165.SR6}
\]

## 3. Proof and seam verification

### 3.1 Tangent identity, multiplicity, and character

For a tuple of (165.SR4), the definitions
\(a=d'-d\), \(b=m'-m\) are unique, and conversely
\((a,b,d,m)\) reconstructs \((d',m')=(d+a,m+b)\) uniquely.  Direct
expansion gives

\[
 (d+a)(m+b)-dm=db+am+ab=db+a(m+b)=db+a m'.
\tag{165.SR7}
\]

Because \(d,d'\) are odd, \(a=2q\).  For odd \(d\),

\[
 \chi_4(d+2q)=(-1)^q\chi_4(d),
\]

and \(\chi_4(d)^2=1\); hence

\[
 \boxed{\chi_4(d')\chi_4(d)=(-1)^{a/2}.}
\tag{165.SR8}
\]

The tangent equation

\[
 bd+am=r-ab
\tag{165.SR9}
\]

is therefore exact.  If \(ab\ne0\), with
\(\delta=(|a|,|b|)\), unrestricted integral solutions exist exactly when
\(\delta\mid r\), and after fixing one solution they are

\[
 d=d_0+\frac a\delta t,\qquad
 m=m_0-\frac b\delta t.
\tag{165.SR10}
\]

Literal positivity, oddness, squarefreeness, profiles, and selectors only
retain a subset of these points.  The one-zero cases reduce to
\(bd=r\) or \(am=r\); \((a,b)=(0,0)\) is impossible for \(r>0\).
This verifies the tangent bijection and multiplicity.

### 3.2 Monotone sector and exact atom normalization

On literal support there is a fixed \(\kappa>0\) with
\(d,m,d',m'\ge\kappa L\).  If \(a,b\ge0\), (165.SR7) gives

\[
 r=db+a m'\ge\kappa L(a+b).
\tag{165.SR11}
\]

Since \(r<R\le L+1\), only \(O(1)\) pairs \((a,b)\) occur.  For each
such pair there are \(O(L)\) possible \(d\)'s and \(O(L)\) possible
\(m\)'s; \(d',m',r\) are then determined.  Thus there are \(O(L^2)\)
literal atoms in the *complete union over all shifts*.  The Fejer weight
is at most one and (165.SR3) bounds each atom product, so

\[
 \boxed{|\mathfrak C_{\mathrm{mon}}^{\rm rem}|ll L^2.}
\tag{165.SR12}
\]

No additional factor \(R\) is present: \(r\) is a function of
\((a,b,d,m)\), not another free choice.  If \(a,b\le0\), not both zero,
then \(r=db+a m'<0\).  If one displacement is zero and the other is
negative, the same formula is negative.  Therefore every nonempty tuple
outside the monotone sector has \(ab<0\).  The blind report's normalization
seam is consequently resolved by the literal atom (165.SR2).

### 3.3 Divisor-gcd progression

Let \(g=(d,d')\), \(d=gu\), \(d'=gv\), \((u,v)=1\).  Since
\(d,d'\) are odd, \(g,u,v\) are odd.  The product equation becomes

\[
 g(vm'-um)=r.
\]

Thus \(g\mid r\), \(r=gh\), and all solutions of
\(vm'-um=h\) are

\[
 m=m_0+vt,\qquad m'=m'_0+ut.
\tag{165.SR13}
\]

After choosing a canonical base solution, the map between literal tuples
and \((g,h,u,v,t)\) is bijective.  Along it,

\[
 N(t)=A+K_dt,\quad N(t)+r=A+r+K_dt,\quad
 K_d=guv=\frac{dd'}g,\quad
 \chi_4(d')\chi_4(d)=\chi_4(uv).
\tag{165.SR14}
\]

Since \(d,d'\asymp L\), \(K_d\asymp L^2/g\).  Intersecting this product
progression with a shell of length \(M_L\asymp L^2\) gives a geometric
row of \(O(1+g)\) points.  Squarefree masks, selectors, parity branches,
and hard profiles only delete points from it.  The sign in (165.SR14) is
constant along the row.

### 3.4 Cofactor-gcd progression and even-even parity

Let \(s=(m,m')\), \(m=su\), \(m'=sv\), \((u,v)=1\).  Then

\[
 s\mid r,\quad r=sh,\quad vd'-ud=h.
\]

After a base solution is fixed, all solutions are
\((d,d')=(d_0+vt,d'_0+ut)\).  Requiring both divisors to be odd selects
one parity class \(t=t_0+2k\), so

\[
 d=D_0+2vk,\qquad d'=D'_0+2uk,\qquad
 N(k)=N_0+K_sk,\quad K_s=2suv=\frac{2mm'}s.
\tag{165.SR15}
\]

This is again bijective after fixing the canonical base and parity class.
Since \(K_s\asymp L^2/s\), the geometric row has \(O(1+s)\) points.

The character ratio under \(k\mapsto k+1\) is

\[
 (-1)^v(-1)^u=(-1)^{u+v}.
\tag{165.SR16}
\]

If \(r\) is odd, the two products have opposite parity.  Hence \(s\) is
odd and \(u,v\) have opposite parity, so (165.SR16) is \(-1\).  If
\(r\) is even and both products are odd, then \(s,u,v\) are odd and the
ratio is \(+1\).  If both products are even and squarefree, write
\(m=2m_1\), \(m'=2m'_1\) with \(m_1,m'_1\) odd.  Then

\[
 \nu_2(s)=1,\qquad u,v\ \text{odd},\qquad 4\mid r,\qquad h=r/s\ \text{even}.
\tag{165.SR17}
\]

Thus the ratio is again \(+1\).  This verifies the previously delicate
even-even branch and proves

\[
 \chi_4(d(k))\chi_4(d'(k))
 =\sigma_0(-1)^{(r\bmod2)k}.
\tag{165.SR18}
\]

### 3.5 Phase derivatives and resonance

Let \(K_{\rm row}\) denote the actual increment in the product when the
integer row parameter increases by one, and put

\[
 x(t)=x_0+K_{\rm row}t,\qquad
 \Psi(t)=J(\sqrt{x(t)+r}-\sqrt{x(t)}).
\]

Then the convention-independent formulas are

\[
\begin{aligned}
 \Psi'(t)&={JK_{\rm row}\over2}
   \{(x+r)^{-1/2}-x^{-1/2}\},\\
 \Psi''(t)&={JK_{\rm row}^2\over4}
   \{x^{-3/2}-(x+r)^{-3/2}\},\\
 \Psi'''(t)&={3JK_{\rm row}^3\over8}
   \{(x+r)^{-5/2}-x^{-5/2}\}.
\end{aligned}
\tag{165.SR19}
\]

For the cofactor row, \(K_{\rm row}=K_s\asymp L^2/s\),
\(r=sh\), and the row length is \(O(s)\).  Therefore

\[
 |\Psi'|\asymp Jh/L,\qquad
 \Psi''\asymp Jh/(sL),\qquad
 |\Psi'''|\asymp Jh/(s^2L).
\tag{165.SR20}
\]

The effective phase is \(\Psi(k)+(r\bmod2)k/2\).  A first-derivative
argument needs distance from integers of its derivative, and an exact
discrete argument needs control of

\[
 \left\|J\{\Delta_r(x+K_{\rm row})-\Delta_r(x)\}
       +{r\bmod2\over2}\right\|_{\mathbb R/\mathbb Z},
 \qquad \Delta_r(x)=\sqrt{x+r}-\sqrt x.
\tag{165.SR21}
\]

Neither is supplied.  Equations (165.SR19)--(165.SR21) verify the phase
ledger and prevent a large-real-derivative overclaim.

### 3.6 Parity-window connector and sharpened frontier

For a zero-extended window sum \(Y_s=\sum_{j<R}z_{s+j}\), split it into
the two absolute-parity sums \(Y_s^{(0)}+Y_s^{(1)}\).  Then

\[
 |Y_s|^2\le2(|Y_s^{(0)}|^2+|Y_s^{(1)}|^2).
\]

After summing over all window origins and dividing by \(R\), a pair is
retained on the right exactly when its gap is even, and it is counted in
exactly \(R-r\) windows.  Hence

\[
 \boxed{\mathfrak E_R\le2\mathfrak E_R^{(2)}},
 \qquad
 \mathfrak E_R^{(2)}
 =D+2\Re(\mathfrak C_{2,\mathrm{mon}}^{\rm rem}
          +\mathfrak C_{2,\mathrm{opp}}^{\rm rem}).
\tag{165.SR22}
\]

Zero extension makes the count exact for even or odd \(R\).  Combining
(165.SR12), (165.SR22), the accepted diagonal
\(D\ll L^2X^\varepsilon\), and the accepted sliding inequality proves
(165.SR6).  This reconciles the blind monotone sector, the conductor's
cofactor parity classification, and the discovery report's parity
connector.

### 3.7 Scope of the derivative and Poisson no-go

Shiftwise Cauchy gives at best \(L^2X^\varepsilon\) per shift and hence
\(L^3X^\varepsilon\) after \(R\asymp L\) shifts.  This misses one factor
\(L\) in the correlation and \(L^{1/2}\) in the scalar.

For a cofactor row, \(s\mid r<R\) and \(L\ll H\le J^{1/2}\) imply

\[
 \lambda:=\Psi''\asymp\frac{Jh}{sL}\gg1.
\]

Thus the classical real second-derivative expression
\(T\sqrt\lambda+\lambda^{-1/2}\), with \(T\ll s\), is no better than
the trivial \(T\)-bound.  The first derivative is likewise useless
without (165.SR21).

On a smooth nondegenerate divisor-gcd row of length \(T\asymp g\), the
derivative image has length \(\asymp Jh/L\).  Taking absolute values of
all stationary dual modes gives the capacity

\[
 \frac{Jh}{L}\left(\frac{gL}{Jh}\right)^{1/2}
 =\left(\frac{Jgh}{L}\right)^{1/2},
\tag{165.SR23}
\]

whose ratio to \(g\) is
\(\asymp(Jh/(gL))^{1/2}\gg1\).  This verifies only the following
route-scoped statement: completing a smooth full row and then bounding
its stationary dual modes separately is adverse.  Short or heavily
deleted rows, boundary terms, coupled dual-mode cancellation, and
aggregate arithmetic methods are not covered by (165.SR23).  In
particular, (165.SR23) is neither a physical lower bound nor a universal
Poisson no-go.

## 4. First doubtful or unproved step

The algebra, counting, parity, phase differentiation, and endpoint
connector through (165.SR22) are verified.  The first unproved estimate is
(165.SR1), the complete even-shift opposing-displacement aggregate.

In the cofactor-gcd form its character is constant on each row.  A proof
must therefore preserve cancellation across primitive \((u,v)\) slopes,
across tangent displacements \(a/2\), across shifts, or across dual modes,
while retaining the two literal squarefree masks, both row-dependent
selectors, both parity branches, all profiles, and hard endpoints.  No
accepted bounded-variation estimate in \(a/2\), no modulo-one resonance
bound for (165.SR21), and no applicable aggregate shifted-divisor theorem
is present in the reviewed artifacts.

The conductor candidate should repair the typo `t)` in its cofactor-gcd
statement and use one product-step convention in (165.C11)--(165.C15).
These are presentation repairs, not mathematical failures.

## 5. Control tests and outcomes

| Seam | Outcome |
|---|---|
| Tangent identity and inverse multiplicity | **GREEN.** Equations (165.SR7)--(165.SR10) are bijective after literal restrictions. |
| \(\chi_4=(-1)^{a/2}\) | **GREEN.** Equation (165.SR8) follows exactly from the modulus-four character. |
| Monotone \(a,b\ge0\) sector | **GREEN, promotable.** It has \(O(L^2)\) atoms over all shifts; (165.SR2)--(165.SR3) resolve the normalization seam. |
| Negative monotone sector and complement | **GREEN.** The nonpositive and one-zero-negative cases are empty; every remaining tuple has \(ab<0\). |
| Divisor-gcd bijection and support length | **GREEN.** The sign is constant and the geometric row has \(O(1+g)\) points. |
| Cofactor-gcd bijection and support length | **GREEN.** Oddness selects one parameter parity and the row has \(O(1+s)\) points. |
| Even-even squarefree parity | **GREEN.** Equation (165.SR17) records \(\nu_2(s)=1\), \(u,v\) odd, \(4\mid r\), and \(h\) even. |
| Phase derivatives and powers | **GREEN after notation normalization.** Equation (165.SR19) uses the actual row step and yields (165.SR20). |
| First-derivative route | **GREEN no-go scope.** Large real size supplies no integer/half-integer gap. |
| Second-derivative route | **GREEN no-go scope.** Its standard bound is vacuous because \(\lambda\gg1\); no higher-order impossibility is asserted. |
| Absolute dual-mode route | **GREEN with restriction.** Equation (165.SR23) applies to smooth full rows and only after dual modes are made positive. |
| Parity-window connector | **GREEN, promotable.** Equation (165.SR22) is endpoint-exact and independent of XOR energy. |
| Actual coefficient and hard boundaries | **GREEN.** They remain in \(\lambda\); every progression statement permits literal deletions and isolated values. |
| Missing power | **GREEN ledger, OPEN saving.** Positive shiftwise control restores \(L^3\), one factor \(L\) above (165.SR1). |
| Downstream scope | **GREEN.** No full residual, other channel, hard-TOP parent, M9--M2, M9, bridge, target, or exponent follows. |
| Numerical experimentation | **NOT USED.** This review is entirely algebraic and analytic. |

## 6. Dependencies and exact artifacts used

This review used only:

- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reports/blind_fejer_short_shift_rederivation.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/candidates/conductor_round165_gcd_parity_progression_reduction.md`;
- `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reports/actual_residual_short_shift_attack.md`; and
- `proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md`.

No sibling hostile report, external source, or numerical experiment was
used.

## 7. Recommended state effect

**Promote after the two presentation repairs** the exact parity-window
connector, tangent bijection and character identity, both gcd progression
normal forms, the squarefree parity dichotomy, and the normalized phase
derivative ledger as a proved-internal reduction.

**Promote the monotone displacement sector** \(a,b\ge0\) as a strict
owner-complete target-safe sector.  It costs \(O(L^2)\) across the complete
shift aggregate, not \(O(L^2)\) per shift.  The natural Round-165 terminal
label for this affirmative state effect is
`strict_residual_short_shift_sector`.

**Retain (165.SR1) as the first open theorem.**  It is narrower than the
full Round-164 correlation: only even shifts and opposing displacements
remain.  The parity connector and monotone-sector estimate prove that
(165.SR1) is sufficient for the complete residual scalar.

**Record route-scoped obstructions only** for shiftwise modulus, a large
real first derivative without modulo-one separation, the classical
second-derivative estimate in the inherited range, and a smooth full-row
Poisson transform followed by absolute values of its stationary modes.
Do not state a universal phase, Poisson, spectral, or literature no-go.

**Make no downstream promotion.**  The complete residual, full \(t=1\)
face, other few-point channels, hard TOP, BAL, UNBAL, M9--M2, M9--M1,
endpoint uniformity, M9, the conditional bridge, the quarter theorem, and
both global exponents remain open or unchanged.
