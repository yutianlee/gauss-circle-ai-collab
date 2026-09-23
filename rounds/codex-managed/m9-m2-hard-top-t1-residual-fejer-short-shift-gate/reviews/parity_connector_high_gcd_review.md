# Round 165 seam review: parity connector and high divisor-gcd sector

## 1. Result

**GREEN, with two statement-clarity repairs and no mathematical repair.**

The discovery report's parity-window connector is exact for every integer
(R\ge2), including odd (R), every hard support endpoint, and the full
zero extension:

\[
 \boxed{\mathfrak E_R\le2\mathfrak E_R^{(2)}.}
\tag{165.R1}
\]

If

\[
 D=\sum_N|c_N^{\rm rem}|^2,
 \qquad
 C=\Re\mathfrak C_{R,J,L}^{\rm rem},
\tag{165.R2}
\]

and (C_2) is the same aggregate restricted to even shifts, then

\[
 \boxed{C\le\frac D2+2C_2.}
\tag{165.R3}
\]

Thus the one-sided even-shift theorem in (165.D4) is genuinely sufficient
for the complete residual Fejer target and, through the accepted
Round-164 sliding inequality, for the residual scalar target.  It does not
bound any individual odd shift and does not use the XOR scalar as an
energy estimate.

For odd (R=2S+1), the exact endpoint formula is stronger and clearer
than the discovery report's prose: if (x_n=z_{2n}), (y_n=z_{2n+1}),
and \(\mathcal E_T(w)=T^{-1}\sum_k|\sum_{j<T}w_{k+j}|^2\), then

\[
\boxed{
 \mathfrak E_{2S+1}^{(2)}
 =\frac{S+1}{2S+1}\{\mathcal E_{S+1}(x)+\mathcal E_{S+1}(y)\}
 +\frac{S}{2S+1}\{\mathcal E_S(x)+\mathcal E_S(y)\}.}
\tag{165.R4}
\]

Consequently, the terminal even gap (2S=R-1) occurs once and has exact
weight (1/R).  There is no floor, ceiling, or half-window error.

The hostile report's high-common-divisor estimate is also correct after
making explicit that this is the **character-divisor gcd**

