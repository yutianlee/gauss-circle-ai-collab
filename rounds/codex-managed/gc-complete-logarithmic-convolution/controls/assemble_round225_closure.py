"""Assemble conductor artifacts after reading all frozen Round225 reviews.

No shared state is modified here. The separate closure validator decides
whether the identity State Patch may be recorded. Never run after archival.
"""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

base = Path("rounds/codex-managed/gc-complete-logarithmic-convolution")
assert not (base / "controls/artifact_hashes.json").exists()
now = datetime.now(timezone.utc).isoformat()

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def put(p, value):
    Path(p).write_text(value.strip() + "\n", encoding="utf-8")

def obj(p, value):
    put(p, json.dumps(value, indent=2, ensure_ascii=False))

attack = base / "reports/complete_nonlinear_prime_attack.md"
norm = base / "reports/complete_factor_norm_audit.md"
blind = base / "reports/blind_finite_convolution.md"
control = base / "controls/conductor_complete_envelope_control.md"
finite_packet = base / "briefs/blind_finite_convolution_statement.md"
scalar_packet = base / "briefs/blind_envelope_statement.md"
scalar = base / "reviews/independent_envelope_rederivation.md"
frozen = {
    attack: "952cd0ad2697cbe9c8cf28e4feba8bb04f2f22ce59884848dca7959c282dd521",
    norm: "0a9eed845bbb0e2a3a32c1003f60fe2c85ce627061484d9463d657b32f0c6353",
    blind: "56b082ce59ac8799f7c05573ce3b5a770b32714b13fd7f6ac36e1bde131724e2",
    control: "1f8cd3be4e5aeb9c10e161018e615e59175cd3fedd338501113b8ab1d6e0c593",
    scalar: "6798954c20b615d7c53fd4478d2c05128364ab79f0ecec2fcf523e8e8aadd63c",
    scalar_packet: "5007a095cdbc780a2ada7063438bcaf74f85f72d8a988264c150ec3ebfbbf815",
    finite_packet: "a5e2bc3a6d7b07e43bcfcfbd4db63d15f9120c3be00ea5b4257abde8e1b2a5b7",
}
assert all(sha(p) == h for p, h in frozen.items())
review_targets = {
    base / "reviews/conductor_finite_convolution_review.md": [blind, finite_packet],
    base / "reviews/independent_complete_attack_review.md": [attack],
    base / "reviews/independent_complete_norm_review.md": [norm],
    base / "reviews/independent_envelope_application_review.md": [control],
}
review_hashes = {
    base / "reviews/independent_complete_attack_review.md":
        "ec86ea7ea4b279f4cda380fbabcdd899e633c682a4aa97e8f02a3e310adce628",
    base / "reviews/independent_complete_norm_review.md":
        "936a443c92b06a1726f611092817d009e4fc499486270c918175a92a22f26b8f",
    base / "reviews/independent_envelope_application_review.md":
        "1ffc928458c32b3f1912ef564603eb5d05a5739be140dc52fd6ef9bdcc23f9fe",
}
assert all(sha(p) == h for p, h in review_hashes.items())
for p, targets in review_targets.items():
    s = p.read_text(encoding="utf-8")
    assert "GREEN" in s
    assert all(re.search(rf"^#{{1,2}} {i}\.", s, re.M) for i in range(1, 8))
    assert all(sha(a) in s for a in targets)
assert sha(scalar_packet) in scalar.read_text(encoding="utf-8")

deps = [
    Path("protocol.md"), Path("state/proof_obligations.yml"),
    Path("strategy/gauss_circle_strategy_review_2026-09-23.md"),
    Path("strategy/round225_complete_circle_logarithmic_convolution.md"),
    base / "briefs/conductor_complete_circle_wave.md",
    Path("strategy/gauss_circle_strategy_checkpoint_round223_2026-09-28.md"),
    Path("rounds/codex-managed/m9-m1-complete-gar-prime-amplification/synthesis.md"),
    Path("rounds/codex-managed/gc-complete-signed-convolution-attack/synthesis.md"),
    Path("proofs/kernels/gc_complete_square_root_large_values_moment_bound.md"),
    Path("sources/bourgain_2017_exponent_pair.md"),
]
core = [attack, norm, blind, control, finite_packet, scalar_packet, scalar]
bindings = "\n".join(f"- {p.as_posix()}: {sha(p)}." for p in core + list(review_targets) + deps)

