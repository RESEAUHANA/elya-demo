"""Vérifie que tous les liens internes du site généré pointent vers une page existante."""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bad, count = [], 0
for d, _, files in os.walk(ROOT):
    if "_src" in d or ".git" in d:
        continue
    for f in files:
        if not f.endswith(".html"):
            continue
        p = os.path.join(d, f)
        h = open(p, encoding="utf-8").read()
        if "{root}" in h:
            bad.append(("{root} non remplacé", os.path.relpath(p, ROOT)))
        for u in re.findall(r'href="([^"]+)"', h):
            if u.startswith(("http", "mailto", "#")):
                continue
            count += 1
            t = os.path.normpath(os.path.join(d, u))
            if os.path.isdir(t):
                t = os.path.join(t, "index.html")
            if not os.path.exists(t):
                bad.append((u, os.path.relpath(p, ROOT)))
print(count, "liens internes vérifiés,", len(bad), "problème(s)")
for b in bad[:40]:
    print(b)
