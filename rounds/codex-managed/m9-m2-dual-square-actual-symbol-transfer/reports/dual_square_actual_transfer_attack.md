# Complete actual dual-square transfer and owner self-return

Campaign: m9-m2-dual-square-actual-symbol-transfer
Round: 106
Task: dual_square_actual_transfer_attack
Role: discovery
Starting graph SHA-256: 2b61ad459192c94e83ee80adfa3bdda5374df87b01f42c4a0ab306c07eb817de

## 1. Result

The proposed normalization (106.13) is the **correct zeroth interior
stationary symbol**, including its factor \(e(1/8)\). For either sign of
the reciprocal mode, all three Gaussian operations can be done without a
missing factor of \(2\), \(d\), \(g\), \(n\), or \(\ell\). If

\[
 n=|2\nu-g|,\qquad \sigma=\operatorname {sgn}(g-2\nu),
\]

for the displayed orientation, the two Poisson frequencies at a joint
interior saddle are \(m=\sigma\ell\) and
\(s=\sigma(d-2h)>0\), and

\[
 y_*^2={\ell\over n},\qquad
 k_*={J(\sqrt {b_*}-\sqrt a)\over2}\sqrt{n\over\ell},
 \qquad b_*={4d^2Xn\ell\over s^2}.                         \tag{106.A1}
\]

The stationary value is

\[
 -\sigma\left(J\sqrt{dn\ell/s}-{1\over2}\sqrt{as/d}\right)^2, \tag{106.A2}
\]

and the smooth-bulk leading coefficient is

\[
 \boxed{
 e(1/8){g^{1/2}b_*^{3/4}\over
 dJ^{1/2}n^{3/4}\ell^{1/4}}
 A^\circ_{ga,gb_*}(g\ell/n).}                          \tag{106.A3}
\]

This is multiplied by the literal \(\mu(d)\widehat W_R(\nu)\), the
smooth profile values, and the phase (106.A2); those factors are not
absorbed into (106.A3).

The opposite orientation has the same formula with
\(n=|2\nu+g|\) and the corresponding reflected sign. The three
Gaussian units are \(e(1/8),e(-\sigma/8),e(\sigma/8)\), so their
product is always \(e(1/8)\).

Formula (106.A3), however, is **not the complete owner-preserving
symbol**. The exact physical factor is a normalized complete Fresnel
operator, not point evaluation of \(A^\circ\); and a sharp integer owner
does not become its value at the generally nonintegral point \(b_*\).
After exact two-variable Poisson summation it becomes a nonlocal
conjugated projector on the dual vector. This is already true for the
sharp maximal interval and is unavoidable for the square-ray,
exact-centre, original-mode, floor, star, and prior one-count owners.

Consequently (106.14)--(106.16) are not proved as stated. There is an
exact complete transform, given below as a sum of triple oscillatory
integrals, but its stationary remainder contains the full conjugated
actual-owner kernel. Fourier inversion returns that kernel owner by
owner to the original zero-extended fixed-\(a\) row and preserves its
capacity. Thus the complete transfer supplies neither the missing full
\(D\)-saving nor a new range \(D\le X^\theta\) for any fixed
\(\theta>0\). The already accepted prescribed polylogarithmic range is
unchanged.

The smallest exact survivor is

\[
 \boxed{\quad
 \widetilde P_{\mathrm{act},I}
   =T\,P_{\mathrm{act},I}\,T^{-1},
 \quad}                                                       \tag{106.A4}
\]

acting on the normalized complete-Fresnel dual vector. Here
\(P_{\mathrm{act},I}\) is the product of the sharp maximal cutoff and
all literal residual owners, and \(T\) is the exact Fourier/Poisson
transfer before stationary truncation. Equivalently, (106.A4) is the
complete signed nonzero-shift actual Gram after the scalar dual-square
phase and its Jacobian have been removed. It is nonlocal in
\((\ell,s)\), has the same operator norm and rank as the primal owner,
and is precisely the actual-vector estimate still missing.

## 2. Exact statement and hypotheses

Work on one residual hard-top block with \(J=\sqrt X\),

