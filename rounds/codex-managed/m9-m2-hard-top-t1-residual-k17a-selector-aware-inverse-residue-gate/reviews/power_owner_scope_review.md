# Round 177 review: primitive alias power and downstream-owner scope

## Verdict

**GREEN, with three non-blocking scope clarifications recommended below.**
The formalized kernel
`proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_alias_conductor_reduction.md`
correctly proves the exact alias folding, the reduced-conductor coefficient
mass, the complete \(q\le(\log X)^B\) Fourier packet, and its physical
small-primitive-modulus corollary.  Its one-square-root, \(TT^*\),
Parseval-diagonal, collision, incomplete-lift, and two-orientation claims
are correctly scoped as capacities or route obstructions.  None is stated
or usable as literal K17a lower mass.

The precise promoted mathematical content may be limited to

\[
 \boxed{
 \sum_{j=0}^{g-1}c_u(\ell+ju_0)=c_{u_0}(\ell),\qquad
 \sum_{\operatorname{cond}(\ell)=q}|c_{u_0}(\ell)|
 \ll {q\over u_0}\log(2q),}
\tag{177.P1}
\]

the target-safe packet (177.K12), and the physical corollary (177.K13).
The high-conductor estimate (177.K34), complete K17a, every downstream
owner, and every exponent implication remain open.

## 1. Polylogarithmic-conductor packet

The proof of (177.K12) is power-correct.  At fixed
\((\kappa,u,u_0)\), with \(g=u/u_0=(u,n)\), the literal counts are

\[
 \#n_0=O(u_0),\qquad \#v=O(L/\kappa),
 \qquad \#t=O(\kappa),
\tag{177.P2}
\]

so both orientations together have \(O(Lu_0)\) capacity.  For aliases
of exact conductor \(q\mid u_0\),

\[
 \ell=(u_0/q)a,\quad(a,q)=1,\qquad
 c_{u_0}(\ell)={q\over u_0}c_q(a),
\tag{177.P3}
\]

and therefore

\[
 \sum_{\operatorname{cond}(\ell)=q}|c_{u_0}(\ell)|
 \ll {q\over u_0}\log(2q).
\tag{177.P4}
\]

Multiplication of (177.P2) and (177.P4) gives the correct positive
capacity \(Lq\log(2q)\).  For \(Q=(\log(2X))^B\),

\[
 \sum_{u_0\mid u}\sum_{\substack{q\mid u_0\\q\le Q}}
 Lq\log(2q)
 \ll LQ\log(2Q)\tau(u)^2.
\tag{177.P5}
\]

There are \(O(L/\kappa)\) supported \(u\)'s, and
\(\sum_{\kappa<\delta L}\kappa^{-1}\ll\log(2L)\).  Divisor and
polylogarithmic factors are absorbed by epsilon rebudgeting, yielding
\(L^2X^\varepsilon\).  Both orientations, every exact gcd stratum,
the determinant cutoffs, original-gcd cutoff, selectors, parity branches,
and zero extension are present; all literal restrictions only delete or
downweight atoms.

The kernel is also correct that this is stronger than merely proving the
physical sector \(u_0\le Q\).  Every alias of such an atom has
\(q\mid u_0\le Q\), while (177.K12) additionally controls low-conductor
aliases belonging to atoms with \(u_0>Q\).  The Fourier packet has an
exact complementary packet \(q>Q\).  It is an owner-complete transform
sector, but it should not be renamed a physical incidence partition.

## 2. One-square-root ledger

The claimed obstruction is exact for the mechanism as scoped.  Before
oscillation, the exact-\(q\) alias packet has capacity

\[
 Lq\log(2q).
\tag{177.P6}
\]

Granting a uniform \(q^{1/2}\) saving to each reciprocal alias and then
recombining those aliases positively leaves

\[
 L\sqrt q\log(2q),
\tag{177.P7}
\]

which is not the local \(L X^\varepsilon\) scale for power-size \(q\).
The primitive near-half aliases have \(q=u_0\) and constant-size
coefficients, so this loss cannot be assigned only to negligible aliases.
If one positively sums the optimistic primitive-alias certificate over
\(u\asymp L/\kappa\), its available global scale is

\[
 \sum_{\kappa}\sum_{u\asymp L/\kappa}L\sqrt u
 \ll L^{5/2}X^\varepsilon,
\tag{177.P8}
\]

