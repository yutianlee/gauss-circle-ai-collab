from __future__ import annotations

import argparse
import re
from pathlib import Path


MATH_HINTS = [
    "\\",
    "_",
    "^",
    "{",
    "}",
    "sum",
    "int",
    "prod",
    "frac",
    "sqrt",
    "pi",
    "epsilon",
    "alpha",
    "beta",
    "gamma",
    "delta",
    "theta",
    "lambda",
    "sigma",
    "omega",
    "infty",
    "leq",
    "geq",
    "sim",
    "ll",
    "gg",
    "cdot",
    "times",
    "mathbb",
    "operatorname",
    "O_",
    "N(",
    "E(",
    "P(",
    "R^",
    "X^",
]


def looks_like_math(text: str) -> bool:
    stripped = text.strip()
    if len(stripped) < 3 or len(stripped) > 500:
        return False
    if stripped.startswith(("http://", "https://")):
        return False
    lower = stripped.lower()
    return any(hint.lower() in lower for hint in MATH_HINTS)


def normalize_bare_display_math(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "[":
            block: list[str] = []
            j = i + 1
            while j < len(lines) and lines[j].strip() != "]":
                block.append(lines[j])
                j += 1
            if j < len(lines) and looks_like_math("\n".join(block)):
                out.append("$$")
                out.extend(block)
                out.append("$$")
                i = j + 1
                continue
        out.append(line)
        i += 1
    return "\n".join(out) + ("\n" if markdown.endswith("\n") else "")


def strip_outer_markdown_fence(markdown: str) -> str:
    stripped = markdown.strip()
    if not stripped.startswith("```markdown"):
        return markdown
    lines = stripped.splitlines()
    if len(lines) >= 2 and lines[0].strip().lower() == "```markdown" and lines[-1].strip() == "```":
        return "\n".join(lines[1:-1]).strip() + "\n"
    return markdown


def normalize_copied_display_operators(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    in_display_math = False
    for line in lines:
        stripped = line.strip()
        if stripped == "$$":
            in_display_math = not in_display_math
            out.append(stripped)
            continue
        if in_display_math and re.fullmatch(r"={2,}", stripped):
            out.append("=")
            continue
        out.append(line.rstrip())
    return "\n".join(out) + ("\n" if markdown.endswith("\n") else "")


def normalize_final_newline(markdown: str) -> str:
    return markdown.rstrip() + "\n"


def normalize_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    normalized = strip_outer_markdown_fence(original)
    normalized = normalize_bare_display_math(normalized)
    normalized = normalize_copied_display_operators(normalized)
    normalized = normalize_final_newline(normalized)
    if normalized != original:
        path.write_text(normalized, encoding="utf-8", newline="\n")
        return True
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Normalize copied web AI Markdown responses.")
    parser.add_argument("paths", nargs="+", help="Markdown files to normalize.")
    args = parser.parse_args(argv)

    changed = []
    for item in args.paths:
        path = Path(item)
        if normalize_file(path):
            changed.append(str(path))

    if changed:
        print("Normalized:")
        for path in changed:
            print(f"- {path}")
    else:
        print("No normalization needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
