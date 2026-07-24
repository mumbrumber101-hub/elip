#!/usr/bin/env python3
"""Atomic manifest status update: set_status.py <unit-id> <status> [note-to-append]"""
import json, sys, os, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "manifest.json")
ORDER = ["pending", "extracted", "transcribed", "translated", "reviewed"]

uid, status = sys.argv[1], sys.argv[2]
note = sys.argv[3] if len(sys.argv) > 3 else None
assert status in ORDER, f"bad status {status}"

with open(PATH, encoding="utf-8") as f:
    m = json.load(f)
hit = [u for u in m["units"] if u["id"] == uid]
assert len(hit) == 1, f"unit {uid} not found"
hit[0]["status"] = status
if note:
    hit[0]["notes"] = (hit[0]["notes"] + "; " if hit[0]["notes"] else "") + note

fd, tmp = tempfile.mkstemp(dir=ROOT, suffix=".json")
with os.fdopen(fd, "w", encoding="utf-8") as f:
    json.dump(m, f, indent=2, ensure_ascii=False)
    f.write("\n")
os.replace(tmp, PATH)
print(f"{uid} -> {status}")
