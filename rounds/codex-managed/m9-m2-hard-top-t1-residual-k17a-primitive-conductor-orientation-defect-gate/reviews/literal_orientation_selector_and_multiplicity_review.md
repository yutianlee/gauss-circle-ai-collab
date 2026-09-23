# Round 179 literal orientation, selector, and multiplicity seam review

## 1. Result

**Verdict: GREEN.**

The formalized kernel
`m9_m2_hard_top_t1_residual_k17a_primitive_conductor_parity_self_return.md`
matches the two accepted predecessor kernels and all three Round 179
reports at every assigned literal seam:

- the plus/minus amplitudes retain the complete zero-extended literal
  coefficient and remove only the exact-conductor phase;
- every occupied bucket is a unit bucket;
- the fixed-stratum, residue-pair, and inverse-product bucket
  multiplicities retain all physical `v`, `n_0`, gcd, and fibre lifts;
- the fixed-modulus reflection is an involution only of the unrestricted
  Diophantine lattices, not of the complete live orientation domains;
- the endpoint-preserving exchange changes the local outer row and replaces
  both selected divisors by complementary factors outside literal support;
- the selected/no-pair field, squarefree masks, profiles, endpoints, and
  zero extension supply no unproved conjugacy; and
- the first open estimate is exactly the complete centered defect
  (179.K19), which self-returns by (179.K12) to the original literal
  orientation block minus the already-safe low-conductor packet.

No mathematical repair is required.  There is one harmless wording point:
the last paragraph of the proof says “the `q` unit buckets”; the exact
number is `phi(q)`.  In the stated prime and prime-square controls
`phi(q) asymp q`, so the claimed `asymp Lq` capacity and every formal
statement remain correct.  If the kernel is edited later, “the
`phi(q) asymp q` unit buckets in these controls” would be more literal.

The first unresolved issue is not a defect in the kernel.  It is the
analytic inequality (179.K19): no accepted relation controls the sign-odd
literal orientation difference after all selectors, endpoints, phases,
and lifts are restored.

## 2. Exact statement and hypotheses reviewed

The review retains the accepted Round-176/177 packet with

\[
g=(u,n),\qquad u=gu_0,\qquad n=gn_0,\qquad(n_0,u_0)=1,
\tag{179.R1}
\]

odd `u,u_0`, `(u,v)=1`, both opposing orientations, and the complete
literal fields inside

\[
A_z^\pm=\Lambda_z^\pm e(\Psi_z^\pm+t_z/2).
\tag{179.R2}
\]

For each atom the unreduced primitive residue is

\[
\beta_z=\bar v n_0\pmod {u_0},
\tag{179.R3}
\]

and its exact-conductor bucket at `q | u_0` is obtained only by reduction
of (179.R3) modulo `q`.  The review checks the formalized definitions
(179.K3)--(179.K4) against the literal amplitudes (176.K18), (176.K20),
the two-orientation identity (176.K21), and the primitive-alias block
(177.K15)--(177.K17).

For the multiplicity seam put

\[
h=u_0/q,\qquad u=ghq.
\tag{179.R4}
\]

The exact accepted upper ledgers to be preserved are:

\[
\#\{z\text{ at fixed }(\kappa,u,u_0)\}\ll u_0L,
\tag{179.R5}
\]

\[
\#\{z\text{ over one ordered residue pair modulo }q\}
\ll \kappa gh^2\asymp Lh/q,
\tag{179.R6}
\]

and, after the `phi(q)` ordered unit pairs producing one inverse product,

\[
\#\{z:\bar v n_0\equiv b\pmod q\}
\ll Lu_0/q.
\tag{179.R7}
\]

The orientation seams reviewed are the fixed-modulus reflection

\[
I(s,w)=(u-s,v-w)
\tag{179.R8}
\]

and the endpoint-preserving exchange

\[
J(u,v,s,w,+)=(v,u,w,s,-).
\tag{179.R9}
\]

No assertion is reviewed or accepted unless it preserves the literal
displacement domain, outer row, primitive modulus, endpoint products,
selected divisor, parity branch, squarefree and coprimality masks,
profiles, hard values, endpoint conjugations, phases, and zero extension.

## 3. Proof or derivation

### 3.1 Literal amplitudes and unit bucket support

In the accepted cross-gcd kernel, the plus orientation is

