# On-shell normalization and live-wrap seam review

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Round: 196
- Review seam: exact-conductor normalization, live wrap, and conductor mixing
- Candidate reviewed: `candidates/formalized_hard_m1_t1_p2_on_shell_carrier_self_return.md`
- Starting graph SHA-256: `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
- Verdict: **REPAIR**
- Numerical theorem evidence: none

## 1. Verdict and first defect

No algebraic equality among (196.K5)--(196.K18) is false after all of the
inherited K185/K187/K191 hypotheses are imported.  The candidate's central
conclusion is correct: the primitive (4q) carrier is a parity-restored
shadow, whereas one literal exact-conductor atom retains ((-1)^t); the
missing (E_U(S_0)) factor destroys the fixed step multiplier and creates
a bulk product-rule commutator.  This is a valid route-scoped no-go.

The candidate nevertheless needs repair before it can serve as a
self-contained durable kernel.  The first formal defect occurs in
(196.K3)--(196.K4): the displayed hypotheses use (\bar v_U) and later infer
that (S_{0,omega}) is a unit, but they do not explicitly state

\[
 (u,v)=1,qquad U\mid u,qquad\text{hence }(U,v)=1.
\tag{R196.1}
\]

K185.27 and K191.C3 do supply (R196.1), so this omission does not invalidate
the derivation.  It does leave the formal statement locally incomplete at
the exact point on which the live-wrap argument depends.  The same repaired
hypothesis line should state the inherited conditions

\[
 U=\mathfrak m q>4Q,quad q>Q,quad
 \mathfrak m|a|_q>Q,quad Q\mathfrak m<Y,quad
 (a,q)=1,quad (U,h)=1,quad
 \kappa,g,U hbox{odd}.
\tag{R196.2}
\]

There is a second required precision repair.  A wrap does not disappear
from the zero-extended difference operator.  There is no **live-to-live**
wrap: its new endpoint has (S_0=0) and is killed by ((U,h)=1).  The
live-to-dead transition survives as a coprimality/zero-extension boundary
atom carrying the original coefficient.  Statements that the wrap is
“deleted” or that the wrap sector is “empty” must be qualified in this
way.  This repair strengthens the no-go and prevents an accidental loss of
the boundary event.

Subject to those repairs and the product-rule notation repair in Section 5,
the candidate passes this seam.  The verdict is **REPAIR**, not FAIL,
because the normalization/support self-return is mathematically sound.

## 2. Exact normalization and orientation audit

K185.30--K185.36 give, for both orientations,

\[
 S=S_{0,\omega}(h)+Ut,qquad
 S_{0,+}\equiv\bar v_Uh,qquad
 S_{0,-}\equiv-\bar v_Uhpmod U,
\tag{R196.3}
\]

and the exact pre-Fourier row factor

\[
 E_U(S_{0,\omega})sum_t(-1)^tB_\omega(h,t),
 \qquad E_U(s)=(-1)^s.
\tag{R196.4}
\]

K187.7 expands (E_U(S_{0,omega})), not ((-1)^t).  At exact conductor
(q), the unique mode representation is

\[
 k=\frac Uq a=\mathfrak m a,qquad
 c_U(k)=\frac qU c_q(a)=\mathfrak m^{-1}c_q(a),
\tag{R196.5}
\]

and the oriented phase is

\[
 e(\epsilon_\omega k\bar v_Uh/U)
 =e(\epsilon_\omega a\bar v_qh/q).
\tag{R196.6}
\]

Therefore candidate equation (196.K5) is exactly normalized:

\[
 \mathfrak m^{-1}c_q(a)(-1)^t
 e(\epsilon_\omega a\bar v_qh/q)B_\omega(h,t).
\tag{R196.7}
\]

There is no missing conjugation and no orientation-sign reversal.

Because (U) is odd,

\[
 (-1)^S=(-1)^{S_0+Ut}=E_U(S_0)(-1)^t,
 \qquad
 (-1)^t=E_U(S_0)(-1)^S.
\tag{R196.8}
\]

Thus (196.K13) and the use of it in (196.K8) have the correct direction.
The determinant congruences are also signed correctly.  In the plus chart,
(2h\equiv vx\pmod q); in the minus chart,
(2h\equiv-vx\pmod q).  Hence

\[
 \epsilon_\omega\bar v_qh\equiv\bar2_qx\pmod q
\tag{R196.9}
\]

for both orientations.  Since (x=\kappa U+2S), inherited oddness of
(kappa,U) gives

\[
 (-1)^S=\chi_4(\kappa U)\chi_4(x).
\tag{R196.10}
\]

Equations (R196.7)--(R196.10) prove candidate (196.K8) exactly.  The
factor (E_U(S_0)) is nonconstant and cannot be dropped inside a fixed
exact-conductor packet.

## 3. Oddness, units, and primitive (4q) carrier

The required hypotheses are all present in the accepted chain:

- K185.27 gives (kappa,g,U) odd, ((gU,v)=1), and ((U,h)=1);
- K187.15 gives (q\mid U), (k=(U/q)a), and ((a,q)=1);
- K191.C2--C3 gives (U=\mathfrak m q>4Q), (U\mid u),
  (g=u/U), and ((u,v)=1).

It follows that (q,mathfrak m,kappa,U,x) are odd, that (v) is a unit
modulo both (U) and (q), and that (S_{0,omega}) is a unit whenever
the height is live.  Candidate (196.K3) should reproduce these facts
explicitly rather than relying only on the phrase “retain the exact
accepted core.”

For

\[
 b_{q,a}\equiv q+4a\bar2_q\pmod{4q},
\tag{R196.11}
\]

(b_{q,a}) is odd.  For every prime (p\mid q),
(b_{q,a}\equiv2a\not\equiv0\pmod p).  Hence

\[
 (b_{q,a},4q)=1.
\tag{R196.12}
\]

The representative of (\bar2_q) is harmless: changing it by (q)
changes (R196.11) by a multiple of (4q).  The step-two multiplier is

\[
 e(b_{q,a}/(2q))=-e(a/q),
\tag{R196.13}
\]

and

\[
 (1+e(a/q))c_q(a)=\frac{2e(a/q)}q.
\tag{R196.14}
\]

Thus (196.K6)--(196.K7) are correct, but only for the parity-restored
shadow.  Candidate (196.K8), not (196.K6), is the literal fixed-mode
factorization.

## 4. Live multiplier, wrap, and near-half mode

Take the adjacent-(S) step (S\mapsto S+1), equivalently
(x\mapsto x+2), at fixed ((\kappa,U,v,w)).  In the plus chart it sends
(h\mapsto h+v); in the minus chart it sends (h\mapsto h-v).  In both
cases

\[
 S_0\mapsto[S_0+1]_U.
\tag{R196.15}
\]

If (S_0\ne U-1), then (t) is unchanged and the literal factor in
(196.K5) has ratio (e(a/q)).  If (S_0=U-1), then (t\mapsto t+1) and
the formal ratio is (-e(a/q)).  This proves (196.K16).

On live support, (R196.1)--(R196.2) imply

\[
 (S_0,U)=1,qquad S_0\ne0.
\tag{R196.16}
\]

At the forward wrap the new residue is (0).  Equivalently, the new
height is divisible by (U), so the new atom is killed by the
coprimality mask.  Therefore every live-to-live adjacent pair is nonwrap
and has multiplier (e(a/q)), as the candidate claims.

The zero-extended edge must nevertheless be retained.  A live atom at
(S_0=U-1) can be followed by a dead atom at (S_0=0), and a dead atom at
(S_0=0) can be followed by a live atom at (S_0=1).  These are
coprimality flips/boundary events, not denominator-cancelling paired
differences.  The repaired candidate should say this at the first wrap
claim, rather than leaving it only implicit in its later commutator list.

For every odd (q>1), (a=(q-1)/2) is a unit modulo (q), and

\[
 \left|(1-e(a/q))c_q(a)\right|
 =\frac2q\cot\!\left(\frac{\pi}{2q}\right)\asymp1.
\tag{R196.17}
\]

Thus (196.K17) is correct.  It is a coefficient-level falsifier of a
uniform (q^{-1}) conclusion; it does not prove that a near-half row has
nonzero literal endpoint mass in every open packet.

## 5. Product rule and conductor mixing

The candidate should define

\[
 \Delta_2B(x)=B(x)-B(x-2),qquad
 B^-=B(x-2),qquad
 E_U^-=E_U(S_0(x-2)).
\tag{R196.18}
\]

With this convention, (196.K18) has the correct sign:

\[
 \Delta_2(E_UB)=E_U\Delta_2B+(E_U-E_U^-)B^-.
\tag{R196.19}
\]

For application to the literal term it should also display the solved
form

\[
 E_U\Delta_2B
 =\Delta_2(E_UB)-(E_U-E_U^-)B^-.
\tag{R196.20}
\]

On a live-to-live edge, (S_0) and its predecessor are nonzero and the
step is nonwrap, so

\[
 |E_U-E_U^-|=2.
\tag{R196.21}
\]

At a wrap, (R196.21) is replaced by the zero-extension boundary event
described above; it is not permissible to delete the whole difference.
Equations (R196.19)--(R196.21) validate the parity-kernel commutator
self-return and its sign.

Candidate (196.K15) is also exact:

\[
 E_U(S_0)e(kS_0/U)
 =\sum_{r\bmod U}c_U(r)e((r+k)S_0/U).
\tag{R196.22}
\]

For full normalization clarity, the repaired line should retain the
outside coefficient:

\[
 \mathfrak m^{-1}c_q(a)E_U(S_0)e(kS_0/U)
 =\mathfrak m^{-1}c_q(a)
  \sum_{r\bmod U}c_U(r)e((r+k)S_0/U).
\tag{R196.23}
\]

The frequencies (r+k) have varying gcd with (U), and therefore varying
exact conductors, reduced numerators, projective bands, and safe/core
status.  Equation (R196.23) is a convolution, not the original
exact-conductor decomposition at shifted frequency.  Complete
recombination of the original literal modes gives

\[
 (-1)^t\sum_{k\bmod U}c_U(k)e(kS_0/U)
 =(-1)^tE_U(S_0)=(-1)^S,
\tag{R196.24}
\]

so no distinguished (c_q(a)) remains.  The conductor-mixing conclusion
is correct.

Finally, K191.C17 transports

\[
 (S,w)\mapsto
 (S-\epsilon_\omega\rho_U(v),
  w-\epsilon_\omega\gamma_U(v)),
\tag{R196.25}
\]

and hence changes (x) by (2\epsilon_\omega\rho_U(v)) between current
and transported-previous sites.  It is not the adjacent-(S) operator.
At fixed height, (t\mapsto t+1) changes (x) by (2U).  The candidate's
claim that no accepted common literal (Delta_2) precedes the scalar
identity is therefore correct.

## 6. Required repairs

Before promotion of the no-go kernel, make the following exact repairs.

1. **Complete (196.K3)--(196.K4).**  Add (R196.1)--(R196.2), or cite
   K185.27 and K191.C2--C3 directly in the displayed hypothesis line.
   In particular, state ((U,v)=1) before using (\bar v_U), and retain
   (U>4Q) and the fast packet restrictions.
2. **Qualify wrap deletion.**  Replace “the wrap is deleted” and “the
   wrap sector is empty” by: there is no live-to-live wrap; the wrap is a
   live-to-dead or dead-to-live coprimality/zero-extension boundary event
   with no paired denominator cancellation.  Retain that event in the
   literal commutator ledger.
3. **Define the product-rule convention.**  Add (R196.18) and the solved
   identity (R196.20).  This confirms that the commutator enters with the
   minus sign when (E_U\Delta_2B) is isolated.
4. **Clarify conductor convolution.**  State (R196.23), including the
   outside exact-conductor coefficient, and say explicitly that its
   coefficients are not the original (c_U(r+k)) packet weights.
5. **Preserve the logical qualifier.**  Keep (196.K17), (196.K18), and
   the bounded-array discussion labelled as operator-capacity controls.
   They establish no nonvanishing or lower mass for the actual endpoint
   product and do not disprove a different coefficient-sensitive theorem.

No repair is needed to the orientation signs, parity identity,
(4q)-primitivity calculation, coefficient identity, near-half magnitude,
or the conclusion that the inherited event transport is not (Delta_2).

## 7. Scope and disposition

The candidate proves only a normalization/support self-return for the
proposed carrier-denominator mechanism.  It does not prove a literal lower
bound, failure of the complete (P_2) estimate, or a target-safe strict
sector.  The unchanged available positive estimate is

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll u\{\kappa+\min(Y,D_L)\}X^\varepsilon,
\tag{R196.26}
\]

and the exact open-region deficit remains

\[
 \frac{\min(Y,D_L)}{Q\mathfrak m\kappa}>1.
\tag{R196.27}
\]

After the repairs above, this seam should pass as inconclusive/no-go
evidence only.  Keep complete (P_2), (P_1), complete original (t=1),
all other original-(t) incidences, the hard small-(t) owner, smooth
(M_1), GAR, every (M_2) parent, endpoint uniformity, (M9), both
bridges, the quarter theorem, and every exponent unchanged.

Artifacts audited in full were the formal candidate, all three Round-196
reports, the conductor reconciliation, and the exact K185, K187, K191,
and Round-195 capacity kernels.  No web source or computation was used.
