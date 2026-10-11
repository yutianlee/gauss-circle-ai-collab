"""Close Round206 only after exact-hash reviews; preserve mathematical state."""
import copy
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

root = Path.cwd()
sys.path.insert(0, str(root))
from math_collab.campaigns import validate_campaign, _next_campaign
from math_collab.proof_obligations import (
    load_graph, dump_graph, validate_graph,
    validate_patch_against_graph, apply_state_patch,
)

cid = 'gc-complete-signed-shell-arithmetic'
base = Path('rounds/codex-managed') / cid
now = datetime.now(timezone.utc).isoformat()
terminal = 'scoped_arithmetic_method_no_go'
gp = Path('state/proof_obligations.yml')

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))

def write(p, obj):
    Path(p).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n',
                       encoding='utf-8', newline='\n')

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def contract(p):
    s = Path(p).read_text(encoding='utf-8')
    assert all(re.search(rf'^#{{1,2}} {i}\.', s, re.M) for i in range(1, 8)), p
    return s

start = read(base / 'controls/starting_state_hashes.json')
assert all(sha(p) == h for p, h in start.items()), 'Protected starting state changed'
for p, h in read(base / 'controls/frozen_artifact_hashes.json').items():
    assert sha(p) == h, ('Frozen input changed', p)
prior_campaigns = [
    'm9-m1-t1-complete-source-coefficient-mask-analysis',
    'gc-whole-discrepancy-twelfth-moment',
    'gc-strategy-signed-moment-majorant-review',
    'gc-complete-signed-convolution-attack',
    'gc-complete-large-values-duality',
    'gc-full-frontier-moment-strategy-review',
]
archive_count = 0
for prior in prior_campaigns:
    for p, h in read(Path('rounds/codex-managed') / prior / 'controls/artifact_hashes.json').items():
        assert sha(p) == h, ('Closed artifact changed', p)
        archive_count += 1

oldraw = gp.read_bytes()
g = load_graph(gp)
assert len(g['proof_obligations']) == 399 and not validate_graph(g, root=root)
m = read('state/active_campaign.yml')
assert m['round_index'] == 206 and m['campaign_id'] == cid and m['status'] == 'active'
assert not validate_campaign(m, g, root=root)
frozen = read(base / 'plan.json')['campaign']
for key in ['frozen_target', 'completion_criteria', 'resource_policy', 'controls',
            'target_obligations', 'review_seams']:
    assert m[key] == frozen[key], ('Frozen scope drift', key)
assert len(m['tasks']) == len(frozen['tasks']) == 3
for t, f in zip(m['tasks'], frozen['tasks']):
    assert {k: v for k, v in t.items() if k != 'status'} == {
        k: v for k, v in f.items() if k != 'status'}
    contract(t['report_path'])

power = base / 'controls/conductor_sixth_moment_power_ledger.md'
contract(power)
reviews = [
    (base / 'reviews/independent_shifted_source_review.md',
     [base / 'reports/shifted_moment_source_attack.md']),
    (base / 'reviews/independent_divisor_obstruction_review.md',
     [base / 'reports/actual_divisor_shell_attack.md']),
    (base / 'reviews/independent_bridge_power_review.md',
     [base / 'reports/blind_odd_shell_bridge.md', power]),
]
for review, artifacts in reviews:
    s = contract(review)
    assert 'GREEN' in s, review
    for artifact in artifacts:
        assert sha(artifact).lower() in s.lower(), (review, artifact)