\[
 b=a+2q,\quad a\asymp b\asymp A,\quad q\asymp D,\quad
 a<b<4a,\quad K\asymp {JD\over A},\quad G\asymp {L\over A},
\]

and retain the literal zero extension, all actual profiles and both
orientations. Expand primitivity exactly as

\[
 {\bf1}_{(a,q)=1}=\sum_{d\mid a,\ d\mid q}\mu(d),\qquad q=du.
                                                               \tag{106.A5}
\]

Since \(a\) and every \(d\mid a\) are odd,
\(e(du/2)=(-1)^u\). For the displayed orientation put

\[
 c=\nu-g/2=-\sigma n/2,\qquad
 n=|2\nu-g|\ge1,\qquad \sigma\in\{1,-1\}.             \tag{106.A6}
\]

Let \({\cal O}_{a,d,u,k,g,\nu,I}\) denote the complete product of the
maximal cutoff \(du\in I\), the moving open reciprocal interval, the
finite odd-lift fibre, the square-ray and exact-centre complements, the
safe-ratio and original-mode owners, every dyadic/floor/star/hard-top
profile, and all prior one-count complements. The physical amplitude is

\[
 Q_{a,du,g}(y)=2gy\,A^\circ_{ga,g(a+2du)}(gy^2),\qquad
 r_{u,k}={J(\sqrt{a+2du}-\sqrt a)\over2k}.             \tag{106.A7}
\]

All additional bounded-variation \(k\)-profiles may be included in
\({\cal O}\). The literal one-mode summand after (106.A5) is

\[
\begin{aligned}
 S^\sigma_{a,d,g,\nu,I}
 =\sum_{u,k\in\mathbb Z}&e(du/2){\cal O}_{a,d,u,k,g,\nu,I}
 \int Q_{a,du,g}(y)\\
 &\times e\!\left(gk(y-r_{u,k})^2
       -\sigma {n\Lambda_{du}\over2k}\right)dy,
\end{aligned}                                                   \tag{106.A8}
\]

where forbidden \(u,k\), \(k\le0\), and empty fibres have value zero.
The full row is the sum of
\(\mu(d)\widehat W_R(\nu)S^\sigma\), all actual \(g,R,\nu\), both
orientations, and the finite profile ledger.

There are two exact statements.

First, choose any compactly supported smooth cardinal interpolation
\({\cal A}(v,t,y)\) of
\({\cal O}_{a,d,u,k,g,\nu,I}Q_{a,du,g}(y)\) at integer \((u,k)\).
Two-dimensional Poisson summation gives the exact identity

\[
 S^\sigma_{a,d,g,\nu,I}
 =\sum_{h,m\in\mathbb Z}\iiint {\cal A}(v,t,y)
       e(\Phi^\sigma_{h,m}(v,t,y))\,dy\,dt\,dv,          \tag{106.A9}
\]

with

\[
 \Phi^\sigma_{h,m}={dv\over2}+gt(y-r_{v,t})^2
  -\sigma {n\Lambda_{dv}\over2t}-hv-mt.                \tag{106.A10}
\]

This is the complete owner-preserving transform. It has no omitted
stationary, transition, equality, nonstationary, endpoint, empty-fibre,
or singleton term. Different cardinal interpolations change individual
dual integrals but not their complete sum.

Second, on a smooth interior piece for which the three saddles are
separated from every cutoff transition and all amplitude seminorms are
controlled, the leading term of (106.A9) is (106.A1)--(106.A3), with
the exact support

\[
 b_*\in a+2I,\qquad {nb_*\over4}<\ell<na,\qquad
 s=\sigma(d-2h)>0\text{ odd},                              \tag{106.A11}
\]

plus the transformed smooth profiles evaluated at
\((u_*,k_*,y_*)\). Equalities in (106.A11) are transition saddles and
are not included in the interior formula.

For an exact physical, rather than zeroth Gaussian, symbol define

\[
 {\cal C}_{a,b,g}(k,r)
 :=e(-1/8)\sqrt{2gk}
 \int Q_{a,b,g}(y)e(gk(y-r)^2)dy.                       \tag{106.A12}
\]

Then the physical part of the transformed leading coefficient is

