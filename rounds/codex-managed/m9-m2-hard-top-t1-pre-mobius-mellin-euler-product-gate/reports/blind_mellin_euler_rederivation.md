# Round 168 statement-only Mellin--Euler rederivation

- Campaign: m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate
- Task: blind_mellin_euler_rederivation
- Role: statement-only blind rederiver
- Status: candidate evidence only; no shared-state mutation is licensed

## 1. Result

### 1.1 Exact Euler product

Let

\[
\mathcal F(s,w)
=
\sum_{\substack{d_1,d_2\ge1\\
2\nmid d_1\\
d_1d_2\ {\rm squarefree}}}
\frac{\chi_4(d_1)}{d_1^s d_2^w},
\qquad \Re s,\Re w>1.
\tag{168.R1}
\]

Keeping squarefreeness, coprimality, parity, and the character in one local family gives

\[
\boxed{
\mathcal F(s,w)
=(1+2^{-w})
\prod_{p\ {\rm odd}}
\left(1+\chi_4(p)p^{-s}+p^{-w}\right).}
\tag{168.R2}
\]

Equivalently,

\[
\boxed{
\mathcal F(s,w)=L(s,\chi_4)\zeta(w)\mathcal G(s,w),}
\tag{168.R3}
\]

where

\[
\mathcal G(s,w)
=(1-2^{-2w})
\prod_{p\ {\rm odd}}
\left(1+\chi_4(p)p^{-s}+p^{-w}\right)
\left(1-\chi_4(p)p^{-s}\right)
\left(1-p^{-w}\right).
\tag{168.R4}
\]

The product \(\mathcal G\) converges absolutely and is holomorphic for

\[
\Re s>\frac12,\qquad \Re w>\frac12.
\tag{168.R5}
\]

In that region the only possible pole displayed by this factorization is \(w=1\); \(L(s,\chi_4)\) has no pole at \(s=1\). The residue at \(w=1\), if not cancelled by the literal transform, is

\[
\operatorname*{Res}_{w=1}\mathcal F(s,w)
=L(s,\chi_4)\mathcal G(s,1).
\tag{168.R6}
\]

### 1.2 Exact endpoint-lawful representation

There is an exact two-variable Mellin--Perron--Stieltjes representation that does not discard hard point values or choose a half-weight convention.

Put

\[
W(d_1,d_2)
=\mathcal A_{L,X}(d_1,d_2)
e\!\left(J\sqrt{d_1d_2}\right)
\tag{168.R7}
\]

on the integer lattice, with the literal half-open endpoints, floors, stars, hard values, and zero extension already included. Extend \(W\) by zero outside its finite support and define the forward mixed difference

\[
\Delta W(a,b)
=W(a,b)-W(a+1,b)-W(a,b+1)+W(a+1,b+1).
\tag{168.R8}
\]

Then

\[
W(d_1,d_2)
=\sum_{a\ge d_1}\sum_{b\ge d_2}\Delta W(a,b).
\tag{168.R9}
\]

For \(c_s,c_w>1\), define the finite Stieltjes polynomial

\[
\mathcal P_W(s,w)
=\sum_{a,b\ge1}\Delta W(a,b)
(a+\tfrac12)^s(b+\tfrac12)^w.
\tag{168.R10}
\]

Double Perron inversion at the nonintegral thresholds \(a+\tfrac12\), \(b+\tfrac12\) gives the exact iterated-limit identity

\[
\boxed{
\mathcal S_{L,1}
=
\lim_{T_s\to\infty}\lim_{T_w\to\infty}
\frac1{(2\pi i)^2}
\int_{c_s-iT_s}^{c_s+iT_s}
\int_{c_w-iT_w}^{c_w+iT_w}
\mathcal F(s,w)
\frac{\mathcal P_W(s,w)}{sw}\,dw\,ds.}
\tag{168.R11}
\]

This formula retains every endpoint law exactly. Ordinary Lebesgue Mellin inversion of a smoothed model would not recover arbitrary isolated hard values; (168.R8)--(168.R11) do.

### 1.3 Scoped no-go

The packet does not supply enough analytic structure to prove

\[
\mathcal S_{L,1}\ll_\varepsilon L^{3/2}X^\varepsilon
\tag{168.R12}
\]

by contour motion, residues, functional equations, or hybrid absolute mean values.