evidence = [Path(t['report_path']) for t in m['tasks']] + [power]
evidence += [p for p, _ in reviews]
bindings = '\n'.join(f'- `{p.as_posix()}`: `{sha(p)}`.' for p in evidence)
judge = base / 'reviews/conductor_round206_reconciliation.md'
judge_text = r'''# Round 206 conductor reconciliation

Campaign: gc-complete-signed-shell-arithmetic. Role: conductor, post-report
reconciliation. Date: 2026-09-26. Starting graph SHA256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
This report adjudicates the frozen complete objective. No new source or
local candidate is silently promoted to the accepted graph.

## 1. Result

GREEN for scoped arithmetic-attempt closure only. The complete actual
divisor/CRT and shifted-pair attempts have been carried through and
priced. They give no improved complete twelfth moment or pointwise bound.
The actual centered absolute sixth expansion is rigorously too large for
the proposed sufficient certificate. This rejects the specified placement
of absolute values, not the signed arithmetic target.

The conductor selects an identity State Patch. All399 graph nodes and the
proof draft remain unchanged. The refined block sixth estimate is useful
evidence for the remaining power budget, but is not made a separate graph
fragment or presented as an improved full parent bound.

## 2. Exact target and hypotheses

T>=2 is real, X=T^2, I=[T/sqrt(2),sqrt(3)T], J=[X/2,3X], and every
dyadic N with T^(52/125)<N<T^(99/125) is retained. The actual fixed radial
mollifier and smooth partition are exactly those of the independently
reviewed205 interface. Let H_N be its physical frequency block, S_N its
curved shell, and Z_N its centered additive filter of width
h_N(x)=2sqrt(x)/sqrt(N). Write N=T^alpha and
omega(alpha)=min(alpha/4,beta,(1-alpha)/2), beta=2theta_LY-1/2.

The frozen whole-middle target remains integral_I|sum_N S_N|^12
<<T^(29/25+epsilon). All complementary frequency ranges and transform
errors have already been estimated at that scale in205. A uniform
single-block estimate suffices after logarithmic aggregation. Success at
this milestone would imply only102/325; it is not the full quarter proof.

## 3. Reconciled derivation and restored powers

The isolated analyst independently proves the curved-to-additive bridge
S_N(R)=R^(-1/2)Z_N(R^2)+O(T^(-1/2+epsilon)N^-1)+O_A(T^-A).
It includes the inclusive origin term, integer centers, discrete mean
subtraction, variable widths and infinite tails. Its conditional sixth
conversion uses only the supplied circle supremum and is valid with
exponent47/125+6beta<29/25. The conductor has additional inherited
physical-block information: the elementary supremum N^(1/4) makes the
stronger variance sixth input integral_J|Z_N|^6<<X^(1+epsilon)H^3 imply
middle p12<<T^(1+epsilon), where H=T/sqrt(N). These are compatible claims
with different explicit available inputs; the blind report is not faulty
for proving the weaker sufficient conclusion in its isolated packet.

The direct frequency-spacing calculation gives M2(H_N)<<TN^-1/2.
Intersecting its Chebyshev bound with the accepted204 distribution at
V0=N^(13/220) gives M6(H_N)<<TN^-29/110. The possible W^4 term is smaller
throughout the complete band. The corresponding p12 bound has worst power
1+(272/55)beta at alpha=4beta and is worse than the accepted10beta.
Thus the legal pair-source variance error is avoidable for this second
moment, but removing it does not supply the missing six-factor estimate.

The exact sufficient sixth threshold through these suprema is
integral_J|Z_N|^6<<T^(129/25-6omega(alpha)+epsilon). Relative to XH^3,
it allows T^(ell(alpha)+epsilon), with
ell=4/25+3alpha/2-6omega>=4/25. The complete additional saving needed
from the proved block sixth bound is
g(alpha)=6omega-4/25-29alpha/110>0.
Its endpoint values are2436/6875 and3509/13750; its maximum is
(272/55)beta-4/25 at alpha=4beta. No unestimated sub-band is deleted.

For the actual a(n)=r2(n)-pi, the exact sixth expansion retains every
shift and equality pattern. Patterns with at most three distinct shifts
are bounded absolutely by X^(1+epsilon)H^3. The joint four-, five-, and
six-distinct-shift part is still open, with all repeated coordinates in
the former two strata retained. The exact hyperbola identity retains the
quotient characters and moving thresholds. Weighted CRT yields its full
signed local-density main term plus an absolute endpoint-error cost
X^(3+epsilon)H^6. This is an upper-bound cost, never a lower bound on the
actual signed error. Raw all-divisor opening costs X^(6+epsilon)H^6.

Separately, r2(n) lies in4Z, hence |r2(n)-pi|>=4-pi. Uniform nonvanishing
of the actual limiting filter and a pointwise BV/Riemann-sum argument
prove that the full termwise absolute sixth expansion is at least cXH^6.
It exceeds even the weaker sufficient threshold by at least T^(136/125)
before epsilon losses. Removing the already-safe <=3-distinct sector
does not remove this obstruction. This is a genuine actual-coefficient
majorant obstruction with precisely limited scope, not a signed-moment
lower bound and not a necessity claim for this sufficient certificate.

The source audit checks exactly three primary interfaces. HKLDW1705.04771v3
Theorem7.1 gives a legal pair transfer XH+X^(1-lambda)H^2 with unspecified
positive lambda, after retaining all local densities and variable-width
weight variation. The restored p12 power is
max(1+8beta,2-2lambda+6beta), not an improvement. Its exponential-weight
error is not imported for arbitrary weights. Hughes--Rudnick's sixth
smoothing range M<<T^(2(1-delta)/31), together with M>>N, misses every
middle scale. Tanigawa--Zhai's divisor fourth-moment width U>>X^(3/7)
misses H<<X^(99/250), independently of its object and moment mismatch.

An independent review corrected a source-report overstatement: replacing
c_k-pi^2 by c_k while retaining signed autocorrelation does not by itself
force XH^2. The zero Fourier mode vanishes, and the difference is only
-pi^2 A_K(0) integral wh=O(XH). Taking absolute autocorrelation weights
does cause the larger cost. The corrected final report is hash-bound.

## 4. First unproved step

What remains is an actual signed bound for the complete joint4--6-distinct
shift contribution at the relaxed threshold, or a direct p12 method that
bypasses that certificate. Neither independence, pair information, nor
the global circle bound proves it. The CRT main term and endpoint
remainder must be controlled together or separately with valid costs;
neither may be discarded. A variance sixth conjecture is stronger than
needed and is not substituted for the frozen target.

The quarter theorem, M1/M2, parent obligations and source qualifications
stay open or unchanged as in the graph. No new external theorem is
accepted. The positive surrogate in the blind report diagnoses coarse
inputs only and is explicitly not an actual-r2 counterexample.

## 5. Controls, reviews and outcome

All eleven frozen controls are accounted for across the reports and
independent seams: complete middle range; actual character; all divisors
and shifts; curvature/mean; infinite tails; real endpoints; signed versus
absolute quantities; restored powers; primary-source hypotheses; no
Gaussian inference; full-proof scope. The blind report finished before
unmasking for the source seam. Subsequent edits to that report were only
two rendering repairs, leaving its mathematical content and provenance.

The conductor checked the actual absolute lower bound, exact CRT masks,
Jacobian, and exponent algebra independently. The three post-report
reviews cover disjoint principal seams and bind the final artifacts.
No decision rests on voting. All work was analytical/algebraic/source
inspection; there were no mathematical numerical experiments. Mechanical
hash, schema and identity-patch checks certify archival/state consistency
only, not a historical theorem or an asymptotic argument.

## 6. Exact dependencies and final evidence hashes

The inherited inputs are protocol.md, the starting graph and frozen206
manifest/strategy/briefs; the accepted204 large-values kernel; the
reviewed205 middle-band interface and source gate; and the exact primary
theorem locations recorded in the source report and its independent
review. Round200--205 archive hashes are rechecked at closure. The user's
2026-09-23 strategy review is unchanged.

FINAL_HASH_BINDINGS

The reviews specify their inherited-interface limits; the source seam
does not purport to reprove the preceding radial reconstruction. The
bridge/power seam and archived205 review cover that separate dependency.

## 7. Conductor decision and State Patch

Apply the mechanically validated identity patch after all required gates
are green. Archive the scoped no-go and precise missing arithmetic
inequality; retain the best complete moment exponent10beta and pointwise
theta_LY. No graph fragment or proof-draft edit is justified by this round.

After closing206,207 is pending design from these closed artifacts. Its
candidate direction is the complete signed4--6-shift correlation with the
relaxed saving profile, not another pair-variance calculation or repeated
absolute estimate. No successor is started here. The next mandatory broad
strategy/current-literature review remains208 after205--207.
'''.replace('FINAL_HASH_BINDINGS', bindings)
judge.write_text(judge_text, encoding='utf-8', newline='\n')
assert 'GREEN for scoped arithmetic-attempt closure only' in contract(judge)
for t in m['tasks']:
    assert sha(t['report_path']) in judge_text