matching the inherited one-saving barrier and remaining a factor
\(L^{1/2}\) above target.

Equation (177.P7) is not a universal no-go for all large sieves.  It rules
out exactly one conductor-square-root saving followed by positive
fixed-conductor recombination.  A second coupled saving, a full \(q\)
saving, or signed averaging across \(q,u_0,u,\kappa\), selectors, or
orientations remains outside its scope.  The kernel states this distinction
correctly.

## 3. Exact \(TT^*\), Parseval diagonal, and collisions

With both orientations inside the atom label \(z\), the identities

\[
 H_\ell=\sum_zA_ze(\ell b_z/u_0),\qquad
 B_b=\sum_{z:b_z=b}A_z,
\tag{177.P9}
\]

give exact Parseval

\[
 \sum_{\ell\bmod u_0}|H_\ell|^2
 =u_0\sum_{b\bmod u_0}|B_b|^2.
\tag{177.P10}
\]

Keeping the rank-one matrix
\(c_{u_0}(\ell)\overline{c_{u_0}(\ell')}\) reconstructs
\(|\sum_bE_{u_0}(b)B_b|^2\), exactly the original physical block
squared.  This is a genuine self-return identity, not an estimate.

If alias Cauchy replaces the rank-one matrix by the identity, the
coefficient-independent physical self-diagonal in the resulting positive
majorant is

\[
 D=u_0\sum_z|A_z|^2,\qquad
 D\ll Lu_0^2X^\eta,\qquad
 \sqrt D\ll u_0\sqrt L\,X^\eta.
\tag{177.P11}
\]

Thus this particular nonnegative diagonal certificate is not target-safe
for \(u_0>\sqrt L\), even if every off-diagonal is otherwise removed.
This does not say that the exact energy is bounded below by \(D\): signed
off-diagonal terms inside each \(B_b\) can cancel the self-diagonal.

The collision statement is also correct.  For fixed \(b\), orientation,
and physical \(v\), the congruence

\[
 n_0\equiv\pm bv\pmod{u_0}
\tag{177.P12}
\]

has \(O(1)\) representatives in the length-\(O(u_0)\) determinant
interval; there are \(O(u)\) values of \(v\) and \(O(\kappa)\) fibre
sites.  Hence \(\#B_b=O(u\kappa)=O(L)\), with only a constant change for
both orientations, and positive bucket Cauchy gives

\[
 u_0\sum_b|B_b|^2
 \ll u_0L\sum_z|A_z|^2
 \ll L^2u_0^2X^\eta.
\tag{177.P13}
\]

Its square root is \(Lu_0\), the raw stratum capacity.  Equations
(177.P11)--(177.P13) verify exactly the scopes claimed in (177.K31):
nonnegative diagonal closure fails on the stated power range; positive
collision closure can self-return completely; neither is literal lower
mass.

## 4. Incomplete lifts and the two orientations

No lift multiplicity is missing from (177.K10)--(177.K11).  To make the
ledger explicit, at final alias conductor \(q\) put

\[
 h=u_0/q,\qquad u=ghq.
\tag{177.P14}
\]

The physical \(v\)-interval has \(O(gh)\) lifts of a residue modulo
\(q\); the \(n_0\)-interval has \(O(h)\) lifts; and the fibre has
\(O(\kappa)\) sites.  Thus a fixed ordered residue pair modulo \(q\)
has available lift multiplicity

\[
 O(\kappa gh^2)=O(Lh/q),
\tag{177.P15}
\]

and a fixed inverse-product residue has \(q\) such ordered pairs and hence
\(O(Lh)=O(Lu_0/q)\) atoms.  The largest coefficient at conductor \(q\)
has size \(q/u_0=1/h\); positive recombination therefore returns scale
\(L\) per product residue and \(Lq\) over all residues.  Completion modulo
\(q\) may not silently replace the length-\(u\) interval by one primitive
period.  The kernel's raw count already pays these lifts.

For \(u_0>1\), \(a=\bar v n_0\) is a nonzero unit and

\[
 E_{u_0}(-a)=-E_{u_0}(a).
\tag{177.P16}
\]

The kernel correctly refuses to turn (177.P16) into an orientation
cancellation.  The evident interchange
\((u,v,s,w,+)\mapsto(v,u,w,s,-)\) replaces each selected divisor by its
complement.  In the odd--odd branch, a live squarefree divisor satisfies
\(d>\sqrt N\), so \(N/d<\sqrt N\) and is in the literal zero extension;
equality is impossible for squarefree \(N>1\).  In the even--even branch,
the complement is even and is not an allowed odd character-bearing
divisor.  The endpoint amplitudes and conjugations therefore do not pair.
Separating orientations by a modulus loses a possible new signed theorem,
while merely placing both in (177.P10) adds cross-orientation collisions
and proves no saving.

## 5. Literal-lower-mass and false-control audit

The kernel never promotes a capacity to physical mass:

- (177.K10) and (177.K11) are upper counts;
- (177.K31) is explicitly the available size of a coefficient-independent
  positive diagonal certificate, not a lower bound for the exact
  Parseval energy;
- (177.K32) is a conditional power ledger after granting one saving, not
  a claim about the literal sum;
- positive collision return is a method upper capacity; and
- (177.K33) is an anchor identity whose missing amplitude pairing is
  stated explicitly.

The usual coherent or dechirped arrays can show sharpness only for a
coefficient-uniform interface.  They need not satisfy the literal
selected/no-pair field, square-root phase, squarefree support, endpoints,
or profiles, and the kernel does not use them as K17a lower bounds.  A
literal signed bucket cancellation could make (177.P10) much smaller than
either positive certificate and remains unexcluded.

## 6. Downstream-owner and exponent quarantine

The implication boundary is correct:

| Object | Review status | Permitted effect |
|---|---|---|
| Exact alias folding and conductor mass | **GREEN proved** | Auxiliary algebra only |
| Complete \(q\le(\log X)^B\) Fourier packet | **GREEN proved** | Target-safe strict transform sector |
| Physical \(u/(u,n)\le(\log X)^B\) sector | **GREEN proved corollary** | Target-safe strict physical sector |
| High-conductor complement (177.K14) | **OPEN** | No bound beyond route capacities |
| Local high-conductor theorem (177.K34)/(177.K35) | **OPEN** | Would be sufficient, but is not proved |
| Complete K17a | **OPEN** | No closure from the strict packet alone |
| Complete residual scalar and full displayed \(t=1\) | **OPEN** | No implication |
| Other hard-TOP channels and complete hard TOP | **OPEN** | No implication |
| BAL, UNBAL, and M9--M2 | **OPEN** | No implication |
| Direct M1 parents or GAR, endpoint uniformity, and M9 | **OPEN** | No implication |
| Both bridges and the quarter theorem | **OPEN** | No implication |

No exponent ledger changes.  In particular, the inherited internal
\(1/3\) exponent, the repaired external benchmark
\(0.3144831759740614\ldots\), and the target \(1/4\) remain exactly where
they stood before this kernel.  The strict packet supplies no new global
exponent and no comparison between those values.

The phrase in the kernel that “every exponent remain open” should be read
only as “no exponent owner or exponent value is changed.”  Some numerical
ledger values are already recorded facts, so the latter wording is more
precise.

## 7. Required repairs and final recommendation

No mathematical correction is required.  Three documentary repairs are
recommended before this kernel is used as a template for a later analytic
attack:

1. After (177.K32), add the explicit lift ledger (177.P14)--(177.P15), so
   that “final conductor \(q\)” cannot be misread as licensing a single
   length-\(q\) completion.
2. After (177.K31), display the self-diagonal and bucket bounds
   (177.P11)--(177.P13), and retain the words “positive majorant” and
   “available capacity.”  This prevents the diagonal from being cited as
   literal lower mass.
3. Replace “every exponent remain open” by “this kernel changes no
   exponent owner or numerical exponent value,” preserving the inherited
   \(1/3\), \(0.3144831759740614\ldots\), and \(1/4\) ledger.

With those scope clarifications recorded in this review, the kernel is
mathematically sound for promotion of (177.K6), (177.K9), (177.K12), and
(177.K13), and for retention of (177.K29)--(177.K33) as a route-scoped
capacity/self-return obstruction with no implication edge.  Do not promote
(177.K34), (177.K35), complete K17a, any downstream owner, or any exponent
claim.

This review used no numerical experiment, web source, or external theorem,
and edited no file other than this assigned review.
