"""Reuse the validated identity-closure machinery without touching206."""
from pathlib import Path
import ast

old=Path('rounds/codex-managed/gc-complete-signed-shell-arithmetic/controls/close_round206.py')
new=Path('rounds/codex-managed/gc-signed-rational-filter-attack/controls/close_round207.py')
s=old.read_text(encoding='utf-8')
s=s.replace('207','NEXT_ROUND_PLACEHOLDER').replace('206','207').replace('NEXT_ROUND_PLACEHOLDER','208')
s=s.replace('gc-complete-signed-shell-arithmetic','gc-signed-rational-filter-attack')
s=s.replace("    'gc-full-frontier-moment-strategy-review',\n]", "    'gc-full-frontier-moment-strategy-review',\n    'gc-complete-signed-shell-arithmetic',\n]")
s=s.replace('closed_round200_through205','closed_round200_through206').replace('Round200--205','Round200--206')
s=s.replace('scoped_arithmetic_method_no_go','scoped_rational_method_no_go')
s=s.replace('conductor_sixth_moment_power_ledger.md','conductor_rational_norm_ledger.md')
s=s.replace('independent_shifted_source_review.md','independent_signed_norm_review.md')
s=s.replace('reports/shifted_moment_source_attack.md','reports/periodic_hyperbola_attack.md')
s=s.replace("[base / 'reports/periodic_hyperbola_attack.md']", "[base / 'reports/periodic_hyperbola_attack.md', power]")
s=s.replace('independent_divisor_obstruction_review.md','independent_rational_majorant_review.md')
s=s.replace('reports/actual_divisor_shell_attack.md','reports/signed_rational_moment_attack.md')
s=s.replace('independent_bridge_power_review.md','independent_threshold_even_cutoff_review.md')
s=s.replace('reports/blind_odd_shell_bridge.md','reports/blind_periodic_threshold.md')
start=s.index("judge_text = r'''")
end=s.index("judge.write_text(judge_text",start)
s=s[:start]+"judge_text = judge.read_text(encoding='utf-8').replace('FINAL_HASH_BINDINGS', bindings)\n"+s[end:]
s=s.replace('GREEN for scoped arithmetic-attempt closure only','GREEN for scoped rational-attempt closure only')
start=s.index("synthesis = r'''")
end=s.index('hygiene = []',start)
s=s[:start]+"assert (base / 'synthesis.md').is_file()\n\n"+s[end:]
start=s.index("reason = ('")
end=s.index('patch = dict(',start)
s=s[:start]+'''reason = ('Complete signed rational-filter and reciprocal estimates recover existing bounds only. '
          'The actual termwise rational sixth majorant is at least X^3H after single-frequency '
          'grouping; signed sextuple cancellation remains open. Threshold, mask and width costs '
          'are fully paid. Archive this scoped no-go without graph promotion.')
'''+s[end:]
s=s.replace('round_207_closed_identity_patch_scoped_arithmetic_no_go','round_207_closed_identity_patch_scoped_rational_no_go')
s=s.replace('green_round207_scoped_arithmetic_closure','green_round207_scoped_rational_closure')
start=s.index("    decision_rule='Round207 closes")
end=s.index("write('state/validation_matrix.yml'",start)
s=s[:start]+'''    decision_rule='Round207 closes a complete signed rational attempt and actual-coefficient '
                  'majorant no-go; signed target remains open. Identity patch, no complete gain. '
                  'Round208 pending mandatory strategy/current-literature review.',
)
'''+s[end:]
start=s.index('         conductor_interventions=[')
end=s.index("for t in m['tasks']:",start)
s=s[:start]+'''         conductor_interventions=[
             'Required a complete signed estimate after periodic transformation; both arms and every harmonic retained.',
             'Separated F/e(-lambda x) and K/e(+lambda x) conventions and checked exact mod4 factors.',
             'Introduced an explicit even-cutoff variant with its own exact quotient limit; obtained independent review.',
             'Proved rational variance with collision grouping, actual width and joint prefix energy, not a power-sized mask count.',
             'Routed one post-report seam cycle after all discovery reports, preserving original blind isolation.',
             'Repaired seven bare-CR TeX defects byte-preservingly before final review hashes.',
             'Kept majorant lower bound separate from signed moment and exact-deleted variants; no graph fragments promoted.',
         ])
'''+s[end:]
start=s.index("write('state/next_round_plan.yml', dict(")
end=s.index('summary = _next_campaign',start)
s=s[:start]+'''write('state/next_round_plan.yml', dict(
    round_index=208, status='pending_design', campaign_id=None,
    starting_graph_sha256=sha(gp), predecessor_round=207,
    predecessor_terminal_label=terminal, tasks=[],
    candidate_objective='Mandatory broad strategy and current-primary-literature review after205--207: '
                        'select a complete arithmetic objective capable of a genuine parent or exponent gain.',
    candidate_method='Compare signed rational total-frequency aggregation, actual high-value arithmetic, '
                     'and other full-source routes with current harmonic, spectral, geometric and arithmetic methods. '
                     'Audit exact theorem hypotheses and every reconstruction cost before selecting a route.',
    first_unproved_estimate='The full signed middle p12 target T^(29/25), or a sufficient K6 bound '
                            'T^(129/25-6omega). Existing bound leaves g=6omega-4/25-29alpha/110>0 everywhere.',
    exact_closed_dependencies=[p.as_posix() for p in evidence] + [judge.as_posix(), (base / 'synthesis.md').as_posix()],
    design_constraint='Design only after closed207 evidence. Repeating an auxiliary transform, recovered variance, '
                      'single-frequency grouping or termwise sextuple majorant is not a new gain. '
                      'Do not infer a target refutation from a scoped majorant obstruction.',
    full_goal_scope='Retain the full quarter theorem, adequate high-moment requirements and open M1/M2. '
                    'The current p12 milestone would only imply102/325.',
    scheduled_review='Round208 is the required broad strategy/current-literature checkpoint.',
    prior_turn_classification=assessment['goal_turn_classification'],
))
'''+s[end:]
start=s.index("note = '''")
end=s.index("for p in ['state/project_summary.md'",start)
s=s[:start]+'''note = """
## Round207 signed rational-filter attack (2026-09-27)

The complete signed reciprocal estimate recovers the existing physical
coefficient supremum. Direct rational variance pays collisions, variable
width and moving prefixes with logarithms. The hyperbola threshold error
is target-safe; an independently reviewed even cutoff makes it rapid.

Actual single-frequency grouping leaves l1 mass of order sqrt(X).
The termwise integrated rational sixth majorant is at least X^3H,
exceeding the sufficient threshold by at least T^(517/250). This lower
bound includes exact and near triple relations and does not lower-bound
the signed moment or reject joint total-frequency cancellation.

Identity State Patch: all399 graph nodes and proof-draft bytes unchanged.
No improved complete moment or pointwise exponent; M1/M2 and quarter
remain open. Three reports and three exact-hash seams are green in their
declared scopes. See rounds/codex-managed/gc-signed-rational-filter-attack/synthesis.md.
Round208 is pending design as the mandatory broad strategy and current-
literature review after205--207.
"""
'''+s[end:]
s=s.replace("b'## Round 207 complete signed-shell arithmetic (2026-09-26)'", "b'## Round207 signed rational-filter attack (2026-09-27)'")
s=s.replace('strategy/round207_complete_signed_shell_arithmetic_attack.md','strategy/round207_signed_rational_filter_attack.md')
s=s.replace('GREEN for scoped arithmetic-attempt closure only','GREEN for scoped rational-attempt closure only')
ast.parse(s)
assert 'round206_' not in s and 'round_206_' not in s
assert "'gc-complete-signed-shell-arithmetic'" in s
assert 'round_index=208' in s and 'round_index=207' in s
new.write_text(s,encoding='utf-8',newline='\n')
print('Prepared207 closure machinery; no closure/state mutation performed.')
