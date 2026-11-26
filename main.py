"""Office Artifacts: The One-Line Placard Contest.

Writes a single-line museum placard for an ordinary office object,
treated as an ancient artifact, to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os

ENTRY = "Stapler, Office of Eternal Meetings, circa 1987. Forged in boredom, worshipped by interns, it binds what no one will ever read again. Do not touch. It remembers."


def main():
    # The gate counts the file's characters (1-180), so the entry is
    # written exactly, with no trailing newline, and checked first.
    assert 1 <= len(ENTRY) <= 180, "entry must be 1-180 characters"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