synthesis = r'''# Round 206 synthesis

The complete signed-shell arithmetic attack is closed with a scoped
method no-go and no improved complete moment bound. The identity State
Patch preserves all399 graph nodes and the proof draft byte-for-byte.

The actual centered termwise absolute sixth expansion has size at least
cXH^6, too large even for the relaxed sufficient sixth threshold. The
full signed moment is not lower-bounded by this majorant. Exact divisor
hyperbola/CRT opening retains all characters, moving masks and local
densities, but its independently summed endpoint-error cost is
X^(3+epsilon)H^6. That cost is an upper estimate, not an impossibility
theorem for signed CRT cancellation.

All patterns with at most three distinct shifts are already safe. The
joint four-, five-, and six-distinct-shift correlation remains unproved.
Every middle dyadic scale T^(52/125)<N<T^(99/125), real endpoint, infinite
tail and repeated coordinate remains in the problem.

The statement-only bridge rederivation and later independent seam reviews
validate the filter normalization and exact conversion costs. The direct
block second moment is TN^-1/2; intersecting it with the accepted level-set
bound gives a frequency-resolved sixth estimate TN^-29/110. Its supremum
interpolation still loses to the existing full p12 exponent10beta.

The next arithmetic estimate need not attain a Gaussian/variance sixth
scale. With N=T^alpha and omega=min(alpha/4,beta,(1-alpha)/2), it suffices
to prove integral|Z_N|^6<<T^(129/25-6omega+epsilon). The saving still
needed from the proved sixth estimate is
g(alpha)=6omega-4/25-29alpha/110>0 throughout the entire middle band.

Three exact primary-source interfaces were checked: the actual-r2 pair
theorem transfers legally but does not give six-factor information;
Hughes--Rudnick's smoothing range and Tanigawa--Zhai's divisor fourth
moment miss the required parameter range. No external result was newly
accepted. A source-review correction distinguishes signed autocorrelation
from taking its absolute value; the final corrected artifact is reviewed.

The complete p12 target T^(29/25+epsilon), any better pointwise exponent,
M1/M2 and the full quarter theorem remain open. Even success at this
milestone would imply only102/325. The local no-go is evidence about a
specified estimation method, not a refutation of the target.

Three seven-section reports, the conductor power ledger, three exact-hash
reviews and conductor reconciliation form the evidence. All work was
analytical/source review, with no mathematical numerical experiment.
See reviews/conductor_round206_reconciliation.md, state_patch.json and
controls/closure_validation.json for exact bindings and state checks.

Round207 is pending design only after this closure. Its candidate direction
is the complete signed4--6-shift problem at the relaxed threshold; no
smaller unestimated complement is introduced. The next mandatory broad
strategy and current-literature review is208.
'''
(base / 'synthesis.md').write_text(synthesis, encoding='utf-8', newline='\n')

