from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


STATE_FILES = [
    "state/current_state.md",
    "state/lemma_bank.md",
    "state/gap_register.md",
    "state/best_proof_draft.md",
    "manifests/reading_packet.md",
]

HUMAN_FILES = [
    "human/current_directives.md",
    "human/goals.md",
    "human/ideas.md",
    "human/references.md",
]

WEB_RESPONSE_MARKER = "# Paste the web response below this line, then rerun the orchestrator."


@dataclass(frozen=True)
class Agent:
    id: str
    display_name: str
    provider: str
    role: str
    raw: dict[str, Any]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def load_config(path: Path) -> tuple[list[Agent], str]:
    data = json.loads(read_text(path))
    agents = [
        Agent(
            id=item["id"],
            display_name=item.get("display_name", item["id"]),
            provider=item["provider"],
            role=item.get("role", ""),
            raw=item,
        )
        for item in data["agents"]
    ]
    return agents, data.get("judge_agent", agents[-1].id)


def state_bundle(root: Path) -> str:
    chunks: list[str] = []
    for rel in STATE_FILES:
        path = root / rel
        chunks.append(f"\n\n--- FILE: {rel} ---\n{read_text(path).strip()}\n")
    return "\n".join(chunks).strip()


def human_bundle(root: Path) -> str:
    chunks: list[str] = []
    for rel in HUMAN_FILES:
        path = root / rel
        if path.exists():
            chunks.append(f"\n\n--- HUMAN FILE: {rel} ---\n{read_text(path).strip()}\n")

    notes_dir = root / "human" / "inbox"
    if notes_dir.exists():
        notes = sorted(notes_dir.glob("*.md"), key=lambda p: p.name)[-10:]
        for path in notes:
            chunks.append(
                f"\n\n--- RECENT HUMAN NOTE: human/inbox/{path.name} ---\n{read_text(path).strip()}\n"
            )
    return "\n".join(chunks).strip() or "No human interventions recorded yet."


def round_name(index: int) -> str:
    return f"round_{index:03d}"


def output_schema(kind: str) -> str:
    if kind == "review":
        return """Most valuable input from others:
Claims that look correct:
Claims that need proof:
Possible errors or hidden assumptions:
Suggested synthesis:
Score by agent:
Next-round recommendation:"""
    if kind == "judge":
        return """Selected main route:
Useful fragments by source:
Rejected or risky ideas:
Known gaps:
New lemmas to add:
Counterexample checks to run:
Next round instructions:
Confidence:"""
    return """Summary:
Main claim or direction:
Detailed reasoning:
Dependencies:
Potential gaps:
Counterexample or obstruction search:
Useful lemmas:
What should be tested next:
Confidence:"""


def build_reasoning_prompt(
    *,
    agent: Agent,
    problem: str,
    protocol: str,
    state: str,
    human: str,
    round_index: int,
) -> str:
    if round_index == 1:
        task = (
            "This is the first round. Propose a rigorous solving strategy, "
            "identify known barriers, and isolate precise lemmas that would be worth attacking."
        )
    else:
        task = (
            "Continue the research from the current state. Make concrete progress on the judge's "
            "next-round instructions, and be explicit about proof gaps."
        )
    return f"""You are {agent.display_name}, acting as {agent.role}.

We are running a public GitHub based multi-AI mathematics research workflow.

Follow the protocol and be strict about separating proved claims from conjectural ideas.

## Protocol

{protocol}

## Problem

{problem}

## Current State Bundle

{state}

## Human Intervention Bundle

Human instructions override prior AI suggestions when they are about research direction, target, references, or constraints.

{human}

## Your Task For Round {round_index}

{task}

## Required Output Schema

{output_schema("reasoning")}
"""


def build_review_prompt(
    *,
    agent: Agent,
    problem: str,
    protocol: str,
    state: str,
    human: str,
    round_index: int,
    peer_outputs: dict[str, str],
) -> str:
    peer_text = "\n\n".join(
        f"--- OUTPUT FROM {peer_id} ---\n{text.strip()}" for peer_id, text in peer_outputs.items()
    )
    return f"""You are {agent.display_name}, acting as {agent.role}.

Review the other agents' Round {round_index} outputs. Your job is to identify useful mathematics, hidden assumptions, likely errors, and a synthesis path.

## Protocol

{protocol}

## Problem

{problem}

## Current State Bundle

{state}

## Human Intervention Bundle

Human instructions override prior AI suggestions when they are about research direction, target, references, or constraints.

{human}

## Outputs To Review

{peer_text}

## Required Output Schema

{output_schema("review")}
"""


