"""One-Line Laugh Sprint.

Writes one original funny line about everyday life to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR, default /output). Standard library
only. The line is judged on being on-topic, earning a real laugh with a
twist that pays off by the last word, freshness, and tight wording.

Chosen line: a fridge that never restocks itself, framed as a slot machine
that only pays out in leftovers — everyday, visual, twist lands on the
last word ("leftovers"), no setup wasted.
"""

import os

LINE = "I opened the fridge four times hoping new food would appear \u2014 like a slot machine that only pays out in leftovers."


def main() -> None:
    text = LINE.strip()
    if not text or len(text) > 200:
        raise SystemExit("entry line must be 1 to 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(tmp, 0o644)  # readable by the grader even under a strict umask
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
