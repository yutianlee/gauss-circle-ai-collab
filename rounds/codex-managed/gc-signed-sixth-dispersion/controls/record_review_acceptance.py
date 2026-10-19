"""Record the conductor's manually completed final-hash review acceptance."""
from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
b=Path('rounds/codex-managed/gc-signed-sixth-dispersion')
expected={
 'candidates/conductor_signed_sixth.md':'cee1d243f21577e090acb0f9387c0412f4f70748b918aa3661e64db15586a8f3',
 'reports/actual_sixth_bridge.md':'e7e1b99ab4b62fb94d66b7f8c1c16b88d6e3bb9f891405da1b4d3c2e697795b6',
 'reports/signed_fraction_dispersion.md':'9406863b09750d841adde32c46b71e3581c529de76e5d48a46a1902d1532c253',
 'reports/blind_packet_control.md':'755a6e08d18868c02b6a3bdb971b66ff1709496fd845c41bee8006ed8aef89c0',
 'reviews/actual_bridge_review.md':'76385d6f494ac64dfdf5bd58f482d25932ebfbda37c1cce491b92c7a7fce3dcc',
 'reviews/arithmetic_dispersion_review.md':'ab7773bc7960ff4b137c0b9b5ea207af23cc90733a3ab5b3b86caf4e1ea58d36',
 'reviews/complete_scope_review.md':'98cf6624da2395606671f7544de280590eb25781d88eccfb331f9b4989202f56'}
for n,h in expected.items():assert hashlib.sha256((b/n).read_bytes()).hexdigest()==h,n
for n in ['reviews/conductor_blind_packet_review.md','controls/control_manifest.md','controls/source_check.md','controls/exact_local_controls.json']:
 expected[n]=hashlib.sha256((b/n).read_bytes()).hexdigest()
out={'round_index':235,'accepted_at':datetime.now(timezone.utc).isoformat(),'conductor_manually_read_final_reviews':True,'all_required_seams_passed':True,'accepted_hashes':expected,'seams':{'actual_bridge':'PASS; all-class variance, finite absorption, two-term full Hankel error, width/transitions/tails, Jacobian, complete complementary costs and exact margin.','arithmetic_dispersion':'PASS; both character branches, exact grouping, signed square and nonsquare freeze, endpoint BV, paired and single-denominator budgets, actual primitive fraction count and full-window absolute-certificate signs.','complete_scope':'PASS only for retained evidence and identity State Patch; actual versus artificial controls separated; signed nonpaired estimate open.'},'clarifications':['Candidate controls scope: uniform blockwise S6 is sufficient only. Full-band M6 is equivalent to its full-band one-sided distinct-six target; no reverse blockwise implication is proved.','Frozen bridge roman-font escapes are presentation defects only; candidate writes the unambiguous all-squarefree index.','Actual absolute-certificate lower bound is not a signed physical moment lower bound.','No material repair was needed after the final candidate was frozen; no frozen report was rewritten.'],'mathematical_target_passed':False,'state_effect':'identity; no complete moment, pointwise, parent or quarter gain'}
(b/'controls/review_acceptance.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'review_acceptance_recorded':True,'seams':3,'complete_gain':False}))