The first interface failure is transform control. Boundedness and finite support give only

\[
\sum_{a,b}|\Delta W(a,b)|\ll L^2,
\tag{168.R13}
\]

with no target-safe two-variable variation, angular decay, or finite-height truncation estimate. Hard endpoints forbid assumed rapid decay.

Even after granting a smooth fixed-relative interior model, the square-root phase places the radial Mellin mass at height

\[
T_{\rm rad}\asymp JL.
\tag{168.R14}
\]

On critical contours, an optimal Lindelöf-sized pointwise bound or a standard \(T_{\rm rad}^{1+\varepsilon}\) hybrid second moment, used after absolute values or Cauchy, certifies only the capacity

\[
L\,T_{\rm rad}^{1/2}X^\varepsilon
=L^{3/2}J^{1/2}X^\varepsilon,
\tag{168.R15}
\]

which misses (168.R12) by \(J^{1/2}\). A successful Mellin route therefore needs a new signed oscillatory hybrid estimate across the full coupled radial spectrum, together with an exact bound for the \(w=1\) residue and all hard endpoint measures. No such estimate is contained in the statement packet.

This is a route-scoped no-go, not a disproof of (168.R12).

## 2. Exact statement and hypotheses

The arithmetic coefficient in (168.B1) is

\[
a(d_1,d_2)
=\mathbf 1_{2\nmid d_1}
\mathbf 1_{d_1d_2\ {\rm squarefree}}
\chi_4(d_1).
\tag{168.R16}
\]

Squarefreeness of \(d_1d_2\) simultaneously implies that \(d_1\) and \(d_2\) are squarefree and \((d_1,d_2)=1\). No Möbius opening is used.

The analytic weight \(W\) is bounded, supported on \(d_1,d_2\asymp L\), and includes all data named in the packet. Consequently it has \(O(L^2)\) lattice support. No smoothness or bounded-variation norm beyond boundedness is assumed.

The exact representation (168.R11) uses:

1. zero extension of the literal lattice weight;
2. finite mixed differences, so all exchanges with the \(a,b\) sums are finite;
3. initial contours \(c_s,c_w>1\), where (168.R1) converges absolutely; and
4. half-integer Perron thresholds, so equality with an integer never occurs and no unintended \(1/2\)-weight is introduced.

If a contour is moved only to

\[
\Re s=\frac12+\eta,\qquad \Re w=\frac12+\eta,
\]

then \(\mathcal G\) is holomorphic by (168.R5). Moving the \(w\)-contour across \(w=1\) creates the explicit residue

\[
\frac1{2\pi i}
\int
L(s,\chi_4)\mathcal G(s,1)
\frac{\mathcal P_W(s,1)}{s}\,ds.
\tag{168.R17}
\]

There is no analogous \(s=1\) residue. Moving either contour past \(0\) would additionally cross the Perron poles \(1/s\) or \(1/w\), which encode cumulative endpoint terms and cannot be omitted.

## 3. Proof/derivation

### 3.1 Euler factors and analytic factorization

At \(p=2\), oddness forbids \(2\mid d_1\), while squarefreeness permits \(2\) in \(d_2\) at most once. The local factor is

\[
1+2^{-w}.
\]

For an odd prime \(p\), squarefreeness and coprimality allow exactly three choices:

- \(p\) divides neither variable;
- \(p\) divides \(d_1\), contributing \(\chi_4(p)p^{-s}\);
- \(p\) divides \(d_2\), contributing \(p^{-w}\).

This proves (168.R2).

For \(p\) odd, put

\[
x=\chi_4(p)p^{-s},\qquad y=p^{-w}.
\]

After extracting the local factors of \(L(s,\chi_4)\zeta(w)\), the correction is

\[
(1+x+y)(1-x)(1-y)
=1-x^2-y^2-xy+x^2y+xy^2.
\tag{168.R18}
\]

At \(p=2\), the correction is

\[
(1+2^{-w})(1-2^{-w})=1-2^{-2w}.
\]

The nonconstant terms in (168.R18) are

\[
O\!\left(p^{-2\Re s}+p^{-2\Re w}
+p^{-\Re s-\Re w}\right).
\]

Their prime sum converges under (168.R5), proving (168.R3)--(168.R5).

Two one-variable controls confirm the normalization:

\[
\mathcal F(s,+\infty)
=\prod_{p\ {\rm odd}}(1+\chi_4(p)p^{-s}),
\]

