"""Serialize the conductor's completed mathematical review decision."""
from pathlib import Path
import json,hashlib
root=Path.cwd();rel=Path('rounds/codex-managed/gc-actual-upper-tail-a');base=root/rel
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
review_names=['independent_signed_tail_review.md','independent_actual_controls_review.md','independent_complete_restoration.md','conductor_blind_analytic_review.md']
expected={
 'independent_signed_tail_review.md':'dbcb1eb37c35c50e9cf69220ed235708de8252e9fde7737f79809bd6c93e8235',
 'independent_actual_controls_review.md':'90626beac5b2bb38331884b13d4d493599c7a540688d5e6d8684d86aadcb2a48',
 'independent_complete_restoration.md':'596521a43af94c57c2fba8e5698128bf40aceb512d0bf3a7cdc36b77094fe103'}
for name,h in expected.items(): assert sha(base/'reviews'/name)==h
paths=[base/'reviews'/n for n in review_names]+[base/'candidates/conductor_tail_restoration.md',base/'candidates/conductor_seam_repairs.md',base/'synthesis.md']
reason='Bounded target-A attempt isolates sufficient actual exceptional-set quadratic saving a*=10beta-32/25, but obtains no such saving. Exact product representation and actual localized covariance controls rule out only the tested first-average/uniform-pair-decorrelation shortcuts. Independent review passes after the explicit theta convention repair. Accepted complete10beta and all parent/quarter statuses remain unchanged.'
status='''# Round231 closed: upper-tail A remains open

11 October2026. The user-authorized bounded analytic attempt is complete, with three frozen initial reports, four nonauthor review seams, bounded controls and one localized convention repair. No complete moment or pointwise improvement was proved. This is attempt1 on the adopted upper-tail premise; earlier Round231-labelled strategy packets were prelaunch evidence.

The useful sufficient target is now explicit: for actual F_(16/125), the quadratic energy on {|F|>T^(16/125)} should be bounded by T^(-a*+epsilon), a*=10beta-32/25=0.009663519481... . Its signed reciprocal-product version requires T^(2-a*+epsilon) on the same actual exceptional set. These estimates remain unproved. Exact resonance zeros and small signed first means cannot replace this bound. Actual positive, negative and disjoint covariance controls exclude uniform pairwise decorrelation at their stated component scope; they do not disprove target A.

Both distribution terms, the threshold boundary, all errors and the exact L/F/H restoration are paid conditionally. Complete32/25 would improve moments only, giving the weaker pointwise consequence207/650. The correct accepted relation is theta=(1+2beta)/4. The graph's401 nodes, accepted exponent10beta=1.289663519481..., pointwise benchmark0.314483175974..., and proof-draft bytes are unchanged under a validated identity State Patch. Quarter, M1/M2 and endpoint obligations remain open; accepted216 is only its stated twelfth-order reduction.

Strategy now requires a quantitative estimate for actual restricted weighted aggregate correlations, including the rigid same-two-adic sector. Another exact transform or a generic odd-kernel argument does not reset the attempt count. Reassess after at most two attempts on unchanged premises. Round232 is pending design with no tasks and no automatic launch.

Authoritative round record: rounds/codex-managed/gc-actual-upper-tail-a/synthesis.md. Reviews and controls are in that campaign; mechanical closure is recorded in controls/closure_validation.json. Historical snapshots below describe earlier states and are not current launch instructions.'''
barrier='''# Round231 closed barrier and strategy packet

- Target A and its integrated alternative remain OPEN. No actual high-tail lower bound or all-method impossibility was proved.
- The sufficient energy Q_tail<=T^(-a*+epsilon), a*=10beta-32/25, must retain the actual full-F exceptional set. The signed product covariance budget is T^(2-a*), with both amplitude and radius Jacobian paid.
- Small signed first averages, kernel oddness and a slow-window covariance are not this exceptional-set bound. Positive near covariance survives oddness.
- Same-two-adic frequencies have rigid character signs on each product-difference class. Actual localized components refute uniform power-saving pairwise decorrelation for every distinct pair. Mixed-valuation alternation requires actual weight/range control.
- One product packet has size at most T^(-1/2+epsilon); high events require at least T^(157/250-epsilon) distinct signed packets in a rectangle. This is a necessary count, not an event-probability estimate.
- Nearest-q identities require unique ownership; the second-Poisson all-q formula instead has genuine distinct Fourier indices. Boundary ties include both aliases. The negative branch is conjugate.
- Both tails, the threshold boundary, all smooth transitions, infinite complementary tail, small factors and summed errors remain paid. No arbitrary-mask ceiling or automatic F/C threshold-tail equivalence is allowed.
- Accepted theta=(1+2beta)/4; conditional32/25 is a moment milestone only. Attempt1 closed without a complete gain; no Round232 launch.

Evidence: rounds/codex-managed/gc-actual-upper-tail-a/synthesis.md, frozen reports, nonauthor reviews and controls. These scoped controls do not reject aggregate signed cancellation.'''
gate_specs=[
 ('actual_family','green_actual_full_band_and_fixed_coefficients','briefs/actual_interface.md'),
 ('second_poisson','green_exact_sign_factor_and_distinct_fourier_indices','reviews/independent_signed_tail_review.md'),
 ('actual_covariance','green_scoped_positive_negative_disjoint_controls','reviews/independent_actual_controls_review.md'),
 ('blind_independence','green_statement_only_frozen_before_context_expansion','reports/blind_odd_kernel_covariance.md'),
 ('blind_analytic_review','green_exact_covariance_boundaries_and_discrepancy','reviews/conductor_blind_analytic_review.md'),
 ('exceptional_set','green_sufficient_inequality_explicitly_unproved','reviews/independent_signed_tail_review.md'),
 ('all_scales_errors','green_complete_band_tail_and_restricted_error_paid','reviews/independent_signed_tail_review.md'),
 ('complete_restoration','green_both_tails_boundary_ceiling_and_complements','reviews/independent_complete_restoration.md'),
 ('theta_repair','green_localized_repair_independently_verified','candidates/conductor_seam_repairs.md'),
 ('finite_controls','green_exact_and_detuned_diagnostic_controls','controls/control_manifest.md'),
 ('scope_and_no_gain','green_no_actual_tail_disproof_or_unearned_promotion','synthesis.md'),
 ('source_scope','green_no_new_external_theorem_import','synthesis.md')]