\[
 e(1/8){b_*^{3/4}\over
 2dJ^{1/2}g^{1/2}n^{1/4}\ell^{3/4}}
 {\cal C}_{a,b_*,g}(k_*,y_*),                            \tag{106.A13}
\]

before the \(k\)- and \(u\)-stationary corrections are expanded.
Equation (106.A3) is exactly the zeroth replacement
\({\cal C}(k_*,y_*)=Q(y_*)=2g\sqrt{\ell/n}\,
A^\circ_{ga,gb_*}(g\ell/n)\).

## 3. Proof or derivation

Opening the centred integral first gives the exact interaction

\[
 gk(y-r_{u,k})^2+\left(\nu-{g\over2}\right){\Lambda_{du}\over k}
 =gky^2-gJ(\sqrt b-\sqrt a)y+\nu{\Lambda_{du}\over k}. \tag{106.A14}
\]

Thus the density mode \(\nu=0\) is not absent: it is the original
uncentred physical phase. Nevertheless the joint \((y,k)\) saddle is
nondegenerate. This is why the physical Gaussian must be combined with
the reciprocal Gaussian and not silently frozen as an arbitrary slow
coefficient.

At a stationary point of (106.A10), first
\(y=r_{v,t}\). The \(t\)-equation is

\[
 {\sigma n\Lambda_{dv}\over2t^2}=m.
\]

Hence only \(m=\sigma\ell\), \(\ell>0\), has an interior saddle and

\[
 k_*^2={n\Lambda_{du}\over2\ell}.
\]

After this saddle the phase is

\[
 {du\over2}-\sigma J(\sqrt{a+2du}-\sqrt a)\sqrt{n\ell}-hu.
                                                               \tag{106.A15}
\]

Writing \(s=\sigma(d-2h)>0\), its \(u\)-equation is

\[
 {s\over2}={dJ\sqrt{n\ell}\over\sqrt b},
\]

which proves (106.A1). Substitution of
\(u_*=(b_*-a)/(2d)\) gives

\[
\begin{aligned}
 \Phi_*&=-\sigma\left({dXn\ell\over s}
       +{as\over4d}-J\sqrt{an\ell}\right)\\
 &=-\sigma\left(J\sqrt{dn\ell/s}
       -{1\over2}\sqrt{as/d}\right)^2,
\end{aligned}                                                   \tag{106.A16}
\]

and

\[
 e(-\sigma as/(4d))
 =-\sigma i\,\chi_4(a/d)\chi_4(s).                     \tag{106.A17}
\]

This retains, rather than estimates away, the returned odd character.

The three conditional Hessian factors are

\[
 (2gk_*)^{-1/2},\qquad
 \left({k_*^3\over n\Lambda_*}\right)^{1/2},\qquad
 {b_*^{3/4}\over dJ^{1/2}(n\ell)^{1/4}},              \tag{106.A18}
\]

with signatures \(+1,-\sigma,+\sigma\). Since
\(Q(y_*)=2g\sqrt{\ell/n}\,A^\circ_{ga,gb_*}(g\ell/n)\), the product
of (106.A18) and \(Q(y_*)\) is

\[
 {g^{1/2}b_*^{3/4}\over
 dJ^{1/2}n^{3/4}\ell^{1/4}}
 A^\circ_{ga,gb_*}(g\ell/n),
\]

and the signature is \(1\). This proves (106.A3), including its
Gaussian unit. If the physical Gaussian is not expanded, the same
calculation with (106.A12) gives (106.A13).

The reciprocal inequalities transport without approximation at an
interior saddle:

\[
 {J\delta\over2\sqrt a}<k_*<{J\delta\over\sqrt b}
 \iff {nb\over4}<\ell<na.                                \tag{106.A19}
\]

The physical saddle satisfies \(y_*^2=\ell/n\), so its lower and upper
collars map to the same two inequalities. The maximal interval maps to
\(b_*\in a+2I\) only for the interior principal term. Its two sharp
endpoints remain one-sided \(u\)-integrals. As \(b/a\to4\), the
physical and reciprocal interiors collapse together; if the collars
overlap, the smooth interior principal term is empty. Empty and
singleton \(k,u,\ell,s\) fibres, or equality in (106.A19), therefore
belong to the exact transition part of (106.A9), not to (106.A3).