owner = r"""
# Round225 conductor complete-owner review

## 1. Result

GREEN for the scoped finite identities, complete factor/norm audit and
optimistic-envelope comparison. The original complete real circle-wave
estimate is not improved. This is a conductor review of the two attack
reports and the isolated finite/scalar derivations; it is not a substitute
for the independent application review of the conductor's own control.

## 2. Exact statement and hypotheses

Fix the accepted radial mollifier and its real even Schwartz transform
Psi, with possible sign changes. For every real T>=2 and R in [cT,CT],
\[
 B_T(R)=4\sum_{n\ge1}(1*\chi_4)(n)n^{-3/4}\Psi(\sqrt{n/T})
                 \cos(2\pi R\sqrt n-3\pi/4).
\]
The inherited complete REAL bound is T^(beta+epsilon), where
beta=2theta_LY-1/2 and 1/8<beta<27/208. There is no inherited
complex or individual-block beta estimate. The accepted sharp bridge
has error O(T^(1/2+epsilon)) at fixed smoothing width T^(-1/2).
Cutoffs U,V are literal real thresholds, and every original product
scale, both character branches, prime powers and the singleton remain.

## 3. Independent conductor derivation and seam assessment

For psi=1 or chi4, put a=psi, g=mu psi, b=Lambda psi and c=psi log.
The identities a*g=delta and a*b=c remain valid at even arguments
without division by a character value. Splitting g and then b gives
\[
 b=b_{\le V}+g_{\le U}*c-g_{\le U}*a*b_{\le V}
                     +g_{>U}*a*b_{>V}.
\]
The logarithmic convolution is Df=f*(Lambda+chi4 Lambda).
The kernel is log2 at every power of2, 2log p at split prime powers,
and 2log p precisely at even powers of inert primes.
The test is divided by log of the full product only for n>=2.

Convolving the inverse factor with f gives d_1=chi4 and d_chi4=1.
With alpha=f*g and betaV=a*bV restricted as in the reports, the
middle pair is alpha_(<=U)*beta_(>V). Adding the long term leaves
d_psi*beta_(>V); adding the first term yields d_psi*c_psi.
Both branches recombine to f log. This verifies all signs and explains
why a truncated inverse is neither a short supported vector nor the
full bounded inverse contraction.

The actual pointwise bounds f<=d2, |alpha|<=d3 and |betaV|<=log n
give the stated l1/l2 bounds uniformly in U,V. They are upper norms,
not arithmetic correlation estimates. After opening the relevant free
periodic variable, fixed-mod4 subdivision changes the phase to
sqrt(r+a/4) with bounded affine shift. Its normalized derivatives have
the uniform square-root pattern on the positive ambient interval.
The already accepted GLOBAL Bourgain exponent pair applies because
the length-to-phase ratio is legal; proper subintervals retain their
ambient length. Actual logs and smooth product amplitudes enter only
through proved bounded variation after the unweighted estimate.

For r free variables and fixed short product q, choosing the longest
variable M>=(N/q)^(1/r) gives normalized price
T^kappa N^(kappa/2+1/4-1/(2r))q^(-1+1/(2r)).
This reproduces the three Type-I lines in the norm report. If U>=2N,
the exact shell contraction reduces to two periodic factors. Summing
their price min(N^(1/4),T^kappa N^(kappa/2)) with the actual Schwartz
weight over ALL scales gives the independently proved complex
T^(3kappa/2+epsilon)=T^(13/56+epsilon), not a beta consequence.
It is weaker than the accepted real bounds.

For the Type-II block MK~N, Cauchy leaves the proper intersection of
the two product intervals in the unweighted M variable. With
u=R(sqrt(n)-sqrt(n')), |u|/sqrt(M) is at least a constant times
T/sqrt(N)>=T^(1/4) when N<=T^(3/2). The exact diagonal is M^2K.
The summed first kernel term is
T^kappa M^(3/2+kappa/2)K^(2+kappa/2); the inverse-u term is absorbed
by the diagonal in this range. Normalization gives
\[
 N^{1/4}K^{-1/2}+T^{13/168}N^{13/336}K^{1/4}.
\]
This confirms both authors' same bound and the conductor control.
It does not license inserting arithmetic weights inside the source.

Writing N=T^nu, K=T^k, the two powers cross at
k=(71nu-26)/252. At nu=2/3 the value is47/378, but over all scales
the optimistic menu with the classical real block envelope peaks at
nu=226/307 with value81/614. The statement-only scalar derivation
correctly checks all endpoints and gives the interval
((504beta-26)/55,1-2beta) where that menu exceeds beta.
The conductor has checked this derivation independently: the increasing
branch is (55nu+26)/504 after nu=26/71, and its crossing with
(1-nu)/2 is precisely226/307. The inequality27/208<81/614 is exact.
Taking the better COMPLETE real bound leaves beta. A beta cap inside
the scalar diagram is only shorthand for this complete comparison;
it supplies no beta estimate for each block or complex component.

Every expanded coefficient is bounded by a fixed divisor function
times log n. The log denominator and fixed Schwartz order J therefore
pay the full tail n>T^(3/2) at T^(3/8-J/4+epsilon), uniformly in all
cutoffs and real radii. Choosing fixed J sufficiently large is legal.
The original n=1 term is O(1). For gamma>=0 a complete real exponent
gamma restores physical exponent1/4+gamma/2; in general the smoothing
error makes it1/4+max(gamma,0)/2. All compared complete exponents here
are nonnegative. The hypothetical81/614 would restore97/307, worse
than theta_LY, and is not a newly obtained actual bound.

## 4. First unproved step

The entire actual signed eight-term recombination, after the exact
inverse contractions, still needs a uniform bound T^(gamma+epsilon)
with gamma<beta, ultimately gamma=0. The supplied coefficient norms
and unweighted kernels do not give it. Granting an optimal factor
split at every scale is itself unsupported, and even that favorable
grant fails for this named estimate menu.

No lower bound for an actual oscillatory sum follows. The prime-two
absolute-mass control only diagnoses the specified modulus closure.
A stronger signed arithmetic estimate could beat these certificates.

## 5. Required controls and outcomes

GREEN for both branches, all prime powers and2, literal boundary
predicates, finite inverse contractions, the full product logarithm,
the singleton, actual vector norms and all Type-I/II ranges.
GREEN for proper interval and derivative-class premises, mixed scales,
fixed Schwartz seminorms, real-radius uniformity and sharp restoration.
GREEN for statement-only finite and scalar derivations with disclosed
retained history. GREEN for claimant-avoiding final-hash attack/norm
reviews and independent application review of the conductor control.
No new primary theorem was imported; inherited source scope was checked.
Zero mathematical experiments; at least95 percent analytical work.

The finite kernel is elementary and equivalent to the original complete
expression. Separate formalization/promotion would not close an analytic
owner and is not pursued in this bounded round.

## 6. Exact artifacts and provenance

Conductor, round225, gc-complete-logarithmic-convolution. The conductor
authored the envelope control and intervened before attack-report
freeze to correct a general optimizer formula. That provenance is
explicit; the isolated scalar proof, subsequent nonauthor application
review and reciprocal report reviews supply the distinct checks.
All frozen artifacts were read and checked before this disposition.

FINAL_BINDINGS

## 7. Recommended state effect

Retain scoped evidence only; identity State Patch. No graph node,
accepted proof-draft statement, complete real bound, complete moment
bound, pointwise exponent or M1/M2/GAR/endpoint owner changes.
The quarter goal remains open. Close225 before designing mandatory
strategy/current-primary review226.
"""
owner_path = base / "reviews/conductor_complete_owner_review.md"
put(owner_path, owner.replace("FINAL_BINDINGS", bindings))