and

\[
\mathcal F(+\infty,w)
=\prod_p(1+p^{-w})
=\frac{\zeta(w)}{\zeta(2w)}.
\tag{168.R19}
\]

The second equality also checks the \(p=2\) correction.

### 3.2 Exact Stieltjes telescoping and Perron inversion

Because \(W\) has finite support, summing (168.R8) first in \(a\) and then in \(b\) telescopes exactly to (168.R9). Hence

\[
\begin{aligned}
\mathcal S_{L,1}
&=\sum_{d_1,d_2}a(d_1,d_2)W(d_1,d_2)\\
&=\sum_{a,b}\Delta W(a,b)
\sum_{d_1\le a}\sum_{d_2\le b}a(d_1,d_2).
\end{aligned}
\tag{168.R20}
\]

For integer \(a,b\), the thresholds \(a+\tfrac12\), \(b+\tfrac12\) are not attained by \(d_1,d_2\). Double Perron inversion therefore gives

\[
\sum_{d_1\le a}\sum_{d_2\le b}a(d_1,d_2)
=
\lim_{T_s\to\infty}\lim_{T_w\to\infty}
\frac1{(2\pi i)^2}
\int\!\!\int
\mathcal F(s,w)
\frac{(a+\tfrac12)^s(b+\tfrac12)^w}{sw}\,dw\,ds.
\tag{168.R21}
\]

Substitution into (168.R20) proves (168.R11). All hard values occur in the literal numbers \(W(a,b)\), so the mixed difference and Perron representation preserve them.

The variation control (168.R13) follows because every value of \(W\) appears in at most four mixed differences and \(|W|\ll1\) on \(O(L^2)\) lattice sites. This is sufficient for exactness but not for (168.R12).

### 3.3 Radial and angular Mellin frequencies

To see the analytic scale without changing endpoint status, use a smooth interior control weight and write

\[
x=L e^{\rho+\theta},\qquad
y=L e^{\rho-\theta}.
\]

Then

\[
\sqrt{xy}=L e^\rho,\qquad
\frac{dx}{x}\frac{dy}{y}=2\,d\rho\,d\theta.
\]

For \(s=\sigma+it\), \(w=\tau+iu\), the Mellin kernel is

\[
x^sy^w
=L^{s+w}
e^{(s+w)\rho+(s-w)\theta}.
\]

Put

\[
q=t+u,\qquad p=t-u.
\]

The radial phase is

\[
2\pi JLe^\rho+q\rho.
\]

Its stationary equation is

\[
q=-2\pi JLe^\rho,
\tag{168.R22}
\]

so a fixed-relative product shell produces a radial frequency interval of length and size

\[
|q|\asymp T_{\rm rad}=JL.
\]

The angular transform is dual to \(p=t-u\). Smooth fixed-relative ratio profiles can localize \(p\), but half-open angular boundaries and hard endpoint measures have only finite-variation decay; they cannot be assigned rapid decay without a separate lemma.

At \(\sigma=\tau=1/2\), one-dimensional stationary phase in \(\rho\) gives the generic radial transform scale

\[
L\,T_{\rm rad}^{-1/2}
\tag{168.R23}
\]

over a \(q\)-interval of length \(T_{\rm rad}\). Thus its absolute \(L^1\) capacity is \(L T_{\rm rad}^{1/2}\), which is (168.R15).

### 3.4 Contours, residues, functional equations, and mean values

Starting from \(c_s,c_w>1\), moving to \(1/2+\eta\) crosses only the possible \(w=1\) pole in the Euler factorization. The residue is (168.R17); the \(\chi_4\)-twist removes an \(s=1\) pole but does not force (168.R17) to vanish. The literal angular transform and endpoint measures must be used to bound it.

On the main critical contours, the relevant heights satisfy

\[
|t|,|u|\asymp JL
\]

when the angular frequency \(p=t-u\) is bounded. The individual functional equations for \(L(s,\chi_4)\) and \(\zeta(w)\) do not give a two-variable functional equation for \(\mathcal G(s,w)\). Approximate functional equations at these heights have respective lengths

\[
(JL)^{1/2}\quad\text{and}\quad(JL)^{1/2},
\]

so their unseparated product has double length \(JL\). Termwise absolute estimation does not recover the missing factor.

Even granting the hybrid mean-square control