\[
 \delta=(d,d'),
\tag{165.R5}
\]

not the complementary-factor gcd (G=(m,m')) used in the discovery
normal form.  If the exact literal opening is restricted to
(\delta\ge G_0), then

\[
 \boxed{
 |\mathfrak C_{\delta\ge G_0}^{\rm rem}|
 \ll_\varepsilon \frac{L^3}{G_0}X^\varepsilon
 \qquad(1\le G_0<R).}
\tag{165.R6}
\]

In particular, for every fixed (gamma>0), all divisor incidences with
((d,d')\ge\gamma L) form a genuine owner-complete target-safe sector.
The statement includes (d=d'), the squarefree even-even complement
branch, both selector statuses, all star and hard-profile values, and both
outer shell endpoints.

Combining the two verified reductions, the smallest sufficient theorem
currently exposed by these seams is the one-sided **even-shift,
low-character-divisor-gcd** aggregate.  The two clarity repairs recommended
for synthesis are:

1. print (165.R4), rather than saying only that odd (R) needs no
   rounding; and
2. reserve (G=(m,m')) for the discovery coordinate, while writing
   (delta=(d,d')) and (G_0) for the hostile threshold.

## 2. Exact statement and hypotheses

Let (z=(z_N)_{N\in\mathbb Z}) be any finitely supported complex sequence
and (R\ge2) an integer.  Define

\[
 Y_s=\sum_{j=0}^{R-1}z_{s+j},
 \qquad
 Y_s^{(\epsilon)}
 =\sum_{\substack{0\le j<R\\s+j\equiv\epsilon\ (2)}}z_{s+j},
 \quad\epsilon\in\{0,1\},
\tag{165.R7}
\]

and

\[
 \mathfrak E_R=\frac1R\sum_s|Y_s|^2,
 \qquad
 \mathfrak E_R^{(2)}
 =\frac1R\sum_s\bigl(|Y_s^{(0)}|^2+|Y_s^{(1)}|^2\bigr).
\tag{165.R8}
\]

Full-line zero extension is part of these definitions.  Expanding gives

\[
\begin{aligned}
 \mathfrak E_R
 &=D+2\Re\sum_{1\le r<R}
       \left(1-\frac rR\right)\sum_Nz_{N+r}\overline{z_N},\\
 \mathfrak E_R^{(2)}
 &=D+2\Re\sum_{1\le q<R/2}
       \left(1-\frac{2q}{R}\right)\sum_Nz_{N+2q}\overline{z_N},
\end{aligned}
\tag{165.R9}
\]

where (D=\sum_N|z_N|^2\).  For the literal application,
(z_N=c_N^{\rm rem}e(J\sqrt N)), so (D) is the accepted coefficient
energy and the second line of (165.R9) is exactly the theorem (165.D4).

For the high-gcd seam, use the discovery report's literal opening

\[
\begin{aligned}
 \mathfrak C_{R,J,L}^{\rm rem}
 ={}&\sum_{1\le r<R}\left(1-\frac rR\right)
 \sum_{\substack{d,m,d',m'\ge1\\d,d'\ {\rm odd}\\d'm'-dm=r}}
 \chi_4(d')\chi_4(d)\\
 &\qquad\times
 \lambda_{d'm'}(d')\overline{\lambda_{dm}(d)}
 e\!\left(J(\sqrt{d'm'}-\sqrt{dm})\right),
\end{aligned}
\tag{165.R10}
\]

with every unsupported (lambda_N(d)) defined to be zero.  On a nonzero
term, the literal shell and cone give

\[
 d,d',m,m'\asymp L.
\tag{165.R11}
\]

Moreover,

\[
 |\lambda_N(d)|\ll1.
\tag{165.R12}
\]

Indeed, (mu^2(N)\) and (\rho_N(d)) have modulus at most one, the
normalization is \(\asymp1\) on the shell, and the accepted zero-extended
profile has total variation (O(1)).  Since it is zero off its compact
support, its supremum, including hard faces and star values, is also
(O(1)).  Formula (165.R12) is the profile-atom input needed by the
count; no unprinted lower bound or smoothness across an endpoint is used.

## 3. Proof or derivation

### 3.1 Parity-window inequality and exact pair weights

For every (s), one has

\[
 Y_s=Y_s^{(0)}+Y_s^{(1)},
 \qquad
 |Y_s|^2\le2\bigl(|Y_s^{(0)}|^2+|Y_s^{(1)}|^2\bigr).
\tag{165.R13}
\]

Summing (165.R13) over the full integer line and dividing by (R) proves
(165.R1).  No support endpoint appears because (z) is already zero
outside its literal interval.

To verify (165.R9), fix a pair (z_N,z_{N+r}).  It occurs in exactly
(R-r) windows.  It lies in a common parity component if and only if
(r) is even.  Thus a pair at gap (2q<R) has coefficient

\[
 \frac{R-2q}{R}=1-\frac{2q}{R}
\tag{165.R14}
\]

in \(\mathfrak E_R^{(2)}\), while every diagonal term occurs in exactly
(R) windows and therefore has coefficient one.  This proves both lines
of (165.R9), including all Fejer weights.

For (R=2S), direct reindexing gives

\[
 \mathfrak E_{2S}^{(2)}
 =\mathcal E_S(x)+\mathcal E_S(y).
\tag{165.R15}
\]

For (R=2S+1), an even-start window contains (S+1) consecutive terms
of (x) and (S) consecutive terms of (y); an odd-start window contains
(S+1) consecutive terms of (y) and (S) consecutive terms of (x).
Every possible subsequence-window start occurs once.  Dividing the four
window sums by (2S+1) proves (165.R4).  Expanding (165.R4), a subsequence
gap (q<S) receives

\[
 \frac{S+1-q}{2S+1}+\frac{S-q}{2S+1}
 =1-\frac{2q}{2S+1},
\tag{165.R16}
\]

while (q=S) occurs only in the length-(S+1) term and receives
(1/(2S+1)).  These are exactly the weights in (165.R14).

Writing \(\mathfrak E_R=D+2C\) and
\(\mathfrak E_R^{(2)}=D+2C_2\), inequality (165.R1) becomes

\[
 D+2C\le2D+4C_2,
\tag{165.R17}
\]

which is precisely (165.R3).  If the one-sided theorem (C_2\ll_\varepsilon
L^2X^\varepsilon\) holds, then (165.R3) and the accepted
(D\ll_\varepsilon L^2X^\varepsilon) give the complete Round-164
correlation target.  Equivalently,

\[
 \mathfrak E_R\le2\mathfrak E_R^{(2)}
 =2D+4C_2\ll_\varepsilon L^2X^\varepsilon.
\tag{165.R18}
\]

The accepted factor ((M_L+R-1)/R\asymp L) then gives the residual scalar
square (O_\varepsilon(L^3X^\varepsilon)).  This verifies sufficiency
without any estimate for an individual odd shift.

### 3.2 High character-divisor gcd count

In (165.R10), put

\[
 \delta=(d,d'),\qquad d=\delta u,qquad d'=\delta v,
 \qquad (u,v)=1.
\tag{165.R19}
\]

The divisors are odd, so (delta,u,v) are odd.  The product-shift equation
becomes

\[
 \delta(vm'-um)=r.
\tag{165.R20}
\]

Hence (delta\mid r); write (r=\delta h).  By (165.R11), for fixed
(delta),

\[
 u,v\asymp\frac L\delta,
 \qquad 1\le h<\frac R\delta\ll\frac L\delta.
\tag{165.R21}
\]

For fixed ((\delta,u,v,h)), choose one solution of

\[
 v m'-u m=h.
\tag{165.R22}
\]

All solutions are (m=m_0+vt), (m'=m'_0+ut).  Since the physical
(m)-interval has length (O(L)) and (v\asymp L/\delta), the number of
allowed (t)'s is (O(1+\delta)=O(\delta)).  The same conclusion follows
from the (m')-interval.  Dropping squarefreeness, coprimalities,
selectors, parity, and profile supports can only enlarge an absolute
upper bound.  Using (165.R12) and (0<1-r/R\le1), the contribution with
(delta\ge G_0) is therefore

\[
\begin{aligned}
 |\mathfrak C_{\delta\ge G_0}^{\rm rem}|
 &\ll
 \sum_{G_0\le\delta<R}
 \left(\frac L\delta\right)^2
 \left(\frac L\delta\right)\delta\\
 &\ll L^3\sum_{\delta\ge G_0}\delta^{-2}
 \ll \frac{L^3}{G_0}.
\end{aligned}
\tag{165.R23}
\]

Allowing (X^\varepsilon) gives (165.R6).  Every literal tuple is assigned
to exactly one (delta), because (165.R10) is a multiplicity-one divisor
opening.  Thus this is an exact incidence-sector decomposition, not a raw
row heuristic.

The potentially delicate subcases do not change the ledger:

- If (d=d'), then (delta=d), (u=v=1), and (165.R22) is
  (m'-m=h).  For each (delta,h) there are (O(L)=O(\delta)) terms in
  the high-gcd range, exactly as counted in (165.R23).
- If both supported rows are even, the squarefree complements (m,m')
  contain exactly one factor (2).  Since (u,v,delta) are odd,
  (165.R22) forces (h) even.  Restricting the (t)-progression to the
  even-even branch, and then excluding multiples of (4) or nonsquarefree
  odd parts, only decreases its (O(\delta)) length.
- On a selected row, \(\rho_N(d)\in\{0,1\}\); on a no-pair row it equals
  one.  The selector is canonical, so there is no extra selector
  multiplicity.
- Hard endpoints, star values, and profile atoms are values of the same
  bounded (lambda_N(d)).  Each divisor incidence is evaluated once;
  no Stieltjes boundary atom is added to the original correlation.

This verifies that (165.R6) is genuinely owner-complete for the opened
incidence sector.  It is not a statement that a whole row (c_N^{\rm rem})
has a unique gcd: one row may contribute several divisor incidences, each
of which is assigned separately and exactly once.

### 3.3 Combined strict sufficient frontier

Fix (gamma>0) and split the even-shift aggregate as

\[
 C_2=C_{2,<\gamma L}+C_{2,\ge\gamma L},
\tag{165.R24}
\]

where the split is made after the exact divisor opening by
(delta=(d,d')).  Equation (165.R6) gives

\[
 |C_{2,\ge\gamma L}|
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon.
\tag{165.R25}
\]

Therefore the complete residual target follows from the strictly smaller
one-sided theorem

\[
 \boxed{
 C_{2,<\gamma L}
 \ll_{\gamma,\varepsilon}L^2X^\varepsilon,}
\tag{165.R26}
\]

with every literal squarefree indicator, selector, parity branch, profile,
endpoint, and phase retained.  Equation (165.R26) is not proved by either
report; it is the exact surviving seam after the two verified reductions.

## 4. First doubtful or unproved step

There is no doubtful step in (165.R1)--(165.R25).  In particular, odd
(R) creates a positive convex mixture of length-(S) and length-(S+1)
subsequence energies, not a boundary error, and the high-gcd count charges
equal divisors, even-even rows, selectors, and profile atoms explicitly.

The first unproved affirmative statement is (165.R26).  On even shifts,
the discovery report's complement-gcd progression has frozen character;
on the remaining low character-divisor-gcd sector, the hostile report's
positive progression or phase-dual placements still have (L^3)
capacity.  A proof must retain signed interaction across slopes,
progressions, selectors, or phase duals before a positive norm.

The high-gcd lemma is target-safe only for a fixed fractional threshold
(G_0=\gamma L).  Formula (165.R6) is still useful for smaller (G_0),
but it reaches the (L^2) target precisely when (G_0\gg L) up to fixed
constants.  It does not prove density, a lower bound, or cancellation in
the complementary low-gcd sector.

## 5. Control tests and outcomes

| Seam control | Outcome |
|---|---|
| parity-window positivity | **GREEN.** Both sides of (165.R8) are exact full-line sums of squares. |
| full-to-even connector | **GREEN.** Pointwise (165.R13) gives the factor (2), with no shiftwise modulus. |
| even-gap Fejer weights | **GREEN.** A gap (2q) occurs in exactly (R-2q) windows, giving (165.R14). |
| odd-(R) endpoint | **GREEN.** Formula (165.R4) is exact; (q=S) has weight (1/(2S+1)). |
| one-sided algebra | **GREEN.** (D+2C\le2D+4C_2) is exactly (C\le D/2+2C_2). |
| even-shift sufficiency | **GREEN reduction.** Theorem (165.D4), if proved, implies the Round-164 correlation and scalar targets. |
| gcd identity and multiplicity | **GREEN.** (delta=(d,d')) gives one (r=delta h) class for every literal divisor tuple. |
| (L^3/G_0) count | **GREEN.** Per (delta), there are (O((L/\delta)^3\delta)=O(L^3/\delta^2)) tuples. |
| equal-divisor slide | **GREEN.** (u=v=1) is contained with (O(L)=O(\delta)) solutions per high (delta). |
| squarefree even-even branch | **GREEN.** It is a subprogression of the counted solutions and introduces no factor. |
| selector multiplicity | **GREEN.** (\rho\in\{0,1\}) and is canonical on each row. |
| profile atoms and hard values | **GREEN.** Zero-extended variation gives a uniform pointwise bound; atoms are evaluated once. |
| owner completeness | **GREEN with scope.** Complete for the opened divisor-incidence sector, not a unique-gcd partition of product rows. |
| combined frontier | **GREEN reduction, OPEN estimate.** (165.R26) is sufficient and remains unproved. |
| physical and downstream scope | **GREEN quarantine.** No residual target, full (t=1), other channel, hard TOP, M9--M2, M9--M1, M9, bridge, quarter theorem, or exponent is promoted. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

This independent seam review used exactly:

1. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reports/actual_residual_short_shift_attack.md`;
2. `rounds/codex-managed/m9-m2-hard-top-t1-residual-fejer-short-shift-gate/reports/short_shift_arithmetic_hostile_audit.md`; and
3. `proofs/kernels/m9_m2_hard_top_t1_residual_transport_fejer_energy_reduction.md`.

No web source, computation, sibling review, shared state, or other
repository artifact was used.

## 7. Recommended state effect

**Promote, after conductor graph and remaining seam validation,** the
parity-window connector (165.R1), its exact odd-(R) formula (165.R4), and
the one-sided corollary (165.R3) as a proved-internal reduction.  State the
open sufficient theorem with the literal range (1\le q<R/2) and weight
(1-2q/R).

**Promote or retain as a proved sector lemma,** again subject to conductor
state validation, the exact opened-incidence estimate (165.R6), with
(delta=(d,d')) and fixed-fraction consequence
(delta\ge\gamma L).  Its owner is the complete divisor-incidence sector;
do not print it as a unique partition of product rows.

**Apply the two statement repairs in synthesis:** include the convex
odd-(R) mixture (165.R4), and keep (delta=(d,d')), (G=(m,m')), and
the threshold (G_0) notationally distinct.  Also cite (165.R12) when
using the high-gcd tuple count so hard/star values are visibly charged.

**Keep open** (165.D4) and the still smaller sufficient theorem
(165.R26).  Do not promote the residual target, complete (t=1) face,
remaining few-point channels, hard TOP, either smooth M2 packet,
M9--M2, M9--M1, endpoint uniformity, M9, the conditional bridge, the
quarter theorem, or either global exponent.