\[
d=\kappa u,\quad d'=\kappa u+2s,\quad
m'=\kappa v,\quad m=\kappa v+2w,\quad sv-wu=n,
\tag{179.R10}
\]

and the minus orientation is

\[
d'=\kappa u,\quad d=\kappa u+2s,\quad
m=\kappa v,\quad m'=\kappa v+2w,\quad uw-sv=n.
\tag{179.R11}
\]

The factors `Lambda^plus` and `Lambda^minus` in (176.K18) and
(176.K20) contain the Fejer weight, determinant and original-gcd gates,
positive-displacement indicators, both endpoint coefficients, and every
other literal field by zero extension.  The formalized kernel's
`A_z^plus` and `A_z^minus` in (179.K3) retain exactly these factors and
the square-root and half-frequency phases.  Only the conductor phase
`e(plus_or_minus a beta_z/q)` is removed before bucketing.  Thus (179.K3)
does not smooth, periodicize, average, or discard a literal field.

Since `(u,v)=1` and `u_0 | u`, `v` is a unit modulo `u_0`.  Since
`(n_0,u_0)=1`, their product `beta_z=bar(v)n_0` lies in `U(u_0)` and its
reduction lies in `U(q)` for every `q | u_0`.  The bucket definition
(179.K4) is therefore exact.  In particular, the sign law for
`K_q(b)` is never applied to a nonunit residue.

### 3.2 Physical lifts and bucket capacity

The accepted support has `u,v asymp L/kappa`, `n_0=O(u_0)`, and
`O(kappa)` fibre sites.  This gives (179.R5).  More finely, a fixed
`v` residue modulo `q` has `O(gh)` lifts across its physical interval,
a fixed `n_0` residue has `O(h)` lifts, and the fibre has `O(kappa)`
sites.  Hence one ordered residue pair has the multiplicity (179.R6).

For fixed `b=bar(v)n_0 mod q`, choosing a unit residue for `v` uniquely
determines the residue of `n_0`; there are `phi(q)` such ordered pairs.
Multiplying (179.R6) by `phi(q) <= q` gives (179.R7), and summing (179.R7)
over the `phi(q)` occupied buckets is still bounded by the complete
`O(u_0L)` mass (179.R5).  Thus the formalized proof's bucket shadow
`O(Lu_0/q)` and total mass are compatible and do not erase the `g`, `h`,
or `kappa` repetitions.

The prime and prime-square adversarial controls in (179.K15)--(179.K16)
may consequently place `O(Lu_0/q)` aligned artificial atoms in each unit
bucket.  Since `phi(p) asymp p` and `phi(p^2) asymp p^2`, their centered
defects have size `asymp Lq`.  This is a valid coefficient-uniform
capacity test.  The formalized kernel correctly states that these arrays
are not realizations of the literal selector and phase field and hence are
not literal lower mass.

The blind report's stronger single-bucket operator-norm example used only
the isolated total-mass hypotheses and can put the complete mass in one
bucket.  That is valid in its statement-only model but does not respect
the later-unmasked literal per-bucket bound (179.R7).  The formalized
kernel does not import that stronger claim; it uses the distributed
prime/prime-square construction, so this seam is GREEN.

### 3.3 Fixed-modulus reflection

Substitution into (179.R10)--(179.R11) gives

\[
u(v-w)-(u-s)v=sv-wu=n,
\tag{179.R12}
\]

so (179.R8) is an involution between the unrestricted plus and minus
Diophantine lattices.  It keeps `u,v,n,g,u_0`, every divisor `q | u_0`,
and the residue `beta_z` fixed.  If the plus fibre is
`(s_t,w_t)=(s_0+ut,w_0+vt)`, the minus canonical fibre satisfies

\[
s_0^-=u-s_0,\qquad w_0^-=v-w_0,\qquad
I(s_t,w_t)=(s^-_{-t},w^-_{-t}).
\tag{179.R13}
\]

The half-frequency is preserved because
`e((-t)/2)=e(t/2)=(-1)^t`.  This algebra alone does not give a literal
pairing.  A plus live point has `s,w >= 1`, while its image is live only
when

\[
1\le s\le u-1,\qquad1\le w\le v-1.
\tag{179.R14}
\]

A primitive fibre advances by `(u,v)`, so at most one of its sites can
lie in (179.R14).  The complete positive domain is therefore not mapped
bijectively.

