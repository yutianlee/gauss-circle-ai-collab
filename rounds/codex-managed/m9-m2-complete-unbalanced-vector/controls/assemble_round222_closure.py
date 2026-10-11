"""Prepare conductor closure artifacts only after final reports and reviews exist.

This does not close the round, apply a State Patch, or mutate shared state.
"""
import hashlib, json, re
from pathlib import Path

base = Path('rounds/codex-managed/m9-m2-complete-unbalanced-vector')
assert not (base/'controls/artifact_hashes.json').exists()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def put(p,s): Path(p).write_text(s,encoding='utf-8',newline='\n')
def write(p,o): put(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
joint=base/'reports/joint_cross_modulus_attack.md'
product=base/'reports/actual_product_phase_attack.md'
finite=base/'reports/blind_cross_modulus.md'
control=base/'controls/conductor_weighted_period_control.md'
review_joint=base/'reviews/independent_cross_modulus_review.md'
review_product=base/'reviews/independent_product_phase_review.md'
review_weighted=base/'reviews/independent_weighted_period_review.md'
review_finite=base/'reviews/conductor_finite_cross_modulus_review.md'
for p,claim in [(review_joint,joint),(review_product,product),(review_weighted,control),(review_finite,finite)]:
    s=p.read_text(encoding='utf-8')
    assert 'GREEN' in s and sha(claim) in s
    assert all(re.search(rf'^#{{1,2}} {i}\.',s,re.M) for i in range(1,8))
for p in [joint,product,finite,control]:
    b=p.read_bytes()
    assert not re.search(rb'\r(?!\n)',b)
    assert not any(x<32 and x not in (9,10,13) for x in b)
    assert all(re.search(rf'^#{{1,2}} {i}\.',b.decode(),re.M) for i in range(1,8))

owner=r'''# Round222 conductor complete-owner and power review

## 1. Result

GREEN for scoped finite and failed-certificate evidence only. Neither complete
UNBAL nor a complete moment estimate improves. The graph and proof draft must
remain unchanged. The joint-frequency argument has a fully paid but weak upper
bound; only the rectangle argument has the proved actual-weight certificate
lower bound described below. These are distinct conclusions.

## 2. Exact hypotheses and owner

For every real X, the frozen actual smooth target is
\[
T=\sum_{h,k}\chi_4(h)a(h,k)e(\sqrt{Xhk})
 \ll_\epsilon (LK)^{3/4}X^\epsilon,
\qquad K=XL/D^2,\quad K/L>16.
\]
The exact smooth physical factor is
\(-e(1/8)X^{1/4}(LK)^{-3/4}/(2\pi)\), with an \(O_W(1)\)
error. The actual taper and slanted profile remain in a. The hard top is a
different owner. Accepted160's reciprocal vector and flat envelope keep their
strict flat scope; neither is an automatic identity for every companion.

## 3. Independent algebra and complete cost audit

Opening the weighted Kloosterman row gives frequency
\(t=x-\bar j\pmod n\), not the bare primitive frequency x. Its constant
coefficient is \(U_{g,n}/n\). Zeroing the h=0 residue subtracts
\(F_{g,n}(0)/n\) from every Fourier coefficient. For moduli n,m, the shared
frequencies are indexed by \(0\le v<(n,m)\); for coprime moduli the common-period
correlation after deletion is exactly
\((U_{g,n}-F_{g,n}(0))\overline{(U_{g',m}-F_{g',m}(0))}\).
Thus neither bare-row orthogonality nor zero-column deletion estimates the
actual weighted mean. This agrees with the independently reviewed conductor
control and needs no first-argument coprimality assumption.

For the finite physical window, every frequency p/q shared by n multiples of q
has grouped coefficient bounded by
\[
X^\epsilon\sum_{g\ll K}g^{-1}
 \sum_{n\asymp R/g,\ q\mid n}n^{-1}
 \ll X^\epsilon(1+\log(2K))/q,\qquad R=X/D.
\]
The sum of coefficient squares costs only logarithms after summing
\(\varphi(q)/q^2\). Circular spacing is at least a constant times \(R^{-2}\);
the absolute finite Gram row sum is \(O(H+R^2\log R)\), with H comparable to R.
Every prefix mask admits the SAME Fourier envelope
\(O(\min(1,1/\min(r,2H+1-r)))\), independent of its endpoint.
Its sum is logarithmic, so column-space triangle costs a squared logarithm
in energy. This justifies the application even though the coefficients of
different prefix masks are different. The full joint energy is at most
\(R^2X^\epsilon\), and the final h-Cauchy costs \(R^{1/2}\): the resulting
flat physical bound is \(R^{3/2}X^\epsilon\). All g strata, coincident
rationals, long frequencies, masks, and the once-only Ramanujan removal are
paid. It loses to the inherited flat envelope; no lower bound for this joint
energy or actual sum has been proved.

For the product matrix, \(\chi_4(h+2r)\chi_4(h)=(-1)^r\) on odd rows;
odd increments vanish. The exact signed increment phase has derivative
\(\sqrt{Xk}/\sqrt{h+2r}+1/2\), which has integer aliases. The matrix-norm
step discards these fixed-vector signs. In its four-corner trace they multiply
to one. For row separation r, the column phase has second derivative of size
\(Rr/K^2\); bounded variation and the elementary second-derivative estimate
give \(\min(K,\sqrt{Rr}+K/\sqrt{Rr})\). Squaring and summing every row pair
gives
\[
E_4\ll X^\epsilon[LK^2+RL^3+(LK^2/R)\log(2L)],
\]
where the cross term \(L^2K\) is absorbed because K>L. Multiplying
\((LK)^{1/2}E_4^{1/4}\) by the physical factor gives
\[
X^{1/4+\epsilon}\min\{(LK)^{1/4},(K+DL+L/D)^{1/4}\}+O_W(1).
\]
In exponent coordinates a=delta-ell, the price is
\[
\min\{(1-a)/2,\max(1/2-\delta/4-a/4,
                         1/4+\delta/2-a/4)\}.
\]
Splitting at delta=1/3 and a=1/3 shows it is nowhere smaller than
\(\min(a,(1-a)/2)\) where that accepted flat envelope is legal. It also
does not improve the elementary smooth envelope \(\min(D,\sqrt{XL/D})+O(1)\):
if delta<=1/3 its K term costs at least D; if delta>=1/3 and LK>=DL,
then L>=D^3/X and its DL term costs at least D; otherwise its dual triangle
cap is already smaller than the trace bound.

The actual lower buffer is proved from nonzero fixed eta,W and Phi(0)=1 on
one interior rectangle when L/H tends to zero. It yields squared coefficient
mass comparable to LK, hence \(E_4\ge (\operatorname{tr}AA^*)^2/n_h\gg LK^2\).
This applies to the actual slanted symbol on that family, not to arbitrary
clipped pieces or the different160 weighted matrix. For a literally dyadic
test sequence take \(X=2^{24m}, D=2^{8m}, L=2^m, K=2^{9m}\). Then the trace
upper and lower powers match; its normalized price is \(X^{11/32}\) up to
epsilon, even after its dual coefficient-triangle cap. The independent
original-d triangle instead costs \(X^{1/3}\) here; it is a stronger fallback
but still above quarter. We do not assert the 11/32 floor after taking this
additional fallback. No lower bound for the signed T or P(X) follows.

For the displayed smooth block, the original-d triangle gives D and the
dual triangle with its paid O(1) error gives sqrt(XL/D). This is the
unchanged fallback, uniformly at most X^(3/8+epsilon) on the active triangle.
Both quarter shifts, negative frequencies and the real projection cost only
fixed factors for these upper bounds. O(log^2 X) one-count labels cost epsilon.
Column cuts/stars use their actual variation; row cuts use zero extension.
Terms outside this representation are NOT assigned this sharper bound.
The O(D) fallback applies to the displayed original-side expression and its
verified bounded-weight cuts: a single h boundary costs O(D/L), a single d
endpoint O(1), and bounded-variation cutoff differences O(D). An unspecified
correction without an exhibited original-side representation and coefficient-
mass bound retains its inherited estimate and owner; this review does not
claim it paid by O(D). The independent product review required this scope
repair in the claimant report before its revised final hash was frozen.
Hard TOP, BAL, M1 and other independently owned modules retain their
inherited estimates. Nothing in this ledger closes them.

## 4. First unproved step

The sufficient short-window target is E_actual <= X^(1/2+epsilon)/R, not the
proved R^2 upper price. It also needs a justified complete-owner transfer.
For the product argument, a signed estimate before the all-vector norm is
missing. After that replacement, the actual buffered trace already forbids
the quarter conclusion from that certificate. Neither failure forbids a
different coefficient-sensitive signed theorem. All full-proof parents
and the unbounded fixed-order moment route remain open.

## 5. Controls and outcome

GREEN: correct K and phase; real X and its residual centre; both characters;
all gcd and long-frequency rows; complete versus partial periods; zero column
versus constant mode; fixed versus arbitrary vectors; exact masks/floors/stars;
actual lower buffer versus enlarged controls; full restored norms and powers;
smooth versus hard endpoint ownership; no complete gain from a fragment.
The odd-prime one-residue weighted control is an alternate vector, not an
actual lower bound. The dyadic sequence above is an actual-symbol control for
the rectangle certificate. All checks are analytical; zero experiments.

## 6. Dependencies and provenance

Conductor NONBLIND complete-owner review, round222, 2026-09-28. The conductor
supplied the weighted-mean diagnostic and requested a proved lower buffer;
therefore independent claimant-avoiding report reviews supply the separate
audit. No new external source is imported. Exact final artifact bindings:

FINAL_OWNER_BINDINGS

Starting/final required graph SHA256:
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
The accepted smooth transform, accepted160 kernel, historical143 report and
frozen actual interface are used only in their recorded scopes.

## 7. Recommended state effect

No graph or proof-draft change. Retain finite algebra and explicitly scoped
failed-certificate evidence. Do not promote complete UNBAL, a signed lower
bound, an endpoint transfer, a full moment improvement, or the quarter goal.
Close222 after mechanical validation; review the entire strategy and current
primary literature in223 before selecting another analytic objective.
'''
owner_deps=[joint,product,control,review_joint,review_product,review_weighted,
 base/'briefs/conductor_actual_unbal_interface.md',
 Path('rounds/codex-managed/m9-frequency-phase-diagram/reports/dual_three_quarter_attack.md'),
 Path('proofs/kernels/m9_m2_unbalanced_inverse_selector_reciprocity_projective_obstruction.md')]
owner=owner.replace('FINAL_OWNER_BINDINGS','\n'.join(f'- `{p.as_posix()}`: `{sha(p)}`.' for p in owner_deps))
put(base/'reviews/conductor_complete_owner_review.md',owner)

decision=dict(
 round_index=222,decision='retain_graph_archive_scoped_failed_certificates_and_require_full_strategy_review',
 terminal_label='complete_unbal_vector_attempt_no_new_bound',graph_mutation=False,
 complete_unbal_bound_improved=False,complete_moment_bound_improved=False,pointwise_exponent_change=False,
 reason='The literal weighted cross-modulus rows retain the original reciprocal row total in their common-period mean even after zero-column deletion. The completely paid joint short-window Gram closure gives only R^(3/2)X^epsilon. The original product-phase rectangle closure erases the fixed character signs and has an actual buffered certificate floor X^(11/32) on a legal dyadic family; its full upper price improves neither the elementary smooth bound nor the accepted scoped flat envelope. All masks, gcd rows, frequencies, real-centre factors and owner/endpoint limits are retained. These are reviewed finite and failed-certificate results, not actual signed lower bounds or a complete UNBAL estimate.',
 goal_turn_classification='stalled_no_complete_estimate_or_exponent_gain_scoped_failures_archived',
 first_unproved_estimate='Complete actual T_(L,K)<< (LK)^(3/4)X^epsilon for every real X and literal residual smooth UNBAL block remains unproved. All other full M1/M2/GAR frontiers, endpoint obligations and the sufficient unbounded fixed-even-moment family remain open. No external blocker is present.',
 next_objective='After222 closure, design the mandatory round223 broad strategy and current-primary-source review of all complete full-proof frontiers; select one quantified complete estimate with a credible net saving after every cost.',
 next_method='Compare the closed220--222 findings with the pinned September23 review and authoritative graph. Recheck the full M1 HARD/SMOOTH, M2 TOP/BAL/UNBAL, GAR and whole-discrepancy moment interfaces, including their first unproved estimates. Audit exact current primary theorem hypotheses only where they could change the net power. Archive repetitive positive-norm failures; do not count finite identities, local components, or unpriced vector grants as complete progress. Freeze any successor analytic objective only after that review closes.',
 state_note='Round222 closes with an identity State Patch and no complete analytic gain. Bare Kloosterman complete-period orthogonality does not survive the actual row-dependent Fourier weights, and deleting h=0 does not remove their constant mode. The fully priced joint finite-window closure costs R^(3/2)X^epsilon. The exact signed product increments retain (-1)^r, but the tested rectangle norm removes it; its actual buffered trace certificate costs X^(11/32) on one legal family, not a lower bound for the actual signed sum. Its restored upper estimate improves neither the elementary smooth fallback nor the accepted flat envelope in its legal scope. All profiles, masks, gcd/frequency rows, real centres and endpoint owners are kept. All401 graph nodes, proof-draft bytes and the qualified Li--Yang benchmark remain unchanged; complete UNBAL, all full-proof parents, the sufficient moment family and quarter goal remain open. The round is stalled at a complete estimate, not externally blocked. Mandatory broad strategy/current-primary review223 is pending design after220--222.',
 interventions=[
 'Froze the complete actual UNBAL target, correct K=XL/D^2 and phase e(sqrt(Xhk)); forbade flat-to-complete and hard-endpoint transfers.',
 'Assigned two orthogonal one-mechanism attacks and an isolated statement-only finite derivation, with reused history disclosed and zero experiments.',
 'Independently derived the weighted constant-mode and gcd-period control and required a separate post-isolation application review.',
 'Required the joint attack to estimate every row, coincident frequency and literal short mask, rather than substitute an unestimated vector theorem or complete-period delta.',
 'Required the product attack to attempt signed increments first, locate the all-vector loss, prove an actual lower buffer, and restore the trace powers over the full parameter range.',
 'Required explicit original-side fallback representations and endpoint scope; distinguished the rectangle certificate floor from an actual signed lower bound and from its stronger original-d fallback.',
 'Required an encoding repair before product review and one independent-review scope repair: unspecified extra corrections cannot inherit O(D) without their original-side representation and coefficient-mass proof. Final-hash reviews bind the repaired report; no content was promoted from preliminary files.',
 'Reconciled scoped finite identities and failed certificates, retained every accepted bound, and scheduled the mandatory full review only after validated222 closure.'
 ])
write(base/'controls/closing_decision.json',decision)

synthesis=r'''# Round222 synthesis: complete actual UNBAL vector attempt

## 1. Result

Terminal: **complete_unbal_vector_attempt_no_new_bound**. The frozen complete
UNBAL inequality remains open. No accepted pointwise exponent, complete moment
estimate or full-proof parent improves. Retain the reviewed finite algebra and
scoped failed-certificate costs as evidence. Apply an identity State Patch.

## 2. Exact objective and hypotheses

Every real X and literal residual smooth block:
\[
T_{L,K}=\sum\chi_4(h)a_{L,K}(h,k)e(\sqrt{Xhk})
\ll_\epsilon (LK)^{3/4}X^\epsilon,\quad K=XL/D^2,\ K/L>16.
\]
The actual Vaaler taper, both quarter shifts/signs, profiles, floors, stars,
support crossings and transform errors remain in scope. The physical factor
is X^(1/4)(LK)^(-3/4), with the exact fixed complex constant and O_W(1)
error retained in the reports. Flat strict identities do not cover all
nonflat/endpoint companions. The full target remains
P(X)<<X^(1/4+epsilon), with every other M1/M2/GAR and endpoint parent open.

## 3. Mathematical synthesis and quantified costs

The isolated finite report proves bare Kloosterman orthogonality only on a
complete common period. Arbitrary windows instead give their exact Fourier
kernel. Simple nearby unit-frequency rows demonstrate that short-window
orthogonality is false in that larger class; this is not a complete actual
Kloosterman-vector lower bound. Constant row twists preserve all-vector norms,
while a prescribed vector output can change.

The actual weighted row has Fourier constant U_(g,n)/n. Deleting the h=0
residue leaves (U_(g,n)-F_(g,n)(0))/n. For coprime moduli the complete
correlation is the product of those unnormalized residual row totals. All
noncoprime shared frequencies remain in the exact gcd formula. Thus common-
period orthogonality cannot eliminate the original weighted target. This is
an algebraic scope control, not a signed lower bound or a new estimate.

The joint attack keeps every (g,n,j,h) row and literal prefix, groups equal
rational frequencies, and pays their R^(-2) spacing and common Fourier mask
envelope. Its proved energy is E<=R^2 X^epsilon; h-Cauchy restores only
R^(3/2)X^epsilon physically. This is a weak upper price, not an obstruction
to sharper signed evaluation. The strict flat envelope
min(X^a,X^((1-a)/2)), a=delta-ell, remains stronger in its accepted scope.

The product attack derives the exact signed even increments (-1)^r and
their integer aliases before passing to a matrix norm. Its rectangle trace
loses the fixed character vectors and satisfies
\[
E_4\ll X^\epsilon[LK^2+RL^3+(LK^2/R)\log(2L)].
\]
The complete normalized upper price is
\[
X^{1/4+\epsilon}\min\{(LK)^{1/4},(K+DL+L/D)^{1/4}\}+O_W(1).
\]
It does not beat the elementary smooth envelope, nor the accepted flat
envelope where legal. On a proved interior actual-symbol buffer, E4>=cLK^2.
At D=X^(1/3),L=X^(1/24),K=X^(3/8), for example along X=2^(24m), the trace
certificate and its dual triangle cap cost X^(11/32) up to epsilon. That
floor concerns this certificate, never the signed sum. The separate
original-d triangle costs X^(1/3) there and remains available.

For every displayed smooth original block, the unchanged fallback is
min(D,sqrt(XL/D))+O_W(1), uniformly at most X^(3/8+epsilon). Verified original-
side cuts and listed endpoints retain their conservative finite-sum costs.
An unspecified correction without a demonstrated original-side expression
retains its inherited estimate and owner, with no O(D) certification from
this round. This qualification was repaired in the claimant report after
independent review. Hard top and independent owners retain their own bounds.
All displayed sign channels, O(log^2 X) labels, column variation, row cuts
and the exact smooth transform error are included; no unproved extra package
is certified by the fallback ledger.

## 4. First unproved steps and strategic assessment

The joint certificate would need its literal energy <=X^(1/2+epsilon)/R,
plus a complete-owner transfer, instead of the proved R^2 price. The product
route needs a signed actual-vector estimate before the all-vector norm;
after that step its buffered trace cannot prove quarter. Neither report
rules out other genuinely signed methods.

This round provides no complete analytic or exponent progress. In accordance
with the pinned strategy, do not count these mechanism-specific closures as
progress toward the exponent. They constrain method selection and are
archived without graph growth. There is no external blocker. Mandatory
broad strategy/current-primary review223 is the next pending design, after
closed220--222; another analytic subpartition is not automatically authorized.

## 5. Controls and review outcome

The three reports satisfy the seven-section contract. Statement-only current-
packet isolation was retained with prior-history disclosure. Independent
final-hash reviews cover weighted application, joint completion and product
signs/powers. Conductor reviews cover finite algebra and complete owner
restoration. Exact actual-versus-enlarged controls, all gcd/frequency rows,
literal supports, real centres and endpoint limits are explicit. Zero
mathematical experiments; at least95 percent analytical effort. No new
external theorem was imported or asserted applicable.

## 6. Dependencies and provenance

Conductor synthesis, campaign m9-m2-complete-unbalanced-vector, round222.
Pinned September23 review and checkpoint220 guide complete-owner accounting.
Accepted smooth duality, flat143/160 interfaces and220 mask algebra remain
scoped as written. Exact final report and review hashes are recorded in
controls/final_evidence_hashes.json and the reconciliation; the archive binds
all final files. Starting graph SHA256:
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.

## 7. State effect and conductor decision

Identity State Patch only: zero creates, updates, corrections or rejections;
all401 nodes and proof-draft bytes remain unchanged. No UNBAL, parent,
endpoint, moment or quarter promotion. Preserve the qualified repaired
Li--Yang real-X exponent and every accepted internal result. Close only
after graph/campaign/patch validation, all review gates and immutable archive
checks pass. Leave223 pending design for the required broad strategy review.
'''
put(base/'synthesis.md',synthesis)

reconciliation=r'''# Round222 conductor reconciliation

## 1. Result

GREEN for scoped finite and failed-certificate evidence only. Three assigned
reports and five final-hash reviews support no change to accepted mathematics.
The terminal label is complete_unbal_vector_attempt_no_new_bound.

## 2. Exact scope

The frozen actual UNBAL target uses K=XL/D^2 and e(sqrt(Xhk)) for every real X,
with all actual coefficients, signs, profiles, floors, stars and errors. The
full quarter theorem and separate complete parents remain open. Neither a
finite identity nor a flat-component certificate replaces this objective.

## 3. Proof and reconciliation

Accept the finite correlation and weighted-mean identities in their stated
scopes. The priced joint Gram upper estimate is R^(3/2) physically and gives
no gain. The rectangle trace removes fixed-vector character information,
and its proved actual buffered certificate floor exceeds quarter; its
complete upper price loses to inherited fallbacks. The complete-owner review
independently restores all powers and distinguishes the dual triangle from
the stronger original-d fallback. The independent product review required
the report to restrict O(D) companion pricing to displayed original-side
expressions, verified cuts and listed endpoints; unspecified correction
packages keep inherited estimates and are not claimed certified here.
Independent reviewers were not claimants
of the reports they audited. Reviews are nonblind except for the explicitly
isolated current finite packet; prior history is disclosed.

## 4. First gap

A signed actual-vector estimate strong enough for the complete UNBAL owner
is missing. There is no claimed signed lower bound or general impossibility
result. All other full-proof estimates remain open; no external blocker is
being asserted. The closing mechanical validation must still confirm the
identity patch, exact hashes, schemas, protected archives and every gate.

## 5. Controls

All written controls are analytical, including the actual buffered family,
the alternate-vector weighted correlation, near-frequency finite control,
all gcd rows, both characters, literal masks and endpoint ownership. Zero
mathematical experiments. No source import, partial-period orthogonality,
scalar-to-vector grant, arbitrary-to-actual lower-bound transfer or flat-to-
complete transfer is accepted. The product file's encoding repair preceded
review; its narrow companion-scope repair preceded the revised final-hash
review. Immutable prior-round files are checked, not rewritten.

## 6. Exact final artifact bindings

FINAL_HASH_BINDINGS

These bindings are inserted by the closure script only after all final
evidence hashes and seven-section reports are checked. Graph and draft
starting hashes remain independently pinned in starting_state_hashes.json.

## 7. Recommended state effect

Apply the validated identity patch in memory and replay it, leaving graph
and proof-draft bytes untouched. Close222 with ten green scoped gates and
archive the round. Require the mandatory broad strategy/current-primary
review223 to be designed from the closed state. The full objective is active
and unproved; finite and failed-certificate evidence is not an exponent gain.
'''
put(base/'reviews/conductor_round222_reconciliation.md',reconciliation)

provenance=json.loads((base/'controls/dispatch_provenance.json').read_text())
provenance['post_report_reviews']={
 'independent_weighted_period_review':'/root/full_frontier_sources, NONBLIND post-isolation application review of conductor control',
 'independent_cross_modulus_review':'/root/full_frontier_sources, NONBLIND claimant-avoiding final-hash joint report review',
 'independent_product_phase_review':'/root/joint_divisor_kernel, NONBLIND claimant-avoiding final-hash product report review',
 'conductor_finite_cross_modulus_review':'Conductor independent finite algebra and operator-scope review',
 'conductor_complete_owner_review':'Conductor NONBLIND physical powers, literal scopes and full-owner restoration'}
provenance['product_pre_freeze_repair']='Removed accidental control bytes and restored inline TeX before independent review. One subsequent same-round review repair restricts companion O(D) fallback to displayed original-side expressions, verified cuts and listed endpoints; unspecified corrections retain inherited estimates. Final review binds revised report hash below.'
provenance['final_report_hashes']={p.as_posix():sha(p) for p in [joint,product,finite]}
write(base/'controls/dispatch_provenance.json',provenance)
evidence=[joint,product,finite,control,review_joint,review_product,review_weighted,review_finite,
 base/'reviews/conductor_complete_owner_review.md',base/'controls/dispatch_provenance.json',
 base/'synthesis.md',base/'controls/closing_decision.json']
write(base/'controls/final_evidence_hashes.json',{p.as_posix():sha(p) for p in evidence})
print(json.dumps({'prepared':True,'shared_state_changed':False,'final_evidence_items':len(evidence),'product_hash':sha(product)},indent=2))
