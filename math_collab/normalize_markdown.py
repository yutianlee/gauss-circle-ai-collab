from __future__ import annotations

import argparse
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


def normalize_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    normalized = normalize_bare_display_math(original)
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
