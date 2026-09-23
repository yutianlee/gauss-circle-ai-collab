# Round 196 hostile on-shell carrier and endpoint-commutator audit

- Campaign: `m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate`
- Task: `carrier_collision_endpoint_hostile_audit`
- Role: barrier/no-go
- Starting graph SHA-256:
  `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`
- Status: candidate evidence only; no shared-state edit
- Numerical theorem evidence: none

## 1. Result

**Verdict: exact route-scoped NO-GO.**  The two determinant congruences,
the parity identity, the artificial primitive (4q)-carrier, and the
scalar identity

\[
 (1+e(a/q))c_q(a)=\frac{2e(a/q)}q
\tag{196.H1}
\]

are algebraically correct.  They do **not** occur together in one literal
exact-conductor atom.  The first false operator-level replacement is

\[
 \frac1{\mathfrak m}c_q(a)(-1)^t
 e\!\left(\frac{\epsilon_\omega a\bar v_qh}{q}\right)B
 \quad\rightsquigarrow\quad
 \frac1{\mathfrak m}c_q(a)(-1)^S
 e\!\left(\frac{\epsilon_\omega a\bar v_qh}{q}\right)B.
\tag{196.H2}
\]

Here (S=S_{0,\omega}(h)+Ut), (0\le S_{0,\omega}<U), and
(U=\mathfrak m q) is odd.  The left side is the exact Round-187
conductor atom.  The right side differs from it by the nonconstant anchor
factor

\[
 E_U(S_{0,\omega})=(-1)^{S_{0,\omega}}.
\tag{196.H3}
\]

Multiplication by (196.H3) convolves all (U)-Fourier modes and hence all
exact conductors, projective bands, and safe/core packets.  It cannot be
inserted while retaining the coefficient (\mathfrak m^{-1}c_q(a)).
Full mode recombination is an exact self-return to the pre-conductor
anchor, not an estimate of the Round-195 open packet.

The exact repaired on-shell carrier is

\[
 \boxed{
 L_{U,q,a}(x)=E_U([S]_U)\,
 \chi_4(\kappa U)\chi_4(x)
 e\!\left(\frac{a\overline2_qx}{q}\right)
 =(-1)^t e(aS/q),
 \qquad x=\kappa U+2S.}
\tag{196.H4}
\]

On literal support ((U,h)=1), the canonical residue
(S_0=[S]_U) is a unit and in particular is nonzero.  Therefore every
live-to-live step (x-2\to x) is a non-wrap step, (t) is unchanged,
and

\[
 \frac{L_{U,q,a}(x)}{L_{U,q,a}(x-2)}=e(a/q),
\tag{196.H5}
\]

not (-e(a/q)).  The only wrap on which the ratio would be
(-e(a/q)) lands at (S_0=0), equivalently (U\mid h), and is deleted
by the literal coprimality mask.  Zero extension turns that would-be
cancelling edge into an unpaired boundary atom.

Consequently, even if an exact literal step-two difference were supplied,
its live interior factor would be

\[
 (1-e(a/q))c_q(a)
 =\frac{2e(a/q)(1-e(a/q))}{q(1+e(a/q))},
\tag{196.H6}
\]

which retains the complete near-half-frequency singular mass.  Restoring
the omitted factor (E_U) in a proposed product rule creates the bulk
commutator

\[
 E_U(S_0)\Delta_2B(x)
 =\Delta_2(E_UB)(x)
   +\{E_U(S_0-1)-E_U(S_0)\}B(x-2),
\tag{196.H7}
\]

whose multiplier has modulus (2) on every non-wrap adjacent residue.
Thus the proposed (\Delta_2) mechanism returns to the available
(u\min(Y,D_L)X^\varepsilon) capacity before endpoint, mask, carry,
phase, or birth/death commutators are even priced.  This is an
operator-normalization and support no-go; it is not a lower bound for the
literal coefficient and does not disprove the desired signed estimate by
some different mechanism.

No nonempty new target-safe strict sector is proved.  The only
denominator-cancelling wrap sector is empty on nonzero literal support;
restricting to an anchor-parity submask would be an unpriced proper
submask with a full complement.