hygiene = []
for p in base.rglob('*.md'):
    raw = p.read_bytes()
    s = raw.decode('utf-8')
    assert not re.search(rb'\r(?!\n)', raw), ('Bare CR in mathematical text', p)
    assert '\ufffd' not in s and not any(ord(c) < 32 and c not in '\n\r\t' for c in s), p
    hygiene.append(p.as_posix())
protected = [
    'GC-target', 'Conditional-bridge', 'M9', 'M9-M1', 'M9-M2',
    'M9-endpoint-uniformity', 'GC-external-Li-Yang-theta-star',
    'GC-weighted-square-root-exact-resonance-mass',
    'GC-physical-twelfth-moment-absolute-majorant-obstruction',
    'GC-complete-square-root-large-values-moment-bound',
]
reason = ('Complete actual divisor/CRT and shifted-source attempts yield no improved complete moment. '
          'The actual absolute sixth expansion is too large for the sufficient certificate; '
          'the signed4--6-distinct-shift correlation remains open at an explicit relaxed threshold. '
          'Archive the reviewed scoped no-go and power ledger without graph promotion.')
patch = dict(
    round_index=206, campaign_id=cid, starting_graph_sha256=start[gp.as_posix()],
    proof_obligations=dict(create=[], update=[], correct_rejected=[], reject=[], no_change=protected),
    round_assessment=dict(terminal_label=terminal, reason=reason),
    reversibility=dict(rule='Identity patch. In-memory application, inverse identity and replay '
                       'equal the original graph. Graph and proof-draft bytes are not rewritten.'),
)
assert not validate_patch_against_graph(g, patch)
applied, result = apply_state_patch(copy.deepcopy(g), patch, round_index=206, judge_ref=judge.as_posix())
assert applied == g and not result.created and not result.updated
assert not result.rejected and not result.corrected_rejected
inverse = copy.deepcopy(applied)
replay, _ = apply_state_patch(copy.deepcopy(inverse), patch, round_index=206, judge_ref=judge.as_posix())
assert inverse == g and replay == g and dump_graph(replay) == dump_graph(g)
write(base / 'state_patch.json', patch)
preflight = dict(
    round_index=206, status='green_identity_patch_preflight', graph_schema='pass',
    campaign_schema='pass', identity_patch='pass', reverse_identity_replay='pass',
    all_399_nodes_and_other_graph_data_unchanged=True,
    exact_review_hashes={a.as_posix(): sha(a) for _, arts in reviews for a in arts},
    three_report_hashes={t['report_path']: sha(t['report_path']) for t in m['tasks']},
    frozen_scope_and_briefs_unchanged=True, closed_round200_through205_archives_unchanged=True,
    protected_archive_entries_checked=archive_count, report_hygiene=hygiene,
    mathematical_numerical_experiments=0, analytic_target='open',
    complete_moment_bound_improved=False, pointwise_exponent_change=False,
)
write(base / 'controls/closure_preflight.json', preflight)
matrix = read('state/validation_matrix.yml')
old_gates = copy.deepcopy([x for x in matrix['gates'] if not x['id'].startswith('round206_')])
for gate in matrix['gates']:
    if gate['id'].startswith('round206_'):
        gate['status'] = 'green_scoped_attempt_only_signed_target_open'
