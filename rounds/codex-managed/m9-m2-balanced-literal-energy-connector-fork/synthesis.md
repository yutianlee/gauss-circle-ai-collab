# Round 114 synthesis: literal full-product energy and double-far survivor

Campaign: `m9-m2-balanced-literal-energy-connector-fork`
Round type: core analytic attack
Starting recorded graph SHA-256:
`411adc0c93d2451dfc1235840f27063b3ef4869d0c67aebfbbc74fe9ef04387c`

Resulting graph SHA-256:
`6eb6eb5941e6d4720294c6b0890356113700db3201cf7c19337b96fb5ed47155`

## 1. Conductor decision

Promote the exact full-product energy connector, the equal-product bound,
the radial and determinant target-safe corridors, the literal determinant
ray identity, and the corrected full-symbol mean-square implication.
Retain the balanced estimate as open and name its smallest direct survivor:
the actual signed double-far shifted-divisor energy.

The four August 21 strategy files contained two useful mechanisms but also
two unproved identifications.  Round 114 resolves them:

- the packet energy diagonal is `hk=h'k'=g^2uv=g'^2u'v'`, not
  `uv=u'v'`;
- the model `u^2/m` identity is not itself a literal connector;
- the square-root phase has its own exact determinant ray identity;
- the old full-symbol mean square really does imply the fixed balanced
  packet, but it does not imply the independent hard TOP parent; and
- generic broad transversality is false for arbitrary bounded
  coefficients, so any continuation must use the actual signed symbol.

This round proves new target-safe branches and a precise no-go.  It does
not prove the broad survivor, the balanced parent, or any exponent.

## 2. Exact energy connector

For one fixed literal balanced block define

\[
a_B^<(h,k)=\chi_4(h)
\eta\!\left(\frac{\gcd(h,k)}{\sqrt L/2}\right)A_B(h,k).
\]

The Round-113 packet identity recombines coefficientwise to

\[
Z_B(R)=\sum_\sigma G_\sigma Q_{B,\sigma}^{\rm full}(R)
=2i\sum_{h,k}a_B^<(h,k)e(R\sqrt{hk}).
\tag{114.S1}
\]

Thus its squared budget is `L^3X^epsilon`.  If

\[
c_B(n)=\sum_{hk=n}a_B^<(h,k),
\]

then

\[
\sum_n|c_B(n)|^2\ll_\varepsilon L^2X^\varepsilon.
\tag{114.S2}
\]

The full product, including both gcd lifts, is the true diagonal.

## 3. Two target-safe corridors

For two packet atoms put

\[
\Delta=h'k'-hk,
\qquad
\rho=hk'-h'k.
\]

Elementary divisor and lattice-line counts prove, uniformly for fixed
`1<=K/L<=16`,

\[
\sum_{|\Delta|\le U}|a_B^<(h,k)a_B^<(h',k')|
\ll_\varepsilon L^2(U+1)X^\varepsilon,
\tag{114.S3}
\]

\[
\sum_{|\rho|\le Q}|a_B^<(h,k)a_B^<(h',k')|
\ll_\varepsilon L^2(Q+1)X^\varepsilon.
\tag{114.S4}
\]

Hence the union `|Delta|<=L` or `|rho|<=L` is target-safe absolutely.
The exact ray slice `rho=0` costs only `O(L^2 log L)`.

Writing `(h',k')=(h+p,k+q)`, the literal rank-one identity is

\[
\sqrt{h'k'}-\sqrt{hk}
-\frac12\sqrt{\frac kh}p
-\frac12\sqrt{\frac hk}q
=-\frac{\rho^2}
{4(hk)^{3/2}(P+\sqrt{Q_0})}.
\tag{114.S5}
\]

The companion identities

\[
\Delta+\rho=q(h+h'),
\qquad
\Delta-\rho=p(k+k')
\tag{114.S6}
\]

give divisor-bounded multiplicity for fixed nonaxial invariants.  They do
not reduce the global `L^4` coefficient-blind capacity.

## 4. Mean-square connector and its correction

For the full smooth symbol, the proposed estimate

\[
\sum_{\substack{h\asymp L\\h\ {\rm odd}}}
\left|\sum_{k\asymp K}A_B(h,k)e(R\sqrt{hk})\right|^2
\ll_\varepsilon L^{1/2}K^{3/2}X^\varepsilon
\tag{114.S7}
\]

implies `|T_B|<<(LK)^(3/4)X^epsilon` by Cauchy.  Subtracting the proved
high-gcd owner and using (114.S1) gives the balanced packet target.

Equation (114.S7) remains unproved and is stronger than the direct scalar
target.  It erases `chi_4(h)` because the character is outside each inner
row.  The opposite Gram orientation retains the character and has target
`L^(3/2)K^(1/2)X^epsilon`; it is also unproved.  The old mean-square node's
direct implication to all of `M9-M2` is removed because TOP is independent.

## 5. Smallest open survivor and no-go

After the two corridors, the exact remaining actual-symbol energy is

\[
\mathcal E_{B,\rm df}
=\sum_{|r|>L}\sum_n e\!\left(R(\sqrt n-\sqrt{n+r})\right)
\sum_{\substack{hk=n,\ h'k'=n+r\\|hk'-h'k|>L}}
a_B^<(h,k)\overline{a_B^<(h',k')}.
\tag{114.S8}
\]

The balanced packet target is equivalent, up to the proved target-safe
terms, to

\[
|\mathcal E_{B,\rm df}|ll_\varepsilon L^3X^\varepsilon.
\tag{114.S9}
\]

This is open.  On a fixed product pair the phase in (114.S8) is independent
of the determinant, so large `|rho|` alone creates no internal oscillation.
A phase-adapted bounded coefficient array has double-far energy of order
`L^4`; therefore coefficient-uniform broad, large-sieve, or divisor-count
arguments cannot prove (114.S9).  The literal `chi_4(h)chi_4(h')`, gcd
cutoff, and slanted Vaaler symbol must enter the next inequality.

## 6. Proof-state effect

Create a proved double-corridor reduction, a proved full-symbol mean-square
connector, and the open double-far actual energy.  Correct the scope of the
old proposed mean-square node and update the balanced parent with the new
survivor.  Record the false primitive-product, model-ray, fixed-invariant,
coefficient-uniform, and overbroad implication shadows.

No status change is made to the balanced estimate, either other M2 parent,
M9-M2, either M1 parent, endpoint uniformity, M9, the conditional bridge,
or the Gauss-circle target.

## 7. Next strategy

Round 115 may continue BAL only on the exact inner correlation in
(114.S8).  The preferred fork is:

1. derive its literal character-twisted shifted-divisor coefficient and
   test a noninvertible dispersion or spectral inequality with all
   conductors and main terms explicit; or
2. prove that its nonoscillatory main term survives at `L^4` capacity for
   the actual symbol, which would park this broad mechanism.

Do not run generic cone decoupling on determinant separation: Round 114
proves that determinant geometry alone is invisible inside fixed product
fibres.  The graded local-moment lane and direct-M1 minimization remain the
next alternatives if this signed shifted-divisor fork returns at equal
capacity.

The best internal pointwise exponent remains `1/3`; the audited external
benchmark remains `0.3144831759740614...`; the pointwise quarter exponent
remains unproved.
