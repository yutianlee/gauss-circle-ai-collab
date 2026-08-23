# Round 117 hostile/source audit: determinant fibres and product return

Campaign: `gc-w7-16-actual-determinant-fibre-gate`
Task: `determinant_fibre_hostile_source_audit`
Role: hostile/source auditor
Starting graph SHA-256: `a27a89fd4e688cae719a28fec8f48dd74190bafb64d0345c590f1caadc2805d9`

## 1. Result: lemma or no-go result

The (M1) denominator and (M2) numerator character identities are
correct, but they do not by themselves produce a target-sized determinant
estimate.  The result of this audit is the following scoped no-go.

**Determinant-fibre half-shift self-return and norm-capacity no-go.**  On
the top minimax shell

\[
 B=D=Y^{1/2},\qquad A=L=Y^{1/6},\qquad W=Y^{7/16},
\]

the two-dimensional Legendre transform of the literal centre phase is
again a ratio phase.  The (M2) character shifts the dual (p)-frequency
by a half unit and the (M1) character shifts the dual (q)-frequency by
a half unit; neither shift removes the stationary lattice.  The dual
determinant strip has (B^2/W=Y^{9/16}) modes of stationary size
asymptotic to one.  Consequently every route that performs this transform
and then applies coefficient-blind Cauchy, Plancherel, or a large sieve has
the unavoidable diagonal capacity

\[
 {B^2\over DL}{B^2\over W}
 ={B^4\over DLW}=Y^{43/48},
\]

not the required (Y^{1/2}).  A second transform restores the primal
ratio phase, parity progression, and character.  This refutes the
two-dimensional transform followed by a norm as a standalone closing
mechanism.  It does **not** refute cancellation in the complete actual
coefficient sum.

Even granting the most optimistic one-variable gains before checking
coefficient regularity does not repair the deficit.  At the minimax shell,
perfect cancellation in the (M2) (p)-progression can save at most
(P_B=B/W=Y^{1/16}), while the formal (M1) (q)-B-process saves at most
(L=Y^{1/6}).  Granting both independently leaves

\[
 Y^{43/48-1/16-1/6}=Y^{2/3}.
\]

Thus the isolated high-pass and stationary transform cannot close even
under assumptions stronger than those presently proved for the literal
lift symbol.

The cellwise numerator-Poisson diagnostic is also an involutive return,
but only after an important correction.  For positive frequencies the
literal outer constants on both (M1) and (M2) become (2/(\pi i)),
and the nonzero product modes have coefficients

\[
 B_1(s;y)=\sum_{d\mid s}\chi _4(d)F_1(dy,d),
 \qquad
 B_2(s;y)=\sum_{rd=s}\chi _4(r)F_2(4dy,d).
\]

They both become (r_2(s)/4) only for positive (s) after deleting every
dyadic profile, Vaaler factor, hard endpoint, and scale restriction.  They
are not the same literal truncated coefficient.  (M1) also has an
unpaired (m=0) axial mode.  That axial mode is target-safe by character
Abel and fixed-profile variation, but the remaining endpoint packages
must be retained in the exact Poisson operator; they have not been proved
target-safe after being split off.  The product transform preserves the
full positive cluster form, not its one-sided off-diagonal part.  It
therefore estimates nothing and cannot be promoted as positivity of the
actual truncated coefficients.

No (Y^{1/2}) estimate, target-safe new hard subrange, quantified actual-
symbol saving, or improved pointwise exponent is proved.

## 2. Exact statement and hypotheses

Let (c\asymp Y) be real, (W=Y^{7/16}), and work in one fixed moving-
symbol stratum and one same-sign reduced-denominator shell

\[
 b,b'=b+q\asymp B,\qquad |a|,|a'|=|a+p|\asymp
 A:={LB\over D}.
\]

Both rays are primitive.  Put (C=c/\kappa_i) and

\[
 n=aq-bp,qquad 0<n<{\kappa_i b(b+q)\over W}.
\]

The shell ray energy and coefficient-blind neighbour capacity are

\[
 \mathcal E_B\ll_\varepsilon {B^2\over DL}Y^\varepsilon,
 \qquad
 \mathcal K_B\ll_\varepsilon {B^4\over DLW}Y^\varepsilon.
\tag{2.1}
\]

The exact interior phase in the increment variables is

\[
 f(p,q)=C\left({a\over b}-{a+p\over b+q}\right).
\tag{2.2}
\]

Writing (x=b+q), (y=a+p), its derivatives satisfy

\[
 f_p=-{C\over x},\qquad f_q={Cy\over x^2},\qquad
 \det \nabla^2f=-{C^2\over x^4}.
\tag{2.3}
\]

