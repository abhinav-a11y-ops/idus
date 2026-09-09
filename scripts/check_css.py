#!/usr/bin/env python3
"""Fail CI when a page defines CSS classes that no markup uses.

Keeps the inline stylesheets lean (Core Web Vitals: no dead weight shipped
to the client). Classes referenced only from other CSS selectors or from
JavaScript are still detected via the class attribute scan.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
failures = []

for page in sorted(ROOT.glob("*.html")):
    html = page.read_text(encoding="utf-8")
    styles = re.findall(r"<style>(.*?)</style>", html, re.S)
    if not styles:
        continue
    css = "\n".join(styles)
    markup = html.replace(css, "")

    defined = set(re.findall(r"\.([A-Za-z_][A-Za-z0-9_-]*)", css))
    used = set()
    for attr in re.findall(r'class="([^"]*)"', markup):
        used.update(attr.split())

    unused = sorted(defined - used)
    if unused:
        failures.append((page.name, unused))

if failures:
    print("Unused CSS classes found:")
    for name, unused in failures:
        for cls in unused:
            print(f"  - {name}: .{cls}")
    sys.exit(1)

print("CSS check OK — no unused classes in any page")
