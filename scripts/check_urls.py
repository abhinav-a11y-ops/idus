#!/usr/bin/env python3
"""Fail CI when SEO URLs drift apart.

Checks:
  * index.html has a canonical link
  * every sitemap <loc> is on the canonical's origin, lives under the
    canonical's base path, and the mapped file exists in the repo
  * robots.txt points at <canonical>/sitemap.xml
  * og:image and twitter:image agree and the mapped file exists in the repo

The canonical may be a project-site URL such as
https://abhinav-a11y-ops.github.io/idus/ — the repo root maps to that base
path, so URL -> repo-file mapping strips the base path.
"""
import pathlib
import re
import sys
from urllib.parse import urlsplit

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")
SITEMAP = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
ROBOTS = (ROOT / "robots.txt").read_text(encoding="utf-8")

errors = []

canon_match = re.search(r'rel="canonical"\s+href="([^"]+)"', INDEX)
if not canon_match:
    errors.append("index.html has no canonical link")
    canon = None
else:
    canon = canon_match.group(1)


def url_to_repo_path(url, canon_origin, canon_base):
    """Map an absolute URL to a repo-relative path, or None if it is outside
    the canonical origin/base."""
    parts = urlsplit(url)
    if f"{parts.scheme}://{parts.netloc}" != canon_origin:
        return None
    path = parts.path
    if canon_base:
        if not path.startswith(canon_base):
            return None
        path = path[len(canon_base):]
    path = path.lstrip("/")
    if not path:
        path = "index.html"
    return path


if canon:
    cp = urlsplit(canon)
    canon_origin = f"{cp.scheme}://{cp.netloc}"
    canon_base = cp.path.rstrip("/")
    canon_base_url = canon.rstrip("/")

    # Sitemap entries: on origin, under base path, file must exist.
    locs = re.findall(r"<loc>([^<]+)</loc>", SITEMAP)
    if not locs:
        errors.append("sitemap.xml contains no <url> entries")
    for loc in locs:
        rel = url_to_repo_path(loc, canon_origin, canon_base)
        if rel is None:
            errors.append(f"sitemap URL not under canonical {canon_base_url}/: {loc}")
        elif not (ROOT / rel).is_file():
            errors.append(f"sitemap URL has no matching repo file: {loc} -> {rel}")

    # robots.txt must reference <canonical>/sitemap.xml
    robots_sitemap = re.search(r"Sitemap:\s*(\S+)", ROBOTS)
    expected = canon_base_url + "/sitemap.xml"
    if not robots_sitemap:
        errors.append("robots.txt has no Sitemap: line")
    elif robots_sitemap.group(1).rstrip("/") != expected:
        errors.append(f"robots.txt Sitemap is {robots_sitemap.group(1)}, expected {expected}")

    # og:image and twitter:image must agree and point at a file in the repo.
    og = re.search(r'property="og:image"\s+content="([^"]+)"', INDEX)
    tw = re.search(r'name="twitter:image"\s+content="([^"]+)"', INDEX)
    if og and tw and og.group(1) != tw.group(1):
        errors.append("og:image and twitter:image differ")
    for name, url in (("og:image", og and og.group(1)), ("twitter:image", tw and tw.group(1))):
        if not url:
            errors.append(f"index.html is missing {name}")
            continue
        rel = url_to_repo_path(url, canon_origin, canon_base)
        if rel is None:
            errors.append(f"{name} is not under the canonical base path: {url}")
        elif not (ROOT / rel).is_file():
            errors.append(f"{name} file missing from repo: {rel}")


if errors:
    print("URL checks FAILED:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print("URL checks OK — sitemap, robots, canonical and social tags are consistent")