## 2. Exact statement and hypotheses

Retain the exact Round-195 open packet region

\[
 \kappa<D_L,\qquad
 \min(Y,D_L)>Q\mathfrak m\kappa,\qquad Q=H_B,
\tag{196.H8}
\]

inside the accepted Round-192 physical (P_2) core.  Thus

\[
 U=\mathfrak m q>4Q,\quad q>Q,\quad
 \mathfrak m|a|_q>Q,\quad Q\mathfrak m<Y,
 \quad U\mid u,
\tag{196.H9}
\]

((u,v)=1), ((U,h)=1), and (a\in(\mathbb Z/q\mathbb Z)^\times).
The physical cofactor (m) is never identified with the spectral lift
(\mathfrak m).  Keep the (T=0) branch, every simultaneous strict
(T\ge1) Farey condition, the projective (J)-band, both primitive
orientations, both square-root frequency signs (\sigma), the full
anchor aggregate, all endpoint and residual fields, and one outer real
part.

In the plus chart,

\[
 d=\kappa gU,\quad d'=g(\kappa U+2S),\quad
 m'=\kappa v,\quad m=\kappa v+2w,
 \quad h=Sv-Uw,
\tag{196.H10}
\]

\[
 \delta_+=\kappa(U-v)-2w,\qquad
 \eta_+=\kappa(U-v)+2S.
\tag{196.H11}
\]

In the minus chart,

\[
 d'=\kappa gU,\quad d=g(\kappa U+2S),\quad
 m=\kappa v,\quad m'=\kappa v+2w,
 \quad h=Uw-vS,
\tag{196.H12}
\]

\[
 \delta_-=\kappa(U-v)+2S,\qquad
 \eta_-=\kappa(v-U)+2w.
\tag{196.H13}
\]

The physical mask is imposed before Fourier expansion and differencing:

\[
 P_2=\mathbf1_{\{|d-gm|\le D_L\}}
     \mathbf1_{\{|d'-gm'|>D_L\}}.
\tag{196.H14}
\]

Let (S_{0,\omega}(h)\in[0,U)) be the canonical anchor from Round 191,

\[
 S_{0,\omega}(h)\equiv
 \epsilon_\omega\bar v_Uh\pmod U,
 \qquad \epsilon_+=1,\quad\epsilon_-=-1,
\tag{196.H15}
\]

and write (S=S_{0,\omega}+Ut).  The exact-conductor Fourier mode is
(k=\mathfrak m a), and

\[
 c_U(\mathfrak m a)=\frac1{\mathfrak m}c_q(a),
 \qquad
 c_q(a)=\frac{2}{q\{1+e(-a/q)\}}.
\tag{196.H16}
\]

The no-go theorem asserted here is:

1. the determinant and character formulas (196.H19)--(196.H25) below
   are exact algebraic identities;
2. the actual atom is (196.H29), not its parity-restored shadow;
3. on every live adjacent pair the actual multiplier is (e(a/q)), so
   a genuine (\Delta_2) does not cancel (196.H16);
4. parity restoration creates the bulk commutator (196.H7) and mixes
   exact conductors;
5. the literal operator contains no accepted step-two event difference:
   its existing height difference transports (x) by
   (2\epsilon_\omega\varrho_U(v)), while a fixed-height affine step
   transports (x) by (2U);
6. every remaining physical commutator listed in Section 3.5 has only the
   inherited positive-capacity bound, so the target

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll Q\mathfrak m\kappa uX^\varepsilon
\tag{196.H17}
\]

is not proved by this carrier route.

## 3. Proof or derivation

### 3.1 Determinant, on-shell coordinate, parity, and primitive carrier

Direct expansion of (196.H10)--(196.H13) gives

\[
 2h=v\eta_+ +U\delta_+-\kappa(U^2-v^2),
\tag{196.H18}
\]

\[
 2h=U\eta_- -v\delta_-+\kappa(U^2-v^2).
\tag{196.H19}
\]

Put

