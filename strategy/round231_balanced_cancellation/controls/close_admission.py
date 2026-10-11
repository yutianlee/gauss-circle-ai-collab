"""Close corrected research evidence; accepted mathematics remains immutable."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime
import hashlib
import json
import subprocess
import sys

root = Path.cwd()
p = root / 'strategy/round231_balanced_cancellation'

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def write(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

plan = read(p / 'plan.json')
assert plan['status'] == 'in_progress', 'Already closed; do not rerun.'
expected = {
    'reports/balanced_reciprocal_attack.md': 'fa63868418be5c8d24d30284394976fa3e0f1df077117dc3a9227441d55cf61f',
    'reports/balanced_source_audit.md': 'bd7beaa816e2443be41aaed903e92c8b884b1b827b1ea5b2fb1eb9004b0e9cd7',
    'reports/blind_hankel_tail.md': '03b30638eb6da7242343731ac03b425e2f09e16749f73685adc343a357cd01d5',
    'conductor_combined_owner.md': '9f5d9a31c0624e7ee97a21bcdfa2e638154fa313cc45cbab198856222366d76b',
    'conductor_seam_repairs.md': 'e4dc22c726eb241e24a4e7c485202ea6b6b567ecc4e16a3708d435ddc82eab14',
    'reviews/review_source_application.md': '39a778d3ddcf1acdd25b21be6206bd86559c4abef1067cb781056cdfa64d68a4',
    'reviews/review_reciprocal_signs.md': '8bfd3a3c5ed3b4a43f668708a57e9234dca99965ba35ceb3bd59e27df3524b03',
    'reviews/review_hankel_and_owner.md': 'bb9b8654518c8ee42c4f609bccd575b1f74c61d29cb52626280d9d19fc677d24',
}
for f, h in expected.items():
    assert sha(p / f) == h, f
assert read(p / 'controls/finite_controls.json')['status'] == 'passed'
assert (p / 'conductor_decision.md').is_file()
review_status = {
    'reviews/review_source_application.md': 'pass_with_attached_complementary_budget_correction',
    'reviews/review_reciprocal_signs.md': 'pass_with_attached_logarithm_correction_and_real_phase_clarification',
    'reviews/review_hankel_and_owner.md': 'pass',
}
protected = read(p / 'controls/starting_hashes.json')

def check(item):
    f, h = item
    return f if not (root / f).is_file() or sha(root / f) != h else None

with ThreadPoolExecutor(max_workers=8) as pool:
    changed = [f for f in pool.map(check, protected.items()) if f]
assert not changed, ('Unexpected preclosure change', changed)
assert sha(root / 'state/proof_obligations.yml') == plan['starting_graph_sha256']

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
meta = ['state/next_round_plan.yml', 'state/current_round.md', 'state/next_campaign.md',
        'state/project_summary.md', 'state/failure_ledger.md']
write(p / 'controls/preclosure_metadata_snapshot.json',
      {f: (root / f).read_text(encoding='utf-8') for f in meta})
decision = {
    'completed_at': now,
    'status': 'not_admitted',
    'analytic_campaign_launched': False,
    'packet': 'strategy/round231_balanced_cancellation',
    'decision': 'strategy/round231_balanced_cancellation/conductor_decision.md',
    'mechanism': 'Actual central balanced reciprocal character cancellation, exact bilinear source application, and combined norm/factor ownership',
    'findings': [
        'A reviewed actual-character smooth rectangle bound gives T^epsilon[(T/N)^(1/2)+T^(-1/2)] after one-variable Poisson and an integer-product resonance count. Absolute summation over remaining frequencies yields no complete gain.',
        'Exact quarter-frequency fibres are imaginary and their leading real circle term vanishes. Physical detuning produces coherent real individual fibres, so a uniform per-frequency square-root bound is false. This is not a full-wave or moment lower bound.',
        'KRW Proposition5 applies to the actual sharp moving fibre intervals after logarithmic completion and product partial summation. Its leading term T^(1/8)N^(1/16), even optimistically combined with head/tail bounds, reaches ceiling1/6 and moment certificate5/3, insufficient for10beta.',
        'The independently rederived smooth actual Hankel tail and norm band were already reviewed in Rounds203/205/208. They are verification, not new progress; historical attribution was corrected before closure.',
        'Combining that old norm band with the recent adaptive factor cutoff gives an exact parameterized owner C_gamma with all complementary terms paid at m(gamma)=max(1,10gamma,1+20gamma/13). For gamma16/125 the sufficient residual target32/25=1.28 is explicit but unproved.',
        'Three frozen reports and three nonauthor reviews completed. Attached corrections replace log(2D) by log(2+D), clarify exact versus detuned real resonances, and restore the complementary29/25 floor in sharp-moment conversion. Exact finite controls passed.',
    ],
    'scope': 'Corrected signed rectangle estimate, scoped source/control failures, and exact residual interface; no new complete exponent.',
    'graph_effect': 'none; no State Patch or promotion',
    'required_new_input': 'Signed cancellation across reciprocal frequencies or a direct radius-averaged estimate for actual C_gamma at m(gamma)<10beta, with every sharp arithmetic cutoff and complementary owner restored. Merely reproducing the old Hankel tail or assuming fibrewise square-root cancellation cannot supply it.',
    'complete_target': 'Preferred M12<=T^(29/25+epsilon); explicit modest target32/25 also open; accepted10beta=1.289663519481... unchanged.',
}
nxt = read(root / 'state/next_round_plan.yml')
assert nxt['round_index'] == 231 and nxt['status'] == 'pending_design' and not nxt['tasks']
old = nxt.get('latest_admission_check')
if old:
    nxt.setdefault('admission_check_history', []).append(old)
nxt['latest_admission_check'] = decision
write(root / 'state/next_round_plan.yml', nxt)

summary = """# Current research status - central balanced cancellation test closed