decision={
 'round_index':231,'campaign_id':'gc-actual-upper-tail-a','conductor_review_complete':True,
 'result':'upper_tail_A_attempt_closed_without_complete_gain','reason':reason,
 'reviewed_artifact_hashes':{p.relative_to(root).as_posix():sha(p) for p in paths},
 'gates':[{'id':'round231_'+name,'status':status,'artifact':(rel/path).as_posix()} for name,status,path in gate_specs],
 'interventions':['Bounded initial work stopped at a precise exceptional-set gap; no additional discovery cycle launched.','Four nonauthor seams completed. Independent review corrected only the conductor theta convention against a frozen original; correction verified.','Close attempt1 with an identity patch after green scoped gates; preserve all accepted parents and historical artifacts.'],
 'assessment':{'complete_moment_gain':False,'pointwise_gain':False,'target_A_proved':False,'target_A_disproved':False,'new_actual_component_controls':True,'independent_review_complete':True,'attempts_on_current_premise_completed':1,'terminal_label':'upper_tail_A_attempt_closed_without_complete_gain'},
 'future_constraint':'No successor is designed or launched. Use closed231 evidence to select one quantitative actual exceptional-set/aggregate-correlation objective, or revise the mechanism. Pay the rigid collision sector and full owners; an equivalent transform does not reset attempt1. Reassess after at most two attempts on unchanged premises; preserve other complete routes.',
 'status_summary':status,'barrier_summary':barrier}
(base/'closure_decision.json').write_text(json.dumps(decision,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Conductor decision serialized: four completed review seams; one verified localized repair; no complete gain.')
