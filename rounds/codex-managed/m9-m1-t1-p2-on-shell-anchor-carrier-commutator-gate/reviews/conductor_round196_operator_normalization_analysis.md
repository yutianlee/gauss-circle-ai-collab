# Conductor Round-196 operator-normalization analysis

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Starting graph:
  `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
- Status: independent conductor analysis before report reconciliation
- Numerical evidence: none

## 1. Literal exact-conductor atom

The accepted Round-185 canonical parametrization is

\[
 S=S_{0,\omega}(h)+Ut,
 \qquad 0\le S_{0,\omega}(h)<U,
 \qquad U=\mathfrak m q\text{ odd}.
\tag{196.CA1}
\]

The physical parity splits exactly as

\[
 (-1)^S=(-1)^{S_{0,\omega}(h)}(-1)^t.
\tag{196.CA2}
\]

Round 187 Fourier-expands only the canonical-anchor factor
((-1)^{S_{0,\omega}(h)}). Consequently the literal exact-conductor
((q,a)) atom, before any norm, is

\[
 \boxed{
 \mathfrak m^{-1}c_q(a)(-1)^t
 e\!\left(\frac{\epsilon_\omega a\bar v_qh}{q}\right)
 B_\omega(h,t),}
 \qquad
 c_q(a)=\frac{2}{q\{1+e(-a/q)\}}.
\tag{196.CA3}
\]

This normalization is fixed by (K185.30)--(K185.36) and
(K187.12)--(K187.16). It cannot be changed inside one exact-conductor mode.

## 2. Correct on-shell reduction and the missing factor

The determinant congruences themselves are correct. In both orientations,
with (x=\kappa U+2S),

\[
 \epsilon_\omega\bar v_qh\equiv\bar2_qx\pmod q.
\tag{196.CA4}
\]

Also, because (x) and (\kappa U) are odd,

\[
 (-1)^S=\chi_4(\kappa U)\chi_4(x).
\tag{196.CA5}
\]

Thus the proposed pure algebraic identity

\[
 (-1)^S e(\epsilon_\omega a\bar v_qh/q)
 =\chi_4(\kappa U)\chi_4(x)e(a\bar2_qx/q)
\tag{196.CA6}
\]

is true. It is not, however, the phase in the literal atom (196.CA3).
Put

\[
 E_U(S_0)=(-1)^{S_0}.
\]

Equations (196.CA2)--(196.CA6) give the actual identity

\[
 \boxed{
 (-1)^t e(\epsilon_\omega a\bar v_qh/q)
 =E_U(S_{0,\omega})\chi_4(\kappa U)\chi_4(x)
  e(a\bar2_qx/q).}
\tag{196.CA7}
\]

The omitted multiplier (E_U(S_{0,\omega})) is precisely the complete
canonical-anchor parity that Round 187 expanded. Inserting it into one
mode either changes that mode or reintroduces the full Fourier sum and
mixes exact conductors.

## 3. Step-two multiplier and carry dichotomy

Let (S\mapsto S+1), so (x\mapsto x+2), and write

\[
 S_0'=[S_0+1]_U,
 \qquad
 c_U(S_0)=\mathbf1_{\{S_0=U-1\}}.
\]

Then (t'=t+c_U(S_0)). The primitive factor on the right of (196.CA6)
has multiplier

\[
 z_{q,a}=-e(a/q),
\tag{196.CA8}
\]

but the phase in the literal atom has multiplier

\[
 \boxed{(-1)^{c_U(S_0)}e(a/q).}
\tag{196.CA9}
\]

It equals (e(a/q)) on every nonwrap step and equals
(-e(a/q)) only at a canonical-anchor wrap. This recovers the accepted
carry-dependent retained-mode law. Hence the fixed multiplier (196.CA8)
cannot be applied to (196.CA3) without commuting the missing (E_U)
factor.

## 4. Exact commutator self-return

If the missing factor is absorbed into an amplitude, an exact step-two
difference obeys

\[
 \Delta_2(E_UB)(S)
 =E_U(S_0)\Delta_2B(S)
  +\{E_U(S_0)-E_U(S_0^-)\}B(S-1).
\tag{196.CA10}
\]

On a nonwrap adjacent step,
(E_U(S_0)=-E_U(S_0^-)), so the commutator coefficient in the second
term has modulus (2). At a wrap that coefficient is zero, but the
live/dead coprimality flip survives after zero extension as an unpaired
boundary atom with the original coefficient. Thus even a constant (B)
produces a full-size commutator on every nonwrap pair, and the wrap
supplies no denominator-cancelling pair. No inherited variation theorem
bounds (196.CA10) or the boundary atom below the positive event capacity.

The coefficient identity

\[
 (1-z_{q,a})c_q(a)=\frac{2e(a/q)}q
\tag{196.CA11}
\]

therefore applies only after replacing the literal carrier by (196.CA6),
and the replacement creates exactly the unpriced term (196.CA10). Keeping
the literal carrier instead leaves the carry-dependent multiplier
(196.CA9), for which (196.CA11) is not the relevant factor on nonwrap
steps. These are the two sides of the same self-return.

## 5. Fourier boundary interpretation

For one exact conductor define

\[
 K_q(s)=\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}
 c_q(a)e(as/q).
\]

Then (196.CA11) is exactly

\[
 K_q(s)+K_q(s+1)
 =\frac2q\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}
   e(a(s+1)/q),
\tag{196.CA12}
\]

the normalized Ramanujan boundary kernel. After all exact conductors are
recombined, Fourier inversion gives only the cyclic parity identity

\[
 E_U(s)+E_U([s+1]_U)=2\mathbf1_{\{s=U-1\}}.
\tag{196.CA13}
\]

Thus denominator cancellation is the Fourier form of moving alternating
mass to canonical-wrap boundaries. It is not an independent cancellation
theorem for the literal endpoint sequence. Recombining the modes returns
to the pre-Round-187 physical alternating sum and its known capacity.

## 6. Geometric mismatch of the two orientations

In the plus chart (x=d'/g) is the far coordinate. Increasing the far
defect by two sends (S\mapsto S+1), (x\mapsto x+2), and
(h\mapsto h+v). Because (v\asymp L/\kappa) while one live height block
has length (Y\ll L/\kappa), a fixed row has only (O(1)) such samples.
Zero extension therefore exposes full births and deaths rather than a long
literal difference chain.

In the minus chart (x=d/g) is the retained close coordinate. The far
step is (w\mapsto w+1), (h\mapsto h+U), while (S) and (x) remain
fixed. A step (x\mapsto x+2) instead changes the close coordinate and is
not the literal far/height transport. Pairing such sites crosses rows and
changes the physical mask, endpoints, arithmetic support, phases, and
zero extensions.

Therefore there is no common inherited event transport furnishing a
literal (Delta_2) simultaneously in both orientations. A cross-row
pairing would require exactly the new coefficient-sensitive theorem that
Round 195 left open.

## 7. Provisional state consequence

The on-shell congruence, parity identity, primitive formal carrier, and
coefficient formula are valid algebra. They do not identify the literal
exact-conductor atom. The first operator-level obstruction is the missing
canonical-anchor factor in (196.CA7); after it is restored, the
carry/commutator and orientation mismatches (196.CA9)--(196.CA13) return
to full positive capacity.

This is a rigorous no-go for the proposed carrier-denominator mechanism
from the accepted interfaces. It is not a lower bound for the literal
operator and does not disprove a future coefficient-sensitive cross-row
theorem. Pending independent report and seam review, no strict sector,
owner, bridge, theorem, or exponent should be promoted.