for review, _ in reviews:
    matrix['gates'].append(dict(id='round206_' + review.stem, status='green', artifact=review.as_posix()))
matrix['gates'].append(dict(id='round206_identity_patch_scope', status='green',
                           artifact=(base / 'controls/closure_preflight.json').as_posix()))
assert all(x['status'].startswith('green') and Path(x['artifact']).is_file()
           for x in matrix['gates'] if x['id'].startswith('round206_'))
assert old_gates == [x for x in matrix['gates'] if not x['id'].startswith('round206_')]
matrix.update(
    promotion_status='round_206_closed_identity_patch_scoped_arithmetic_no_go', graph_sha256=sha(gp),
    analytic_target_status='open_complete_signed_middle_band_moment',
    decision_rule='Round206 closes the complete arithmetic attempt with a reviewed absolute-placement '
                  'no-go, not a target refutation. Identity patch; no improved complete bound. '
                  'Round207 pending design; broad strategy review208.',
)
write('state/validation_matrix.yml', matrix)
# Durable mathematical state is untouched: the validated and gated patch is identity.
assert gp.read_bytes() == oldraw and all(sha(p) == h for p, h in start.items())
assessment = dict(
    decision='retain_graph_archive_scoped_arithmetic_no_go', terminal_label=terminal,
    graph_mutation=False, main_result=reason, resulting_graph_sha256=sha(gp),
    patch_effect=f'0_create_0_update_0_correct_0_reject_{len(protected)}_no_change',
    complete_moment_bound_improved=False, pointwise_exponent_change=False,
    goal_turn_classification='scoped_method_no_go_precise_remaining_signed_estimate_no_complete_bound_gain',
)
m.update(status='complete', completed_at=now, closing_assessment=assessment,
         post_report_reviews=[p.as_posix() for p, _ in reviews],
         conductor_interventions=[
             'Kept the complete frozen middle range and all arithmetic errors; required an actual estimate beyond the transform.',
             'Refined the sufficient sixth threshold; variance scale was not treated as necessary for the frozen p12 target.',
             'Derived direct block variance and intersected it with the accepted level-set bound; retained the unchanged best full p12 exponent.',
             'Reused three completed tasks for one bounded seam cycle, preserving the original statement-only isolation.',
             'Corrected the source autocorrelation overstatement before final review hashes; fixed two TeX rendering defects without mathematical changes.',
             'Archived the scoped no-go as evidence instead of multiplying graph fragments; full target stays open.',
         ])
