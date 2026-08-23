# Hostile addendum: the direct birth-block theorem strengthens to \(K/L\)

Campaign: `gc-w7-16-joint-stieltjes-reciprocal-curvature-gate`
Round: 129
Reviewed artifact:
`candidates/conductor_birth_block_abel_curvature.md`
Starting graph SHA-256:
`476b1445ef73d86627fd87de8bd2dd76a5efa53564a5b195230f2ad33ba2bbe8`

Status: independent candidate review only; no shared proof state is edited.

## Decision

The conductor candidate is valid after a strengthening: its direct
actual-family estimate has no \(J_B^{1/2}\) loss.  For every literal
character-split branch and every \(\rho\mid a'\), one has

\[
 \boxed{
 \left|\sum_{v\in I}^{*}U_{i,\rho,\eta}(v)e(\phi(v))\right|
 \ll_\varepsilon {K_\rho\over L}Y^\varepsilon,}
 \tag{129.A1}
\]

where

\[
 K_\rho=min\!\left(
 N_\rho,
 N_\rho\sqrt{\Lambda_\rho}+\Lambda_\rho^{-1/2}
 \right),\quad
 N_\rho\asymp {Q_B\over\rho},\quad
 \Lambda_\rho=\lambda_B\rho^2.
 \tag{129.A2}
\]

The exact identity

\[
 N_\rho\Lambda_\rho
 =L\rho\,(J_B-1)
 \tag{129.A3}
\]

absorbs all nonconstant birth-block endpoint costs.  After the accepted
divisor sum and Round-127 outer factor, (129.A1) rigorously gives

\[
 \boxed{|\mathfrak O_i|\ll_\varepsilon Y^{35/48+\varepsilon}}
 \tag{129.A4}
\]

for the complete critical fixed block, uniformly over all
\(D/L\le B\le D\).  This conclusion coexists with the hostile report's
counterexample: the generic norm-relative inequality is false, while
(129.A1) is a direct absolute theorem for the exact Stieltjes-character
family.

## Strengthened one-threshold proof

Fix \(t\asymp D\), write

\[
 R_t(v)={\tau(v)\over a'}
 \sum_{g\le t/(\rho v)}^{*}{\chi_4(g)\over g}P_{a'}(g),
 \qquad M_t(v)=\left\lfloor{t\over\rho v}\right\rfloor.
 \tag{129.A5}
\]

Do not first estimate the \(g\)-variation of the cumulative sums
\(Z_t(g)\).  Instead, partition the physical \(v\)-window into the
maximal blocks on which \(M_t(v)\) and its literal star convention are
fixed.  Character Abel summation, before any modulus over \(g\), gives
uniformly on every such block

\[
 \left|{1\over a'}
 \sum_{g\le M}^{*}{\chi_4(g)\over g}P_{a'}(g)\right|
 \ll_\varepsilon {Y^\varepsilon\over |a'|G}
 \ll_\varepsilon {Y^\varepsilon\over L}.
 \tag{129.A6}
\]

The number \(R_t\) of nonempty birth blocks satisfies

\[
 R_t\ll_\varepsilon 1+{DQ_B\over B^2}
 =1+(J_B-1),
 \tag{129.A7}
\]

and their total length is at most \(N_\rho\).  Equality stars can add only
divisor-many singleton blocks, absorbed by \(Y^\varepsilon\).

On each block \(J\), weighted second-derivative summation gives

\[
 \left|\sum_{v\in J}^{*}\tau(v)e(\phi(v))\right|
 \ll
 (\|\tau\|_\infty+\operatorname {Var}_J\tau)
 \min\!\left(|J|,|J|\sqrt{\Lambda_\rho}
                    +\Lambda_\rho^{-1/2}\right).
 \tag{129.A8}
\]

If \(K_\rho=N_\rho\), the trivial estimate and (129.A6) immediately
give (129.A1).  Otherwise sum the curvature branch of (129.A8).  The
block lengths contribute
\(N_\rho\sqrt{\Lambda_\rho}\).  The one constant block endpoint is
the \(\Lambda_\rho^{-1/2}\) already present in \(K_\rho\).  Every
nonconstant birth block is absorbed without Cauchy because (129.A3)
implies

\[
 (J_B-1)\Lambda_\rho^{-1/2}
 ={N_\rho\sqrt{\Lambda_\rho}\over L\rho}
 \le N_\rho\sqrt{\Lambda_\rho}.
 \tag{129.A9}
\]

The bounded total variation of \(\tau\) creates only
\(O(N_\rho\sqrt{\Lambda_\rho}+\Lambda_\rho^{-1/2})\): for the length
part use the largest block length, and for the endpoint part sum the
intrinsic variations over the disjoint blocks.  Equations
(129.A6)--(129.A9) prove the one-threshold version of (129.A1).

Zero-extending the actual denominator profile gives the exact discrete
Stieltjes decomposition

\[
 w(d)=\sum_{t\ge d}c_t,qquad \sum_t|c_t|\ll1.
 \tag{129.A10}
\]

Minkowski over \(t\), now applied to the already uniform bound
(129.A1), preserves \(K_\rho/L\).  No \(D\), \(G\), \(J_B\),
\(N_\rho^{1/2}\), or full-lift factor is introduced.

## Literal seam audit

| Seam | Check | Decision |
|---|---|---|
| Exact physical coefficient | Round-128 factors the lift weight into the fixed sampled-BV frequency factor \(P_{a'}(g)\) and the zero-extended sampled-BV denominator profile \(w(g\rho v)\). | **Pass.** This is precisely (129.A5) and (129.A10); there is no unpriced mixed \((g,v)\) support. |
| Common lift character | \(\chi_4(g)\) remains inside (129.A6) until its bounded partial sums are used. | **Pass.** No unsigned lift sum or liftwise modulus is taken. |
| M1 reduced character | The two exact identities \(\chi_4(b')=(e(b'/4)-e(-b'/4))/(2i)\) give \(\vartheta_{1,\pm}=\pm1/4\). | **Pass.** The linear terms have zero second derivative and merely translate the stationary aliases. |
| M2 reduced character | \(\chi_4(|a'|)\) is fixed in \(v\). | **Pass.** It changes only a constant branch factor. |
| Reciprocal aliases | (129.A8) is a second-derivative bound uniform in every integer first-derivative crossing; (129.A9) prices one endpoint term per birth block. | **Pass.** No alias is deleted or assumed nonstationary. |
| Floors and stars | Floors define the birth blocks.  A strict/weak face changes their half-open convention; exact equality stars give divisor-many singletons. | **Pass with \(Y^\varepsilon\).** |
| Taper and clipping | The determinant taper, sign sector, fixed cell, and half-open shell cut form the accepted multiplier \(\tau\), supported on \(O(1)\) clipped intervals with bounded zero-extended variation. | **Pass.** Its variation is charged once in (129.A8). |
| Möbius progressions | The estimate is uniform in \(\rho\mid a'\) after the nonprimitive extension. | **Pass.** Sum only after (129.A1); divisor functions cost \(Y^\varepsilon\). |
| Shell ownership | The physical window has length \(Q_B\le B\) and meets \(O(1)\) half-open \(B\)-owners. | **Pass.** Each inner term has one owner and the outer ray is not duplicated. |
| Phase-adapted false control | A bounded-mass phase-adapted denominator profile can make \(\|U\|_{V^2}\) anomalously small. | **Expected failure of the norm formulation only.** Absolute estimate (129.A1) remains valid and is exactly what the assembly uses. |

## Divisor sum and all-\(B\) capacity

For \(\lambda_B\le1\), split divisors at
\(\rho=\lambda_B^{-1/2}\).  When
\(\rho\le\lambda_B^{-1/2}\), (129.A2) is bounded by

\[
 Q_B\sqrt{\lambda_B}+{1\over\rho\sqrt{\lambda_B}};
\]

when \(\rho>\lambda_B^{-1/2}\), its trivial branch is
\(Q_B/\rho\le Q_B\sqrt{\lambda_B}\).  Therefore

\[
 \sum_{\rho\mid a'}K_\rho
 \ll_\varepsilon
 \min\!\left(Q_B,
 Q_B\sqrt{\lambda_B}+\lambda_B^{-1/2}\right)Y^\varepsilon.
 \tag{129.A11}
\]

The same conclusion is immediate when the trivial \(Q_B\) branch is
smaller.  This uses only \(\tau(a')\) and \(\sigma_{-1}(a')\), as in the
accepted top-shell proof.

The accepted Round-127 complete cross-shell ledger is

\[
 \underbrace{O(LD)}_{\text{outer rays}}
 \cdot
 \underbrace{O(L)}_{\text{numerator increments}}
 \cdot
 \underbrace{O(L^{-1})}_{\text{outer coefficient}}
 \cdot
 \underbrace{O(L^{-1}K_B)}_{\text{inner estimate}}
 =O(DK_B),
 \tag{129.A12}
\]

where

\[
 K_B=min\!\left(Q_B,
 Q_B\sqrt{\lambda_B}+\lambda_B^{-1/2}\right).
\]

At \(B=Y^b\), \(1/3\le b\le1/2\),

\[
 Q_B=Y^{b-5/48},\qquad
 \lambda_B=Y^{2/3-2b},\qquad
 Q_B\sqrt{\lambda_B}=Y^{11/48},\qquad
 \lambda_B^{-1/2}\le Y^{1/6}.
 \tag{129.A13}
\]

At \(b=1/3\), the trivial and curvature branches meet at
\(Y^{11/48}\); for \(b>1/3\), the curvature branch is
\(Y^{11/48+o(1)}\).  Hence uniformly in every allowed shell,

\[
 K_B\ll Y^{11/48+o(1)},\qquad
 DK_B\ll Y^{35/48+o(1)}.
 \tag{129.A14}
\]

There are only logarithmically many half-open \(B\)-shells, so (129.A4)
follows.  The ledger contains neither \(J_B^{1/2}\) nor an unowned
cross-shell coefficient.

## Final recommendation

**Certify after conductor incorporation** the direct actual-family
birth-block theorem (129.A1), with the stronger \(K_\rho/L\) right side,
and the complete all-\(B\) critical fixed-block consequence
\(Y^{35/48+\varepsilon}\).  The candidate's use of
\(J_B^{1/2}K_\rho/L\) is valid but non-sharp; (129.A3) removes that
factor before threshold superposition.

**Retain/reject separately** the norm-relative formulation.  The hostile
stationary-alias profile still refutes a theorem stated solely in terms of
\(\|U\|_{V^2}\); it does not refute the absolute physical-family theorem
proved here.

The new fixed-block bound remains \(Y^{11/48}\) above the
\(Y^{1/2}\) determinant target and gives no global pointwise improvement.
Make no change to M9-M1, M9-M2, endpoint uniformity, M9, the conditional
quarter theorem, or the Gauss-circle target.  No numerical experiment or
external source was used.
