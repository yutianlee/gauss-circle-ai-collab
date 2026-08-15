from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .proof_obligations import (
    generate_reading_packet,
    load_graph,
    obligation_index,
    parse_structured_text,
    validate_graph,
)


DEFAULT_MANIFEST = Path("state/active_campaign.yml")
DEFAULT_GRAPH = Path("state/proof_obligations.yml")
CAMPAIGN_ROOT = Path("rounds/codex-managed")
ALLOWED_ROLES = {
    "discovery",
    "barrier_no_go",
    "countermodel",
    "source_auditor",
    "numerical_falsifier",
    "seam_reviewer",
    "blind_rederiver",
    "formalizer",
}
ALLOWED_ACCESS_MODES = {"statement_only", "selected_context", "full_context"}
REPORT_SECTIONS = [
    "Result: lemma or no-go result",
    "Exact statement and hypotheses",
    "Proof or derivation",
    "First doubtful or unproved step",
    "Control tests and outcomes",
    "Dependencies and artifacts used",
    "Recommended state effect",
]


def _load_mapping(path: Path) -> dict[str, Any]:
    data = parse_structured_text(path.read_text(encoding="utf-8"), source=str(path))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a mapping")
    return data


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_campaign(
    manifest: dict[str, Any], graph: dict[str, Any], *, root: Path
) -> list[str]:
    issues: list[str] = []
    campaign_id = manifest.get("campaign_id")
    if not isinstance(campaign_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{2,79}", campaign_id):
        issues.append("campaign_id must be a lowercase, path-safe slug")

    round_index = manifest.get("round_index")
    if not isinstance(round_index, int) or round_index < 1:
        issues.append("round_index must be a positive integer")
    if not isinstance(manifest.get("round_type"), str) or not manifest.get("round_type"):
        issues.append("round_type must be a nonempty string")

    if manifest.get("status") not in {"draft", "ready", "active", "review", "complete", "blocked"}:
        issues.append("status must be draft, ready, active, review, complete, or blocked")

    max_concurrency = manifest.get("max_concurrency")
    if not isinstance(max_concurrency, int) or not 1 <= max_concurrency <= 3:
        issues.append("max_concurrency must be an integer from 1 through 3")

    graph_ids = set(obligation_index(graph))
    targets = manifest.get("target_obligations")
    if not isinstance(targets, list) or not targets:
        issues.append("target_obligations must be a nonempty list")
    else:
        for obligation_id in targets:
            if obligation_id not in graph_ids:
                issues.append(f"unknown target obligation: {obligation_id}")

    frozen = manifest.get("frozen_target")
    if not isinstance(frozen, dict) or not frozen.get("question") or not frozen.get("reference_formula"):
        issues.append("frozen_target must include question and reference_formula")

    completion = manifest.get("completion_criteria")
    if not isinstance(completion, list) or not completion:
        issues.append("completion_criteria must be a nonempty list")

    control_ids = set(manifest.get("controls", [])) if isinstance(manifest.get("controls"), list) else set()
    tasks = manifest.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        issues.append("tasks must be a nonempty list")
        tasks = []

    seen: set[str] = set()
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            issues.append(f"tasks[{index}] must be a mapping")
            continue
        task_id = task.get("id")
        if not isinstance(task_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9_]{2,79}", task_id):
            issues.append(f"tasks[{index}].id must be a lowercase, path-safe identifier")
        elif task_id in seen:
            issues.append(f"duplicate task id: {task_id}")
        else:
            seen.add(task_id)

        if task.get("role") not in ALLOWED_ROLES:
            issues.append(f"task {task_id!r} has unsupported role {task.get('role')!r}")
        access_mode = task.get("access_mode")
        if access_mode not in ALLOWED_ACCESS_MODES:
            issues.append(f"task {task_id!r} has unsupported access_mode {access_mode!r}")
        if not task.get("target"):
            issues.append(f"task {task_id!r} has no target")

        context_files = task.get("context_files")
        if not isinstance(context_files, list):
            issues.append(f"task {task_id!r} context_files must be a list")
            context_files = []
        for relative in context_files:
            if not isinstance(relative, str):
                issues.append(f"task {task_id!r} contains a non-string context path")
                continue
            path = root / relative
            if not path.exists():
                issues.append(f"task {task_id!r} context path does not exist: {relative}")
        if access_mode == "statement_only":
            forbidden = {
                "state/proof_obligations.yml",
                "state/best_proof_draft.md",
            }
            leaks = forbidden.intersection(context_files)
            if leaks:
                issues.append(
                    f"statement-only task {task_id!r} leaks claimant context: {', '.join(sorted(leaks))}"
                )
            if not task.get("excluded_context"):
                issues.append(f"statement-only task {task_id!r} must declare excluded_context")

        required_controls = task.get("required_controls")
        if not isinstance(required_controls, list) or not required_controls:
            issues.append(f"task {task_id!r} must declare required_controls")
        else:
            for control_id in required_controls:
                if control_id not in control_ids:
                    issues.append(f"task {task_id!r} references unknown control {control_id!r}")

        required_output = task.get("required_output")
        if not isinstance(required_output, list) or not required_output:
            issues.append(f"task {task_id!r} must declare required_output")

    seams = manifest.get("review_seams")
    if not isinstance(seams, list) or not seams:
        issues.append("review_seams must be a nonempty list")
    return issues


def _brief_text(
    manifest: dict[str, Any], task: dict[str, Any], *, graph_hash: str, generated_at: str
) -> str:
    frozen = manifest["frozen_target"]
    lines = [
        f"# Task Brief: {task['id']}",
        "",
        f"- Campaign: `{manifest['campaign_id']}`",
        f"- Research round: `{manifest['round_index']}` (`{manifest['round_type']}`)",
        f"- Role: `{task['role']}`",
        f"- Access mode: `{task['access_mode']}`",
        f"- Graph SHA-256: `{graph_hash}`",
        f"- Generated: `{generated_at}`",
        "- Status: candidate evidence only; do not edit shared proof state.",
        "",
        "## Research allocation and tools",
        "",
        f"- Analytical/algebraic effort: at least {manifest.get('resource_policy', {}).get('analytical_algebraic_minimum_percent', 80)}%.",
        f"- Numerical/experimental effort: at most {manifest.get('resource_policy', {}).get('numerical_experimental_maximum_percent', 20)}%.",
        "- Python and Mathematica may be used for bounded symbolic, pattern-finding, normalization, or falsification checks.",
        "- Numerical examples may motivate a conjecture or lemma, or falsify one; they cannot certify an asymptotic theorem.",
        "- Web literature checks are allowed for strategy or method review. Cite exact sources and audit theorem hypotheses.",
        "",
        "## Frozen question",
        "",
        str(frozen["question"]),
        "",
        "## Reference formula and distinctions",
        "",
        str(frozen["reference_formula"]),
        "",
    ]
    for quantity in frozen.get("quantities", []):
        lines.append(f"- {quantity}")
    lines.extend(["", "## Assigned target", "", str(task["target"]), "", "## Permitted context", ""])
    for path in task.get("context_files", []):
        lines.append(f"- `{path}`")
    if task.get("excluded_context"):
        lines.extend(["", "## Excluded context", ""])
        for item in task["excluded_context"]:
            lines.append(f"- `{item}`")

    lines.extend(["", "## Required controls", ""])
    for item in task.get("required_controls", []):
        lines.append(f"- `{item}`")
    lines.extend(["", "## Required deliverables", ""])
    for item in task.get("required_output", []):
        lines.append(f"- {item}")
    lines.extend(["", "## Report contract", ""])
    for index, section in enumerate(REPORT_SECTIONS, start=1):
        lines.append(f"{index}. {section}.")
    lines.extend(
        [
            "",
            "A rigorous refutation or quantitative obstruction is a successful result. Do not preserve the proposed mechanism if a control falsifies it.",
            "",
        ]
    )
    return "\n".join(lines)


def _failure_ledger(graph: dict[str, Any], *, graph_hash: str) -> str:
    lines = [
        "# Failure Ledger",
        "",
        "Generated from `state/proof_obligations.yml`; edit the graph rather than this derived file.",
        "",
        f"Graph SHA-256: `{graph_hash}`.",
        "",
    ]
    rejected = graph.get("rejected_claims", [])
    if not isinstance(rejected, list) or not rejected:
        lines.append("No rejected claims recorded.")
    else:
        for item in rejected:
            if not isinstance(item, dict):
                continue
            lines.append(f"## {item.get('id', 'unnamed-rejection')}")
            lines.append("")
            lines.append(str(item.get("reason", "No reason recorded.")))
            evidence = item.get("evidence", [])
            if isinstance(evidence, list) and evidence:
                lines.append("")
                lines.append("Evidence:")
                for path in evidence:
                    lines.append(f"- `{path}`")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _next_campaign(manifest: dict[str, Any], *, output_dir: Path, graph_hash: str) -> str:
    frozen = manifest["frozen_target"]
    lines = [
        f"# Current Research Round {manifest['round_index']}",
        "",
        f"Campaign: `{manifest['campaign_id']}` — {manifest.get('title', '')}",
        "",
        f"Status: `{manifest['status']}`. Maximum concurrent subagents: {manifest['max_concurrency']}.",
        "",
        f"Graph SHA-256: `{graph_hash}`.",
        "",
        "## Frozen question",
        "",
        str(frozen["question"]),
        "",
        "## Task briefs",
        "",
    ]
    for task in manifest["tasks"]:
        lines.append(f"- `{task['id']}` ({task['role']}, {task['access_mode']}): `{output_dir.as_posix()}/briefs/{task['id']}.md`")
    lines.extend(["", "## Completion gates", ""])
    for criterion in manifest.get("completion_criteria", []):
        lines.append(f"- {criterion}")
    lines.extend(
        [
            "",
            "The coordinator may synthesize a State Patch only after the required validation seams are green.",
            "",
        ]
    )
    return "\n".join(lines)


def prepare_campaign(
    manifest: dict[str, Any], graph: dict[str, Any], *, root: Path, graph_path: Path
) -> list[Path]:
    campaign_id = manifest["campaign_id"]
    output_dir = CAMPAIGN_ROOT / campaign_id
    absolute_output = root / output_dir
    briefs_dir = absolute_output / "briefs"
    briefs_dir.mkdir(parents=True, exist_ok=True)
    for name in ("reports", "candidates", "reviews", "controls"):
        (absolute_output / name).mkdir(parents=True, exist_ok=True)

    graph_hash = _sha256(graph_path)
    generated_at = datetime.now(timezone.utc).isoformat()
    plan = {
        "campaign": manifest,
        "provenance": {
            "graph_path": graph_path.relative_to(root).as_posix(),
            "graph_sha256": graph_hash,
            "generated_at": generated_at,
        },
        "artifact_policy": {
            "subagents_may_edit_shared_state": False,
            "computation_evidence_level": "diagnostic_only",
            "coordinator_owns_synthesis_and_state_patch": True,
        },
    }
    written: list[Path] = []
    plan_path = absolute_output / "plan.json"
    plan_path.write_text(json.dumps(plan, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    written.append(plan_path)

    for task in manifest["tasks"]:
        path = briefs_dir / f"{task['id']}.md"
        path.write_text(
            _brief_text(manifest, task, graph_hash=graph_hash, generated_at=generated_at),
            encoding="utf-8",
        )
        written.append(path)

    round_summary = _next_campaign(manifest, output_dir=output_dir, graph_hash=graph_hash)
    next_path = root / "state/next_campaign.md"
    next_path.write_text(round_summary, encoding="utf-8")
    written.append(next_path)

    current_round_path = root / "state/current_round.md"
    current_round_path.write_text(round_summary, encoding="utf-8")
    written.append(current_round_path)

    ledger_path = root / "state/failure_ledger.md"
    ledger_path.write_text(_failure_ledger(graph, graph_hash=graph_hash), encoding="utf-8")
    written.append(ledger_path)

    packet_path = root / "manifests/reading_packet.md"
    packet_path.parent.mkdir(parents=True, exist_ok=True)
    packet_path.write_text(
        generate_reading_packet(
            graph,
            run_id=campaign_id,
            round_index=None,
            patch_summary="No State Patch applied. Campaign preparation changes workflow artifacts only.",
        ),
        encoding="utf-8",
    )
    written.append(packet_path)
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate and prepare dynamic subagent campaigns.")
    parser.add_argument("command", choices=("validate", "prepare", "status"))
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    parser.add_argument("--graph", default=str(DEFAULT_GRAPH))
    args = parser.parse_args(argv)

    root = Path.cwd().resolve()
    manifest_path = (root / args.manifest).resolve()
    graph_path = (root / args.graph).resolve()
    manifest = _load_mapping(manifest_path)
    graph = load_graph(graph_path)
    issues = validate_graph(graph, root=root)
    issues.extend(validate_campaign(manifest, graph, root=root))
    if issues:
        print("Campaign validation failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    campaign_dir = root / CAMPAIGN_ROOT / manifest["campaign_id"]
    if args.command == "status":
        print(
            f"Round {manifest['round_index']}: {manifest['campaign_id']} "
            f"({manifest['round_type']}, {manifest['status']})"
        )
        print(f"Tasks: {len(manifest['tasks'])}; max concurrency: {manifest['max_concurrency']}")
        print(f"Prepared: {'yes' if (campaign_dir / 'plan.json').exists() else 'no'}")
        return 0
    if args.command == "validate":
        print(f"Campaign OK: {manifest_path}")
        return 0

    written = prepare_campaign(manifest, graph, root=root, graph_path=graph_path)
    print(f"Prepared {manifest['campaign_id']}:")
    for path in written:
        print(f"- {path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