\[
 x_+=\kappa v+\eta_+=\kappa U+2S=\frac{d'}g,
 \qquad
 x_-=\kappa v+\delta_-=\kappa U+2S=\frac dg.
\tag{196.H20}
\]

Thus (x) is the same odd allocation coordinate in both charts.  Since
(q\mid U), reduction of (196.H18) modulo (q) gives
(2h\equiv vx\pmod q), while reduction of (196.H19) gives
(2h\equiv-vx\pmod q).  Since (v) is a unit modulo (q),

\[
 \bar v_qh\equiv\overline2_qx\pmod q\quad(+),
 \qquad
 -\bar v_qh\equiv\overline2_qx\pmod q\quad(-).
\tag{196.H21}
\]

For odd (A=\kappa U) and (x=A+2S),

\[
 \chi_4(A)\chi_4(x)
 =(-1)^{(A-1)/2+(x-1)/2}=(-1)^S.
\tag{196.H22}
\]

Equations (196.H21)--(196.H22) prove the purely algebraic identity

\[
 (-1)^S e\!\left(\frac{\epsilon_\omega a\bar v_qh}{q}\right)
 =\chi_4(\kappa U)\chi_4(x)
  e\!\left(\frac{a\overline2_qx}{q}\right).
\tag{196.H23}
\]

Also (\chi_4(x)=e(-1/4)e(x/4)) for odd (x).  Hence the right side
of (196.H23) is the constant (\chi_4(\kappa U)e(-1/4)) times

\[
 e\!\left(\frac{b_{q,a}x}{4q}\right),
 \qquad b_{q,a}\equiv q+4a\overline2_q\pmod{4q}.
\tag{196.H24}
\]

The integer (b_{q,a}) is odd, and modulo every prime divisor of (q)
it is congruent to (2a); therefore ((b_{q,a},4q)=1).  Its ratio under
(x\mapsto x+2) is

\[
 z_{q,a}=e(b_{q,a}/(2q))=-e(a/q).
\tag{196.H25}
\]

Finally,

\[
 (1-z_{q,a})c_q(a)
 =(1+e(a/q))\frac{2}{q\{1+e(-a/q)\}}
 =\frac{2e(a/q)}q.
\tag{196.H26}
\]

Thus none of (196.H18)--(196.H26) has a sign or representative error.
The error is their application to the literal exact-conductor atom.

### 3.2 Exact Fourier normalization and the missing anchor factor

Round 187 expands the physical parity by

\[
 E_U(S_0)=(-1)^{S_0}
 =\sum_{k\bmod U}c_U(k)e(kS_0/U).
\tag{196.H27}
\]

Because (U) is odd and (S=S_0+Ut),

\[
 (-1)^S=(-1)^tE_U(S_0).
\tag{196.H28}
\]

The factor (E_U(S_0)) is precisely what is Fourier-expanded.  It is
therefore absent from a single retained mode.  At
(k=\mathfrak m a), the exact atom (suppressing only unchanged literal
fields) is

\[
 \boxed{
 \frac1{\mathfrak m}c_q(a)(-1)^t
 e\!\left(\frac{\epsilon_\omega a\bar v_qh}{q}\right)
 B_{\omega,\sigma}(h,t).}
\tag{196.H29}
\]

The determinant equations imply
(S_{0,\omega}\equiv S\pmod U) in both orientations: in the plus chart
(h\equiv Sv\pmod U), and in the minus chart
(-h\equiv Sv\pmod U).  Hence (196.H21) also gives

\[
 e\!\left(\frac{\epsilon_\omega a\bar v_qh}{q}\right)
 =e(aS/q)=e(a\overline2_qx/q).
\tag{196.H30}
\]

Combining (196.H23), (196.H28), and (196.H30) proves the repaired formula
(196.H4).  The proposed primitive carrier is missing (E_U(S_0)).

This factor cannot be absorbed into a constant coefficient.  Indeed,

\[
 E_U(S_0)e(kS_0/U)
 =\sum_{\ell\bmod U}c_U(\ell)
   e((k+\ell)S_0/U).
\tag{196.H31}
\]

Thus parity restoration convolves the retained (k=\mathfrak m a) mode
with every Fourier mode.  The shifted modes have different exact
conductors, reduced numerators, (J)-bands, projective cuts, and safe/core
status.  In particular (196.H31) is not an identity internal to the
Round-195 open packet.  At full mode level, (E_U^2=1) gives

\[
 \sum_{k\bmod U}c_U(k)E_U(S_0)e(kS_0/U)=1,
\tag{196.H32}
\]

so inserting physical parity and then recombining all modes returns the
bare ((-1)^t) aggregate.  Conversely the literal sum without the extra
factor returns ((-1)^S).  Either full recombination undoes the
exact-conductor split; it supplies no estimate for its high-conductor
remainder.

### 3.3 Literal step multiplier and exact near-half falsifier

Let (S_0=[S]_U).  Under (S\mapsto S+1), the literal phase in
(196.H29) has ratio

\[
 (-1)^{c_U(S)}e(a/q),
 \qquad c_U(S)=\mathbf1_{\{S_0=U-1\}},
\tag{196.H33}
\]

because (t) changes only at the canonical wrap.  On the literal support
((U,h)=1), (196.H15) shows ((S_0,U)=1); in particular (S_0\ne0).
Therefore a wrap step ends at a deleted height (U\mid h).  Every
live-to-live predecessor step (S-1\to S) has the ratio (e(a/q)),
which proves (196.H5).

This sign distinction has a full conductor-scale consequence.  For any
odd (q\ge3), take the unit
(a=(q-1)/2).  Then

\[
 |c_q(a)|=\frac1{q\sin(\pi/(2q))}\ge\frac2\pi,
\tag{196.H34}
\]

and the actual live difference factor satisfies

\[
 |(1-e(a/q))c_q(a)|
 =\frac2q\cot\!\left(\frac{\pi}{2q}\right)\asymp1.
\tag{196.H35}
\]

By contrast, the artificial factor in (196.H26) has modulus (2/q).
Thus the literal step loses the entire desired conductor cancellation on
the two primitive near-half modes already responsible for the retained
Fourier energy in Round 187.  This is an exact analytical falsifier, not a
numerical experiment.

If one moves (E_U) into the amplitude so as to retain the artificial
carrier, the exact product rule is (196.H7).  For a current nonzero
residue (S_0\ne0),

\[
 |E_U(S_0-1)-E_U(S_0)|=2.
\tag{196.H36}
\]

At (S_0=0) this commutator vanishes, but that current atom is deleted by
((U,h)=1).  Hence the parity/Fourier commutator is a bulk term on every
possible live adjacent edge.  Its positive norm is the same order as the
original amplitude norm.  No capacity-to-literal-mass inference is made.

### 3.4 There is no accepted literal (\Delta_2) event operator

The accepted exact difference is the Round-191 height difference
(\Delta^-_hW(h)).  Its determinant transport is

\[
 (S,w)\mapsto
 (S-\epsilon_\omega\varrho_U(v),
  w-\epsilon_\omega\gamma_U(v)),
\tag{196.H37}
\]

so its (x)-displacement is
(-2\epsilon_\omega\varrho_U(v)), not (-2).  Normalized Abel
summation returns (196.H37) exactly to the original height sum; it is not
a new cancellation.  At fixed (h), the solutions are
(S=S_{0,\omega}(h)+Ut), so the affine step has
(x\mapsto x+2U), again not (x\mapsto x+2).

A flattening by (x) can of course define
(A(x)=\sum_{\xi:x(\xi)=x}a_\xi), but no accepted identity states
(A=\Delta_2B) for a literal event sequence (B).  Defining (B) by an
indefinite partial sum is a tautological inverse difference with full
support capacity and endpoint terms.  Replacing the divisor-supported
sequence by consecutive odd (x)'s fills precisely the arithmetic holes
that must remain literal.

Even granting a hypothetical exact (\Delta_2B), Sections 3.2--3.3 show
that the correct carrier produces (196.H6), or equivalently that the
artificial carrier produces the full commutator (196.H7).  The route
therefore fails before any estimate for (B) is attempted.

### 3.5 Literal endpoint, mask, carry, phase, and zero-extension ledger

For completeness, consider the labelwise-minimal adjacent-(S) map
(\tau:(S,w)\mapsto(S-1,w)).  Any different reindexing of (w) must be
specified and proved separately and changes both endpoints rather than
only one.  Put

\[
 A_0=\kappa gU,\qquad C_v=\kappa v.
\tag{196.H38}
\]

The actual ordered endpoint pairs are

\[
\begin{array}{c|cc}
 & (N_{0,\omega},d_{0,\omega})&(N_{1,\omega},d_{1,\omega})\\ \hline
 +&(A_0(C_v+2w),A_0)&((A_0+2gS)C_v,A_0+2gS)\\
 -&((A_0+2gS)C_v,A_0+2gS)&(A_0(C_v+2w),A_0).
\end{array}
\tag{196.H39}
\]

Thus (\tau) translates the variable plus upper endpoint, or the
variable minus lower endpoint, by

\[
 (\Delta N,\Delta d)=(2gC_v,2g)
\tag{196.H40}
\]

from predecessor to current, while the other endpoint is fixed.  It also
changes height by

\[
 h_+-h_+\circ\tau=v,\qquad
 h_--h_-\circ\tau=-v.
\tag{196.H41}
\]

These exact formulas force all of the following commutators.

1. **Physical (P_2) mask.**  In the plus chart
   (\delta_+\) is fixed and (\eta_+\) changes by (2); in the minus
   chart (\eta_-\) is fixed and (\delta_-\) changes by (2).  The
   upper-far or lower-close threshold can therefore flip.  The exact
   product rule retains (P-P\circ\tau); post-expansion scalar masking
   is not the physical operator.
2. **Divisibility and coprimality support.**  The height mask
   (G(h)=\mathbf1_{(U,h)=1}) can flip under (196.H41), and it deletes
   the only denominator-cancelling anchor wrap.  The variable divisor
   changes by (2g), so squarefree support, endpoint divisibility,
   allocation coprimality, selected-prime masks, parity predicates, and
   residual selectors need not persist.  Live squarefreeness of
   (\kappa gU) does not make the translated divisor squarefree.
3. **Canonical carry and affine support.**  The predecessor anchor is
   ([S-1]_U).  At an ordinary live edge the carry is zero and yields the
   wrong multiplier (+e(a/q)); at the wrap the next height is killed.
   Positivity intervals for (t) can change, creating affine births and
   deaths.  No carry sign pairs the two orientations.
4. **Fejer factor.**  For
   (F(h)=1-2\kappa gh/R_0),

   \[
    |F(h)-F(h\circ\tau)|=\frac{2\kappa gv}{R_0}\asymp1
   \tag{196.H42}
   \]

   on the inherited shell scale (\kappa v\asymp L).  This is a
   (v)-height shift, not the already safe unit-height Fejer projection;
   its commutator has full pointwise size.
5. **Endpoint products and conjugation.**  With
   (\Lambda=\lambda_1\overline{\lambda_0}), the product difference must
   be opened in its fixed order.  Equation (196.H40) acts on the upper
   factor in the plus chart and on the conjugated lower factor in the
   minus chart.  Profile branch, floor, star, half weight, hard sample,
   endpoint trace, numerical profile, and endpoint zero extension can all
   change.  The two translations are not a common scalar shift.
6. **Square-root phase.**  The phase (\Psi_{\omega,\sigma}) sees the
   endpoint change (196.H40).  No accepted identity makes
   (\Psi-\Psi\circ\tau) small or pairs it across orientations; both
   signs (\sigma) remain in the one outer aggregate.
7. **Cells and crossings.**  Moving ((N,d)) by (196.H40) can cross the
   original shell branch, strict endpoint-ratio cone, profile cell,
   floor, hard-sample, or real-(X) crossing.  These are discrete event
   vectors, not derivatives of a common smooth amplitude.
8. **Outer and endpoint zero extension.**  The height displacement
   (|v|\asymp L/\kappa) is comparable with the full live height scale,
   while one dyadic block has (Y\ll L/\kappa).  Common support can be
   empty or (O(1)) per primitive row, and the remaining terms are
   births and deaths.  At an anchor wrap the coprimality zero extension
   leaves exactly an unpaired boundary atom.  Endpoint zero extensions
   are additional and distinct.
9. **Orientation assembly.**  In the plus chart (x=d'/g); in the minus
   chart (x=d/g).  Thus the same formal (x)-shift acts on opposite
   endpoint factors.  The (++,+-,-+,--) Gram blocks cannot be replaced
   by two separate orientation norms, and both frequency signs and all
   conjugations stay under the one outer real part.

The (T=0) branch and all strict (T\ge1) Farey row predicates remain in
this ledger.  The normalization obstruction is rowwise and applies to
both.  Deleting either branch, or restricting to a submask on which one
of the terms above vanishes, leaves an unpriced exact complement.

### 3.6 Restored powers and the self-return

Round 195 proves only

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll u\{\kappa+\min(Y,D_L)\}X^\varepsilon.
\tag{196.H43}
\]

The (\kappa u) term is safe.  On (196.H8), the remaining positive
capacity has the unresolved ratio

\[
 \mathfrak D(p)=
 \frac{\min(Y,D_L)}{Q\mathfrak m\kappa}>1
\tag{196.H44}
\]

relative to (196.H17).  The exact lift in (196.H16) cancels the
(\mathfrak m) in a *proved* fixed-packet target before the outer divisor
sum; it does not erase (196.H44).  The accepted target ledger is

\[
 QX^\eta
 \sum_{\kappa\ll L}\sum_{u\asymp L/\kappa}
 \kappa u\,\tau_3(u)\log^{O(1)}(2u)
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\tag{196.H45}
\]

If the artificial difference were literal, (196.H26) would replace the
near-half coefficient by (2/(\mathfrak m q)=2/U).  Equations
(196.H34)--(196.H36) show that the repaired live difference instead
retains an order-(1/\mathfrak m)) coefficient on the primitive
near-half modes, and the parity commutator has the same atom count as the
uncancelled term.  The endpoint, mask, Fejer, phase, and zero-extension
commutators in Section 3.5 have no sharper accepted estimate than the
second term of (196.H43).  Hence the complete multiplier (196.H44)
returns.  It is a capacity upper bound only; no positive power may be
absorbed into (X^\varepsilon).