reason = (
    "Both actual logarithmic/Vaughan branches and their full inverse contractions "
    "are valid, but no complete signed bound below inherited beta is obtained. "
    "The scoped generic factor certificate can reach47/378 locally at N=T^(2/3); "
    "even freely granting optimal factors at every scale leaves worst exponent81/614 "
    "at N=T^(226/307), above beta. All actual cutoff terms, norms, singleton, infinite "
    "tail and sharp reconstruction are paid. Upper-certificate capacity is not an "
    "actual arithmetic lower bound. No complete real, moment or pointwise gain."
)
gap = (
    "Uniformly for every real T>=2 and R in [cT,CT], bound the ENTIRE actual real "
    "eight-term logarithmic/Vaughan recombination, or its exact contracted circle "
    "wave, by T^(gamma+epsilon) with gamma<beta=2theta_LY-1/2, ultimately gamma=0. "
    "Every scale, singleton, sign, cutoff and Schwartz tail remains included."
)
interventions = [
    "Frozen objective unchanged; all three initial tasks remained within one Vaughan family.",
    "Conductor highlighted exact full Mobius contractions before norms and independently reproduced the bilinear exponents.",
    "A general optimizer formula in discovery correspondence was corrected before report freeze; no frozen report retained that error.",
    "Conductor expanded the local comparison to all scales, then assigned a separate isolated scalar rederivation containing no anticipated result.",
    "Final norm report explicitly records fixed-mod4 affine-square-root derivatives, ambient intervals, length/phase convention and bounded-T fallback.",
    "After reports froze, discovery author reviewed norm author and norm author reviewed discovery author; the finite/scalar rederiver separately reviewed the conductor's application.",
    "Review clarification preserves beta as a COMPLETE real bound, and general physical restoration uses max(gamma,0).",
]
state_note = (
    reason + " Identity State Patch: all401 graph nodes and proof-draft bytes unchanged. "
    "The independently derived complex13/56 bound is a weaker scoped certificate, "
    "not a new real benchmark. The missing estimate is: " + gap +
    " Full quarter, unbounded fixed-order moments, M1/M2/GAR and endpoints remain open. "
    "Zero mathematical experiments. Mandatory strategy/current-primary review226 is pending design."
)
decision = dict(
    round_index=225, campaign_id="gc-complete-logarithmic-convolution",
    generated_at=now, decision="close_bounded_attempt_without_complete_gain",
    terminal_label="complete_logarithmic_convolution_no_new_bound",
    graph_mutation=False, complete_frontier_bound_improved=False,
    complete_moment_bound_improved=False, pointwise_exponent_change=False,
    reason=reason,
    goal_turn_classification="no_progress_on_complete_bounds_bounded_mechanism_closed_with_verified_controls",
    next_objective="Mandatory broad full-goal strategy and current-primary-source review226 after closed225; select one complete parent inequality.",
    next_method="Review complete signed methods against all-scale225 costs and the pinned Sep23 strategy; a local exponent, finite identity or unestimated complement cannot count as progress.",
    first_unproved_estimate=gap, state_note=state_note, interventions=interventions,
)
obj(base / "controls/closing_decision.json", decision)

