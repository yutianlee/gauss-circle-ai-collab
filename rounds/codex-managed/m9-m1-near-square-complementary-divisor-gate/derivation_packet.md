# Round 122 derivation packet: near-square complementary divisors

Campaign: `m9-m1-near-square-complementary-divisor-gate`

Starting graph SHA-256:
`3e85caebbaf6c69d0019009bee3ce8f720f34f579bfb0cfa2035b92be0fb2c13`

## Accepted input

Round 121 proves, for both signs and at the reciprocal target scale, that
the complete literal lower-radial antecedent is equivalent to

\[
 \mathcal B_{\rm flat}^{(N)}(X)
 =\sum_{k\in\mathbb Z}D_N(k)W_{R,y}(k),
 \qquad W_{R,y}(k)=\widehat J(k)-\widehat J(k+1),
\tag{122.D1}
\]

where (R=X^{1/4}), (y=\lfloor\sqrt X\rfloor),
(N=\lfloor X\rfloor),

\[
 J(t)=\eta(yt){V_{\rm low}(4R^2t^2)\over t}
\tag{122.D2}
\]

on its positive arc,

\[
 D_N(k)=\sum_{d\leq y}\chi_4(d)
 \left(\left\lfloor{N+k\over d}\right\rfloor
 -\left\lfloor{N\over d}\right\rfloor-{k\over d}\right)
\tag{122.D3}
\]

for every integer (k), and the target is

\[
 \sum_kD_N(k)W_{R,y}(k)\ll_\varepsilon RX^\varepsilon.
\tag{122.D4}
\]

The difference weight is the (k)-th Fourier coefficient of

\[
 K_{R,y}(t)=J(t)(1-e(-t)).
\tag{122.D5}
\]

This cancels the formal (1/t) size, but the one-sided transition
(\eta(yt)) remains at scale (1/y). Any Fourier envelope must price
that boundary uniformly.

## Proposed noninvertible structure

For (m=N+k>0), pair a divisor (d\mid m) with (m/d). The accepted
coefficient is truncated at the fixed (y\), not at (\sqrt m\), and
(m\) may be even. A lawful formula must therefore:

- write (m=2^a m_0) with (m_0) odd;
- track (\chi_4(d)) only on odd divisors;
- distinguish (m_0\equiv1\pmod4) and
  (m_0\equiv3\pmod4);
- keep the two thresholds (y\) and (m_0/y\) distinct;
- retain exact-square and central-divisor ties;
- preserve the signed (k)-wavelet and its prescribed centre (N\).

For odd (m\), the elementary starting identity is

\[
 \sum_{\substack{d\mid m\\d>y}}\chi_4(d)
 =\chi_4(m)
 \sum_{\substack{q\mid m\\q<m/y}}\chi_4(q),
\tag{122.D6}
\]

with strict/weak boundary conventions audited at (d=y\) and
(d=\sqrt m\). For even (m\), (122.D6) must be applied to the odd part
with the correct changed threshold, not with the meaningless factor
(\chi_4(m)=0\).

## Capacity and forbidden shortcuts

The trivial discrepancy bound is (O(y)), while the target is
(R=\sqrt y\). The already proved local mod-four and resonance-tubewise
routes retain at least (R^{3/2}) capacity after local norms. Round 64--65
also shows that Fourier completion and one-variable crossing Abel
summation can be exact self-returns.

Do not:

- use fixed-(X) Schwartz decay without uniform (R,y)-norms;
- take absolute values over (k), divisor complements, parity branches,
  or central bands before proving their aggregate cost;
- replace the truncated coefficient by the full
  (\sum_{d\mid m}\chi_4(d)=r_2(m)/4\) without the exact complementary
  tail;
- use the desired quarter-circle discrepancy to bound a short interval;
- call the divisor involution a gain if recombination reconstructs
  (122.D1);
- infer blockwise M1, M9-M2, endpoint uniformity, M9, or an exponent from
  a reduction of the lower GAR child.

## Required outcome

Derive the exact localized and (2)-adic complementary-divisor formula,
then prove the full target, a strict target-safe branch, a quantitative
signed saving/inverse theorem, or a rigorous self-return/no-go. Identify
the first genuinely unproved inequality and the exact downstream scope.
