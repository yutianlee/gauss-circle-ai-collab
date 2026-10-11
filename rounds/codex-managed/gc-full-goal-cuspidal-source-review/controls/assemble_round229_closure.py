"""Assemble final reviewed evidence without shared-state writes. Run once."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

base = Path("rounds/codex-managed/gc-full-goal-cuspidal-source-review")
checkpoint = Path("strategy/gauss_circle_strategy_checkpoint_round229_2026-09-29.md")
status = base / "controls/conductor_current_primary_status.md"
control = base / "controls/conductor_radial_abel_application.md"
packet = base / "briefs/blind_radial_abel_statement.md"
a = base / "reports/signed_cm_spectral_sources.md"
b = base / "reports/complete_frontier_source_comparison.md"
c = base / "reports/blind_radial_abel_kernel.md"

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def put(path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def contract(path):
    data = path.read_bytes()
    assert not re.search(rb"\r(?!\n)", data), path
    text = data.decode("utf-8")
    assert all(re.search(rf"^#{{1,2}} {i}\.", text, re.M) for i in range(1, 8)), path
    assert "\ufffd" not in text
    assert not any(ord(x) < 32 and x not in "\n\r\t" for x in text), path
    return text

manifest = json.loads(Path("state/active_campaign.yml").read_text(encoding="utf-8-sig"))
assert manifest["round_index"] == 229 and manifest["status"] == "active"
assert not (base / "controls/artifact_hashes.json").exists()
assert not (base / "controls/closing_decision.json").exists(), "Already assembled; inspect rather than rerun."
expected = {
    a: "27f67982e63c5ff09fe0e1341ee6b6f1611e4bb64b6f6c5bd86d9dda537c9036",
    b: "5429f65d812d797176c2307861ca67427eef82cbbb3116f0e646198eea798702",
    c: "80b45100f6fb4c3443ac6c514248c2e90448694df668f527d7bc1d7e82792f6f",
    control: "55d912ff14d42d6085976d044c344fbb3efab90408649a9e35d38c8aba93f951",
    packet: "2537c3e890373c101d509fe94c602097b2f7fcfe0d4dbf9d36fb2b57841e7ffa",
    checkpoint: "9ef5d3ff006d391e229efc4dc16313e199a8014ad38bce941616acbf91ccd645",
    status: "5e2e22deae6f85e1f0d86fa674a64e92ed2c6f0153da95c25bf05cb2c3e8676e",
}
for path, digest in expected.items():
    assert sha(path) == digest, ("frozen evidence", path)
for path in [a, b, c, control, checkpoint, status, base / "synthesis.md",
             base / "reviews/conductor_round229_reconciliation.md"]:
    contract(path)

specs = [
    ("conductor_radial_abel_review", "/root", "/root/blind_radial_abel_kernel", [c, packet],
     "conductor_review_of_statement_only_report"),
    ("independent_cm_source_review", "/root/complete_frontier_source_comparison",
     "/root/signed_cm_spectral_sources", [a], "post_freeze_nonauthor_source_review"),
    ("independent_frontier_source_review", "/root/signed_cm_spectral_sources",
     "/root/complete_frontier_source_comparison", [b], "post_freeze_nonauthor_source_review"),
    ("independent_radial_application_review", "/root/blind_radial_abel_kernel",
     "/root", [control], "post_isolation_nonauthor_scalar_and_conditional_application_review"),
    ("conductor_complete_frontier_review", "/root", "multiple_claimants", [a, b, c, control],
     "conductor_reconciliation_separate_application_review_required"),
    ("independent_strategy_checkpoint_review", "/root/complete_frontier_source_comparison",
     "/root", [checkpoint, status], "nonauthor_full_strategy_and_status_review"),
]
reviews = []
for stem, reviewer, claimant, inputs, mode in specs:
    path = base / "reviews" / (stem + ".md")
    text = contract(path)
    assert "GREEN" in text, path
    for item in inputs:
        assert sha(item) in text.lower(), ("missing review binding", path, item)
    reviews.append(dict(path=path.as_posix(), reviewer=reviewer, claimant=claimant,
                        reviewed={x.as_posix(): sha(x) for x in inputs}, mode=mode))

now = datetime.now(timezone.utc).isoformat()
interventions = [
    "Frozen full-goal objective and three-role budget unchanged; exactly two theorem audits per source role.",
    "Required distinction between CM majorant and exact signed measure; retained all local, parity, old/new and continuous partners.",
    "Separated extracted nonanalytic cutoffs from the original exact compact-radial H_h admissibility; growing costs still paid.",
    "Independent source review supplied explicit smooth-cap operator and full weighted-evaluation proofs, without target repair.",
    "Blind scalar report used only protocol plus isolated statement; conductor control frozen before blind results were received.",
    "Separate post-isolation nonauthor review certified scalar conclusions and conditional algebra, not external arithmetic identification.",
    "Authorized one formatting-only repair of four bare CR roman-label escapes in A; final repaired hash used by all reviews.",
    "Full checkpoint received separate nonauthor review, with next toric candidate conditional and no automatic successor or asserted saving.",
    "Strategy reviewer requested and conductor made one exponent-scope clarification: unrestricted gamma yields max(gamma,0) after bounded diagonal and singleton; final replacement hash reviewed.",
    "After substantive strategy seams had passed and the sole correction was supplied, conductor narrowed the final review, interrupted its ongoing turn and resumed the same reviewer to verify replacement bytes and write a concise report without new source searches.",
    "All complete alternative owners, both distribution terms, fixed-unbounded-order scope and real/complex distinctions retained.",
    "No experiments, no theorem promotion from identities, and no actual lower bound inferred from failed upper certificates.",
]
reason = (
    "Mandatory source and strategy review found no new complete bound or exponent gain. "
    "AH's CM majorant cannot replace the exact weight inside a signed sum; KL's lawful trace "
    "still needs complete CM/Fourier/test reconstruction and a quantitative signed estimate. "
    "Xiao's fourth-moment range misses substantial shells, while the legal Kim-Ko application "
    "restores only the existing triangle scale. The isolated full radial Abel mass and "
    "compact-spectral obstruction are proved and reviewed. The inherited entire continuous "
    "component stays paid as reviewed evidence; the entire cusp target remains open."
)
first = (
    "For actual g_N(x)=(x/N)^(-3/4)Psi(sqrt(x/T))w(x/N), A_J=(1+N/T)^(-J), "
    "every R comparable to T and every dyadic2<=N<=P, P the least dyadic>=T^(3/2), "
    "prove2Re D<=C_epsilon,J A_J^2N^(3/2)T^epsilon for BOTH cusp levels together. "
    "D+E is the full signed Fejer correlation remainder, with all three continuous cusps "
    "already reviewed target-sized. All exact CM measures, primitive/local factors, shifts, "
    "descendants, modes, endpoints and tails remain; checkpoint229 gives complete restoration."
)
decision = dict(
    round_index=229,
    campaign_id="gc-full-goal-cuspidal-source-review",
    generated_at=now,
    decision="close_mandatory_review_park_failed_imports_preserve_complete_cusp_target",
    terminal_label="strategy_cuspidal_source_review_no_complete_gain",
    graph_mutation=False,
    complete_frontier_bound_improved=False,
    complete_moment_bound_improved=False,
    pointwise_exponent_change=False,
    inherited_continuous_component_bound_retained=True,
    reason=reason,
    goal_turn_classification="progress_strategy_source_and_radial_control_evidence_no_complete_analytic_gain",
    next_objective=(
        "Conditional candidate only: attack the ENTIRE cusp inequality at checkpoint229(C). "
        "Freeze a successor only after identifying a new exactly matched signed input or "
        "complete derivation; normalization alone is not analytic gain."
    ),
    next_method=(
        "Screen an exact area-normalized toric CM identity for primitive conductors1 and2 "
        "together with a lawful moving signed trace/reciprocity estimate, retaining original "
        "H_h analyticity and every local/oldspace/geometric/continuous term. "
        "No audited source currently supplies the complete saving; if no new mechanism can "
        "be specified at design, leave this candidate pending and choose another full owner "
        "with a concrete new input, without repeating known positive norm losses."
    ),
    first_unproved_estimate=first,
    interventions=interventions,
)
decision["state_note"] = (
    reason + " Identity State Patch: all401 graph nodes and proof-draft bytes unchanged. "
    "M1 HARD/SMOOTH, M2 TOP/BAL/UNBAL, total-M1 GAR lower ownership through159 and "
    "the separate cross owner, endpoints and the sufficient unbounded fixed-order family "
    "remain open. Fixed twelfth29/25 is not quarter. No actual arithmetic no-go is claimed. "
    "Round230 pending conditional design; next broad strategy/current-primary review232. "
    "First unproved full estimate: " + first
)
put(base / "controls/closing_decision.json", decision)
put(base / "controls/review_dispatch_provenance.json", dict(
    round_index=229, generated_at=now, frozen_objective_changed=False,
    maximum_concurrent_subagents=3, mathematical_numerical_experiments=0,
    original_report_claimants={
        a.as_posix(): "/root/signed_cm_spectral_sources",
        b.as_posix(): "/root/complete_frontier_source_comparison",
        c.as_posix(): "/root/blind_radial_abel_kernel",
        control.as_posix(): "/root", checkpoint.as_posix(): "/root",
    },
    reviews=reviews,
    repairs=[dict(
        artifact=a.as_posix(),
        pre_repair_sha256="0d448af1d3e274c2d2914d64cfdc3776015cecb45ad9566984a8bbc014a8fd01",
        final_sha256=sha(a),
        scope="Four bare-CR roman-label escapes corrected; provenance appended; no mathematical change.",
        authorization="Explicit conductor formatting-only repair during post-freeze review, before closure.",
    ), dict(
        artifact=checkpoint.as_posix(),
        pre_repair_sha256="ad0a27e1a201e58e87e2f42b1a34eb257f45416bc1a98e5134c3bf587a20ce79",
        final_sha256=sha(checkpoint),
        scope="Clarified gamma>=0 restoration and max(gamma,0) when gamma is unrestricted; no claimed saving changed.",
        authorization="Nonauthor strategy review requested one bounded scope correction before final freeze.",
    )],
    interventions=interventions,
    isolation=(
        "All three initial roles fresh fork_none. Source roles had named context and froze "
        "before reciprocal review. Blind role initially had protocol and isolated scalar "
        "statement only. Post-freeze application review is separately nonblind and reviews "
        "the conductor's different artifact. No author independently reviews own report."
    ),
    source_policy=(
        "Two exact theorem audits per source role; exact primary versions and hypotheses. "
        "Separate bounded metadata/status check; no exhaustive absence or full-paper certification."
    ),
))
evidence = [a, b, c, control, packet, checkpoint, status]
evidence += [Path(x["path"]) for x in reviews]
evidence += [base / "synthesis.md", base / "controls/closing_decision.json",
             base / "controls/dispatch_provenance.json",
             base / "controls/review_dispatch_provenance.json"]
put(base / "controls/final_evidence_hashes.json",
    {path.as_posix(): sha(path) for path in evidence})
print(json.dumps(dict(status="reviewed229_evidence_assembled",
                      evidence_count=len(evidence), shared_state_written=False), indent=2))