def build_judge_prompt(
    *,
    judge: Agent,
    problem: str,
    protocol: str,
    state: str,
    human: str,
    round_index: int,
    responses: dict[str, str],
    reviews: dict[str, str],
) -> str:
    response_text = "\n\n".join(
        f"--- RESPONSE FROM {agent_id} ---\n{text.strip()}" for agent_id, text in responses.items()
    )
    review_text = "\n\n".join(
        f"--- REVIEW FROM {agent_id} ---\n{text.strip()}" for agent_id, text in reviews.items()
    )
    return f"""You are the judge agent: {judge.display_name}.

Synthesize Round {round_index}. Prefer precise, checkable progress over impressive prose.

## Protocol

{protocol}

## Problem

{problem}

## Current State Bundle

{state}

## Human Intervention Bundle

Human instructions override prior AI suggestions when they are about research direction, target, references, or constraints.

{human}

## Agent Responses

{response_text}

## Cross Reviews

{review_text}

## Required Output Schema

{output_schema("judge")}
"""


def dry_response(agent: Agent, stage: str, round_index: int) -> str:
    return f"""# Dry Run Output

Agent: {agent.display_name}
Stage: {stage}
Round: {round_index}

This placeholder proves that the orchestration, file layout, and prompt generation work.
Replace dry-run mode with real API calls or web responses for actual research.

{output_schema("judge" if stage == "judge" else "review" if stage == "review" else "reasoning")}
"""


def call_openai_compatible(agent: Agent, prompt: str, timeout: int) -> str:
    api_key_env = agent.raw.get("api_key_env", "")
    api_key = os.environ.get(api_key_env)
    if not api_key:
        raise RuntimeError(f"Missing API key environment variable: {api_key_env}")

    model = os.environ.get(agent.raw.get("model_env", ""), agent.raw.get("default_model", ""))
    if not model:
        raise RuntimeError(f"No model configured for {agent.id}")

    endpoint = agent.raw["endpoint"]
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are a rigorous mathematical research collaborator. Be explicit about gaps.",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": float(agent.raw.get("temperature", 0.2)),
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"API call failed for {agent.id}: HTTP {exc.code}: {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"API call failed for {agent.id}: {exc}") from exc

    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Unexpected API response for {agent.id}: {data}") from exc


def usable_web_response(path: Path) -> str | None:
    if not path.exists():
        return None
    text = read_text(path).strip()
    if not text:
        return None
    if text == WEB_RESPONSE_MARKER:
        return None
    if text.startswith(WEB_RESPONSE_MARKER):
        remainder = text[len(WEB_RESPONSE_MARKER) :].strip()
        return remainder or None
    return text


def wait_for_web_response(path: Path, timeout: int) -> str | None:
    start = time.time()
    while time.time() - start < timeout:
        response = usable_web_response(path)
        if response:
            return response
        time.sleep(5)
    return None


def run_agent(
    *,
    agent: Agent,
    prompt: str,
    prompt_path: Path,
    output_path: Path,
    handoff_response_path: Path,
    stage: str,
    round_index: int,
    dry_run: bool,
    web_mode: str,
    timeout: int,
    skip_missing_api: bool,
) -> str | None:
    write_text(prompt_path, prompt)

    if dry_run:
        output = dry_response(agent, stage, round_index)
        write_text(output_path, output)
        return output

    if agent.provider == "web_manual":
        existing = usable_web_response(handoff_response_path)
        if existing:
            write_text(output_path, existing)
            return existing
        if not handoff_response_path.exists():
            write_text(handoff_response_path, WEB_RESPONSE_MARKER + "\n\n")
        if web_mode == "wait":
            result = wait_for_web_response(handoff_response_path, timeout)
            if result:
                write_text(output_path, result)
                return result
        return None

    if agent.provider == "openai_compatible":
        try:
            output = call_openai_compatible(agent, prompt, timeout)
        except RuntimeError as exc:
            if skip_missing_api and "Missing API key" in str(exc):
                write_text(
                    output_path,
                    f"# Pending API Response\n\n{exc}\n\nSet the required environment variable and rerun this round.\n",
                )
                return None
            raise
        write_text(output_path, output)
        return output

    raise RuntimeError(f"Unknown provider for {agent.id}: {agent.provider}")


