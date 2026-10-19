from pathlib import Path
import json,hashlib
root=Path.cwd();rel=Path('rounds/codex-managed/gc-signed-sixth-dispersion');b=root/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
expected={'actual_sixth_bridge':'e7e1b99ab4b62fb94d66b7f8c1c16b88d6e3bb9f891405da1b4d3c2e697795b6','signed_fraction_dispersion':'9406863b09750d841adde32c46b71e3581c529de76e5d48a46a1902d1532c253','blind_packet_control':'755a6e08d18868c02b6a3bdb971b66ff1709496fd845c41bee8006ed8aef89c0'}
frozen={}
for n,h in expected.items():
 p=b/'reports'/(n+'.md');assert sha(p)==h;frozen[p.relative_to(root).as_posix()]=h
write(b/'controls/frozen_initial_reports.json',frozen)
c=b/'candidates/conductor_signed_sixth.md';ch=sha(c);assert ch=='cee1d243f21577e090acb0f9387c0412f4f70748b918aa3661e64db15586a8f3'
m=json.loads((root/'state/active_campaign.yml').read_text(encoding='utf-8'));assert m['round_index']==235
m['status']='review'
for t in m['tasks']:t.update(status='complete',frozen_report_sha256=expected[t['id']])
m['conductor_interventions']+=['Statement-only brief was sanitized before spawning the blind agent; no application, graph or manifest was read by that task.','All three initial reports frozen before expanded nonauthor review.','Candidate explicitly treats blockwise S6 as sufficient only; no unproved reverse implication from the full-band target.','Initial bounded attempt is closed to further discovery; one nonauthor review/repair cycle remains.']
write(root/'state/active_campaign.yml',m)
common=['protocol.md','state/proof_obligations.yml','state/active_campaign.yml',(rel/'candidates/conductor_signed_sixth.md').as_posix(),(rel/'controls/control_manifest.md').as_posix(),(rel/'controls/exact_local_controls.json').as_posix(),(rel/'controls/source_check.md').as_posix()]
specs={
 'actual_bridge_review':('You did not author actual_sixth_bridge.md. Audit candidate3A/3B and the bridge report: actual all-class variance, fixed233 application, full Hankel normalization and two-term summability, both norm transitions, every dual tail, variable-width linearization, Jacobian, complete actual complements and exact margin. Check source hypotheses and inherited qualifications. Do not validate only your own arithmetic report.', ['reports/actual_sixth_bridge.md'],'actual'),
 'arithmetic_dispersion_review':('You did not author signed_fraction_dispersion.md or blind_packet_control.md. Audit candidate3C/3D/3E and both reports: exact hyperbola freeze and signed square packet, two-character grouping constants, bounded-variation endpoint costs, paired and single-denominator sectors, actual absolute-certificate proof including primitive rational count and all negative contributions across the full center window. Also audit the independent filter/control signs. No signed-moment lower bound follows from a sum of moduli.', ['reports/signed_fraction_dispersion.md','reports/blind_packet_control.md'],'arithmetic'),
 'complete_scope_review':('Your isolated report is frozen; expanded context is allowed only for this new nonauthor review. Independently audit the conductor candidate and both actual reports for full-versus-blockwise implications, exact target/epsilon margin, retained all-harmonic and complementary costs, moving cutoff/width, actual-versus-artificial controls, first gap and State Patch scope. Independently sanity-check the actual certificate primitive-fraction count and character-sign positivity on the full window. Do not review only your own isolated result.', ['reports/actual_sixth_bridge.md','reports/signed_fraction_dispersion.md'],'scope')}
for name,(task,extra,tag) in specs.items():
 context=common+[(rel/x).as_posix() for x in extra]
 if tag in ['actual','scope']:context+=['proofs/kernels/gc_complete_square_root_large_values_moment_bound.md','proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md','strategy/round231_balanced_cancellation/conductor_combined_owner.md','strategy/round231_balanced_cancellation/reports/blind_hankel_tail.md']
 text='# Round235 nonauthor '+name+'\n\nCandidate SHA256 '+ch+'. Starting graph dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306.\n\n'+task+'\n\nRead only this brief and exact listed context; selected graph nodes suffice. About5 minutes, one bounded report. No new discovery or experimental sweep. Seven protocol sections, explicit PASS/FAIL and first doubtful step, exact reviewed hashes. If a material flaw appears, report it immediately and recommend a minimal correction. Write ONLY `'+(rel/'reviews'/(name+'.md')).as_posix()+'`, explicit UTF-8; no edits to candidate/reports/state. Stop.\n\n'+'\n'.join('- '+x for x in context)+'\n'
 (b/'briefs'/(name+'.md')).write_text(text,encoding='utf-8')
print(json.dumps({'status':'review','initial_reports_frozen':3,'candidate_sha256':ch}))
