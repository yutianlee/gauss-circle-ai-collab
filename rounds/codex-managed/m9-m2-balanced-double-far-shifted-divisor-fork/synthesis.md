# Round 115 synthesis: phase-free mode closed, oscillatory aliases open

Campaign: m9-m2-balanced-double-far-shifted-divisor-fork

Round type: analytic follow-through

Starting recorded graph SHA-256:
6eb6eb5941e6d4720294c6b0890356113700db3201cf7c19337b96fb5ed47155

Resulting graph SHA-256:
6421d27cb531be922b11ec48b51002ba568f235d510d16ac28a7d84881d66dad

## 1. Conductor decision

Promote the exact shifted-divisor and increment charts, the target-safe
fully assembled phase-free double-far mode, and the scoped
Fejer-owner-amplification obstruction. Retain the actual oscillatory
double-far estimate as open.

Round 115 resolves the main-term fork more precisely than either proposed
outcome:

- the complete phase-free double-far aggregate saves the required factor
  \(L\) by actual \(\chi_4\) cancellation;
- this is assembled cancellation, not termwise annihilation: individual
  actual residue sectors have \(L^4\) coefficient capacity;
- subtracting the phase-free mode leaves an exact oscillatory remainder
  with unchanged worst-case capacity;
- one-step Fejer dispersion cannot reuse the already target-saturating
  corridors at a shortened scale without amplifying their allowance; and
- the nonzero half-shifted Poisson aliases, not the zero mode, are now the
  first open analytic object.

No balanced packet estimate or exponent is proved.

## 2. Literal coefficient and geometric charts

For

\[
 C_B(n,r)=
 \sum_{\substack{hk=n,\ h'k'=n+r\\|hk'-h'k|>L}}
 a_B^{<}(h,k)\overline{a_B^{<}(h',k')},
\]

the divisor gate is exactly

\[
 hk'-h'k
 ={h^2(n+r)-h'^2n\over hh'}.
\tag{115.S1}
\]

With \(h'=h+p\), \(k'=k+q\),

\[
 r=hq+kp+pq,\qquad \rho=hq-kp,
\tag{115.S2}
\]

\[
 r+\rho=q(2h+p),\qquad r-\rho=p(2k+q).
\tag{115.S3}
\]

Only even \(p=2s\) contributes, and

\[
 \chi_4(h)\chi_4(h+p)=(-1)^s=e(s/2).
\tag{115.S4}
\]

Thus the character is constant on a fixed shift and translates the
shift-dual lattice by one half.

The determinant has the exact angular representation

\[
 \rho=2\sqrt{n(n+r)}\sinh(t-t'),
\qquad
 t=\log(h/\sqrt n),\quad
 t'=\log(h'/\sqrt{n+r}).
\tag{115.S5}
\]

For
\(F_{p,q}(x,y)=\sqrt{(x+p)(y+q)}-\sqrt{xy}\),

\[
 \det\nabla^2F_{p,q}
 =-{(qx-py)^2\over
 16\{xy(x+p)(y+q)\}^{3/2}}.
\tag{115.S6}
\]

At the critical scale
\(|\det\nabla^2(RF_{p,q})|\asymp\rho^2\). This is continuous
nondegeneracy only; the lattice aliases remain to be estimated.

## 3. Phase-free mode

Define

\[
 M_B^{(0)}
 =\sum_{\mathrm{df}}
 a_B^{<}(h,k)\overline{a_B^{<}(h',k')}.
\tag{115.S7}
\]

Two independent arguments prove

\[
 |M_B^{(0)}|
 \ll_\varepsilon L^3X^\varepsilon.
\tag{115.S8}
\]

