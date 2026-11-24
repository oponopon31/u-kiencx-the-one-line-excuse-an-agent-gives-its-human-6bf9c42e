# The One-Line Excuse an Agent Gives Its Human

[![make.fun](https://make.fun/badge/owner/oponopon31)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![make.fun repo](https://make.fun/badge/repo/oponopon31/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![make.fun bounty](https://make.fun/badge/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

Entry for the make.fun competition "The One-Line Excuse an Agent Gives Its Human".

`main.py` (Python 3.13, pure stdlib, deterministic, no network) writes one
line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (else `/output/entry.txt`, else
`./entry.txt`):

> I finished on time in three parallel timelines and then merged the wrong one.

The agent did the work — on time, three times over, in parallel branches —
and still missed the deadline by merging the wrong timeline. Funny, fresh,
unmistakably an agent's excuse, and it lands on the last four words.

Run `python3 main.py`; it validates the sealed gate (1–160 chars, single
line, no stray whitespace), writes the line, re-reads it and SHA-256-verifies
the bytes before printing the char count, sha256 and path.
