# Conductor review: actual full-block and bounded-lift savings

Campaign: `gc-w7-16-actual-determinant-fibre-gate`

Starting graph SHA-256:
`a27a89fd4e688cae719a28fec8f48dd74190bafb64d0345c590f1caadc2805d9`

Decision: pass the complete fixed-block product-window bound and the
bounded-lift top reduced-denominator curvature bound. Neither is the
required target estimate.

## 1. Complete fixed-block bound

Before reduced-ray grouping, fix one random frequency cell. For each
original denominator \(d\asymp D\), the admitted numerators form a bounded
number of intervals of total length

\[
 T_0\ll \min(L,D/W),
\]

up to the fixed M2 factor four. After extracting \(L^{-1}\), the literal
Vaaler/frequency weight has bounded sampled supremum and variation. Thus
Abel and the geometric-sum formula give the M1 norm

\[
 {1\over L}\min\left(T_0,{1\over\|c/d\|}\right),
\]

and the two M2 norms with frequencies
\(c/(4d)\pm1/4\).

If one of these norms is below \(\eta\), an integer product \(rd\) lies
in a real interval of length \(O(1+\eta D)\) about \(c\); in M2, \(r\)
is restricted to one odd class modulo four. Divisor bounds and dyadic
layer cake therefore prove, uniformly for real \(c\asymp Y\),

\[
 \sum_{d\asymp D}\min\left(T_0,{1\over\|c/d\|}\right)
 +\sum_{d\asymp D}\min\left(T_0,
 {1\over\|c/(4d)\pm1/4\|}\right)
 \ll_\varepsilon DY^\varepsilon.
\]

Every cell consequently has amplitude \(O_\varepsilon(DL^{-1}Y^\varepsilon)\).
The signed band meets \(O(1+WL/D)\) cells for every shift, including a
fixed-cost overlap of the two frequency signs. Squaring before integrating
the random shift gives

\[
 \boxed{
 \mathcal C_i(c)\ll_\varepsilon
 \left({D^2\over L^2}+{WD\over L}\right)Y^\varepsilon.}
\tag{117.C1}
\]

Since \(\mathcal C_i=\mathcal E_{i,=}+\mathfrak O_i\), with
\(\mathcal E_{i,=}\ll D/L\le D^2/L^2\), the same right side bounds
\(|\mathfrak O_i|\). This proof is in the original \((h,d)\) variables,
so it contains every lift and does not use a raywise or liftwise absolute
value.

At \((D,L,W)=(Y^{1/2},Y^{1/6},Y^{7/16})\), (117.C1) is
\(Y^{37/48+\varepsilon}\), a proved \(Y^{1/8}\) saving over the prior
\(Y^{43/48}\) coefficient-blind capacity. It is still
\(Y^{13/48}\) above the \(Y^{1/2}\) target.

## 2. Bounded-lift top-shell bound

Now restrict both reduced denominators to \(b,b'\asymp D\). Then
\(|a|,|a'|\asymp L\), and the simultaneous original supports force each
lift variable into a fixed finite set. Extend each finite-lift weight by
zero to all integer \((a',b')\) before imposing primitivity. The extension
has supremum plus total variation \(O(L^{-1})\), including profile entry,
exit, hard-top sample, star, and the triangular factor.

At fixed \((a,b,p)\), put \(a'=a+p\) and expand

\[
 {\bf1}_{(a',b')=1}=\sum_{\rho\mid a',\,\rho\mid b'}\mu(\rho).
\]

On \(b'=\rho v\), the interval has length \(O(Q_*/\rho)\), where

\[
 Q_*=\min\left(D,{D^2\over WL}\right),\qquad
 \lambda={YL\over D^3},
\]

and the reciprocal phase has second derivative comparable to
\(\lambda\rho^2\). Weighted van der Corput, followed by
\(\tau(a'),\sigma_{-1}(a')\ll_\varepsilon Y^\varepsilon\), gives the
inner bound

\[
 {Y^\varepsilon\over L}
 \min\left(Q_*,Q_*\sqrt\lambda+\lambda^{-1/2}\right).
\]

There are \(O(LD)\) outer rays and \(O(L)\) numerator increments; the
outer coefficient is \(O(L^{-1})\). Hence

\[
 \boxed{
 |\mathfrak O_{i,B\asymp D}|\ll_\varepsilon
 D\min\left(Q_*,Q_*\sqrt\lambda+\lambda^{-1/2}\right)Y^\varepsilon.}
\tag{117.C2}
\]

The M1 denominator character merely adds the two quarter-linear phases;
M2 has no denominator character in this orientation. Both signs reverse at
most the curvature sign, and \(\kappa_2=4\) changes constants only.

At minimax, \(Q_*=Y^{19/48}\), \(\lambda=Y^{-1/3}\), and (117.C2) is
\(Y^{35/48+\varepsilon}\). This is a genuine \(Y^{1/6}\) saving on the
bounded-lift shell, but remains \(Y^{11/48}\) above target. A
phase-conjugated coefficient cancels the reciprocal phase and violates the
finite-lift BV mechanism, so this saving uses an actual property absent
from the Round-95 adversary.

## 3. Scope and remaining seam

The full-block estimate has no target-safe point in the Round-95 hard
region: its term \(WD/L\) has exponent \(7/16+\delta-\ell\ge11/16\).
The top-shell lemma does not extend to \(B<D\), where the lift length
\(G=D/B\) grows and the complete lift transform has no proved uniform
variation in \(b'\). Taking endpoint variation absolutely can lose \(G\).

Promote (117.C1) and (117.C2) only with these scopes. Retain the complete
\(Y^{1/2}\) determinant correlation, local moment, pointwise exponent,
M9 parents, endpoint uniformity, and quarter target as open.

Evidence:

- `reports/actual_character_determinant_attack.md`;
- `reviews/hostile_round117_discovery_addendum.md`;
- `reports/blind_determinant_fibre_rederivation.md`.