for t in m['tasks']:
    t['status'] = 'completed'
assert not validate_campaign(m, g, root=root)
write('state/active_campaign.yml', m)

# Preserve all earlier ledger entries and the entire prefix byte-for-byte.
lp = Path('state/round_ledger.yml')
ledger_raw = lp.read_bytes()
s = ledger_raw.decode('utf-8')
ledger = json.loads(s)
assert ledger['active_round'] == 206 and ledger['rounds'][-1]['round_index'] == 206
old_entries = copy.deepcopy(ledger['rounds'][:-1])
entry = ledger['rounds'][-1]
entry.update(status='closed', closing_assessment=assessment, completed_at=now, next_round=207)
for t in entry['tasks']:
    t['status'] = 'completed'
matches = list(re.finditer(r'    \{\r?\n      "round_index": 206,', s))
assert len(matches) == 1
pos = matches[0].start()
eol = '\r\n' if '\r\n' in s else '\n'
new = s[:pos] + eol.join('    ' + line for line in json.dumps(entry, indent=2, ensure_ascii=False).splitlines()) + eol + '  ]' + eol + '}' + eol
assert json.loads(new) == ledger and json.loads(new)['rounds'][:-1] == old_entries
assert new[:pos].encode('utf-8') == ledger_raw[:len(s[:pos].encode('utf-8'))]
lp.write_bytes(new.encode('utf-8'))

# Only after closing206: record a proposed direction, not a frozen/new round.
write('state/next_round_plan.yml', dict(
    round_index=207, status='pending_design', campaign_id=None,
    starting_graph_sha256=sha(gp), predecessor_round=206,
    predecessor_terminal_label=terminal, tasks=[],
    candidate_objective='Prove the complete actual signed4--6-distinct-shift correlation at the '
                        'relaxed sufficient sixth threshold, or obtain a direct full p12 gain '
                        'that bypasses that certificate. Preserve every middle dyadic scale.',
    candidate_method='Use the exact centered r2 hyperbola/CRT expansion and its signed local '
                     'densities without termwise absolute summation. Identify and prove a '
                     'six-factor arithmetic cancellation unavailable to pair variance.',
    first_unproved_estimate='For N=T^alpha and omega=min(alpha/4,beta,(1-alpha)/2), '
                            'integral_J|Z_N|^6 << T^(129/25-6omega+epsilon). '
                            'Current M6(H_N)<<TN^-29/110 leaves required saving '
                            'g(alpha)=6omega-4/25-29alpha/110>0 over the entire middle band.',
    exact_closed_dependencies=[p.as_posix() for p in evidence] + [judge.as_posix(), (base / 'synthesis.md').as_posix()],
    design_constraint='Design only from closed206 artifacts. Do not repeat pair variance, discard '
                      'the CRT endpoint remainder, infer signed lower bounds from majorants, '
                      'replace the relaxed threshold by a necessary Gaussian assumption, or '
                      'create a smaller unestimated complement.',
    full_goal_scope='The p12 milestone would imply only102/325; the full quarter target '
                    'still requires further arithmetic information or adequate arbitrarily high fixed moments.',
    scheduled_review='Mandatory next broad strategy/current-literature review208, after205--207.',
    prior_turn_classification=assessment['goal_turn_classification'],
))
summary = _next_campaign(m, output_dir=base, graph_hash=sha(gp))
summary += ('\n## Closing decision\n\nRound206 closed with a scoped absolute-expansion no-go '
            'and a fully priced complete arithmetic attempt. Identity State Patch; all399 graph '
            'nodes and proof-draft bytes unchanged. The signed middle p12 target and full quarter '
            'theorem remain open. Round207 is pending design; broad review208.\n')
for p in ['state/current_round.md', 'state/next_campaign.md']:
    Path(p).write_text(summary, encoding='utf-8', newline='\n')