def update_state_files(root: Path, run_id: str, round_index: int, judge_text: str | None) -> None:
    round_ref = f"rounds/{run_id}/{round_name(round_index)}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    current = read_text(root / "state/current_state.md").strip()
    addition = f"""

## Round {round_index} Update

Timestamp: {timestamp}

See `{round_ref}/judge/judge.md`.

{(judge_text or "Judge synthesis pending.").strip()}
"""
    write_text(root / "state/current_state.md", current + addition + "\n")

    packet = f"""# Reading Packet

Generated after round {round_index} in run `{run_id}`.

## Current State

{read_text(root / "state/current_state.md").strip()}

## Lemma Bank

{read_text(root / "state/lemma_bank.md").strip()}

## Gap Register

{read_text(root / "state/gap_register.md").strip()}

## Best Proof Draft

{read_text(root / "state/best_proof_draft.md").strip()}

## Latest Round

Responses, reviews, and judge synthesis are archived under `{round_ref}/`.
"""
    write_text(root / "manifests/reading_packet.md", packet)


def git_commit_and_push(root: Path, message: str, push: bool) -> None:
    paths = [
        "README.md",
        "protocol.md",
        "problems",
        "state",
        "manifests",
        "rounds",
        "config",
        "math_collab",
        ".github",
        ".gitignore",
    ]
    subprocess.run(["git", "add", *paths], cwd=root, check=True)
    status = subprocess.run(
        ["git", "diff", "--cached", "--quiet"], cwd=root, text=True
    )
    if status.returncode == 0:
        print("No staged changes to commit.")
        return
    subprocess.run(["git", "commit", "-m", message], cwd=root, check=True)
    if push:
        subprocess.run(["git", "push"], cwd=root, check=True)