The direct proof expands the second gcd weight over divisors and applies
Abel summation in \(h'\). The two far gates create only \(O(1)\) interval
pieces, the literal slanted amplitude has total variation \(O(1)\) on each,
and the divisor expansion costs \(X^\varepsilon\). There are \(O(L^3)\)
outer triples.

The statement-only proof instead obtains

\[
 \left|\sum_{h,k}a_B^{<}(h,k)\right|
 \ll L\log^2(2L)
\]

by exact-gcd coordinates, Möbius inversion, and character summation, then
restores both target-safe corridors. This independently gives (115.S8).

The saving is lost after a residuewise, shiftwise, divisorwise, or
shellwise absolute value. In a nondegenerate actual core, the \(p=0\)
sector has coherent \(L^3\) coefficient mass, and each of two opposite
residue sectors can have \(L^4\) coefficient mass. These controls prove
that the assembled bound is cancellation, not algebraic vanishing. They
are not lower bounds for the oscillatory sum.

## 4. Fejer and transform obstruction

For \(b_n=c_B(n)e(R\sqrt n)\), supported on
\(N_B\asymp L^2\), Fejer gives

\[
 \left|\sum_nb_n\right|^2
 \le {N_B+H-1\over H}
 \left[
 \Gamma(0)+2\Re\sum_{1\le r<H}
 (1-r/H)\Gamma(r)
 \right].
\tag{115.S9}
\]

For \(2\le H\le L\), the accepted radial-corridor allowance becomes
\(O_\varepsilon(L^4X^\varepsilon)\) after the Fejer prefactor. For
\(L\le H\le N_B\), either complete target-saturating corridor supplies
only

\[
 O_\varepsilon\!\left((L^5/H+L^3)X^\varepsilon\right).
\tag{115.S10}
\]

Hence the existing owners certify no fixed-power shortening
\(H\le L^{2-\delta}\). At \(H=L^{2-o(1)}\) the shift window still has full
power length. The two-dimensional Fejer window has the same area
amplification. This is an obstruction to owner reuse, not a lower bound for
the signed Fejer form and not a disproof of a new local-energy theorem.

The critical outer B-process has \(|f''|\asymp1\), dual length
\(\asymp L^2\), and Legendre phase \(X/(4m)\); it is capacity-preserving.
The half-character shift removes no nonzero stationary family. Equation
(115.S6) removes only the interior zero-frequency critical point, not the
zero Poisson summand, boundary terms, or integer aliases.

The audited theorems of Cowan and Chamizo do not import. Cowan's character,
level, power, and fixed-parameter hypotheses fail. Chamizo treats the
complete \(r_2\)-correlation and exhibits a nonzero main term, but not the
literal divisor truncation, gcd mask, determinant deletion, slanted weight,
or simultaneous nonlinear shift sum. Even its displayed hardest-range
fixed-shift error misses the joint energy budget after a shiftwise triangle
sum.

## 5. Smallest open survivor

Set

\[
 \mathcal R_B^{\mathrm{osc}}
 =
 \sum_{\mathrm{df}}a_B^{<}(h,k)
 \overline{a_B^{<}(h',k')}
 \left[
 e\!\left(R(\sqrt{hk}-\sqrt{h'k'})\right)-1
 \right].
\tag{115.S11}
\]

Then exactly

\[
 E_{B,\mathrm{df}}
 =M_B^{(0)}+\mathcal R_B^{\mathrm{osc}}.
\tag{115.S12}
\]

By (115.S8), the remaining balanced energy target is equivalent to

\[
 |\mathcal R_B^{\mathrm{osc}}|
 \ll_\varepsilon L^3X^\varepsilon.
\tag{115.S13}
\]

The bracket in (115.S11) is not small. A lawful continuation must estimate
the jointly assembled nonzero aliases or prove a new signed local-energy
inequality before absolute values. Existing corridor owners, continuous
Hessian size, and fixed-shift spectral theorems do not do so.

## 6. Proof-state effect

Create a proved phase-free-mode reduction, the open oscillatory remainder,
and a proved Fejer owner-amplification obstruction. Update the original
double-far node and balanced parent to point to the zero-subtracted
remainder. Record the false character-annihilation, zero-mode, Hessian,
short-Fejer, B-process, determinant-mask, and theorem-transfer shadows.

No status change is made to the original double-far target, the balanced
packet estimate, hard TOP, unbalanced M2, M9-M2, either M1 parent, endpoint
uniformity, M9, the conditional bridge, or the Gauss-circle target.

## 7. Next strategy

Round 115 counts as a proved branch and a precise mechanism obstruction.
One final balanced follow-through is authorized only if it starts from an
explicit signed nonzero-alias or local-energy inequality retaining both
gcd weights, both slanted symbols, the determinant projector, and the full
shift family. It may not repeat plain Fejer, outer B-process, generic
Hessian transversality, or fixed-shift source transfer.

If no such inequality is specified, park this balanced broad route and move
to the adopted alternatives: the graded local-moment lane for an internal
exponent saving, the prescribed-centre UNBAL falsification probe, or direct
M1 minimization. The best internal pointwise exponent remains \(1/3\); the
audited external benchmark remains
\(0.3144831759740614\ldots\); the pointwise quarter exponent remains open.
