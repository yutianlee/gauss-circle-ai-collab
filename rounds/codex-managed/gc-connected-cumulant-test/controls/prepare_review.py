from pathlib import Path
import json,hashlib
root=Path.cwd();rel=Path('rounds/codex-managed/gc-connected-cumulant-test');b=root/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
expected={'blind_collision_bound':'035febf79ed5f6acc569ad2109f1091b9d014e382a1305b65671743108e9bc7c','connected_certificate_audit':'7e18113aef8099a1724256720d196eecec0d61dd9ab6bddf47590261d51783c6','signed_connected_attack':'09ee3a7ee1031c015cbc34b463b887524d7150966d774fec477d2a9dcad45fa4'}
frozen={}
for n,h in expected.items():
 p=b/'reports'/(n+'.md');assert sha(p)==h;frozen[p.relative_to(root).as_posix()]=h
write(b/'controls/frozen_initial_reports.json',frozen)
c=b/'candidates/conductor_connected_test.md';ch=sha(c);assert ch=='3a443b5e63e826511f99e9428438018e5fc41f358a014fc15d9b8bb75233ae97'
m=json.loads((root/'state/active_campaign.yml').read_text(encoding='utf-8'));assert m['round_index']==234
m['status']='review'
for t in m['tasks']:t.update(status='complete',frozen_report_sha256=expected[t['id']])
m['conductor_interventions'].append('All three initial reports frozen before any expanded cross-review. The initial blind derivation remains isolated evidence.')
write(root/'state/active_campaign.yml',m)
specs={
'signed_remainder_review':('Review conductor candidate Sections3A,3C,3D(C1),3E, plus the signed report and blind report. Independently audit the exact collision coefficients, countable interchange, actual lower-moment hypotheses, signed vs absolute sums and complete budget. You did not author these claims. Do not re-review only your own certificate proof.', ['reports/signed_connected_attack.md','reports/blind_collision_bound.md']),
'certificate_review':('Review candidate Sections3A,3B,3D(C9-C10), C2 and the certificate report. Independently audit every full-harmonic lower proof seam, squarefree mass, repeated-label removal, Schwartz tails, probability factor and corrected-cumulant transfer. You did not author the actual lower-certificate audit. Inspect the exact permitted inherited Gram and shell proofs.', ['reports/connected_certificate_audit.md']),
'complete_scope_review':('Your initial blind report is now frozen; expanded context is allowed only for this new review. Independently review the conductor candidate, actual family binding, probability normalization, accepted216/233 scope, full restoration, first gap and controls. Check that a certificate obstruction is not a signed lower bound and that C1 alone improves no complete exponent.', [])}
for name,(task,extra) in specs.items():
 context=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',(rel/'candidates/conductor_connected_test.md').as_posix(),'proofs/kernels/gc_complete_distinct_radical_moment_reduction.md','proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md',(rel/'controls/control_manifest.md').as_posix(),(rel/'controls/exact_local_controls.json').as_posix()]+[(rel/x).as_posix() for x in extra]
 if name=='certificate_review':context+=['strategy/round231_harmonic_admission/reports/blind_harmonic_pooling.md','strategy/round231_harmonic_admission/conductor_harmonic_obstruction.md']
 text='# Round234 nonauthor '+name+'\n\nCandidate SHA256 '+ch+'; starting graph dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306.\n\n'+task+'\n\nRead only this brief and the following exact context; selected graph nodes suffice. Bounded about5 minutes, one report. No source search or additional experiment needed unless a concrete defect requires a check. Report seven protocol sections, PASS/FAIL, exact reviewed hashes and any first doubtful step. Write ONLY `'+(rel/'reviews'/(name+'.md')).as_posix()+'`, explicit UTF-8; no edits to any candidate/report/state. Stop after report.\n\n'+'\n'.join('- '+x for x in context)+'\n'
 (b/'briefs'/(name+'.md')).write_text(text,encoding='utf-8')
print(json.dumps({'status':'review','initial_reports_frozen':3,'candidate_sha256':ch}))