11 October 2026. The bounded Round231 continuation tested the actual central balanced signed residual through reciprocal character cancellation, a primary bilinear theorem, and an independently derived smooth Hankel tail. No complete moment improvement was obtained. The accepted complete bound remains M12(B_T)<<T^(10beta+epsilon), 10beta=1.289663519481... .

The reviewed reciprocal rectangle bound is T^epsilon[(T/N)^(1/2)+T^(-1/2)]. Its exact quarter-frequency leading term vanishes after taking the real circle phase, while a physical detuning gives a coherent real individual fibre. Thus uniform per-frequency square-root cancellation is false; no full-wave or moment lower bound follows. Cancellation across the reciprocal frequencies or in the radius average remains unquantified.

KRW Proposition5 genuinely applies to the sharp moving divisor intervals after logarithmic completion, but its leading normalized term T^(1/8)N^(1/16) is insufficient. Even its optimistic combination with the head and Hankel bounds reaches ceiling1/6 and moment certificate5/3. This rejects that certificate only.

Historical correction: the independently recovered smooth tail and norm band were already reviewed in Rounds203/205/208 and are not new gains. Combining the inherited band with the recent adaptive factor cutoff gives an exact owner C_gamma on T^(4gamma)<n<2T^(1-2gamma), d,m>=T^(2gamma-13/42)x(n)^(29/84). All complementary owners are paid at m(gamma)=max(1,10gamma,1+20gamma/13). At gamma16/125, proving M12(C_gamma)<<T^(32/25+epsilon) would improve the complete bound to1.28; that estimate is still unproved. The preferred gamma13/125 target29/25 remains open as well.

Three frozen reports, three nonauthor reviews, a forward correction attachment, and independent exact finite controls are complete. Corrections cover the D=1/2 logarithm, real resonance scope, and the complementary29/25 moment floor. Earlier evidence remains immutable. The preceding residual packet's adaptive-cutoff proof, uniform all-polynomial saving cap1/20, conditional inverse-exponent targets and coefficient-energy obstruction retain their original limited scopes.

Analytic Round231 remains pending_design, with no tasks launched, State Patch, accepted promotion, pointwise gain or automatic successor. The graph, proof draft, accepted kernels, validation matrices, active closed Round230 manifest and ledger are unchanged. The missing input is a quantitative signed estimate for the actual central owner. Decision: strategy/round231_balanced_cancellation/conductor_decision.md. Corrected report scope: strategy/round231_balanced_cancellation/conductor_seam_repairs.md.
"""
for f in ['state/current_round.md', 'state/next_campaign.md']:
    (root / f).write_text(summary, encoding='utf-8')

append = """

## Round231 central balanced cancellation admission (2026-10-11)