The literal owner map is as follows.

- The Möbius progression is exact and keeps \(\mu(d)\); odd \(d\)
  preserves alternation, and the dual integer is the odd
  \(s=\sigma(d-2h)\).
- The complete metric series is untouched: every \(\nu\), including
  zero, has an odd positive \(n\), and the two orientations give the two
  reflected dual lattices.
- The finite odd-lift condition remains a \(g\)-fibre. In the interior
  principal term its smooth support is tested at \(b_*\); its literal
  integer entry and exit stay in the transition kernel.
- The two physical collars remain inside (106.A12). Point evaluation
  in (106.A3) is only their zeroth resolved symbol.
- The sharp maximal interval, moving reciprocal integer interval,
  floors, stars, hard top, square-ray, exact-centre, safe-ratio,
  original-mode, diagonal, boundary, and prior one-count owners remain
  multiplication operators before (106.A9). They become nonlocal
  operators after the exact transform; none is exactly the scalar value
  of its indicator at \(b_*\).

The last assertion is not just a missing estimate. Let \(P_E\) be the
diagonal projector of any one owner \(E\) on the finite zero-extended
\((u,k)\)-array, and let \({\cal F}\) denote the unitary Fourier transform
of that array. Then

\[
 \widetilde P_E={\cal F}P_E{\cal F}^{-1},\qquad
 \widetilde P_E^2=\widetilde P_E=\widetilde P_E^*,\qquad
 \|\widetilde P_E z\|_2=\|P_E{\cal F}^{-1}z\|_2.       \tag{106.A20}
\]

Complements and disjoint one-count owners remain complements and
orthogonal projectors under (106.A20). Applying the inverse transform
returns \(P_E\) exactly. The Möbius identity returns term by term by
linearity. A non-idempotent profile or cutoff weight \(M_w\) similarly
returns through
\({\cal F}^{-1}({\cal F}M_w{\cal F}^{-1}){\cal F}=M_w\), although it
is not called a projector. Thus square-ray, centre, safe, boundary and
maximal ownership, and every literal profile multiplier, all self-return
separately; no vote or cancellation between owners is being used.

For example, even the \(u\)-interval owner has dual kernel proportional
to

\[
 K_I(\xi,\xi')=\sum_{u:\,du\in I}e(u(\xi'-\xi)),        \tag{106.A21}
\]

a Dirichlet kernel rather than a diagonal condition on \(b_*\). A
general prior-owner product gives the two-variable analogue of
(106.A21). The subsequent stationary canonical change of variables
from Fourier coordinates to \((\ell,s)\) conjugates this projector once
more but does not diagonalize it or change its norm. This proves the
owner-by-owner self-return (106.A4).

There is also a direct interpolation no-go. If two continuous owner
extensions agree at every integer \(u\), they define the same primal
sum. Their difference may contain

\[
 H(v,t,y)=\sin(\pi v)\psi(v,t,y),                       \tag{106.A22}
\]

which vanishes at every integer \(v\) but is nonzero at a generic
stationary \(u_*\). Its putative pointwise principal owner at \(b_*\)
changes, while the exact sum does not; the change is cancelled by the
remaining dual integrals in (106.A9). Hence a literal identity with a
pointwise owner in (106.A3) is noncanonical. A frozen interpolation and
a complete seminorm/remainder theorem are logically necessary.

The exact error ledger is therefore

\[
 {\cal R}_{\rm act}=
 (\text{complete Fresnel}-\text{zeroth physical Gaussian})
 +\text{\(k\)-transitions/nonstationary modes}
 +\text{\(u\)-transitions/nonstationary modes}
 +\text{conjugated owner kernels}.                         \tag{106.A23}
\]

Equation (106.A9) contains every term in (106.A23), so it is an exact
isolation rather than an omitted-error notation. The accepted bound
(106.3) controls sampled \(k\)-variation for each fixed integer \(q\);
it supplies neither controlled \(u\)-derivatives of (106.A12) nor
seminorms for (106.A20). Thus it cannot prove
\({\cal R}_{\rm act}\ll X^\varepsilon L^2/A\).