review_provenance = dict(
    round_index=225, generated_at=now, frozen_objective_changed=False,
    maximum_concurrent_subagents=3, mathematical_numerical_experiments=0,
    original_report_claimants={
        attack.as_posix(): "/root/full_frontier_sources",
        norm.as_posix(): "/root/joint_divisor_kernel",
        blind.as_posix(): "/root/joint_lattice_kernel",
        control.as_posix(): "/root",
    },
    reviews=[
        dict(path=(base/"reviews/conductor_finite_convolution_review.md").as_posix(),
             reviewer="/root", claimant="/root/joint_lattice_kernel",
             reviewed={blind.as_posix(): sha(blind), finite_packet.as_posix(): sha(finite_packet)},
             mode="claimant_avoiding_finite_derivation_review"),
        dict(path=scalar.as_posix(), reviewer="/root/joint_lattice_kernel",
             reviewed={scalar_packet.as_posix(): sha(scalar_packet)},
             mode="new_statement_only_scalar_rederivation",
             allowed_current_inputs=["protocol.md", scalar_packet.as_posix()],
             retained_history="Prior agent and finite-task history disclosed; no conductor application or anticipated scalar result supplied."),
        dict(path=(base/"reviews/independent_complete_attack_review.md").as_posix(),
             reviewer="/root/joint_divisor_kernel", claimant="/root/full_frontier_sources",
             reviewed={attack.as_posix(): sha(attack)},
             mode="post_freeze_nonauthor_attack_application_review",
             retained_history="Own norm-report authorship disclosed; no current sibling review or conductor control allowed."),
        dict(path=(base/"reviews/independent_complete_norm_review.md").as_posix(),
             reviewer="/root/full_frontier_sources", claimant="/root/joint_divisor_kernel",
             reviewed={norm.as_posix(): sha(norm)},
             mode="post_freeze_nonauthor_complete_norm_and_inherited_source_review",
             retained_history="Own attack-report authorship disclosed; no current sibling review or conductor control allowed."),
        dict(path=(base/"reviews/independent_envelope_application_review.md").as_posix(),
             reviewer="/root/joint_lattice_kernel", claimant="/root",
             reviewed={control.as_posix(): sha(control)},
             mode="post_scalar_freeze_nonauthor_application_review",
             retained_history="Own frozen scalar derivation disclosed, not misrepresented as independent review of itself. No attack/norm reports or sibling reviews allowed."),
        dict(path=owner_path.as_posix(), reviewer="/root",
             reviewed={p.as_posix(): sha(p) for p in core + list(review_targets)},
             mode="conductor_complete_owner_reconciliation",
             limitation="Conductor authored the application control; its required nonauthor review is separate."),
    ],
    interventions=interventions,
    source_policy="No fresh external primary import. Existing global Bourgain source premises checked in the complete norm review and application review; no restricted L4 range is silently enlarged.",
)
obj(base / "controls/review_dispatch_provenance.json", review_provenance)