note = '''
## Round 206 complete signed-shell arithmetic (2026-09-26)

The full divisor/CRT and shifted-pair attempts are closed and reviewed.
The actual centered absolute sixth expansion is at least cXH^6, too large
even for the relaxed sufficient sixth threshold; this is not a lower
bound for the signed moment. Exact hyperbola/CRT opening retains every
local density and moving mask but its absolute endpoint-error cost
X^(3+epsilon)H^6 gives no gain. Patterns with at most three distinct
shifts are safe; the joint4--6-distinct-shift contribution remains open.

Direct frequency spacing gives M2(H_N)<<TN^-1/2. Combining it with the
accepted distribution yields M6(H_N)<<TN^-29/110, still insufficient
for a better complete p12 bound. The required additional sixth saving
is g(alpha)=6min(alpha/4,beta,(1-alpha)/2)-4/25-29alpha/110>0 throughout
52/125<alpha<99/125. A Gaussian variance sixth input is stronger than
needed; the exact relaxed sufficient threshold is retained in the report.

All399 graph nodes and proof-draft bytes are unchanged by an identity
State Patch. Complete p12 exponent10beta and pointwise theta_LY remain
the accepted bounds; M1/M2 and the quarter theorem remain open. No new
external source is promoted. Three reports and three exact-hash seam
reviews pass in their stated scopes. See
`rounds/codex-managed/gc-complete-signed-shell-arithmetic/synthesis.md`.
Round207 is pending design from closed evidence; next broad review208.
'''
for p in ['state/project_summary.md', 'state/current_state.md', 'state/failure_ledger.md']:
    path = Path(p)
    raw = path.read_bytes()
    assert b'## Round 206 complete signed-shell arithmetic (2026-09-26)' not in raw
    path.write_bytes(raw + ('\n' + note).encode('utf-8'))

assert not subprocess.check_output(['git', 'diff', '--name-only', '--',
                                   'rounds/obligation-main', 'rounds/web-research-test']).strip()
assert all(sha(p) == h for p, h in start.items())
validation = dict(preflight, campaign_id=cid, generated_at=now,
                  terminal_label=terminal, starting_graph_sha256=start[gp.as_posix()],
                  final_graph_sha256=sha(gp),
                  canonical_graph_sha256=hashlib.sha256(dump_graph(g).encode()).hexdigest(),
                  graph_nodes=399, original_graph_raw_bytes_unchanged=True,
                  proof_draft_raw_bytes_unchanged=True, previous_ledger_prefix_bytes_unchanged=True,
                  legacy_paths_unchanged=True, next_strategy_checkpoint=208)
validation['status'] = 'green_round206_scoped_arithmetic_closure_no_complete_bound_gain'
write(base / 'controls/closure_validation.json', validation)
vtext = (f'# Round206 closure validation\n\nGREEN for scoped arithmetic-attempt closure only; '
         f'the signed target remains OPEN.\n\nGraph SHA256: `{sha(gp)}`. The identity patch was '
         'validated, applied in memory, reversed and replayed. All399 nodes, graph and proof-draft '
         'bytes and previous ledger prefix bytes are unchanged. Three seven-section reports, '
         'three final-hash reviews, conductor reconciliation, frozen inputs, Round200--205 '
         'archive hashes and output hygiene passed. No improved complete moment or pointwise '
         'exponent was promoted.\n\nSchema validation does not reprove historical nodes or remove '
         'inherited advisories. No mathematical numerical experiment occurred. '
         'Round207 is pending design; the next broad review is208.\n\n'
         f'Details: `{base.as_posix()}/controls/closure_validation.json`.\n')
for p in ['state/last_validation.md', 'state/last_validation_report.md']:
    Path(p).write_text(vtext, encoding='utf-8', newline='\n')
assert not validate_graph(load_graph(gp), root=root)
assert not validate_campaign(read('state/active_campaign.yml'), g, root=root)
subprocess.run(['git', 'diff', '--check'], check=True)
hashes = {p.relative_to(root).as_posix(): sha(p)
          for p in sorted((root / base).rglob('*'))
          if p.is_file() and p.name != 'artifact_hashes.json' and '__pycache__' not in p.parts}
strategy = Path('strategy/round206_complete_signed_shell_arithmetic_attack.md')
hashes[strategy.as_posix()] = sha(strategy)
write(base / 'controls/artifact_hashes.json', hashes)
print(json.dumps({k: validation[k] for k in [
    'status', 'graph_nodes', 'final_graph_sha256', 'proof_draft_raw_bytes_unchanged',
    'complete_moment_bound_improved', 'pointwise_exponent_change']}, indent=2))
