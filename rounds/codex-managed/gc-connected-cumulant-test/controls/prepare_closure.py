"""Write the conductor decision only after explicit final-review acceptance."""
from pathlib import Path
import json,hashlib
root=Path.cwd();rel=Path('rounds/codex-managed/gc-connected-cumulant-test');b=root/rel
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
accept=read(b/'controls/review_acceptance.json');assert accept['all_required_seams_passed'] is True
for name,h in accept['accepted_hashes'].items():assert sha(b/name)==h,(name,'final review hash changed')
assert sha(b/'candidates/conductor_connected_test.md')=='3a443b5e63e826511f99e9428438018e5fc41f358a014fc15d9b8bb75233ae97'
assert read(b/'controls/exact_local_controls.json')['status']=='passed'
reason='The actual signed disconnected contribution is paid at T^(1+epsilon), but the connected aggregate at29/25 remains unproved. The full-harmonic tuplewise absolute connected certificate is at least cT^(5/2), since its entire correction costs only T^(9/4+epsilon). Independent derivation, nonauthor reviews and exact Wolfram/local controls pass. No complete moment or pointwise improvement; identity State Patch and unchanged402-node graph/proof draft.'
summary='''# Round234 closed: connected correlations do not yet give a complete gain

12 October2026 Asia/Shanghai. For the literal actual wave, all harmonics and Q=floor(T^(2/5)), define the connected12 sum K12 using the probability measure w(R/T)dR/(T integral w). The signed disconnected contribution satisfies |I12-K12|<<T^(1+epsilon). The proof uses rapid distinct-class singleton/pair means, exact collision algebra at independent radii, and the already accepted actual moments through order9.

The stronger proposed absolute-cluster method fails: C_conn=(T integral w)sum_distinct|kappa12|>=cT^(5/2). The entire proper-partition correction costs only T^(9/4+epsilon), so it cannot remove the re-audited full-harmonic absolute mass. This is a scoped certificate obstruction, not a lower bound on signed K12, I12 or the complete moment.

The actual one-sided signed estimate K12<=T^(29/25+epsilon) remains OPEN. If supplied it would restore the complete29/25 moment and conditional102/325 sharp exponent; those are not obtained. Complete10beta and the qualified pointwise0.314483175974... remain unchanged. Accepted233's all-fixed-order reduction remains intact; its sufficient unbounded-order signed family and quarter remain open.

Three initial reports were frozen before expanded review; the important collision lemma was independently derived from its statement alone. Three nonauthor reviews of signed remainder, actual lower certificate and complete scope passed at the unchanged candidate hash. Wolfram exact controls, including a disclosed repaired expression, were independently reproduced locally. Computation is diagnostic only.

Conductor decision: retain the new component estimates and scoped obstruction as reviewed evidence, with an identity State Patch. All402 graph nodes and the proof draft remain byte-for-byte unchanged. All pre-existing protected evidence and historical ledger/matrix entries are preserved. No new graph kernel is promoted merely for an equivalent unestimated target.

Strategy: a successor must estimate the genuinely signed cross-tuple aggregate, or introduce a different complete mechanism with quantified costs and falsifiable arithmetic input. Small pair covariances, formal cumulant identities, or tuplewise absolute connected estimates do not supply that input. The earlier upper-tail cycle remains closed after two attempts; this separate connected-correlation premise has one completed attempt. Round235 is pending design, with no tasks or automatic launch.

Record: rounds/codex-managed/gc-connected-cumulant-test/synthesis.md. Candidate and proof details: candidates/conductor_connected_test.md in that campaign. Validation: controls/closure_validation.json. Historical material below is retained evidence, not a launch instruction.'''
barrier='''# Round234 connected-correlation strategy update

- Actual normalized first- and second-order distinct-class absolute means are rapidly small under the fixed smooth radius window; this is not a claim about diagonal pairs or independence.
- Exact mixed-radius collision algebra pays the SIGNED disconnected12 contribution at T^(1+epsilon), using actual lower moments through9. Never move absolute values inside the label-tuple sum in this argument.
- With all harmonics pooled, the actual absolute connected12 certificate is still >=cT^(5/2). The cumulative absolute correction is <=T^(9/4+epsilon). This excludes the proposed tuplewise absolute connected bound at29/25, but not signed connected methods.
- The paid identity I12=K12+O(T^(1+epsilon)) supplies no new K12 estimate. The first gap remains K12<=T^(29/25+epsilon); complete restoration would give102/325 only conditionally. A twelfth moment does not imply quarter.
- Artificial constant and centered Walsh controls distinguish lower moments/pair decorrelation from higher-order independence. They are not actual r2 counterexamples; the actual certificate lower bound has a separate full-harmonic proof.
- Graph/draft unchanged; new proofs remain reviewed campaign evidence. All inherited source qualifications and accepted233 fixed-order quantifiers remain in force.
- One attempt on this separate connected premise is complete; the old two-attempt upper-tail reassessment is not reset. Further use requires a quantitative cross-tuple signed mechanism, not another subtraction identity or absolute cluster norm.

Exact proofs/reviews: rounds/codex-managed/gc-connected-cumulant-test/.'''
synthesis='''# Round234 synthesis and conductor decision

Campaign `gc-connected-cumulant-test`; 12 October2026 Asia/Shanghai. Starting/resulting graph SHA256 `dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306`. Conductor owns this synthesis and State Patch.

## 1. Result and decision

Close the frozen attempt without a complete moment or pointwise gain. The genuine component estimate is |D12|=|I12-K12|<<T^(1+epsilon). The proposed stronger connected absolute-cluster certificate is refuted for the actual functions: C_conn>=cT^(5/2). Retain these as reviewed evidence and apply an identity State Patch. No new accepted graph claim or proof-draft change is needed to record this failed complete strategy.

## 2. Exact statement and paid budgets

All notation is fixed in candidates/conductor_connected_test.md: p12, Q=floor(T^(2/5)), actual full f_d, probability nu_T=w(R/T)dR/(TW), ordered distinct squarefree labels. K12=TW sum_distinct kappa12, with every proper cumulant partition retained. The single outer TW is essential.

| Quantity | Reviewed result | Role |
|---|---|---|
|A1,A2 cross-class absolute normalized means|O_A(T^(-A)) for every fixed A|Pays singleton/pair partitions; no diagonal claim|
|A_q, q>=3 fixed|O(T^(max(q/4-1,0)+epsilon))|Complete elementary upper bound with all Schwartz tails|
|D12=I12-K12, signed|O(T^(1+epsilon))|Paid disconnected contribution|
|TW sum_distinct|m12-kappa12||O(T^(9/4+epsilon))|Absolute correction budget; table maximum is3+9|
|C_conn|>=cT^(5/2)|Actual full-harmonic certificate obstruction|
|K12 one-sided at29/25|OPEN|Required signed arithmetic input|

All terms use the probability normalization before the one final radius mass. No source-average or random-lattice substitution is made.

Accepted216 then pays the head at15/13 and repeated-class error at8beta-1/5<21/25. If K12 at29/25 were proved, complete M12(B_T) at29/25 and sharp102/325 would follow. This attempt proves neither. The accepted complete exponent10beta and qualified external theta are unchanged; all M1/M2/GAR/endpoints and quarter remain open as before. The accepted233 all-fixed-order reduction is preserved, not replaced or promoted into an all-order cumulant theorem.

## 3. Why the proof closes only a component

Smooth frequency separation pays A1,A2 after a polynomial norm cutoff whose complete Schwartz tail is arbitrarily small. For every other proper partition all blocks have size3..9. A statement-only rederivation validates exact equality-partition inclusion-exclusion on independent radius variables. Nonsingleton collision components are controlled by the actual square-sum; singleton components become the complete actual Z at one radius, whose moments through9 are already T^epsilon after normalization. This yields the signed D12 bound without a uniform estimate for arbitrary partial masks.

For the absolute control, a separate one-largest-norm spacing argument bounds each full A_q. All proper shapes cost at most9/4 after the outer T. The prior actual full-harmonic lower certificate is not a graph theorem; it has been explicitly re-audited, including the elementary23/24 square-divisor union bound, every common/mixed harmonic, repeated-label deletion and infinite tail. Both the direct selected-tuple proof and its independent Gram proof are sound under the exact actual hypotheses. Hence connected subtraction cannot erase the5/2 absolute mass.

None of these arguments estimates the remaining signed aggregate. The full bound currently inherited for K12 is at10beta, by its O(T^(1+epsilon)) difference from the actual tail moment. Renaming the moment a connected correlation changes neither that exponent nor the arithmetic gap.

## 4. Independent review and scope

Initial reports signed_connected_attack, connected_certificate_audit and blind_collision_bound are frozen with exact hashes in controls/frozen_initial_reports.json. The blind task read only its isolated statement, own brief and protocol before its report was frozen.

The nonauthor signed_remainder_review checks the mixed-radius identity, actual moment hypotheses, countable limits and target restoration. certificate_review checks the actual lower certificate and full-harmonic cumulant transfer. complete_scope_review checks normalization, actual family binding, fixed-order/restoration scope and the first gap; it explicitly leaves the detailed inherited C10 proof to the separately completed certificate review. This is complementary seam coverage, not a vote. All reviews bind the unchanged conductor candidate SHA256 `3a443b5e63e826511f99e9428438018e5fc41f358a014fc15d9b8bb75233ae97`.

No candidate repair was needed. controls/review_acceptance.json records the conductor's exact final-review acceptance. The countable collision lemma is used only with the actual fixed-T absolute domination; its report correctly warns that bounds on full Z do not alone bound arbitrary truncations.

## 5. Controls and limitations

Exact Wolfram cumulant coefficients at orders2..12, all eight block-size budgets, balanced constant controls, and the harmonic/squarefree/restoration rational margins were reproduced independently with local exact arithmetic. Three separate mixed-radius finite cases also agree exactly, including the discovery report's-68112. A first Wolfram expression in that report failed with a binding error and was repaired; both the failure disclosure and successful replacement are archived. No failed output is evidence. No numerical asymptotic experiment was used; analytical/algebraic effort was at least95%.

The artificial balanced and Walsh families are diagnostics for invalid signed-to-absolute or decorrelation-to-independence inferences. They are not actual r2 examples. The actual no-go depends on the separately proved full-harmonic mass. C_conn is a sum of moduli; there is no positive lower bound claimed for signed K12, I12, or the full physical moment.

## 6. State effect and validation

Identity State Patch: no create/update/reject operation, no graph rewrite, and no proof-draft rewrite. The402 accepted nodes retain the same bytes and hash. Closure validates graph/campaign schemas, the identity application/inverse/replay, all frozen evidence, all protected pre-existing files and prior ledger/validation entries. Exact results are recorded in controls/closure_validation.json and the final artifact manifest. Reviewed component evidence is not silently promoted into accepted mathematics.

## 7. Strategy and stopping rule

The next useful signed-correlation attempt must supply a specific quantitative cancellation mechanism between different label tuples, with a complete budget and controls that survive this actual cumulant obstruction. Approximate pair independence, another partition identity, or taking absolute connected-cluster norms cannot meet the current target. A different complete parent remains possible, but needs its own admission statement and restored costs.

This is one completed attempt on the new connected-correlation premise. The earlier upper-tail two-attempt reassessment remains in force and is not reset. Round235 is pending design with no tasks and no automatic launch. The frozen Round234 objective is closed; no subagent starts a successor.
'''
# Keep the table Markdown syntactically valid without changing its mathematics.
synthesis=synthesis.replace('|TW sum_distinct|m12-kappa12||','|Absolute difference of tuple moments and cumulants, summed with TW|')
(b/'synthesis.md').write_text(synthesis,encoding='utf-8')
gatespec=[
('normalization','single_outer_radius_mass','reviews/complete_scope_review.md'),
('rapid_pairs','distinct_classes_and_full_tail','reviews/signed_remainder_review.md'),
('blind_collision','statement_only_uniform_bound','reports/blind_collision_bound.md'),
('signed_remainder','actual_moments_through_nine','reviews/signed_remainder_review.md'),
('absolute_blocks','all_scales_and_schwartz_tail','reviews/certificate_review.md'),
('harmonic_lower','actual_squarefree_mass_and_full_harmonics','reviews/certificate_review.md'),
('cumulant_transfer','absolute_correction_below_lower_mass','reviews/certificate_review.md'),
('restoration','conditional_only_with_all_paid_owners','reviews/complete_scope_review.md'),
('finite_controls','wolfram_and_local_exact_agree','controls/control_manifest.md'),
('countercontrols','no_independence_or_absolute_swap','reviews/conductor_blind_collision_review.md'),
('first_gap','signed_K12_unproved_no_complete_gain','synthesis.md'),
('state_history','identity_only_protected_inventory','controls/starting_hashes.json')]
gates=[{'id':'round234_'+i,'status':'green_'+s,'artifact':(rel/a).as_posix()} for i,s,a in gatespec]
files=[p for folder in ['reports','reviews','candidates','briefs'] for p in (b/folder).glob('*.md')]
files += [b/'synthesis.md']+[b/'controls'/n for n in ['review_acceptance.json','control_manifest.md','wolfram_checks.wl','wolfram_result.json','exact_local_controls.py','exact_local_controls.json']]
reviewed={p.relative_to(root).as_posix():sha(p) for p in files}
decision={'round_index':234,'campaign_id':'gc-connected-cumulant-test','conductor_review_complete':True,'result':'connected_correlation_test_closed_without_complete_gain','reason':reason,'reviewed_artifact_hashes':reviewed,'gates':gates,'interventions':['Three initial reports frozen before all expanded cross-review; blind isolation preserved.','Signed disconnected bound independently derived and reviewed with complete actual lower moments.','Actual full-harmonic lower certificate re-audited; cumulant subtraction cannot defeat the scoped absolute barrier.','Wolfram finite checks, including disclosed repaired syntax, independently reproduced locally.','Retain new reviewed component evidence without adding another unestimated reduction node; identity closure preserves all402 nodes.'],'assessment':{'actual_disconnected_component_paid':True,'absolute_connected_mechanism_refuted':True,'signed_connected_target_proved':False,'complete_moment_gain':False,'pointwise_gain':False,'quarter_proved':False,'independent_review_complete':True,'prior_upper_tail_attempts_completed':2,'connected_premise_attempts_completed':1},'future_constraint':'No successor launched. A further connected-correlation attempt needs a specific quantitative signed cross-tuple cancellation mechanism; pair decorrelation, another cumulant identity and tuplewise absolute cluster bounds are insufficient. A different complete parent requires a fresh bounded admission with full costs and falsification controls. Accepted233 all-order signed targets remain open; old upper-tail two-attempt reassessment remains in force.','status_summary':summary,'barrier_summary':barrier}
write(b/'closure_decision.json',decision)
print(json.dumps({'decision_prepared':True,'reviewed_artifacts':len(reviewed),'green_gates':len(gates),'graph_effect':'identity'}))