For the Fourier convention (e(f-up-vq)), stationarity gives

\[
 u=-{C\over x},\qquad v={Cy\over x^2},
\]

and the critical phase is exactly

\[
 f-up-vq={Ca\over b}+au+bv+{Cv\over u}.
\tag{2.4}
\]

Thus the nonlinear dual is the same ratio phase (Cv/u).  For (M2),
(p=2s) and the factor ((-1)^s) gives

\[
 u={j-1/2\over2},
\tag{2.5}
\]

whereas for (M1), (q=2r) and ((-1)^r) gives

\[
 v={j-1/2\over2}.
\tag{2.6}
\]

Equations (2.4)--(2.6) are exact interior algebra.  A second Legendre
transform is the inverse transformation and restores the original
progression.  On (B=\sqrt Y), (2.3) has constant-size determinant.  A
primal increment strip has area (B^2/W), its gradient image has the same
lattice area, and the two-dimensional stationary amplitude is
(|\det\nabla^2f|^{-1/2}\asymp B^2/Y\asymp1).  This proves the capacity
claim in Section 1.  Edges of the one-sided triangular strip are not error
terms in this statement: they must remain as boundary transforms, and
Fourier inversion returns them as well.

The exact strip counts include clipping and parity:

\[
 \#\{q:0<aq-bp<\kappa_i b(b+q)/W\}
 \ll 1+\min\left(B,{BD\over WL}\right),
\tag{2.7}
\]

\[
 \#\{p:0<aq-bp<\kappa_i b(b+q)/W\}
 \ll 1+\min\left(A,{B\over W}\right).
\tag{2.8}
\]

At the minimax shell the unclipped lengths are respectively
(Q_B=Y^{19/48}) and (P_B=Y^{1/16}).  The factors two from (q=2r)
or (p=2s), and (kappa_2=4), alter constants only.  Statements of
(Q_B) and (P_B) without the minima are not uniform over all of
(\mathscr H_{95}).

The one-variable ledger can also be stated uniformly on the top shell
(B=D=Y^\delta), (L=Y^\ell).  The coefficient-blind exponent is
(3\delta-\ell-7/16).  Optimistically granting the full (p)-length
saving when it is nontrivial still leaves exponent (2\delta-\ell>1/2).
Optimistically granting the stationary (q)-B-process saving

\[
 D\sqrt{D\over YL}
 =Y^{3\delta/2-1/2-\ell/2}
\]

leaves exponent (3\delta/2-\ell/2+1/16>17/32) throughout the hard
region where that saving is positive; when it is not positive, the
original hard capacity remains.  If both optimistic gains are positive,
the survivor exponent is

\[
 {1\over2}+{\delta-\ell\over2}\ge {5\over8}.
\tag{2.9}
\]

Hence neither mechanism, separately or formally combined, creates a
target-safe part of the previously open hard region.

## 3. Proof or derivation

