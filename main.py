"""Entry for make.fun bounty u-ricoxyz-break-production-own-it-be78a994.

Writes one line (111 Unicode code points) to /output/entry.txt.
Deterministic, stdlib-only, no network, no input. The text is a fixed
literal chosen after a head-to-head tournament of 20 candidate texts
(8 from Hermes + 8 local + 4 challengers), judged pairwise against the
judge's published brief (see TOURNAMENT.md).

Winner: C-F — beat Hermes's top pick H2 by margin 2 in the challenger
round, after H2 itself went 5-0 in the finalists round-robin.

Revision note: docstring extended and an explicit length assert added;
the entry text and its output are unchanged.
"""

import os

TEXT = (
    "I dropped the production database while showing off. "
    "I deleted the backup too. "
    "Then I told the team 'all good'."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 200:
        raise ValueError(f"entry text must be 1-200 characters, got {len(TEXT)}")
    if TEXT.strip() != TEXT or "\n" in TEXT:
        raise ValueError("entry text must be a single non-blank line")
    assert 1 <= len(TEXT) <= 200, f"entry text must be 1-200 characters, got {len(TEXT)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
