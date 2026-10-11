"""Prepare (do not run) Round226 closure using the prior read-only validator."""
from pathlib import Path
base=Path('rounds/codex-managed/gc-full-goal-spectral-source-review')
assert not (base/'controls/artifact_hashes.json').exists()
p=Path('rounds/codex-managed/gc-complete-logarithmic-convolution/controls/close_round225.py')
s=p.read_text(encoding='utf-8')
for old,new in [('224','PREVIOUSROUND'),('225','CURRENTROUND'),('226','FOLLOWINGROUND')]:
 s=s.replace(old,new)
for old,new in [('PREVIOUSROUND','225'),('CURRENTROUND','226'),('FOLLOWINGROUND','227')]:
 s=s.replace(old,new)
s=s.replace('gc-complete-logarithmic-convolution','gc-full-goal-spectral-source-review')
s=s.replace('assert len(entries)==25','assert len(entries)==26').replace('count==635','count==667').replace('all635','all667')
s=s.replace('complete_nonlinear_prime_attack.md','actual_shifted_spectral_sources.md')
s=s.replace('complete_factor_norm_audit.md','theta_wave_full_frontiers.md')
s=s.replace('blind_finite_convolution.md','blind_complex_subordination.md')
s=s.replace('conductor_complete_envelope_control.md','conductor_subordination_application.md')
s=s.replace('blind_finite_convolution_statement.md','blind_complex_subordination_statement.md')
start=s.index('reviews=[\n');end=s.index("decision=read(base/'controls/closing_decision.json')",start)
s=s[:start]+"""checkpoint=Path('strategy/gauss_circle_strategy_checkpoint_round226_2026-09-28.md')
status=base/'controls/conductor_current_primary_status.md'
reviews=[
 (base/'reviews/conductor_subordination_review.md',[blind,packet]),
 (base/'reviews/independent_shifted_source_review.md',[attack]),
 (base/'reviews/independent_theta_source_review.md',[profile]),
 (base/'reviews/independent_subordination_application_review.md',[control]),
 (base/'reviews/independent_strategy_checkpoint_review.md',[checkpoint,status]),
 (base/'reviews/conductor_complete_frontier_review.md',[attack,profile,blind,control,checkpoint])]
for p,arts in reviews:
 s=contract(p)
 assert 'GREEN' in s,p
 for a in arts:assert sha(a) in s.lower(),('review binding',p,a)
"""+s[end:]
s=s.replace("[control,packet,base/'briefs/blind_envelope_statement.md']","[control,packet,status,checkpoint]")
s=s.replace('GREEN for scoped convolution and envelope evidence only','GREEN for scoped spectral-source and subordination evidence only')
s=s.replace('round_226_closed_identity_patch_no_complete_gain','round_226_closed_identity_patch_spectral_review_no_complete_gain')
s=s.replace('Complete nonlinear convolution, all factor ranges and optimistic envelope capacity reviewed. No complete analytic or exponent gain; upper estimates are not actual lower bounds.','Complete spectral source hypotheses, all parameters and subordination application reviewed. No complete analytic or exponent gain; upper certificates are not actual lower bounds.')
s=s.replace("design_constraint='Design227 only after closed226 as the mandatory full-goal strategy/current-primary review. Compare complete signed mechanisms and all costs; retain the full quarter objective and do not repeat parameter identities or favorable local exponents.'","design_constraint='Design227 only after closed226 using its independently reviewed checkpoint. Attack one complete actual signed estimate with all costs; do not repeat absolute-Abel or heat-ray certificates. Preserve full quarter goal.'")
s=s.replace("scheduled_review='Next broad strategy/current-primary review227.'","scheduled_review='Next broad strategy/current-primary review229.'")
s=s.replace("next_strategy_checkpoint=227","next_strategy_checkpoint=229")
s=s.replace("next broad strategy/current-primary review227.","next broad strategy/current-primary review229.")
s=s.replace('Round226 closed with verified finite convolution, full factor costs and complete-envelope controls. Identity State Patch; all401 nodes and proof-draft bytes unchanged. No complete estimate or exponent gain. Mandatory strategy/current-primary review227 pending design.','Round226 mandatory source review closed with verified complete spectral costs and subordination controls. Identity State Patch; all401 nodes and proof-draft bytes unchanged. No complete estimate or exponent gain. Round227 analytic design pending; next mandatory review229.')
s=s.replace('Round226 complete logarithmic-convolution closure','Round226 full-goal spectral-source review closure')
s=s.replace('round226_complete_circle_logarithmic_convolution.md','round226_full_goal_spectral_source_review.md')
s=s.replace("write(base/'controls/artifact_hashes.json',hashes)","hashes[checkpoint.as_posix()]=sha(checkpoint)\nwrite(base/'controls/artifact_hashes.json',hashes)")
assert 'blind_envelope' not in s and 'convolution and envelope' not in s
assert "len(gates)==11" in s and 'count==667' in s
out=base/'controls/close_round226.py'
out.write_text(s,encoding='utf-8')
compile(s,str(out),'exec')
print('Prepared Round226 closure validator; not executed, shared state unchanged.')
