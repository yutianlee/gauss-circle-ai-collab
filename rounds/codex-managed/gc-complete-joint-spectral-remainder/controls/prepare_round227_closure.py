"""Prepare a new closure validator from immutable226; do not execute it."""
from pathlib import Path
base=Path('rounds/codex-managed/gc-complete-joint-spectral-remainder')
assert not (base/'controls/artifact_hashes.json').exists()
s=Path('rounds/codex-managed/gc-full-goal-spectral-source-review/controls/close_round226.py').read_text(encoding='utf-8')
for old,new in [('225','PREV'),('226','CURR'),('227','NEXT')]:s=s.replace(old,new)
for old,new in [('PREV','226'),('CURR','227'),('NEXT','228')]:s=s.replace(old,new)
s=s.replace('gc-full-goal-spectral-source-review','gc-complete-joint-spectral-remainder')
s=s.replace('len(entries)==26','len(entries)==27').replace('count==667','count==701').replace('all667','all701')
s=s.replace('actual_shifted_spectral_sources.md','joint_shift_spectral_attack.md').replace('theta_wave_full_frontiers.md','heegner_joint_norm_audit.md')
s=s.replace('blind_complex_subordination.md','blind_mellin_phase.md').replace('conductor_subordination_application.md','conductor_mellin_phase_application.md')
s=s.replace('blind_complex_subordination_statement.md','blind_mellin_phase_statement.md')
s=s.replace("assert 'not history-free' in contract(blind)","assert 'protocol.md' in contract(blind) and 'blind_mellin_phase_statement.md' in contract(blind)")
start=s.index("checkpoint=Path(");end=s.index("decision=read(base/'controls/closing_decision.json')",start)
s=s[:start]+"""reviews=[
 (base/'reviews/conductor_mellin_phase_review.md',[blind,packet]),
 (base/'reviews/independent_spectral_attack_review.md',[attack]),
 (base/'reviews/independent_heegner_norm_review.md',[profile]),
 (base/'reviews/independent_mellin_application_review.md',[control]),
 (base/'reviews/conductor_complete_frontier_review.md',[attack,profile,blind,control])]
for p,arts in reviews:
 s=contract(p)
 assert 'GREEN' in s,p
 for a in arts:assert sha(a) in s.lower(),('review binding',p,a)
"""+s[end:]
s=s.replace('[control,packet,status,checkpoint]','[control,packet]')
s=s.replace('GREEN for scoped spectral-source and subordination evidence only','GREEN for scoped joint spectral and Mellin-phase evidence only')
s=s.replace('len(gates)==11','len(gates)==10').replace('All11 gates','All10 gates')
s=s.replace('round_227_closed_identity_patch_spectral_review_no_complete_gain','round_227_closed_identity_patch_joint_spectral_no_complete_gain')
s=s.replace('Complete spectral source hypotheses, all parameters and subordination application reviewed. No complete analytic or exponent gain; upper certificates are not actual lower bounds.','Complete joint kernels, source coefficients, spectral norms and Mellin application reviewed. No complete analytic or exponent gain; certificate losses are not actual lower bounds.')
s=s.replace('Design228 only after closed227 using its independently reviewed checkpoint. Attack one complete actual signed estimate with all costs; do not repeat absolute-Abel or heat-ray certificates. Preserve full quarter goal.','Design228 only after closed227 from its reviewed complete spectral kernel and norm evidence. Retain all shifts and spectral parameters, and seek a quantified full signed estimate; formal inversion or another positive envelope is not progress.')
s=s.replace('Round227 mandatory source review closed with verified complete spectral costs and subordination controls. Identity State Patch; all401 nodes and proof-draft bytes unchanged. No complete estimate or exponent gain. Round228 analytic design pending; next mandatory review229.','Round227 complete joint spectral attempt closed with exact kernels and scoped norm/phase controls. Identity State Patch; all401 nodes and proof-draft bytes unchanged. No complete estimate or exponent gain. Round228 pending design; mandatory broad review229.')
s=s.replace('Round227 full-goal spectral-source review closure','Round227 complete joint spectral remainder closure')
s=s.replace('round227_full_goal_spectral_source_review.md','round227_complete_joint_spectral_remainder.md')
s=s.replace('hashes[checkpoint.as_posix()]=sha(checkpoint)\n','')
assert 'checkpoint.as_posix' not in s and 'status=base' not in s
assert 'count==701' in s and 'len(gates)==10' in s
out=base/'controls/close_round227.py';out.write_text(s,encoding='utf-8');compile(s,str(out),'exec')
print('Prepared227 closure only; shared state unchanged.')