No complete gain. Actual reciprocal character cancellation proves a smooth rectangle bound T^epsilon[(T/N)^(1/2)+T^(-1/2)], with all stationary errors and near-product resonances paid. Exact quarter frequencies have zero leading real contribution; detuned physical frequencies can be real-coherent, rejecting only uniform individual-fibre square-root cancellation. No full moment lower bound is established. KRW Proposition5 applies after logarithmic completion of the actual sharp moving intervals and product partial summation, but its controlling T^(1/8)N^(1/16) term cannot improve the complete bound; the optimistic head/source/tail certificate reaches1/6 and moment5/3. The independent Hankel tail reproduction is NOT new: Rounds203/205/208 already contain the estimate and general norm-band principle. Historical attribution was corrected forward. Combining that inherited norm band with the recent adaptive factor cutoff yields the exact C_gamma owner with complementary budget m(gamma); gamma16/125 gives an explicit sufficient32/25 target, still unproved. Three frozen reports, three nonauthor reviews, exact finite controls, and a forward attachment resolve the logarithm endpoint, real-phase scope and complementary-budget restoration. Accepted10beta unchanged; analytic231 pending_design; no State Patch. Decision: strategy/round231_balanced_cancellation/conductor_decision.md. Repairs: strategy/round231_balanced_cancellation/conductor_seam_repairs.md.
"""
for f in ['state/project_summary.md', 'state/failure_ledger.md']:
    with (root / f).open('ab') as handle:
        handle.write(append.encode('utf-8'))

plan['status'] = 'complete'
plan['completed_at'] = now
for task in plan['tasks']:
    task['status'] = 'complete'
    task['report'] = 'reports/' + task['id'] + '.md'
    task['report_sha256'] = sha(p / task['report'])
plan['reviews'] = [{'path': f, 'status': status, 'sha256': sha(p / f)}
                   for f, status in review_status.items()]
plan['repair_attachment'] = {'path': 'conductor_seam_repairs.md',
                             'sha256': sha(p / 'conductor_seam_repairs.md')}
plan['conductor_interventions'] = [
    'Preserved statement-only isolation until the important Hankel tail report was frozen.',
    'Searched the existing mathematical history, found the recovered norm-tail and band already in Rounds203/205/208, and required corrected provenance before closure.',
    'Required complete actual-mask restoration, including bounded variation of each extra cutoff and both character placements.',
    'Identified the exact real-phase cancellation, required an independent detuned real-fibre control, and rejected any full-wave lower-bound inference.',
    'Combined the inherited norm band with the recent adaptive factor cutoff and assigned the parameterized owner to a nonauthor reviewer.',
    'Attached localized endpoint and complementary-budget repairs without altering frozen initial reports; the same review cycle checked the real detuning and inherited-mask seam.',
]
plan['decision'] = 'retain_corrected_evidence_and_exact_owner_no_complete_gain_not_admitted'
plan['graph_effect'] = 'none; corrected reviewed evidence only'
plan['complete_moment_bound_improved'] = False
plan['resource_outcome'] = {
    'analytical_minimum_percent': 95,
    'numerical_maximum_percent': 5,
    'new_source_applications': 2,
    'review_repair_cycles': 1,
    'description': 'Three analytical reports, one combined owner derivation, one forward repair attachment, three nonauthor seams and one bounded exact diagnostic script.',
}
write(p / 'plan.json', plan)

validation = []
for module, args in [('math_collab.validate_state_patch', []), ('math_collab.campaigns', ['validate'])]:
    result = subprocess.run([sys.executable, '-m', module, *args], capture_output=True,
                            text=True, encoding='utf-8')
    validation.append({'command': [sys.executable, '-m', module, *args],
                       'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr})
    assert result.returncode == 0, result.stdout + result.stderr
with ThreadPoolExecutor(max_workers=8) as pool:
    changed = [f for f in pool.map(check, [(f, h) for f, h in protected.items() if f not in meta]) if f]
assert not changed, ('Unexpected protected change', changed)
graph = read(root / 'state/proof_obligations.yml')
closure = {
    'completed_at': now,
    'decision': decision,
    'validation': validation,
    'protected_files_verified': len(protected),
    'authorized_metadata_changes': meta,
    'graph_nodes': len(graph['proof_obligations']),
    'graph_sha256': sha(root / 'state/proof_obligations.yml'),
    'proof_draft_sha256': sha(root / 'state/best_proof_draft.md'),
    'active_manifest_sha256': sha(root / 'state/active_campaign.yml'),
    'frozen_evidence_hashes': expected,
    'review_disposition': review_status,
    'status': 'passed',
}
write(p / 'controls/closure_validation.json', closure)
files = [f for f in p.rglob('*') if f.is_file() and f.name != 'final_evidence_hashes.json']
write(p / 'controls/final_evidence_hashes.json',
      {f.relative_to(p).as_posix(): sha(f) for f in files})
print(json.dumps({'status': 'closed', 'graph_nodes': closure['graph_nodes'],
                  'protected_files': len(protected), 'evidence_files': len(files),
                  'graph_sha256': closure['graph_sha256'],
                  'validators': [v['exit_code'] for v in validation]}, indent=2))