\[
\int_{T}^{2T}
\left|L(\tfrac12+it,\chi_4)\zeta(\tfrac12+it)\right|^2dt
\ll_\varepsilon T^{1+\varepsilon},
\tag{168.R24}
\]

Cauchy combined with (168.R23) yields

\[
L\,T_{\rm rad}^{1/2}X^\varepsilon,
\]

not \(L^{3/2}X^\varepsilon\). Since \(T_{\rm rad}=JL\), the missing factor is \(J^{1/2}\). Hard cutoffs broaden rather than shorten the spectral support.

Therefore contour motion and standard absolute hybrid mean values do not prove (168.R12). One must preserve cancellation in the coupled \(q\)-integral, control the residue, and account for every Stieltjes boundary contribution.

## 4. First doubtful or unproved step

The first unproved step is a target-safe transform theorem for the literal endpoint law:

> Decompose the exact mixed-difference transform \(\mathcal P_W(s,w)/(sw)\) into a bounded-cost smooth interior and explicit endpoint measures, retain the coupled radial oscillation over \(|t+u|\asymp JL\), and prove that the main integral, the \(w=1\) residue, all truncation tails, and every hard endpoint contribution total \(O_\varepsilon(L^{3/2}X^\varepsilon)\).

Boundedness of \(\mathcal A_{L,X}\) gives only (168.R13), so this theorem does not follow from the packet. If one assumes the smooth interior decomposition, the next missing input is a signed hybrid estimate saving \(J^{1/2}\) beyond (168.R24). A functional equation or approximate functional equation alone merely rewrites that missing cancellation.

## 5. Required controls and outcomes

| Required control | Outcome |
|---|---|
| Odd-prime local choices | **PASS.** The three admissible states give \(1+\chi_4(p)p^{-s}+p^{-w}\) |
| Two-adic local factor | **PASS.** Oddness of \(d_1\) gives \(1+2^{-w}\) |
| Squarefree/coprime ownership | **PASS.** It is retained in one Euler factor and never Möbius-separated |
| One-variable Euler limits | **PASS.** Equation (168.R19) checks both character and \(p=2\) normalization |
| Literal hard endpoints | **PASS algebraically.** Mixed differences and half-integer Perron thresholds retain every value exactly |
| Perron truncation | **OPEN.** Exactness is an infinite-height limit; no target-safe finite truncation follows from boundedness |
| Pole ledger | **PASS.** Only the possible \(w=1\) Euler pole is crossed before the critical region; \(s=0,w=0\) matter only if crossed |
| Radial frequency | **PASS.** The square-root phase forces \(|t+u|\asymp JL\) |
| Angular transform | **OPEN at hard boundaries.** Rapid decay is not licensed |
| Approximate functional equation lengths | **PASS.** Each is \((JL)^{1/2}\), giving product length \(JL\) |
| Absolute hybrid-mean route | **FAILS by \(J^{1/2}\).** It yields (168.R15) |
| Unsigned false control | **PASS as a rejection test.** Removing \(\chi_4\) would introduce an \(s=1\) zeta pole; the actual character removes that pole, but pole removal alone does not prove the signed target |
| Downstream scope | **PASS.** No residual, parent, bridge, quarter theorem, or exponent is promoted |

No numerical experiment was used. The report is entirely algebraic and analytic.

## 6. Dependencies/exact artifacts used

Only the following artifacts were read:

1. protocol.md;
2. rounds/codex-managed/m9-m2-hard-top-t1-pre-mobius-mellin-euler-product-gate/blind_statement.md.

No proof graph, active campaign, strategy, prior round, barrier packet, sibling report, source, candidate, review, or synthesis was inspected.

## 7. Recommended state effect

**RETAIN the Mellin--Euler route as open; record the exact Euler product, exact endpoint-lawful Perron--Stieltjes identity, and the scoped absolute-hybrid no-go; make no proof-state change.**

The arithmetic family has a clean factorization and only a possible \(w=1\) Euler pole in the half-plane (168.R5). The exact hard-endpoint transform exists, but boundedness supplies no target-safe truncation or angular decay. Even the smooth control misses the target by \(J^{1/2}\) after absolute hybrid mean values. Do not infer (168.B2), separate the squarefree family by Möbius inversion, discard the residue or hard endpoints, pivot within the round, close a parent, or change an exponent.