synthesis = r"""
# Round225 synthesis: complete logarithmic convolution gives no new bound

## 1. Result

Terminal label: complete_logarithmic_convolution_no_new_bound.
The complete actual circle wave remains bounded at the inherited real
exponent beta=2theta_LY-1/2. This round obtains no complete real bound,
moment improvement or new pointwise exponent. It closes one bounded
Vaughan-decomposition attempt with verified finite algebra and costs.
The identity State Patch preserves all401 nodes and proof-draft bytes;
acceptance is governed by state_patch.json and closure_validation.json.

## 2. Frozen objective and hypotheses

For the fixed accepted radial mollifier, every real T>=2 and
R in [cT,CT], the full objective is
\[
 \sup_R\left|4\sum_{n\ge1}(1*\chi_4)(n)n^{-3/4}
 \Psi(\sqrt{n/T})\cos(2\pi R\sqrt n-3\pi/4)\right|
 \ll_\epsilon T^\epsilon.
\]
An intermediate gain must improve the COMPLETE inherited exponent
beta, retaining possible signs of Psi, the original singleton, every
product scale and the full infinite tail. The complete real benchmark
is not a complex-wave or individual-block bound.

## 3. Derivation and complete quantitative outcome

The exact identity f log=f*((1+chi4)Lambda) retains prime2, inert even
powers and all split prime powers. Its two literal Vaughan branches
each have four terms with signs plus, plus, minus, plus.
The full inverse contractions f*mu=chi4 and f*(mu chi4)=1 show that
all four terms in one branch recombine to d_psi*(psi log).
Both branches return f log exactly. This cancellation is algebraic;
it gives no estimate for the remaining nonlinear phase.

The actual vector norms follow from f<=d2, |alpha|<=d3 and
|betaV|<=log n. All expanded terms admit a complete complexT^(1/4)
bound. A fully contracted boundary choice, with a legal free
periodic-variable exponent-pair application, gives the independently
derived stronger complexT^(13/56) certificate. It is still weaker
than the complete classical REAL T^(1/6) and inherited realT^beta.
No complex estimate is inferred from those real bounds.

For a legal bilinear factor block MK~N, the audited coefficient-uniform
price after normalization is
\[
 T^\epsilon\left(N^{1/4}K^{-1/2}
       +T^{13/168}N^{13/336}K^{1/4}\right).
\]
The diagonal, product-intersection interval, actual norms and smooth
weight variation are retained. The global exponent-pair source is used
only on an unweighted interval with its derivative and length/phase
premises checked. Fixed character classes are finitely many affine
square-root phases, not arbitrary weighted applications.

At N=T^(2/3), the formal optimal short factor K=T^(16/189) gives
47/378<beta. This is not a complete gain: actual cutoffs leave other
factor ranges and short terms, including the prime-two component.
Even granting the best split freely at EVERY scale, the envelope
with the classical bound peaks at
\[
 N=T^{226/307},\qquad K=T^{32/307},\qquad \gamma=81/614>\beta.
\]
An isolated statement-only derivation confirms the complete piecewise
optimization and every endpoint. The interval
((504beta-26)/55,1-2beta) is nonempty and defeats this named menu.
Its capacity is a fact about supplied upper bounds, never an actual
lower bound for the signed wave.

The original singleton costs O(1). Every expanded coefficient is
dominated by a fixed divisor function times log n, and the full tail
beyond T^(3/2) costs T^(3/8-J/4+epsilon) at fixed Schwartz order J.
All remaining scales and cutoff transitions are included.
The accepted sharp bridge restores exponent1/4+gamma/2 for gamma>=0.
Thus inherited beta still gives theta_LY, whereas even the hypothetical
81/614 would give97/307>theta_LY. The latter is not an actual new theorem.

## 4. First doubtful or unproved step

The complete signed eight-term expression, or its exact recombined
circle wave, still needs a uniform T^(gamma+epsilon) estimate for
gamma<beta, ultimately gamma=0. A stronger use of the actual
Mobius/character correlations is not supplied by the audited norm
certificates. This is one complete missing inequality; no new chain
of smaller unestimated complements is opened.

The absolute prime-two control concerns only the displayed closure.
There is no actual signed counterexample and no general rejection of
logarithmic convolution or arithmetic cancellation.

## 5. Controls, independent reviews and validation

The three reports meet the seven-section contract. Finite identities
and scalar optimization each received current statement-only derivation
with retained-history disclosure. The conductor independently checked
both and reproduced the material powers. Report authors then reviewed
the other author's frozen report. A distinct nonauthor application
review checked the conductor envelope, source hypotheses and physical
restoration. Exact hashes and role limitations are in the reconciliation
and review-dispatch provenance.

No fresh primary-source import or mathematical experiment was used.
Inherited source checks explicitly distinguish the global theorem from
the restricted kernel204 L4 parameter window. Analytical effort is at
least95 percent. Graph/campaign schema, frozen target and briefs,
identity patch application/replay, graph/draft byte preservation,
all635 archived entries from200--224, previous ledger prefix and
legacy paths are required before closure. The closure validator records
the11 green gates and concrete outcomes.

## 6. Dependencies and exact artifacts

Campaign gc-complete-logarithmic-convolution, round225, conductor.
The pinned Sep23 strategy, closed223 checkpoint and closed224 synthesis
determine this complete-source test. Closed203 supplies only its
recorded classical envelope; accepted204 supplies the actual sharp
bridge and inherited source interface. All five Li--Yang application
repairs remain in force.

Exact report/control/review hashes are recorded in
controls/final_evidence_hashes.json and
reviews/conductor_round225_reconciliation.md. The starting graph hash is
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
The proof-draft hash is
65989358d00f0ecf7c4d385ea58bfad09eaa026af98924266207c5f8af872f00.
No archived artifact is changed or promoted by being cited.

## 7. Conductor decision and state effect

Close225 as no progress on complete bounds, with a bounded mechanism
closed by verified controls. Apply an identity State Patch. The quarter
goal, sufficient unbounded-fixed-order moment route, distinct-class
moment target and all M1/M2/GAR/endpoint owners remain open.

Design226 only after this closure. It is the mandatory broad strategy
and current-primary-source review. Reassess methods by a complete parent
estimate and net restored exponent; repeating these finite identities,
favorable local factors or scalar norm prices is not a new attack.
The full goal remains active, with no claim that difficulty is a blocker.
"""
put(base / "synthesis.md", synthesis)

