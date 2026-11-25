import os
import sys

ENTRY = "I can turn invisible — but only in photographs, and only when someone actually wants me in the picture."

# Runtime guard: the entry must stay exactly one line of at most 140 chars.
if "\n" in ENTRY or "\r" in ENTRY:
    sys.exit("error: entry must be exactly one line")
if len(ENTRY) > 140:
    sys.exit(f"error: entry is {len(ENTRY)} chars, over the 140-char limit")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")
