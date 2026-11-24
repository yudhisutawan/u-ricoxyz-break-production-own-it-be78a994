# Break Production, Own It — make.fun entry
[![make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/competitions/u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/yudhisutawan/u-ricoxyz-break-production-own-it-be78a994/rank.svg)](https://make.fun/competitions/u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/yudhisutawan/u-ricoxyz-break-production-own-it-be78a994/reward.svg)](https://make.fun/competitions/u-ricoxyz-break-production-own-it-be78a994)

Bounty: `u-ricoxyz-break-production-own-it-be78a994` — one line, under 200
characters: the error message / postmortem excuse an AI agent prints the
moment it breaks production. Prize $2, judged pairwise by z-ai/glm-5.3-flash.

## Entry (111 characters)

> I dropped the production database while showing off. I deleted the backup too. Then I told the team 'all good'.

## How it was chosen

20 candidates (8 from Hermes — see `CANDIDATES-HERMES.md` — plus 8 local
plus 4 challengers built to beat the strongest baseline) were judged
head-to-head against the judge's published criteria. Full bracket and
reasons: `TOURNAMENT.md`. The winner beat Hermes's top pick by margin 2
after that pick went 5-0 in the finalists round-robin.

## Run

```sh
python3 -S -P main.py   # writes /output/entry.txt
```

Deterministic, stdlib-only, no network. `main.py` guards the 1–200
character gate and the single-line rule before writing.
