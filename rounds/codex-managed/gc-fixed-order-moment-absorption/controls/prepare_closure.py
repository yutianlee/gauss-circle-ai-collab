"""Materialize the conductor's narrow promotion decision after reading all final reviews."""
from pathlib import Path
import json,hashlib
root=Path.cwd(); rel=Path('rounds/codex-managed/gc-fixed-order-moment-absorption');base=root/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
expected={
'reviews/independent_actual_kernel_review.md':'1e4a4bce7f60fb9c705d82c35becaf8de99ea86658ea966e495fa5796ab78452',
'reviews/independent_scope_restoration_review.md':'a9dbc1250a9eccf2314212c9d547801c33b8128f6623324d4978191eac2c1729',
'reviews/independent_finite_absorption_review.md':'c744e8111fda2b26ad7fbb771523dd98b9893fd35ad07b3244d1e445948448b6',
'reviews/finite_absorption_final_hash_supplement.md':'43399ef50d39f91972a02990a4455e1cc51dabee1a822dc10edee48bb5c32ff1',
'candidates/conductor_fixed_order_kernel.md':'b1097aa498d0430d5bbe81fb0b8927cc4ffdf278ce838b3ef38f555bc75c31d0'}
for p,h in expected.items(): assert sha(base/p)==h,(p,'frozen hash changed')
files=[p for folder in ['reports','reviews','candidates','briefs'] for p in (base/folder).glob('*.md')]
files += [base/'synthesis.md',base/'controls/control_manifest.md',base/'controls/wolfram_checks.wl',base/'controls/wolfram_result.json',base/'controls/exact_local_controls.py',base/'controls/exact_local_controls.json']
reviewed={p.relative_to(root).as_posix():sha(p) for p in files}
node_id='GC-complete-fixed-even-moment-distinct-absorption'
kernel='proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md'
positive=[kernel]+[(rel/p).as_posix() for p in ['candidates/conductor_fixed_order_kernel.md','reports/actual_fixed_order_bridge.md','reports/hostile_bridge_audit.md','reports/blind_partition_absorption.md','reviews/conductor_blind_absorption_review.md','reviews/independent_finite_absorption_review.md','reviews/finite_absorption_final_hash_supplement.md','reviews/independent_actual_kernel_review.md','reviews/independent_scope_restoration_review.md','candidates/review_repair_record.md','synthesis.md']]
statement=('Fix the nonnegative real radial smooth unit-mass mollifier rho supported in the unit disk, Psi(s)=rho-hat(s e1), and nonnegative smooth w supported[1/2,2], equal1 on[1/sqrt(2),sqrt(3)]. '
'For real T>=2 define a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)), f_d(R)=sum_(s>=1)a_(d s^2)(T)cos(2pi R s sqrt(d)-3pi/4) for squarefree d, B_T=sum_d f_d, L_Q=sum_(d<=Q)f_d, Z_Q=sum_(d>Q)f_d, V_Q=sum_(d>Q)f_d^2 for real Q>=1. '
'Let p>=2 be any fixed even integer independent of T, E_(p,Q) the ordered pairwise-distinct d_1,...,d_p>Q product sum, I_(p,Q)=integral w E_(p,Q), M_p(F)=integral w|F|^p, and J_(p,Q)=integral w V_Q^(p/2). '
'For every0<delta<1, integral w|Z_Q^p-E_(p,Q)|<=delta M_p(Z_Q)+C_(p,delta)J_(p,Q), where C=(p!-1)max(1,((p!-1)/delta)^((p-2)/2)). '
'Thus (1-delta)M_p(Z_Q)<=I_(p,Q)+CJ, I_(p,Q)>=-CJ and |I_(p,Q)|<=(1+delta)M_p(Z_Q)+CJ. '
'For every sufficiently small eta>0, J<<_(p,eta)T Q^(-p/4+eta), while M_p(L_Q)<<_p T Q^(p/4). All harmonics and infinite tails converge absolutely for each fixed T and are retained. '
'At Q=1, the full B_T moment, Z_Q moment, |I_(p,Q)| bound and one-sided I_(p,Q) upper bound at T^(b+epsilon) are equivalent for every b>=1, with each bound quantified for every epsilon>0. '
'At Q=floor(T^(1/p)), the same holds for b>=5/4, or b>=h_p=1+(p-136/13)_+/(4p) using the inherited coefficient-mask distribution; that optional head proof is restricted to1<=Q<=T. '
'For a complete normalized moment exponent b>=1, sharp reconstruction and inclusive-count persistence give exponent1/4+(1+2b)/(4(p+1)). An unbounded sequence of fixed even orders with actual one-sided signed exponents b_p=o(p) would imply the quarter theorem, after paying the head floor. '
'Those signed estimates are not proved. Constants may depend arbitrarily on fixed p; no p growing with T, no tuplewise absolute estimate, no stronger additive replacement of216, no improved full moment or pointwise exponent, and no M1/M2/GAR/endpoint or quarter proof is asserted.')
node={'id':node_id,'type':'lemma','track':'proof_infrastructure','status':'proved_internal','title':'Complete fixed-even-order distinct-squarefree-class reduction by relative absorption','statement_tex':statement,'dependencies':['H1-H3','Divisor-bound-elementary','GC-complete-square-root-large-values-moment-bound','GC-complete-distinct-radical-twelfth-reduction','GC-weighted-square-root-exact-resonance-mass'],'implies':[],'blockers':[],'evidence':{'positive':positive,'negative':[],'inconclusive':[(rel/'controls/control_manifest.md').as_posix()]},'owner':'Codex conductor','next_action':'Prove an actual signed distinct-class aggregate upper bound with a complete improved budget; a b_p=o(p) family at unbounded fixed even orders would suffice for quarter. Preserve signed cancellations and the accepted absolute-certificate obstruction. The reduction alone improves no complete exponent.'}
reason='Accept one reviewed all-fixed-even-order relative-absorption and complete actual distinct-class reduction. Repeated-class terms are absorbed without a baseline beta cost; Q=1 pays head and defect at O(T), and the growing cutoff has explicit paid budgets. The actual signed-integral estimates remain open. No complete moment, pointwise exponent or target parent is improved.'
patch={'round_index':233,'campaign_id':'gc-fixed-order-moment-absorption','starting_graph_sha256':'a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b','proof_obligations':{'create':[node],'update':[],'correct_rejected':[],'reject':[],'no_change':['GC-target','Conditional-bridge','M9','M9-M1','M9-M2','M9-endpoint-uniformity','GC-external-Li-Yang-theta-star','GC-complete-square-root-large-values-moment-bound','GC-complete-distinct-radical-twelfth-reduction','GC-distinct-radical-absolute-certificate-obstruction']},'round_assessment':{'terminal_label':'fixed_order_absorption_reduction_reviewed','reason':reason},'reversibility':{'remove_created_ids':[node_id],'rule':'Remove only the new node to recover the original semantic graph; original bytes are preserved in the prelaunch snapshot. Replay differs only in new-node timestamp, normalized for comparison.'}}
write(base/'state_patch.json',patch)
specs=[
('finite_identity','self_contained_permutation_proof','reviews/conductor_blind_absorption_review.md'),
('blind_initial','statement_only_frozen_before_expansion','reports/blind_partition_absorption.md'),
('finite_final_hash','unchanged_finite_integral_scope','reviews/finite_absorption_final_hash_supplement.md'),
('actual_family','all_harmonics_square_sum_and_real_cutoffs','reviews/independent_actual_kernel_review.md'),
('signed_integral','negative_part_and_nonnegative_offset','reviews/independent_scope_restoration_review.md'),
('head_refinement','A13_repaired_range_verified','reviews/independent_actual_kernel_review.md'),
('sharp_restoration','amplitude_jacobian_smoothing_persistence','reviews/independent_scope_restoration_review.md'),
('fixed_order','p_selected_before_T_no_uniformity_claim','reviews/independent_scope_restoration_review.md'),
('wolfram_controls','exact_coefficients_independently_reproduced','controls/control_manifest.md'),
('repair_provenance','original_retained_final_hash_reviewed','candidates/review_repair_record.md'),
('source_scope','inherited_qualifications_no_new_import','synthesis.md'),
('reduction_only','signed_targets_and_complete_exponents_unchanged','synthesis.md')]
gates=[{'id':'round233_'+i,'status':'green_'+s,'artifact':(rel/a).as_posix()} for i,s,a in specs]
summary='''# Round233 closed: fixed-order absorption reduction accepted

12 October2026 Asia/Shanghai. One new narrow lemma, GC-complete-fixed-even-moment-distinct-absorption, supplies the complete distinct-squarefree-class reduction at every fixed even order. The relative inequality |Z^p-E_p|<=delta|Z|^p+C_(p,delta)V^(p/2) absorbs repeated classes into the unknown moment. For the actual full wave and Q=1, both head and absorption budgets are O_p(T); one-sided signed-integral bounds are equivalent to full moment bounds above that floor. All harmonics, signs, tails and real endpoints are retained.

For Q=floor(T^(1/p)), the defect is T^(3/4+epsilon), the elementary head is T^(5/4), and the optional accepted-distribution head exponent is h_p=1+(p-136/13)_+/(4p). Its layer-cake refinement is restricted to1<=Q<=T. The current complete exponents do not improve: an actual signed estimate remains missing. The graph now has402 nodes with all401 prior nodes unchanged;216's stronger additive twelfth-order lemma is preserved.

An unbounded sequence of fixed even orders with actual signed exponents b_p=o(p) would imply quarter after complete sharp restoration. This is an unproved target family, not an established bound. Choose p before T; constants need not be uniform in p. The absolute distinct-tuple certificate remains insufficient by the accepted T^(p/4-1/2) obstruction, which is not a lower bound for signed I.

Three frozen initial reports, statement-only rederivation, final-hash nonauthor reviews, one optional-head scope repair, and bounded Wolfram checks independently reproduced locally are complete. The State Patch adds only the reduction; the proof draft is appended after validation. Complete10beta, pointwise0.314483175974..., target A and all quarter/M1/M2/endpoints remain unchanged/open as before.

The two earlier local upper-tail attempts remain closed and their reassessment remains in force. Future research must estimate the actual signed aggregate with a concrete arithmetic mechanism and complete costs. Round234 is pending design, has no tasks and is not automatically launched.

Authoritative record: rounds/codex-managed/gc-fixed-order-moment-absorption/synthesis.md. Accepted kernel: proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md. Mechanical validation: controls/closure_validation.json in that campaign. Historical snapshots below are retained evidence, not current launch instructions.'''
barrier='''# Round233 closed strategy and barrier update

- All-fixed-even-order relative absorption is now accepted. It pays repeated-class terms by delta M_p+C J, not by the baseline T^((p-4)beta) ceiling. This is a new complete reduction, not a signed moment estimate.
- I_p and E_p can be negative; keep the offset C J and its negative-part bound. At Q=1, J and the complete small-class head cost O_p(T).
- For floor(T^(1/p)), the head floor is at most5/4, refined to1+(p-136/13)_+/(4p). The optional head derivation has1<=Q<=T. Floors, all harmonics and every mixed head/tail term are paid.
- The actual signed I_(p,Q) upper bounds remain OPEN. Distinct radicals give nonzero frequencies only. The accepted absolute-certificate lower bound T^(p/4-1/2) applies to the chosen cutoffs and bars a tuplewise absolute route to sublinear order exponents; it is not a lower bound for signed I.
- p is fixed before T. Large p-dependent constants are harmless only with this quantifier order; do not set p=p(T).
- Retain216's stronger additive twelfth-order result. The relative reduction does not overwrite it and produces no complete moment or pointwise gain by itself.
- Previous upper-tail attempt count remains2. No third relabeled local product cutoff attempt is authorized by this new bridge. A successor needs a concrete actual aggregate mechanism with a quantified complete implication and tests; a conjectured lemma may be admitted for bounded exploration.

Evidence: rounds/codex-managed/gc-fixed-order-moment-absorption/synthesis.md and the reviewed accepted kernel.'''
draft='''## Round233 accepted fixed-even-order relative reduction

The accepted node `GC-complete-fixed-even-moment-distinct-absorption` extends the complete signed distinct-class interface to every fixed even p>=2. For the actual complete squarefree-class tail, with Z=sum f_d, V=sum f_d^2 and E_p the ordered distinct polynomial,

    integral w|Z^p-E_p|<=delta M_p(Z)+C_(p,delta) integral w V^(p/2).

The variance-power term is O_(p,epsilon)(T Q^(-p/4+epsilon)). At Q=1 it and the complete small-class head cost O_p(T). Hence full B_T and Z_Q moment bounds at any exponent b>=1 are equivalent to a one-sided upper bound on signed I_p=integral w E_p. The negative part is explicitly paid; I_p is not assumed positive. All harmonics and tails remain.

For Q=floor(T^(1/p)), the elementary head floor is5/4, or h_p=1+(p-136/13)_+/(4p) using the accepted distribution refinement restricted to1<=Q<=T. Full sharp reconstruction gives pointwise exponent1/4+(1+2b)/(4(p+1)) for a paid complete b>=1. Thus actual signed estimates b_p=o(p) along unbounded fixed even orders would imply quarter. Those estimates remain unproved; p must be chosen before T.

This adds a reduction only. It does not improve any complete moment or pointwise exponent, prove target A, or close M1/M2/GAR/endpoints. Round216's stronger additive p12 statement and every older node remain unchanged. Proof: `proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md`; review and validation: `rounds/codex-managed/gc-fixed-order-moment-absorption/`.
'''
decision={'round_index':233,'campaign_id':'gc-fixed-order-moment-absorption','conductor_review_complete':True,'promote_reduction_only':True,'result':'fixed_order_absorption_reduction_reviewed','reason':reason,'new_node_id':node_id,'kernel_path':kernel,'candidate_path':(rel/'candidates/conductor_fixed_order_kernel.md').as_posix(),'candidate_sha256':expected['candidates/conductor_fixed_order_kernel.md'],'reviewed_artifact_hashes':reviewed,'gates':gates,'interventions':['Three initial reports frozen; finite statement-only isolation preserved before expanded review.','One literal optional-head range repair independently requested and verified at final hash; no original report changed.','Wolfram exact checks reproduced locally; computation diagnostic only.','Promote one narrow reduction after green reviews and graph preflight; preserve all previous nodes and complete powers.'],'assessment':{'new_complete_reduction':True,'complete_moment_gain':False,'pointwise_gain':False,'target_A_proved':False,'quarter_proved':False,'independent_review_complete':True,'prior_upper_tail_attempts_completed':2},'future_constraint':'No successor launched. Use the newly accepted all-fixed-order absorption bridge only with a concrete actual signed aggregate mechanism and full costs; repeated finite identities or tuplewise absolute certificates supply no estimate. The b_p=o(p) fixed-order signed family remains open. Previous two-attempt upper-tail reassessment remains in force.','status_summary':summary,'barrier_summary':barrier,'draft_addition':draft}
write(base/'closure_decision.json',decision)
print(json.dumps({'promotion_decision_prepared':True,'new_node':node_id,'reviewed_artifacts':len(reviewed),'green_gates':len(gates)}))
