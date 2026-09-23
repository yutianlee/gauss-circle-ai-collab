# Conductor Round-196 report reconciliation

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Round: 196
- Starting graph:
  `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
- Status: conductor reconciliation before formalization and seam review

## 1. Frozen objective and report receipts

Round 196 froze only the exact Round-195 open (P_2) packets

\[
 \kappa<D_L,\qquad
 M:=\min(Y,D_L)>Q\mathfrak m\kappa,
 \qquad Q=H_B,
\tag{196.R1}
\]

and tested the on-shell common-(x) carrier before positive norms. The
three reports are:

1. `reports/literal_on_shell_carrier_commutator_attack.md`, SHA-256
   `5e419a17d867ca8d685b12c23f8e462725894dad4ec3ee78fcbf61eed8ad8684`;
2. `reports/carrier_collision_endpoint_hostile_audit.md`, SHA-256
   `c7b46cd6e9b5caba1b49a782d3e117ffc349a2aa815771f0ab95fa3d3fac6cdc`;
3. `reports/blind_on_shell_phase_rederivation.md`, SHA-256
   `a1f0f342c4e19f43cf1e6f216821af46fa51ff6fd134b20f14d22db1fdecd80e`.

No conclusion is selected by vote. The first two reports independently
reconstruct the literal accepted operator and identify the same first
normalization failure. The blind report is used only for its isolated
algebra after its missing live hypotheses and operator interface are
restored.

## 2. Algebra retained from the proposal

In the plus and minus charts respectively, the determinant equations give

\[
 2h\equiv vx\pmod q,
 \qquad
 2h\equiv-vx\pmod q,
\]

where

\[
 x=\kappa U+2S=d'/g\quad(+),
 \qquad
 x=\kappa U+2S=d/g\quad(-).
\tag{196.R2}
\]

On live support (U,q,\kappa,x) are odd and
(a\in(\mathbb Z/q\mathbb Z)^\times). Hence

\[
 (-1)^S e(\epsilon_\omega a\bar v_qh/q)
 =\chi_4(\kappa U)\chi_4(x)e(a\bar2_qx/q)
\tag{196.R3}
\]

is a primitive additive carrier modulo (4q). Its formal step-two
multiplier and the exact coefficient identity are

\[
 z_{q,a}=-e(a/q),
 \qquad
 (1-z_{q,a})c_q(a)=\frac{2e(a/q)}q.
\tag{196.R4}
\]

These statements are exact algebra. The blind report correctly derives
them but, by statement-only design, does not know whether (196.R3) is a
literal exact-conductor atom.

## 3. Decisive literal normalization repair

The accepted canonical parametrization is

\[
 S=S_{0,\omega}(h)+Ut,
 \qquad 0\le S_{0,\omega}(h)<U,
 \qquad U=\mathfrak m q.
\tag{196.R5}
\]

Round 187 expands the factor
(E_U(S_{0,\omega})=(-1)^{S_{0,\omega}}), not the remaining affine
factor ((-1)^t). Therefore a literal exact-conductor atom is

\[
 \boxed{
 \mathfrak m^{-1}c_q(a)(-1)^t
 e(\epsilon_\omega a\bar v_qh/q)B_\omega(h,t).}
\tag{196.R6}
\]

Since ((-1)^t=E_U(S_{0,\omega})(-1)^S), its exact on-shell form is

\[
 \boxed{
 \mathfrak m^{-1}c_q(a)E_U(S_{0,\omega})
 \chi_4(\kappa U)\chi_4(x)e(a\bar2_qx/q)B_\omega(h,t).}
\tag{196.R7}
\]

Thus the proposal omitted the nonconstant factor (E_U(S_0)). Restoring
it in one mode convolves that mode with the complete (U)-Fourier parity
kernel and mixes exact conductors, projective bands, and safe/core pieces.
Recombining all modes recovers the pre-Round-187 physical parity but removes
the distinguished coefficient to which (196.R4) was to be applied.

This is the first invalid operator step. It sharpens, and does not
contradict, the Round-195 controls that a fixed plus-mode ratio is
carry-dependent and that pre-Fourier parity cannot be multiplied into one
retained mode.

## 4. Live-step, commutator, and orientation self-return

Under (S\mapsto S+1), put

\[
 c_U(S_0)=\mathbf1_{\{S_0=U-1\}}.
\]

The literal atom (196.R6) has ratio

\[
 (-1)^{c_U(S_0)}e(a/q),
\tag{196.R8}
\]

not the fixed (z_{q,a}). Since ((U,h)=1), (S_0) is a nonzero unit
modulo (U). A wrap lands at (S_0=0), equivalently (U\mid h), so there
is no live-to-live wrap.  Its live/dead zero-extension transition
survives as an unpaired coprimality boundary atom with the original
coefficient. Every live-to-live adjacent step is therefore nonwrap and
has ratio (e(a/q)). For the primitive near-half
mode (a=(q-1)/2),

\[
 |(1-e(a/q))c_q(a)|\asymp1,
\tag{196.R9}
\]

whereas (196.R4) would have size (2/q). The singular mass survives.

Equivalently, absorbing (E_U) into the amplitude gives the exact product
rule

\[
 \Delta_2(E_UB)
 =E_U\Delta_2B+(E_U-E_U^-)B^-.
\tag{196.R10}
\]

The second coefficient has modulus (2) on every possible live-to-live
adjacent edge. At the wrap it is replaced by the unpaired
coprimality/zero-extension boundary atom rather than discarded. This
parity commutator returns to the uncancelled event capacity before the
physical mask, squarefree/coprimality, endpoint, carry, birth/death,
Fejer, square-root-phase, cell, crossing, conjugation, or remaining
zero-extension commutators are priced.

There is also no inherited literal step-two event operator. The accepted
Round-191 height transport moves (x) by
(2\epsilon_\omega\rho_U(v)), while a fixed-height affine step moves it
by (2U). The adjacent-(S) step moves height by (v), not one. In the
plus chart (x) is the far coordinate; in the minus chart it is the close
coordinate and remains fixed under the literal far step (w\mapsto w+1).
Thus the two orientations do not supply a common event (Delta_2).

## 5. Power ledger and exact scope

Round 195's strongest fixed-packet estimate remains

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll u\{\kappa+M\}X^\varepsilon.
\tag{196.R11}
\]

The (kappa u) term is target-safe. On (196.R1), the other term still
misses the target by

\[
 \frac{M}{Q\mathfrak m\kappa}>1.
\tag{196.R12}
\]

The exact (mathfrak m^{-1}) lift, coefficient mass, projective bands,
divisors, dyadic heights, and shell ledger would restore the accepted
outer (L^2X^\varepsilon) bound only after the fixed target is proved.
They do not erase (196.R12). No positive power is absorbed into
(X^\varepsilon).

The bounded-array and phase-conjugated controls show only that the repaired
commutator can retain operator capacity. They are not literal endpoint
coefficients and do not prove a lower bound. The no-go excludes this
carrier-denominator mechanism from the accepted interfaces; it does not
disprove a different coefficient-sensitive cross-row theorem for (P_2).

No full target and no nonempty new target-safe strict sector is proved.

## 6. Blind post-unmask disposition

The blind report's algebra (R2)--(R4) is retained after adding the live
hypotheses that (kappa,x,q) are odd and ((a,q)=1). Its substantive
warning is also correct: a locally controlled literal (Delta_2)
primitive is not supplied by the isolated statement, and a manufactured
cumulative primitive can self-return the gain.

After unmasking, its carrier must be labelled the parity-restored shadow,
not the literal atom. Equations (196.R6)--(196.R10) are the missing
operator data. Therefore the blind report is evidence for the algebra and
the need for a genuine difference only; it is not evidence for target
cancellation, a literal commutator estimate, or a strict sector.

## 7. Conductor decision before seam review

Formalize one route-scoped normalization/support self-return kernel. Its
accepted content may be only:

1. the exact algebra (196.R2)--(196.R4);
2. the literal repair (196.R6)--(196.R7);
3. the live multiplier, absence of a live-to-live wrap, surviving
   coprimality boundary atom, and bulk commutator
   (196.R8)--(196.R10);
4. the absence of an inherited common step-two event transport; and
5. the unchanged deficit (196.R12) and method boundary.

Do not create a proved target-safe sector. Keep the complete (P_2)
remainder open and record only inconclusive/no-go evidence on the already
open hard-M1 small-(t) owner. Do not promote (P_1), original (t=1),
any other original-(t) range, either M1 parent, GAR, any M2 parent,
endpoint uniformity, M9, a bridge, the quarter theorem, or any exponent.