Even on this intersection, endpoints do not agree.  With

\[
x=\kappa u(\kappa v+2w),\qquad r=2\kappa n,
\qquad C=2\kappa^2uv+2\kappa uv,
\tag{179.R15}
\]

the plus pair `(x,x+r)` is sent to

\[
(C-x-r,C-x).
\tag{179.R16}
\]

The two square-root differences coincide only on the exceptional midpoint
`2x+r=C`; no accepted selector, squarefree, profile, hard-endpoint, or
coefficient identity is invariant under this reflection.  The statement
in (179.K17) is therefore exact and appropriately negative: it asserts no
conjugacy on the small domain intersection.

### 3.4 Endpoint-preserving exchange and zero extension

For (179.R9), put
`u'=v, v'=u, s'=w, w'=s`.  Then

\[
u'w'-s'v'=vs-wu=n,
\tag{179.R17}
\]

and the minus lower and upper products are exactly the plus lower and
upper products:

\[
\kappa v'(\kappa u'+2s')
=\kappa u(\kappa v+2w),
\tag{179.R18}
\]

\[
\kappa u'(\kappa v'+2w')
=\kappa v(\kappa u+2s).
\tag{179.R19}
\]

Thus the square-root phase is preserved.  However, the map changes the
fixed local row from `u` to `v`, changes `u_0=u/(u,n)` to
`v/(v,n)`, and generally changes `q` and the bucket.  A fixed-row point
would require `u=v`; coprimality then forces `u=v=1`, whose only conductor
is the already-low `q=1`.  Hence (179.R9) is not a high-conductor
involution inside (179.K19).

At the lower endpoint, the plus selected divisor `kappa u` is replaced by
its complement `kappa v+2w`.  At the upper endpoint, `kappa u+2s` is
replaced by its complement `kappa v`.  In the odd branch, a live selected
divisor lies in the upper near-square window, while its complementary
factor is strictly below the square root: equality would make a
squarefree endpoint greater than one a square.  In the even branch, the
complement is even and is not an admissible character-bearing divisor.
The required zero extension therefore sends the exchanged coefficient to
zero.  Equations (179.K18) and its stated selector failure are exact.

### 3.5 Reconciliation with the Round 179 reports

The discovery report proves the projector, the exact `q/u_0`
normalization, target-safe high trace, product-preserving exchange failure,
physical lifts, and prime bucket capacity.  Its asymmetric trace/defect
split is algebraically equivalent to the centered split (179.K8).

The hostile report independently proves the centered all-conductor
identity, `q=1` boundary, trace cancellation, exact self-return, the
fixed-modulus reflection failure, the endpoint-preserving complement
failure, the lift ledger, and the distributed prime/prime-square false
controls.  These statements agree term for term with (179.K7)--(179.K18).

The blind report independently proves the finite projector and canonical
centered trace/defect split.  Its abstract operator norm is correctly
quarantined from literal coefficients.  As noted in Section 3.2, its
single-bucket extremizer belongs only to its statement-only mass model;
the formalized kernel uses the literal per-bucket shadow after unmasking.

Finally, (179.K10)--(179.K13) show that centered conductor summation
reconstructs the original literal orientation block, with `q=1` essential
to trace cancellation.  Therefore (179.K19) is not a new contracted norm:
it is the original unresolved signed block minus a proved low-conductor
piece.  All reports and the formalized kernel agree on this no-go boundary
and do not convert it into literal lower mass.

## 4. First doubtful or unproved step

There is no doubtful or unproved step in the reviewed literal definitions,
unit support, multiplicities, orientation-map calculations, selector
failure, zero extension, or self-return identity.

The first open step is exactly (179.K19):

\[
\left|
\sum_{u_0\mid u}\sum_{q\mid u_0,\ q>Q_B}
\frac q{u_0}\sum_{b\in U(q)}K_q^\circ(b)
\bigl(B^+_{q,b}-B^-_{q,b}\bigr)
\right|
\stackrel{?}{\ll}LX^\varepsilon.
\tag{179.R20}
\]

No accepted result proves that the literal orientation difference is
small, sign-even, conjugate, selector-balanced, or orthogonal to
`K_q^circ`.  The fixed-modulus reflection fails before it can supply such
a relation, and the endpoint-preserving exchange is killed by the literal
selector and zero extension.  By (179.K12), (179.R20) is exactly the
original orientation block minus the safe low centered packet.

