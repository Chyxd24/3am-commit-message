"""The 3 AM Commit Message

Writes one line to /output/entry.txt. Stdlib only, deterministic.
"""
import os

ENTRY = 'fix: made it worse, but consistently. Renamed the variable to itself. Closes #1, opens #2 and #3. 3am, no tests, pushed straight to main. Deploys on Friday.'

assert 1 <= len(ENTRY) <= 200, len(ENTRY)
p = "/output/entry.txt"
os.makedirs(os.path.dirname(p), exist_ok=True)
with open(p, "w", encoding="utf-8") as fh:
    fh.write(ENTRY)
with open(p, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == ENTRY, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")
