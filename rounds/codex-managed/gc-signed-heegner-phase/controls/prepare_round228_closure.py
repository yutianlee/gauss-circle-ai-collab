"""Prepare, but do not execute, the round228 identity closure operation."""
from pathlib import Path
base=Path('rounds/codex-managed/gc-signed-heegner-phase')
assert not (base/'controls/artifact_hashes.json').exists()
src=Path('rounds/codex-managed/gc-complete-joint-spectral-remainder/controls/close_round227.py').read_text(encoding='utf-8')
replacements=[
 ('gc-complete-joint-spectral-remainder','gc-signed-heegner-phase'),
 ('joint_shift_spectral_attack','signed_hecke_functional_attack'),
 ('heegner_joint_norm_audit','complete_eisenstein_pairing'),
 ('blind_mellin_phase','blind_gamma_transition'),
 ('conductor_mellin_phase_application','conductor_gamma_application'),
 ('conductor_mellin_phase_review','conductor_gamma_transition_review'),
 ('independent_spectral_attack_review','independent_signed_hecke_review'),
 ('independent_heegner_norm_review','independent_eisenstein_review'),
 ('independent_mellin_application_review','independent_gamma_application_review'),
 ('round227_complete_joint_spectral_remainder','round228_signed_heegner_phase'),
 ('200--226','200--227'),('200_through226','200_through227'),
 ('<=226','<=227'),('==27 and','==28 and'),('701','732'),
 ('successor228','successor229'),('next_round=228','next_round=229'),
 ('round_index=228,status=\'pending_design\'','round_index=229,status=\'pending_design\''),
 ('Design228 only after closed227 from its reviewed complete spectral kernel and norm evidence. Retain all shifts and spectral parameters, and seek a quantified full signed estimate; formal inversion or another positive envelope is not progress.',
  'Design the mandatory broad strategy/current-primary review229 only after closed228. Assess the full goal, the complete cusp remainder and the reviewed continuous component; do not count a formal identity or paid component as a complete-wave bound.'),
 ('Round228 pending design','Round229 mandatory strategy review pending design'),
 ('leave228','leave229'),
 ('GREEN for scoped joint spectral and Mellin-phase evidence only','GREEN for scoped signed Heegner and gamma-transition evidence only'),
 ('joint spectral and Mellin-phase evidence','signed Heegner and gamma-transition evidence'),
 ('complete joint spectral remainder closure','signed Heegner phase closure'),
 ('complete joint spectral attempt closed with exact kernels and scoped norm/phase controls','signed Heegner phase attempt closed with scoped transform and component estimates'),
 ('Complete joint kernels, source coefficients, spectral norms and Mellin application reviewed. No complete analytic or exponent gain; certificate losses are not actual lower bounds.',
  'Signed Heegner transform, complete continuous component, gamma application and full costs reviewed. No complete-wave analytic or exponent gain; certificate losses are not actual lower bounds.'),
 ('joint_spectral_no_complete_gain','signed_heegner_no_complete_gain'),
 ('No complete estimate or pointwise exponent gain','No complete-wave estimate or pointwise exponent gain'),
 ('No complete estimate or exponent gain','No complete-wave estimate or exponent gain'),
 ('round227','round228'),('Round227','Round228'),('Close227','Close228'),
 ('round_index=227','round_index=228'),("['round_index']==227","['round_index']==228"),
 ("['active_round']==227","['active_round']==228"),
 ('"round_index": 227,','"round_index": 228,'),
 ('round_227','round_228'),('predecessor_round=227','predecessor_round=228')]
for a,b in replacements:src=src.replace(a,b)
# Keep archive endpoint227 and next229; the preceding scoped substitutions
# deliberately do not globally rewrite every occurrence of the integers.
compile(src,'close_round228.py','exec')
(base/'controls/close_round228.py').write_text(src,encoding='utf-8',newline='\n')
print('Prepared close_round228.py; closure NOT executed.')