## 4. First doubtful or unproved step

The first invalid step is not one of the displayed congruences.  It is
the operator identification (196.H2), equivalently the claim that the
literal exact-conductor atom carries the phase in (196.H23) with the
same coefficient (\mathfrak m^{-1}c_q(a)).  The exact ratio of the two
sides is (E_U(S_0)).  Removing it double-counts the physical anchor
parity; retaining it destroys the constant step multiplier and mixes all
exact conductors.

After this repair, the next unsupported equality is a literal

\[
 A_{\rm event}(x)=B(x)-B(x-2)
\tag{196.H46}
\]

before positive norms.  The accepted difference moves (x) by
(2\varrho_U(v)), fixed-height affine support moves it by (2U), and an
adjacent-(x) flattening produces every commutator in Section 3.5.

The first genuinely open inequality remains the original
coefficient-sensitive joint estimate (196.H17) on the full region
(196.H8).  It would have to control the actual anchor factor, endpoint
products, masks, carries, births/deaths, Fejer and square-root phase, and
all four orientation Gram blocks before any positive norm.  This report
neither proves nor refutes such a theorem by another mechanism.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `exact_round195_open_P2_packet_region` | **PASS.** Equations (196.H8)--(196.H17) retain exactly the strict open packet and no larger or smaller physical region. |
| `physical_mask_before_spectral_operations` | **PASS.** (P_2) is imposed in (196.H14); Section 3.5 retains (P-P\circ\tau). |
| `both_T_branches` | **PASS.** (T=0) and every simultaneous strict (T\ge1) row condition remain; the obstruction is rowwise. |
| `both_orientations_and_frequency_signs` | **PASS.** Both determinant charts and both (\sigma) signs remain under one outer real part. |
| `spectral_lift_gcd_vs_kappa` | **PASS.** (U=\mathfrak m q), (k=\mathfrak m a), and the exact (\mathfrak m^{-1}) lift are distinct from physical (\kappa) and cofactor (m). |
| `on_shell_x_coordinate_identity` | **PASS.** Equation (196.H20) proves (x=d'/g) in plus and (x=d/g) in minus. |
| `determinant_anchor_congruence` | **PASS.** Equations (196.H18)--(196.H21) verify both signs. |
| `parity_character_identity` | **PASS algebraically, FAIL as a literal single-mode substitution.** Equation (196.H22) is exact, but its parity has already been Fourier-expanded in (196.H27). |
| `primitive_4q_carrier` | **PASS for the artificial parity-restored atom only.** Equation (196.H24) is primitive; the literal atom is (196.H29). Primitivity alone gives no saving. |
| `exact_conductor_coefficient_normalization` | **PASS with decisive repair.** The atom carries (\mathfrak m^{-1}c_q(a)) and ((-1)^t); replacing it by ((-1)^S) is false. |
| `step_two_multiplier_denominator_cancellation` | **FAIL literally.** The artificial ratio is (-e(a/q)), but every live-to-live ratio is (+e(a/q)); (196.H35) retains order-one near-half mass. |
| `genuine_Delta2_before_identity` | **FAIL.** No accepted event operator has step two in (x); (196.H37) and fixed-height support have different steps. |
| `actual_endpoint_event_vectors` | **PASS as retained data; no estimate.** Equations (196.H39)--(196.H40) keep ordered endpoint products and conjugation. |
| `physical_mask_commutator` | **PASS as a barrier.** The plus far or minus close mask changes under the minimal adjacent-(S) map. |
| `squarefree_coprimality_flips` | **PASS as a barrier.** (G(h)), variable-divisor squarefreeness, divisibility, and allocation coprimality can flip; (G) deletes the only cancelling wrap. |
| `carry_birth_death_zero_extension` | **PASS as a barrier.** Ordinary live edges have no cancelling carry; wrap, affine, height, and endpoint boundary terms remain. |
| `Fejer_square_root_phase` | **PASS as a barrier.** The Fejer commutator is order one in (196.H42), and no square-root phase transport estimate is available. |
| `one_outer_real_part` | **PASS.** No separate orientation or sign modulus is introduced. |
| `complete_packet_power_ledger` | **PASS as a no-go.** Equations (196.H43)--(196.H45) restore (Q,\mathfrak m,\kappa,u,Y,D_L,L,X); (196.H44) remains. |
| `unsigned_character_erased_phase_conjugated_controls` | **PASS as falsifiers.** Erasing parity gives the actual (+e(a/q)) multiplier; phase-conjugating bounded arrays attain capacity but are not literal lower mass. |
| `no_consecutive_or_arbitrary_array_replacement` | **PASS.** Consecutive support would fill divisor/gcd holes. Arbitrary arrays are used only to delimit coefficient-uniform methods, never as claimant coefficients. |
| `no_separate_orientation_norm` | **PASS.** The opposite endpoint translations and all four Gram blocks remain joint. |
| `no_T_branch_or_submask_escape` | **PASS.** No branch is removed. The wrap sector is empty; parity or mask subranges are not claimed without complements. |
| `diagnostic_only` | **PASS.** No computation was used. |
| `original_t1_only_downstream_scope` | **PASS.** Even a future success here would leave (P_1), other original-(t) incidences, and every higher owner listed below. |
| `exponent_quarantine` | **PASS.** No parent, bridge, theorem, or exponent is changed. |

The unsigned, character-erased, phase-conjugated, arbitrary-array,
consecutive-support, separate-orientation, mask-deleted, (T)-deleted,
and proper-submask shadows all fail to certify the literal theorem.  The
phase-conjugated and arbitrary-array controls are method falsifiers only,
not physical lower bounds.

## 6. Dependencies and exact artifacts used

Only the assigned brief and its permitted selected context were used:

1. `rounds/codex-managed/m9-m1-t1-p2-on-shell-anchor-carrier-commutator-gate/briefs/carrier_collision_endpoint_hostile_audit.md` —
   `323ba2aa2f3dfa55c3478cc7d93914c71a12f67c083bdf3def15cad987e4ed8d`.
2. `protocol.md` —
   `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a`.
3. `state/proof_obligations.yml` —
   `f1f6bd2c9ff6370febf37b2c6f50c023cd142470922ffe9ce713e853f5efcce2`.
4. `state/active_campaign.yml` —
   `8aa8f0dea94adc77f6e3e4dbc8a2b43c3a6749aefe7f95c37be0c3867e85dfab`.
5. `state/failure_ledger.md` —
   `6ef6a4427ecb579184f0f1ee89f088702e39e4ce220a407e0c6fd6e93aca245b`.
6. `strategy/round196_m1_t1_p2_on_shell_anchor_carrier_commutator_strategy.md` —
   `10ce6e86cf12bda10fa0581eb5a225844610d8ec802dec5501d752da21dd2f3f`.
7. `proofs/kernels/m9_m1_hard_top_t1_p2_absolute_capacity_sectors.md` —
   `4ce74b520c09b12bd1292dc16dba98e2ec66059619aeb17b068836f0febd0009`.
8. `proofs/kernels/m9_m1_hard_top_t1_high_h_inverse_residue_conductor_reduction.md` —
   `a9145455a872d57debaf0f91cc8a518f80acef4c1b1fb9115dc1851765a992f2`.
9. `proofs/kernels/m9_m1_hard_top_t1_high_h_dual_frequency_projective_reduction.md` —
   `31092b28826b9f36ecaedfb5efc5d7625f4caa4da2cf4c37bd48389c6ac6ee58`.
10. `proofs/kernels/m9_m1_hard_top_t1_fast_signed_inverse_transport_reduction.md` —
    `7e2dacaad8b29924c41578a4545b2edad5770c2a49354c5753a3dee430e291f2`.
11. `proofs/kernels/m9_m1_hard_top_t1_rho_large_farey_covector_reduction.md` —
    `301e51dc49072ed8541fc1183f00a8cddc3768fba025e33289314004f8c38325`.
12. `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reports/p2_gram_diagonal_collision_hostile_audit.md` —
    `52de40ade4e243cca9e0c50edfee5f913c8120a488407b4f39fe951f22d9b8fb`.
13. `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reviews/literal_gram_nogo_owner_scope_seam_review.md` —
    `5b37315c66bd637c127cc8f3fddbb7f94ed14f9f94955c685f90a5960120c197`.
14. `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/reviews/conductor_round195_report_reconciliation.md` —
    `3ff78bbb5f491ec4dfb30ae05123dfcecf8a93e38e17d7fee1c124c5c45b9436`.
15. `rounds/codex-managed/m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate/synthesis.md` —
    `fdcf6ebed7455745034caaa7a30453ed9b84ff4c48440d61b720679d4d06e168`.

No web source, sibling Round-196 report, or computation was used.  No
proof graph, proof draft, validation matrix, strategy, brief, kernel,
review, synthesis, or shared state was edited.

## 7. Recommended state effect

**Retain the Round-195 open status and record this route-scoped no-go; no
promotion.**

1. Keep (196.H18)--(196.H26) only as algebra for the parity-restored
   shadow.  Do not attach (c_q(a)) to that shadow as though it were a
   literal exact-conductor atom.
2. Reject a complete or strict-sector (P_2) closure based on the claimed
   step-two multiplier.  The correct carrier is (196.H4), the live
   multiplier is (196.H5), and the wrap where (196.H26) would apply is
   killed by ((U,h)=1).
3. Reject full anchor recombination as a high-conductor estimate: it mixes
   every conductor and returns to the pre-Fourier packet.  Reject
   consecutive-support completion, post-expansion mask deletion,
   separate orientation norms, or an unpriced parity/wrap submask.
4. The first admissible new theorem remains a coefficient-sensitive joint
   estimate for the complete literal remainder on (196.H8), with the
   actual anchor square wave and every commutator in Section 3.5 retained
   before positive norms.
5. Leave (P_1), every other original-(t) incidence, the hard small-(t)
   owner, smooth M1, GAR, all M2 parents, endpoint uniformity, M9, both
   bridges, the quarter theorem, and all exponent records unchanged.

This report establishes a normalization/support self-return, not literal
lower mass and not failure of the target estimate by all possible methods.