The review therefore does not promote (179.R20), reject (177.K34), or
claim literal lower mass.  It identifies no kernel repair before this
analytic boundary.

## 5. Controls and outcomes

| Control | Outcome |
|---|---|
| literal plus/minus definitions | **GREEN.** (179.K3)--(179.K4) retain the complete amplitudes from (176.K18), (176.K20), and remove only the conductor phase. |
| unit bucket support | **GREEN.** `(u,v)=1` and `(n_0,u_0)=1` imply `beta_z in U(u_0)` and hence in `U(q)`. |
| fixed-stratum atom count | **GREEN.** The kernel uses the accepted `O(u_0L)` complete two-orientation capacity. |
| ordered residue-pair lifts | **GREEN.** `O(gh)` `v`-lifts, `O(h)` `n_0`-lifts, and `O(kappa)` fibre sites give `O(kappa gh^2)=O(Lh/q)`. |
| inverse-product bucket multiplicity | **GREEN.** `phi(q)` ordered unit pairs give the accepted cap `O(Lu_0/q)` per bucket. |
| artificial bucket capacity | **GREEN / diagnostic only.** Distributed prime and prime-square arrays respect the literal count shadow and attain `asymp Lq`; they are not actual coefficients or lower mass. |
| fixed-modulus reflection | **GREEN obstruction.** It maps the unrestricted lattices but not the complete live domain; at most one fibre site is domain-eligible. |
| reflected endpoint pair | **GREEN obstruction.** `(x,x+r)` maps to `(C-x-r,C-x)`; no literal phase or coefficient conjugacy follows. |
| endpoint-preserving exchange | **GREEN obstruction.** It changes the fixed row, primitive modulus, conductor, and bucket; the only fixed-row case has `q=1`. |
| complementary-divisor support | **GREEN obstruction.** Complements are below the upper window in the odd branch and even in the even branch. |
| selector and zero extension | **GREEN.** The exchange maps a live selected atom to a zero-extended coefficient, not to a live opposite orientation. |
| all-conductor self-return | **GREEN.** The centered defect reconstructs the original block; the high part is original minus safe low conductor. |
| blind-report unmasking | **GREEN repair already embodied by kernel.** The formalized false control uses the literal per-bucket shadow rather than importing the blind single-bucket extremizer. |
| first open defect | **OPEN, correctly quarantined.** (179.K19) has no proved selector- and phase-aware contraction. |
| owner and exponent scope | **GREEN.** No other K17a route, hard-TOP channel, parent, bridge, quarter theorem, or exponent is changed. |

No numerical experiment, web source, or external theorem was used.

## 6. Dependencies and exact artifacts used

This review used only the project instructions, authoritative campaign
context already read for Round 179, the formalized kernel, the two accepted
predecessor kernels, and all Round 179 reports:

1. `AGENTS.md`;
2. `protocol.md`;
3. `state/proof_obligations.yml`;
4. `state/active_campaign.yml`;
5. `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_conductor_parity_self_return.md`;
6. `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_reduction.md`;
7. `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_primitive_alias_conductor_reduction.md`;
8. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/reports/literal_primitive_conductor_parity_attack.md`;
9. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/reports/hostile_orientation_defect_capacity_audit.md`; and
10. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-primitive-conductor-orientation-defect-gate/reports/blind_primitive_kernel_rederivation.md`.

No unlisted research artifact was used.  No graph, proof draft, kernel,
strategy, validation artifact, report, synthesis, control, or sibling
review was edited.

## 7. Recommended state effect

**GREEN.** After the remaining independent normalization and
power/owner seams are green, accept the formalized kernel's literal
orientation, selector, multiplicity, and zero-extension statements as
proved internal evidence.

Retain (179.K19), (177.K34), complete K17a, and every downstream owner as
open.  Record only the scoped
`primitive_conductor_orientation_defect_capacity_or_self_return_no_go`:
centered conductor parity self-returns to the original literal block,
the fixed-modulus reflection fails live-domain and endpoint preservation,
and the endpoint-preserving exchange fails fixed-row and selector support.

Do not promote the artificial bucket controls to literal lower mass, do
not infer a strict defect sector, and do not change any bridge, quarter
theorem, internal exponent, external benchmark, or target exponent.  This
review makes no graph edit.