Finally, the interior dual packet has the already indicated scale:
\(\asymp n^2JD\) points and point size
\(\asymp \sqrt{L/J}/n\), hence natural mode-level
\(\ell^2\)-capacity \(\asymp\sqrt{LD}\). This is
\(\sqrt D\) larger than one-row capacity. Exact Fourier inversion and
(106.A20) preserve the full Gram capacity. Therefore Plancherel or
generic square-root cancellation can recover at most the first
\(D^{1/2}\), whereas the maximal theorem needs the full \(D\) and the
rowwise Cauchy-to-Gram route has the exact \(D^2\) deficit. No fixed
positive power of \(D\) can be absorbed into \(X^\varepsilon\).

## 4. First doubtful or unproved step

The first unproved step is the replacement of the exact transform
(106.A9) by a pointwise dual amplitude in (106.14). Before any estimate,
one must freeze a continuous extension of every integer owner and prove a
two-variable seminorm ledger that is invariant under the arbitrary
choice exposed by (106.A22). No such ledger follows from fixed-\(q\)
sampled-\(k\) variation. In particular, \(b_*\) is normally nonintegral,
so \(A^\circ_{ga,gb_*}\), a floor/star owner, a square indicator, or an
exact-centre indicator at \(b_*\) is an analytic interpolation, not a
literal transported owner.

Even after all jagged owners are split off, the first smooth remainder is
the normalized complete-Fresnel defect

\[
 {\cal C}_{a,b,g}(k,r)-Q_{a,b,g}(r).                   \tag{106.A24}
\]

The fixed-row theorem bounds the complete integral but does not give the
aggregate \(u\)-variation and high-order stationary remainder needed to
sum (106.A24), both reciprocal endpoint transitions, and both maximal
endpoint transitions over all \(d,g,\nu,\ell,s\) at scale
\(X^\varepsilon L^2/A\).

After these analytic seams, the genuinely arithmetic missing assertion
is the actual-vector estimate for (106.A4), or equivalently the complete
signed nonzero-shift fixed-\(a\) Gram. The returned factor
\(\chi_4(a/d)\chi_4(s)\) alone is not such an estimate. No terminal M1
divisor theorem can be invoked: the transformed coefficient still
contains the metric mode \(n\), the nonintegral saddle \(b_*\), the
complete Fresnel operator, and the nonlocal owner kernel, and no supplied
theorem has these literal hypotheses.

## 5. Required control test and outcome

- **Scalar stationary points and Gaussian units — passed.**
  Equations (106.A1), (106.A16), and (106.A18) give all three Hessians;
  the total unit is \(e(1/8)\) for both signs.
- **Physical Gaussian interaction and principal normalization — passed
  with correction.** Formula (106.A3) is the correct zeroth interior
  symbol. Formula (106.A13), not point evaluation, retains the complete
  physical Gaussian.
- **Maximal cutoff transport — exact nonlocal return, estimate open.**
  Interior saddles satisfy \(b_*\in a+2I\), but the exact sharp owner is
  the Dirichlet kernel (106.A21) plus both endpoint transitions.
- **Reciprocal integer entry/exit — passed geometrically, estimate
  open.** The strict support is (106.A19); equality, empty and singleton
  fibres remain in (106.A9).
- **Finite odd lifts — retained, not scalarized.** The interior support
  may be evaluated at \(b_*\), while literal lift entry/exit is in the
  conjugated owner kernel.
- **Primitive Möbius progressions — passed.** The coefficient
  \(\mu(d)\), odd parity, \(d^{-1}\) Jacobian and odd dual \(s\) are all
  present.
- **Complete metric density/discrepancy and both orientations — passed.**
  Every \(\nu\), including zero, is retained. Equation (106.A14) shows
  why density is not deleted. The reflected orientation has the same
  normalization.
- **Profiles, floors, stars, hard top and prior owner one-count — passed
  as an exact operator statement, not as a pointwise symbol.** Equation
  (106.A20) preserves each one-count projector, its complement and
  disjointness; conjugation and inversion also preserve every
  non-idempotent profile multiplier.
- **Physical collars and collapsing cone edge — passed for support,
  remainder open.** The two collar boundaries map to (106.A19); overlap
  deletes the interior principal term. The complete collar contribution
  stays in (106.A12) and (106.A23).
