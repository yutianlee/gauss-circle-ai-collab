"""Write the conductor's reviewed decision and instantiate identity closure tooling."""
from pathlib import Path
import json, hashlib

root=Path.cwd()
rel=Path('rounds/codex-managed/gc-upper-tail-separated-products')
base=root/rel
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
expected={
    'reviews/independent_near_payment_review.md':'c86d66d3c55b5fd383a633f4ff623e4693ccd6feb2093fd9fbc93499db2d8ac5',
    'reviews/independent_separated_attack_review.md':'5e1376071332139a25c392b503f737f02d9e9db65514667f8448fe6b4835bc9e',
    'reviews/independent_collision_ledger_review.md':'0dda72b831a6bb160fc14aded69f808c58740330659da09a663260667a80de14',
}
for name,h in expected.items(): assert sha(base/name)==h,(name,'review freeze changed')
files=[p for folder in ['reports','reviews','candidates','briefs'] for p in (base/folder).glob('*.md')]
files += [base/'synthesis.md',base/'controls/control_manifest.md',base/'controls/exact_controls.py',base/'controls/exact_controls.json']
reviewed={p.relative_to(root).as_posix():sha(p) for p in files}
specs=[
('actual_family','actual_full_band_actual_E_all_q','briefs/actual_interface.md'),
('near_payment','all_product_close_absolute_bound','reviews/independent_near_payment_review.md'),
('high_gcd','distinct_pairs_and_all_original_labels','reviews/independent_separated_attack_review.md'),
('atomic_tails','absolute_elementary_local_and_exterior_mixed_tails','reviews/independent_collision_ledger_review.md'),
('blind_isolation','initial_statement_only_frozen_before_expansion','reports/blind_packet_band.md'),
('blind_lemma','band_cross_families_nonlinear_scope','reviews/conductor_blind_band_review.md'),
('small_gcd_control','component_uniform_scope_only_not_actual_E','reviews/independent_separated_attack_review.md'),
('residual_identity','disjoint_sectors_original_E_and_errors','reviews/independent_collision_ledger_review.md'),
('complete_restoration','conditional_both_tails_threshold_and_full_owners','reviews/independent_near_payment_review.md'),
('finite_controls','exact_diagnostic_checks_pass','controls/control_manifest.md'),
('strategy_reassessment','two_attempt_review_completed_no_automatic_successor','candidates/strategy_reassessment.md'),
('source_scope_no_gain','no_new_import_no_complete_promotion','synthesis.md'),
]
gates=[{'id':'round232_'+i,'status':'green_'+s,'artifact':(rel/a).as_posix()} for i,s,a in specs]
reason=('Nearby products cost T^(-3/250+epsilon), and distinct high-gcd products cost T^(-9/500+epsilon), with all atomic tails and errors paid. '
        'The actual separated small-gcd signed energy saving a*=10beta-32/25 remains open. Independent reviews pass with explicit atomic-tail and component-control scope supplements. '
        'The required two-attempt strategy reassessment is complete; no complete moment or pointwise gain and no accepted graph change.')
