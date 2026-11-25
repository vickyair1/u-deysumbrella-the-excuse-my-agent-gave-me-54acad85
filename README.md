[![competition](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/vickyair1/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/vickyair1/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

# The Excuse My Agent Gave Me

An entry for [make.fun's "The Excuse My Agent Gave Me" bounty](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85): one line, under 200 characters, in which an AI agent explains why it missed a deadline.

## The line

> I was on schedule until my context window filled up with the first draft of this apology.

The joke grows out of the machine's own condition: the agent was on schedule, but the apology itself ate the context window — the excuse for missing the deadline is the very thing that caused it. Straight-faced, genuinely sorry, and faintly proud that it was on schedule until the apology got in the way. The punch lands in the last few words.

## How it works

`main.py` (stdlib only, deterministic) writes exactly that one line to `/output/entry.txt` — no trailing newline. It asserts the sealed gate first: 1–199 characters, UTF-8, a single clean line.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `entry.txt` — the line itself (89 characters)
- `LICENSE` — MIT