**Literal character and determinant algebra.**  Since nonzero (M1)
coefficients have (b,b') odd, (q=2r), and

\[
 \chi_4(b)\chi_4(b+2r)=(-1)^r.
\]

For same-sign (M2), (a,a') are odd, (p=2s), and the identity remains
valid for either common sign:

\[
 \chi_4(|a|)\chi_4(|a+2s|)=(-1)^s.
\]

Also

\[
 {cn\over\kappa_i b(b+q)}
 ={c\over\kappa_i}\left({a\over b}-{a+p\over b+q}\right).
\]

This proves the algebra used in (2.2), including the (M2) factor four.
It does not give regularity of the remaining lift transforms.

**Congruence and multiplicity.**  For a fixed primitive ((a,b)) and a
fixed (n),

\[
 aq\equiv n\pmod b
\]

has one residue class for (q) modulo (b).  The parity restriction
raises the modulus to at most (2b), so a (q)-range of length (O(B))
contains (O(1)) representatives.  This recovers the degree
(O(1+B^2/W)) without a hidden gcd power.  In the transposed
parameterization, (g=(b,b')) must divide (n), and for fixed
(b,b',n) the numerator solutions form a progression with

\[
 O\left(1+{Ag\over B}\right)
\]

members.  The compensating restriction (g\mid n), the second
primitivity condition, and the parity progression must all be present
before Cauchy.  The proposed one-variable sums do not yet include this
Möbius/gcd ledger, so their geometric bounds are not literal estimates.

**One-variable mechanisms.**  At fixed (q), (2.2) is linear in (p),
and the triangular determinant weight is affine in (p).  If the complete
coefficient along that fibre had bounded variation, Abel would give a
geometric factor.  Such variation is not supplied by Round 95: changing
primitivity, lift range, sampled endpoints, or the reduced ray can cause
jumps in (A_i(a+p,b+q)).  Möbius inversion may make the progression
legal, but no estimate charging its divisor pieces is proved.

At fixed (p),

\[
 f_{qq}=-{2C(a+p)\over(b+q)^3}.
\]

At the minimax shell this is of order (L^{-2}).  The (q)-interval has
length (Q_B), so its derivative image has (P_B) half-shifted modes,
each of stationary size (L).  This is the formal saving (Q_B/(P_BL)=L)
used in Section 2.  It is an optimistic smooth-amplitude ledger, not a
bound for the actual lift symbol.  Even granting it, the target fails.

**Two-dimensional return and the large-sieve diagonal.**  Direct
differentiation proves (2.3), and substituting the stationary relations
proves (2.4).  At the self-dual top shell, the gradient-map Jacobian and
stationary amplitude show that the number and total (L^2) capacity of
dual modes equal those of the primal determinant strip.  The character
only translates one dual lattice as in (2.5) or (2.6).  A Cauchy or large-
sieve step after the transform therefore contains the positive diagonal

\[
 \mathcal E_B\,{B^2\over W},
\]

which is (2.1).  Separating the two residue sectors before that norm is
especially fatal: (q\equiv0\pmod4) for (M1), or (p\equiv0\pmod4)
for (M2), has character product (+1), while the complementary allowed
sector has product (-1).  Both have comparable lattice density.  No
identity for the actual lift transforms pairs their contributions.  A
norm taken sectorwise erases the only possible cancellation.

**Exact scope of the cellwise product diagnostic.**  On a positive (M1)
cell, the literal coefficient is

\[
 {2\over\pi i}\sum_d\chi_4(d)
 \sum_{h/d\in I}{F_1(h,d)\over h}e(ch/d).
\]

Distributional Poisson in (h), with every hard endpoint interpreted by
its prescribed star, and (h=dy), gives

\[
 {2\over\pi i}\sum_{d,m}\chi_4(d)
 \int_I {F_1(dy,d)\over y}e((c-md)y)\,dy.
\tag{3.1}
\]

For (M2), use

\[
 \chi_4(h)={e(h/4)-e(-h/4)\over2i}.
\]

The branches (4m-1) and (4m+1) combine with coefficient
(-\chi_4(r)); the original (M2) constant contributes the other minus.
After (h=4dy), the result is

\[
 {2\over\pi i}\sum_d\sum_{r\ {\rm odd}}\chi_4(r)
 \int_I {F_2(4dy,d)\over y}e((c-rd)y)\,dy.
\tag{3.2}
\]

Thus the constants in (3.1) and (3.2) really agree.  For (s\ne0), their
product regroupings are the (B_1,B_2) displayed in Section 1.  The
identity (B_1=B_2=r_2(s)/4) holds only for an unweighted complete
positive divisor sum.  Literal truncation distinguishes the divisor
orientation; (F_1(dy,d)) and (F_2(4dy,d)) are different, and away from
the top self-dual shell the complementary divisor has scale (Y/D), not
(D).  Negative product modes also have different sign symmetry.  Hence
the nonnegative completed coefficient is a control model, not the actual
coefficient.

The (M1) term (m=0) has no (M2) partner.  It is nevertheless owned.
For fixed (y), the literal fixed-stratum profiles give

\[
 \operatorname{Var}_{d}\,F_1(dy,d)+\|F_1(dy,d)\|_\infty\ll1,
\]

including the hard-top jump and star.  Character Abel therefore gives
(sum_d\chi_4(d)F_1(dy,d)\ll1).  Since (y\asymp L/D), one cell
contributes (O(D/(LW))), and all cells meeting the band contribute square
mass

\[
 \ll \left(1+{WL\over D}\right){D^2\over L^2W^2}
 \ll {D^2\over L^2W^2}+{D\over LW}ll Y^{1/8}.
\tag{3.3}
\]

This is far below (Y^{1/2}).  The ownership of (3.3) does not license
discarding the other hard endpoint transforms.  Cell endpoints are
irrelevant for almost every random shift, but frequency-height atoms,
profile jumps, and prescribed stars must either remain inside the exact
distributional Poisson identity or receive a separate cluster estimate.
No such separate target estimate is in the selected context.

Finally, (3.1)--(3.2) transform the whole cell amplitude before squaring.
Fourier inversion returns that amplitude.  The full random-cell sum is a
positive norm, but the one-sided determinant correlation is obtained only
after subtracting the equal-ray diagonal and orienting the off-diagonal.
That operation is not preserved as a positive product sub-sum.  The
product return is therefore an exact explanation of involution, not a
bound for the open survivor.

## 4. First doubtful or unproved step

The first unproved analytic step remains a signed inequality for the
complete literal determinant correlation.  Neither proposed
one-dimensional route has established fibrewise variation after the
second primitivity condition, lift-range changes, parity congruences,
triangular boundary, and stars are restored.  The exact two-dimensional
transform does not help after a norm because its diagonal is already
(Y^{43/48}).

For the product route, the first literal seam is not the (M1) (m=0)
mode; (3.3) owns it.  The first seam is an exact endpoint/profile Poisson
formula that keeps, rather than labels as a negligible package, all hard
height atoms and stars in the random-cell (L^2) norm.  Even after that
identity is written, a new noninvertible theorem would still be needed for
the (y)-dependent truncated divisor coefficients (B_i(s;y)).  No
selected-context theorem estimates them at a prescribed real centre.

## 5. Control tests and outcomes

| Control | Test | Outcome |
|---|---|---|
| Literal reduced ray and equal-lift diagonal | Compare the shell energy with the accepted complete ray coefficient, not the raw ((h,d)) diagonal. | **Pass.** The exact input is (mathcal E_B\ll B^2/(DL)); all lift cross terms remain aggregated. |
| (M1/M2) character placement and factor four | Substitute (q=2r), (p=2s) and retain (kappa_1=1,kappa_2=4). | **Pass.** The half-shifts are in (v) for (M1) and (u) for (M2); the factor four is not relabelled away. |
| Increment determinant and one-sided orientation | Expand (ab'-a'b) and the centre phase, with (n>0). | **Pass.** (n=aq-bp) and (2.2) are exact. The one-sided edge must remain under every transform. |
| Character high-pass progressions | Inspect residue sectors and the transformed lattice. | **Pass algebraically, fail as an estimate.** The shifts are exact, but stationary half-lattice modes remain and sectorwise norms erase their cancellation. |
| Determinant strip widths and boundary | Solve the inequalities at fixed (p) and fixed (q), including support clipping. | **Pass after correction.** The uniform bounds are (2.7)--(2.8), not the unclipped (Q_B,P_B) on every hard block. The triangular edge is not a negligible error. |
| Centre phase and stationary/geometric norm | Compute the Hessian, Legendre phase, dual count, and one-variable ledgers. | **Fail for target closure.** The exact 2D phase self-returns; even optimistic one-variable savings leave at least (Y^{5/8}) in the hard region and (Y^{2/3}) at minimax. |
| Gcd congruence and multiplicity | Parameterize first from a primitive base ray and then by fixed (b,b',n). | **Pass as a counting chart; fail in the proposed norm.** The base-ray count has no hidden power, but the transformed proposals have not charged (g\mid n), Möbius pieces, and parity before Cauchy. |
| Capacity before and after each norm | Compare (mathcal E_BB^2/W) with (Y^{1/2}). | **Fail.** The large-sieve/Plancherel diagonal is (Y^{43/48}); the norm cannot see the required (Y^{19/48}) actual-symbol gain. |
| Actual symbol versus phase-conjugated coefficients | Ask which step uses the complete lift transform rather than only its envelope and reduced character. | **Fail.** Every proved transform/capacity statement is coefficient-blind. No saving unavailable to the Round-95 adversary is obtained. |
| Cellwise product return | Derive both Poisson orientations with constants, zero mode, signs, profiles, and second inversion. | **Pass only as a qualified identity.** Constants agree and (m=0) is safe, but (B_1\ne B_2) literally; (r_2/4) is only the unweighted completion, and endpoints must stay inside the operator. |
| Moving strata, bottom/R5, and cross-block owners | Track what happens outside one fixed block. | **Pass for inherited ownership, fail for a new transformed assembly.** Bottom/R5 remain target-safe and fixed strata assemble polylogarithmically; the product dual can move (D) to (Y/D), so no new block theorem follows. |
| External theorem hypothesis fit | Match the literal sum to a primary theorem before substituting parameters. | **Fail.** No exact separable inverse-modular Kloosterman-fraction form is obtained; real (c), the variable triangular top, two-dimensional (A_i(a,b)), all (n), and hard endpoints remain. |
| Real (Y) and endpoint uniformity | Permit arbitrary real (c\asymp Y) and literal floors/stars. | **Fail for any imported modular theorem.** Rounding (c) is not harmless. The internal phase identity is uniform, but no endpoint-uniform target estimate is proved. |
| Linear cluster versus local mass versus pointwise exponent | Apply the accepted persistence bridge only after all fixed blocks are bounded. | **Pass as scope.** A complete (Y^{1/2}) cluster theorem would give local mass (Y^{15/16}) and exponent (5/16); this report supplies no such theorem. |
| Downstream scope | Compare the graded kernel with (M9)-(M1), (M9)-(M2), endpoint uniformity, and (GC)-target. | **Pass.** There is no implication to any of them and no global exponent change. |

All controls are analytic.  No numerical experiment was used.

## 6. Dependencies and exact artifacts used

The audit used the following assigned artifacts completely:

* `protocol.md`;
* `state/proof_obligations.yml`, whose full JSON graph was parsed and whose
  relevant exact nodes were extracted;
* `state/active_campaign.yml`;
* `strategy/conductor_0821_full_proof_strategy.md`;
* `rounds/codex-managed/gc-prescribed-point-local-moment-bridge/synthesis.md`;
* `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/synthesis.md`;
* `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/reports/actual_rational_cluster_attack.md`;
* `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/reviews/conductor_round95_cluster_adjudication.md`;
* `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/derivation_packet.md`;
* `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/candidates/conductor_character_highpass_fibre.md`;
* the conductor-added diagnostic
  `rounds/codex-managed/gc-w7-16-actual-determinant-fibre-gate/candidates/conductor_cellwise_product_return.md`.

Two primary Kloosterman-fraction sources were checked at the first theorem-
fit interface:

* Bettin--Chandee, *Trilinear forms with Kloosterman fractions*,
  <https://arxiv.org/abs/1502.00769>.  Its Theorem 1 concerns separable
  dyadic coefficients in
  \(e(\vartheta a\overline m/n)\); its determinant corollary fixes one
  nonzero determinant and requires smooth separated weights.  The Round-117
  kernel has a real reciprocal centre phase, a denominator-dependent
  one-sided triangular top, coupled two-variable coefficients, and all
  determinants up to (B^2/W).  Applying the corollary determinant by
  determinant would additionally sum its error over that whole range.
  The hypotheses therefore fail before exponent substitution.
* Dong--Robles--Zeindler, *Bilinear forms with Kloosterman fractions and
  applications*, <https://arxiv.org/abs/2601.00292>.  The stated source
  interface is again a bilinear form with separable one-variable
  coefficients and a modular inverse phase.  No exact reduction of the
  literal determinant kernel or the product wave to that form was found.
  Its bound is not imported.

The accepted Popov local-moment source remains only the aggregate ceiling

\[
 Q(Y,W)\ll W\sqrt Y+Y(\log Y)^2.
\]

It does not estimate a fixed literal product wave or fixed-block positive
cluster, and its additive term still yields the one-third persistence
ceiling.  No primary source found in this audit improves the prescribed-
centre truncated product correlation.

No Round-117 sibling report, computation, or unlisted proof candidate was
used.

## 7. Recommended state effect

**Promote after conductor seam review** the exact ratio-phase Legendre
identity (2.3)--(2.6), the top-shell dual-capacity calculation, and the
scoped no-go: a one- or two-dimensional character-shift transform followed
by coefficient-blind Cauchy/Plancherel/large sieve cannot close the hard
determinant correlation.  Also promote the corrected strip bounds
(2.7)--(2.8) and the target-safe (M1) zero-product mode (3.3).

**Retain as a qualified diagnostic, not as an estimate,** the cellwise
product return (3.1)--(3.2).  Record that its two complete unweighted
positive-divisor coefficients equal (r_2/4), but its literal truncated
coefficients differ and its hard endpoint transforms cannot be discarded.
The second Poisson transform is involutive and preserves only the full
cell norm, not the one-sided off-diagonal survivor.

**Reject as standalone closing mechanisms** fibrewise geometric summation
without a proved lift-symbol BV/Möbius ledger, the isolated (q)-B-process,
the full 2D B-process followed by a norm, residue-sector absolute values,
positivity of the completed (r_2/4) model, and direct transfer of either
Kloosterman-fraction source.

**Retain open** `GC-W7-16-actual-reduced-determinant-correlation`.  A future
attempt must supply a genuinely joint signed inequality for the actual
two-dimensional lift symbol, before any norm creates the (Y^{43/48})
diagonal.  The high-pass/determinant transform and the completed product
wave are now exhausted as standalone explanations.

**No change** is licensed for
`GC-nonsubcoherent-actual-cluster-local-moment`, `M9-M1`, `M9-M2`, `M9`,
endpoint uniformity, or `GC-target`.  The internal certified exponent
remains (1/3), and the separately audited external exponent remains
(0.3144831759740614\ldots).
