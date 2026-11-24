# Writes the one pitch to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
# The market: workers who need quiet, priced by the minute.
import os
LINE = "We rent silence by the minute: empty flats for workers who need quiet, because the café is loud and home has children."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)  # same output on every run