- **Stationary, transition and nonstationary errors — exact isolation,
  target bound failed.** Equation (106.A23) lists the complete survivor.
  No accepted \(q\)-seminorm theorem sums it to (106.15).
- **Empty, singleton and equality saddles — passed.** They are direct or
  one-sided terms of (106.A9), never assigned a full Gaussian main term.
- **Pell, near-square, square and fourth-power controls — passed as
  method controls.** The algebra uses no Diophantine gap. Their owner
  projectors self-return, and coherent square phases show that no generic
  extra cancellation may be asserted; no lower bound for the full actual
  vector is claimed.
- **Exact and near metric centres — passed.** Modewise density remains;
  any punctured-window cancellation occurs only after the complete
  \(\nu\)-sum. No mode is removed before transformation.
- **Dual capacity and full-\(D\) gain — failed for the desired theorem.**
  The transform is equal-capacity and mode-level square-root cancellation
  is short by another \(D^{1/2}\); rowwise Gram closure is short by
  \(D^2\).
- **Transform inversion and self-return — passed owner by owner.**
  Equation (106.A20) proves exact return and one-count preservation.
- **Terminal M1 and primary-source map — passed by nonuse.** No external
  theorem or web source was invoked; the returned phase and character do
  not match a supplied literal M1 hypothesis.
- **Downstream and exponent scope — passed.** No polynomial fixed-\(a\)
  Gram, density-discrepancy energy, hard signed cone, other M2 packet,
  M9-M2, M9-M1, endpoint uniformity, M9, quarter theorem, or new exponent
  follows.

No numerical experiment and no external source were used.

## 6. Dependencies and exact artifacts used

- protocol.md
- state/proof_obligations.yml
- state/active_campaign.yml
- rounds/codex-managed/m9-m2-dual-square-actual-symbol-transfer/briefs/dual_square_actual_transfer_attack.md
- rounds/codex-managed/m9-m2-dual-square-actual-symbol-transfer/derivation_packet.md
- rounds/codex-managed/m9-m2-dual-square-actual-symbol-transfer/candidates/conductor_owner_preserving_dual_square.md
- rounds/codex-managed/m9-m2-polynomial-q-maximal-alternation/reports/adjacent_q_transport_attack.md
- rounds/codex-managed/m9-m2-fixed-q-sampled-k-short-shell/reports/fixed_q_sampled_k_attack.md
- rounds/codex-managed/m9-m2-top-endpoint-actual-symbol-variation/reports/centered_integral_variation_attack.md
- rounds/codex-managed/m9-m2-top-endpoint-signed-strict-metric-energy/synthesis.md
- rounds/codex-managed/m9-m2-primitive-ray-q-dispersion/synthesis.md

No sibling Round-106 report, shared synthesis, proof draft, validation
matrix, strategy file, computational artifact, or external source was
read or used.

## 7. Recommended state effect

**Retain** M9-M2-primitive-ray-fixed-a-actual-Gram and
M9-M2-top-endpoint-density-discrepancy-energy as open. Retain the
accepted fixed/polylogarithmic shell and do not promote a fixed
positive-power \(q\)-range.

**Promote only after independent seam review** the scoped smooth-interior
normalization (106.A1)--(106.A3), including the corrected statement that
(106.A3) is a zeroth stationary symbol and that (106.A13) is the complete
physical-Fresnel symbol before later stationary corrections.

**Promote as a route obstruction** the complete-transfer no-go:
literal sharp owners transform to conjugated nonlocal projectors, exact
Fourier inversion returns them owner by owner at equal capacity, and no
pointwise owner-preserving formula of the form (106.14) is canonical
without a frozen interpolation and a full remainder theorem. Revise or
reject any claim that (106.13) by itself is a complete actual symbol or
that full-rank scalar stationary phase supplies a \(D\)-saving.

Retain (106.A4), equivalently the normalized complete-Fresnel signed
actual-vector correlation, as the smallest unresolved survivor. A
future promotion must either estimate this nonlocal kernel directly or
prove a complete interpolation-independent remainder theorem and then a
new signed projection saving. Do not infer any downstream M2, M1, M9,
endpoint, quarter-exponent, or global-exponent claim.
