#!/usr/bin/env python3
"""Generate root index.html listing available version folders.

Usage: run from repository root where version folders live.
"""
from pathlib import Path
import re
import sys


def parse_version(name: str):
    s = name
    if s.startswith('v'):
        s = s[1:]
    s = s.replace('_', '.')
    # keep digits and dots
    s = re.sub(r'[^0-9.]', '', s)
    parts = [p for p in s.split('.') if p != '']
    try:
        nums = tuple(int(p) for p in parts)
        return nums
    except Exception:
        return ()


def find_versions(root: Path):
    versions = []
    for p in sorted(root.iterdir()):
        if not p.is_dir():
            continue
        if p.name.startswith('.'):  # skip .git etc
            continue
        # require an index.html to consider this a doc version
        if (p / 'index.html').exists():
            versions.append(p.name)
    return versions


HTML_TEMPLATE = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>PyJEM Documentation — Versions</title>
    <meta http-equiv="refresh" content="3;url={latest}/" />
    <style>
      body{{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:40px}}
      .box{{max-width:780px;margin:0 auto}}
      ul{{padding-left:1.2em}}
    </style>
  </head>
  <body>
    <div class="box">
      <h1>PyJEM Documentation</h1>
      <p>You will be redirected to the latest version in 3 seconds.</p>
      <p>If you are not redirected, or would like to view another version, use the links below.</p>
      <h2>Available versions</h2>
      <ul>
{items}
      </ul>
      <hr />
      <p>Maintainers: update this file when publishing new versions, or run <code>python scripts/generate_index.py</code>.</p>
    </div>
  </body>
</html>
"""


def main():
    root = Path('.').resolve()
    versions = find_versions(root)
    if not versions:
        print('No version folders with index.html found.', file=sys.stderr)
        return 2
    # sort by parsed numeric version, fallback to name
    def sort_key(name):
        kv = parse_version(name)
        if kv:
            return (*kv,)
        return (0, name)

    versions_sorted = sorted(versions, key=sort_key, reverse=True)
    latest = versions_sorted[0]

    items = []
    for v in versions_sorted:
        items.append(f'        <li><a href="{v}/">{v}</a></li>')

    html = HTML_TEMPLATE.format(latest=latest, items='\n'.join(items))
    out = root / 'index.html'
    out.write_text(html, encoding='utf-8')
    print(f'Wrote {out} -> latest: {latest}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