reconciliation = r"""
# Round225 conductor final reconciliation

## 1. Result

GREEN for scoped convolution and envelope evidence only.
No complete analytic bound, moment bound or pointwise exponent improves.
The terminal label is complete_logarithmic_convolution_no_new_bound.

## 2. Exact hypotheses and conclusion

The frozen actual full real circle wave, both literal Vaughan branches,
all prime powers, every real radius in the dyadic window, singleton and
full Schwartz tail are retained. The strongest inherited complete real
bound stays beta. The optimized81/614 menu is an optimistic conditional
comparison; its local47/378 value is not a complete estimate.

## 3. Proof and review reconciliation

The seven-section conductor owner review independently checks finite
identities, actual coefficient norms, the free-variable Type-I prices,
the complex13/56 boundary certificate, Type-II diagonal and off-diagonal
powers, full scalar optimization and physical reconstruction.
It binds the three frozen reports and conductor control.
Nonclaimant report reviews and a separate nonauthor conductor-application
review agree after checking their own mathematical seams. This decision
is based on those derivations and controls, not on agreement by vote.

The scalar cap by beta is shorthand for selecting the better COMPLETE
real estimate. It is never a componentwise estimate. General restoration
uses1/4+max(gamma,0)/2; the compared complete exponents are positive.
No imported theorem applies to an arbitrary arithmetic-weighted row.

## 4. First unproved step

A complete signed uniform T^(gamma+epsilon) bound with gamma<beta,
ultimately gamma=0, remains unproved. Neither the identity nor any
specified upper-certificate obstruction is an arithmetic lower bound.
All complete parent owners remain open.

## 5. Required controls and outcome

GREEN for current statement-only finite/scalar work with retained
history disclosed, final-hash nonclaimant reviews, literal cutoffs,
prime-power/character zeros, original logarithm and singleton,
full tail, source interval/derivative premises and actual versus generic
scope. Zero mathematical experiments and no new external source import.

Before shared-state writes, close_round225.py must verify all final
bindings, seven-section contracts, frozen scope,401-node graph/campaign
schemas, identity patch/replay, all635 prior archived entries and
unchanged legacy paths. It then records11 green gates, graph/draft byte
preservation and the preserved prior ledger prefix. Only the resulting
closure_validation.json licenses this round's closed state.

## 6. Exact final bindings and provenance

Conductor, round225. Claimants, review routes, permitted context and
retained-history limits are recorded in review_dispatch_provenance.json.
The blind scalar report is independently rederived mathematics, not a
GREEN verdict on itself; its conductor review supplies that judgment.
The conductor's own application control has a separate nonauthor review.

FINAL_HASH_BINDINGS

## 7. Recommended state effect

Identity State Patch only. Keep all401 graph nodes and proof-draft bytes
unchanged, record the bounded no-gain conclusion and archive225.
Do not count this as progress on the complete conjecture. Mandatory
strategy/current-primary review226 remains pending design after closure.
"""
put(base / "reviews/conductor_round225_reconciliation.md", reconciliation)

final_paths = core + list(review_targets) + [
    owner_path, base / "controls/dispatch_provenance.json",
    base / "controls/review_dispatch_provenance.json",
    base / "controls/closing_decision.json", base / "synthesis.md",
]
obj(base / "controls/final_evidence_hashes.json",
    {p.as_posix(): sha(p) for p in final_paths})
print(json.dumps({"status": "conductor_artifacts_assembled_shared_state_unchanged",
                  "final_evidence_bindings": len(final_paths)}, indent=2))