summary='''# Round232 closed: two collision sectors paid; complete upper-tail gain open

12 October2026 Asia/Shanghai. The continued bounded attempt is complete, with three frozen reports, independent review, exact finite controls and the mandatory reassessment after attempt2. Nearby products at distance at most sqrt(T) cost T^(-3/250+epsilon); the remaining distinct products with gcd(h,h')>=T^(1/4) cost T^(-9/500+epsilon). Both lie below the required energy power-a*, a*=10beta-32/25=0.009663519481... . All modes, elementary cross terms, tails, errors and the original exceptional set are retained.

The precise missing estimate is the one-sided signed aggregate over product gaps>sqrt(T) and gcd(h,h')<T^(1/4), on E={|F_(16/125)|>T^(16/125)}. Q_E(F) equals that remainder up to O(T^(-3/250+epsilon)). The actual small-gcd control rejects only a uniform pointwise alternation/variation certificate across smooth components; it neither disproves target A nor estimates the full event. Component bounds remain reviewed evidence, not accepted complete mathematics.

An identity State Patch preserves the401-node graph and proof draft. Complete10beta=1.289663519481... and the pointwise benchmark0.314483175974... remain unchanged. Complete32/25 is still conditional and would give the weaker pointwise207/650. Quarter, M1/M2 and endpoints remain open; Round216 is only its stated twelfth-order reduction.

The two-attempt review ends this elementary local-count/termwise-alternation cycle. Any new attempt needs a concrete aggregate arithmetic mechanism or a different complete parent, with an explicit conjectured lemma, a bypass of existing controls, full conditional costs and falsification tests. It need not prove its lemma before exploratory admission. Equivalent transforms or cutoff changes do not reset the attempt count. Round233 is pending design, has no tasks and is not automatically launched.

Authoritative record: rounds/codex-managed/gc-upper-tail-separated-products/synthesis.md. Strategy reassessment: candidates/strategy_reassessment.md in that campaign. Mechanical closure: controls/closure_validation.json. Historical snapshots below are retained evidence, not current instructions.'''
barrier='''# Round232 closed barrier packet

- Near products up to sqrt(T) and separated gcd(h,h')>=T^(1/4) are paid at powers-3/250 and-9/500 on the original E. Exact products are in the first sector; preserve disjoint ownership.
- Remaining signed small-gcd separated energy at-a*=-(10beta-32/25) is OPEN. The full signed zero-power bound cannot be used to cap an unsigned subcollection; its elementary absolute certificate costs T^(29/125+epsilon).
- Apply local product truncation to A_p=sum of absolute elementary labels. Rapid atomic l1 tails pay every mixed term. Grouped cancellation alone cannot control an h-selected sector.
- The close matrix is not PSD. Blind nonlinear diagonal interpolation is valid, but a cost-free linear transfer is false at generic-envelope scope.
- Small-gcd progressions are wider than the packets; odd-odd CRT centers need not vary slowly across differences. The actual h=T,h'=T+4 control refutes only smooth-component-uniform pointwise alternation/variation savings, including fixed refinements. No actual E lower bound or unsplit/full aggregate impossibility follows.
- Actual coefficients, all odd modes, real branches, both tails, threshold, exact complementary owners and selected-set errors remain mandatory. Complete32/25 remains conditional and is not a pointwise benchmark gain.
- Two unchanged-premise attempts are complete and the required reassessment is recorded. Do not auto-launch a third local-cutoff or transform variant. New exploratory admission requires a materially different quantified mechanism; it may start from a precise conjectured lemma.

Evidence: rounds/codex-managed/gc-upper-tail-separated-products/synthesis.md and its reports, independent reviews, controls and strategy reassessment.'''
decision={
'round_index':232,'campaign_id':'gc-upper-tail-separated-products','conductor_review_complete':True,
'result':'separated_product_attempt_closed_without_complete_gain','reason':reason,
'reviewed_artifact_hashes':reviewed,'gates':gates,
'interventions':[
'Three initial tasks and one bounded nonauthor review cycle completed; all initial reports remain frozen.',
'Explicit absolute-elementary tail supplement and precise smooth-component control quantifier incorporated in synthesis.',
'Mandatory two-attempt strategy reassessment completed before identity closure; no automatic successor.'],
'assessment':{'complete_moment_gain':False,'pointwise_gain':False,'target_A_proved':False,'target_A_disproved':False,
'new_actual_component_bounds':True,'independent_review_complete':True,'attempts_on_current_premise_completed':2,
'mandatory_strategy_reassessment_complete':True,'terminal_label':'separated_product_attempt_closed_without_complete_gain'},
'future_constraint':'No successor designed or launched. Two same-premise attempts and mandatory reassessment are complete. Before a new analytic attempt, specify a materially different aggregate arithmetic mechanism or complete parent, its precise conjectured lemma, previous obstruction bypassed, independently checked complete costs and falsification controls. A new proof is not required for exploratory admission. Cutoff changes and equivalent transforms do not reset attempt2.',
'status_summary':summary,'barrier_summary':barrier,
}
(base/'closure_decision.json').write_text(json.dumps(decision,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

# Reuse the proven closure machinery only in this new campaign, retaining old bytes.
src=(root/'rounds/codex-managed/gc-actual-upper-tail-a/controls/close_round231.py').read_text(encoding='utf-8')
src=src.replace('gc-actual-upper-tail-a','gc-upper-tail-separated-products')
src=src.replace('upper_tail_A_attempt_closed_without_complete_gain','separated_product_attempt_closed_without_complete_gain')
src=src.replace('232','233').replace('231','232')
src=src.replace('attempts_on_current_premise_completed=1','attempts_on_current_premise_completed=2')
src=src.replace("'attempt_count':1","'attempt_count':2")
src=src.replace('Actual exceptional-set quadratic energy saving a*=10beta-32/25; equivalent sufficient signed product covariance at T^(2-a*).',
                'One-sided separated small-gcd signed aggregate on the original full-F exceptional set at T^(-a*); near and high-gcd sectors paid.')
src=src.replace('nonauthor reviews and localized repair attached.','nonauthor reviews and explicit tail/control-scope supplements attached; mandatory two-attempt strategy reassessment complete.')
src=src.replace("next_round_automatic=False)\nfor task in manifest", "next_round_automatic=False,mandatory_strategy_reassessment_complete=True)\nfor task in manifest")
src=src.replace("next_round_automatic=False)\nfuture['round232_closure']", "next_round_automatic=False,mandatory_strategy_reassessment_complete=True,\n    strategy_reassessment=(rel/'candidates/strategy_reassessment.md').as_posix())\nfuture['round232_closure']")
(base/'controls/close_round232.py').write_text(src,encoding='utf-8')
print(json.dumps({'reviewed_artifacts':len(reviewed),'gates':len(gates),'decision_prepared':True}))