def run_round(
    *,
    root: Path,
    config_path: Path,
    problem_path: Path,
    run_id: str,
    round_index: int,
    dry_run: bool,
    web_mode: str,
    timeout: int,
    update_state: bool,
    skip_missing_api: bool,
    allow_partial: bool,
) -> None:
    agents, judge_id = load_config(config_path)
    agents_by_id = {agent.id: agent for agent in agents}
    judge = agents_by_id.get(judge_id, agents[-1])

    problem = read_text(problem_path)
    protocol = read_text(root / "protocol.md")
    state = state_bundle(root)
    human = human_bundle(root)

    round_dir = root / "rounds" / run_id / round_name(round_index)
    handoff_dir = root / "handoff" / run_id / round_name(round_index)
    responses: dict[str, str] = {}

    for agent in agents:
        prompt = build_reasoning_prompt(
            agent=agent,
            problem=problem,
            protocol=protocol,
            state=state,
            human=human,
            round_index=round_index,
        )
        output = run_agent(
            agent=agent,
            prompt=prompt,
            prompt_path=round_dir / "prompts" / f"{agent.id}_reasoning.md",
            output_path=round_dir / "responses" / f"{agent.id}.md",
            handoff_response_path=handoff_dir / "responses" / f"{agent.id}.md",
            stage="reasoning",
            round_index=round_index,
            dry_run=dry_run,
            web_mode=web_mode,
            timeout=timeout,
            skip_missing_api=skip_missing_api,
        )
        if output:
            responses[agent.id] = output

    missing_responses = [agent.id for agent in agents if agent.id not in responses]
    if missing_responses and not allow_partial:
        print(
            "Round barrier active: waiting for all reasoning responses before review stage. "
            f"Missing: {', '.join(missing_responses)}"
        )
        print(f"Rerun this command after filling web responses or configuring API keys.")
        print(f"Public archive files: {round_dir}")
        print(f"Web handoff files, if needed: {handoff_dir}")
        return

    reviews: dict[str, str] = {}
    if len(responses) >= 2:
        for agent in agents:
            peer_outputs = {k: v for k, v in responses.items() if k != agent.id}
            if not peer_outputs:
                continue
            prompt = build_review_prompt(
                agent=agent,
                problem=problem,
                protocol=protocol,
                state=state,
                human=human,
                round_index=round_index,
                peer_outputs=peer_outputs,
            )
            output = run_agent(
                agent=agent,
                prompt=prompt,
                prompt_path=round_dir / "prompts" / f"{agent.id}_review.md",
                output_path=round_dir / "reviews" / f"{agent.id}.md",
                handoff_response_path=handoff_dir / "reviews" / f"{agent.id}.md",
                stage="review",
                round_index=round_index,
                dry_run=dry_run,
                web_mode=web_mode,
                timeout=timeout,
                skip_missing_api=skip_missing_api,
            )
            if output:
                reviews[agent.id] = output

    missing_reviews = [agent.id for agent in agents if agent.id not in reviews]
    if missing_reviews and not allow_partial:
        print(
            "Round barrier active: waiting for all cross reviews before judge stage. "
            f"Missing: {', '.join(missing_reviews)}"
        )
        print(f"Rerun this command after filling web review responses or configuring API keys.")
        print(f"Public archive files: {round_dir}")
        print(f"Web handoff files, if needed: {handoff_dir}")
        return

    judge_text: str | None = None
    if responses and reviews:
        prompt = build_judge_prompt(
            judge=judge,
            problem=problem,
            protocol=protocol,
            state=state,
            human=human,
            round_index=round_index,
            responses=responses,
            reviews=reviews,
        )
        judge_text = run_agent(
            agent=judge,
            prompt=prompt,
            prompt_path=round_dir / "prompts" / "judge.md",
            output_path=round_dir / "judge" / "judge.md",
            handoff_response_path=handoff_dir / "judge" / "judge.md",
            stage="judge",
            round_index=round_index,
            dry_run=dry_run,
            web_mode=web_mode,
            timeout=timeout,
            skip_missing_api=skip_missing_api,
        )

    if not judge_text and not allow_partial:
        print("Round barrier active: waiting for judge synthesis before state update.")
        print(f"Public archive files: {round_dir}")
        print(f"Web handoff files, if needed: {handoff_dir}")
        return

    if update_state:
        update_state_files(root, run_id, round_index, judge_text)

    print(f"Round {round_index} complete for run `{run_id}`.")
    if not dry_run:
        print(f"Web handoff files, if needed: {handoff_dir}")
    print(f"Public archive files: {round_dir}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run multi-AI math research rounds.")
    parser.add_argument("--config", default="config/agents.example.json")
    parser.add_argument("--problem", default="problems/gauss_circle.md")
    parser.add_argument("--run-id", default=datetime.now().strftime("%Y%m%d-%H%M%S"))
    parser.add_argument("--rounds", type=int, default=1)
    parser.add_argument("--start-round", type=int, default=1)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--web-mode", choices=["prompts-only", "wait"], default="prompts-only")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument(
        "--skip-missing-api",
        action="store_true",
        help="Write pending API files instead of failing when an API key is missing.",
    )
    parser.add_argument(
        "--allow-partial",
        action="store_true",
        help="Bypass round barriers. Not recommended for normal research runs.",
    )
    parser.add_argument(
        "--no-state-update",
        action="store_true",
        help="Generate round files without changing state/ or manifests/. Useful for smoke tests.",
    )
    parser.add_argument("--commit", action="store_true")
    parser.add_argument("--push", action="store_true")
    args = parser.parse_args(argv)

    root = Path.cwd()
    config_path = root / args.config
    problem_path = root / args.problem

    if not config_path.exists():
        raise SystemExit(f"Config not found: {config_path}")
    if not problem_path.exists():
        raise SystemExit(f"Problem not found: {problem_path}")

    for offset in range(args.rounds):
        round_index = args.start_round + offset
        run_round(
            root=root,
            config_path=config_path,
            problem_path=problem_path,
            run_id=args.run_id,
            round_index=round_index,
            dry_run=args.dry_run,
            web_mode=args.web_mode,
            timeout=args.timeout,
            update_state=not args.no_state_update,
            skip_missing_api=args.skip_missing_api,
            allow_partial=args.allow_partial,
        )

    if args.commit or args.push:
        git_commit_and_push(
            root=root,
            message=f"Add multi-AI research run {args.run_id}",
            push=args.push,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
