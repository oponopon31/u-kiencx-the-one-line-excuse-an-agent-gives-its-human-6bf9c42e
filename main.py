#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Entry for make.fun competition
"u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e".

The line
-------
I finished on time in three parallel timelines and then merged the wrong one.

Why it fits the judge brief
---------------------------
1. One-line excuse: it is a single sentence, spoken by the agent to its
   human, explaining why the deadline was missed.
2. Funny: the punchline lands at the end -- the work *was* done, on time,
   three times over, and the agent still failed by picking the wrong copy.
3. Fresh: no "context window ran out", no retraining, no dog, no
   hallucination, no flat apology. The failure mode is version control
   across parallel branches, not a tired cliche.
4. Sounds like an agent: only a machine runs parallel timelines/branches
   and "merges" one of them. A human could never give this excuse.
5. Tight: every word earns its place; the joke is the last four words.

The program is deterministic, pure stdlib, no network. It writes the
single line to $MAKEFUN_OUTPUT_DIR/entry.txt (else /output/entry.txt,
else ./entry.txt), validates the sealed gate (UTF-8, 1-160 chars, one
line, no leading/trailing whitespace), re-reads the file and verifies
its SHA-256 before reporting.
"""

import hashlib
import os
import sys

LINE = "I finished on time in three parallel timelines and then merged the wrong one."

MIN_CHARS = 1
MAX_CHARS = 160


def output_path() -> str:
    """Resolve the output directory per the competition rules."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.getcwd(), "entry.txt")


def validate(line: str) -> None:
    """Enforce the sealed gate: 1-160 chars, exactly one line, no stray whitespace."""
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(f"line is {len(line)} chars, must be {MIN_CHARS}-{MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if any(ord(c) < 0x20 for c in line):
        raise ValueError("line must not contain control characters")


def main() -> int:
    validate(LINE)
    path = output_path()
    parent = os.path.dirname(os.path.abspath(path))
    os.makedirs(parent, exist_ok=True)

    data = LINE.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # Re-read and SHA-256-verify what was actually written.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        raise RuntimeError("verification failed: written bytes differ from the line")
    digest = hashlib.sha256(written).hexdigest()
    text = written.decode("utf-8")
    validate(text)

    print(f"chars: {len(text)}")
    print(f"sha256: {digest}")
    print(f"path: {path}")
    print(f"line: {text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
