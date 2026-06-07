#!/usr/bin/env python3
"""Static QA checks for the Ferre Torres B.V. GitHub Pages site."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_HOST = "https://ferretorres.eu/"
STATIC_FILES = {
    "styles.css",
    "sitemap.xml",
    "robots.txt",
    "llms.txt",
    "favicon.svg",
    "site.webmanifest",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def html_files() -> list[Path]:
    return sorted(ROOT.glob("*.html"))


def is_noindex(content: str) -> bool:
    robots = re.search(r'<meta name="robots" content="([^"]*)"', content)
    return "noindex" in robots.group(1) if robots else False


def check_seo_metadata(errors: list[str]) -> None:
    for path in html_files():
        content = read(path)
        title = re.search(r"<title>([^<]+)</title>", content)
        if not title or not 10 <= len(title.group(1)) <= 60:
            errors.append(f"{path.name}: title length {len(title.group(1)) if title else 0}")

        description = re.search(r'<meta name="description" content="([^"]*)">', content)
        if not is_noindex(content) and (
            not description or len(description.group(1)) < 50 or len(description.group(1)) > 160
        ):
            errors.append(f"{path.name}: description length {len(description.group(1)) if description else 0}")

        if not re.search(r'<link rel="canonical" href="https://ferretorres.eu/[^"]*">', content):
            errors.append(f"{path.name}: canonical missing")


def check_json_ld(errors: list[str]) -> None:
    for path in html_files():
        content = read(path)
        for index, match in enumerate(
            re.finditer(r'<script type="application/ld\+json">(.*?)</script>', content, re.S),
            start=1,
        ):
            try:
                json.loads(match.group(1))
            except json.JSONDecodeError as exc:
                errors.append(f"{path.name}: JSON-LD block {index}: {exc}")


def local_asset_names() -> set[str]:
    files = {path.name for path in html_files()}
    files.update(STATIC_FILES)
    asset_dir = ROOT / "assets"
    if asset_dir.exists():
        files.update(str(path.relative_to(ROOT)) for path in asset_dir.glob("*") if path.is_file())
    return files


def check_local_links(errors: list[str]) -> None:
    files = local_asset_names()
    for path in html_files():
        content = read(path)
        for attr in ("href", "src"):
            for url in re.findall(attr + r'="([^"]+)"', content):
                if url.startswith(("http://", "https://", "mailto:", "tel:", "#")):
                    continue
                local_path = url.split("#", 1)[0].split("?", 1)[0]
                if not local_path:
                    continue
                if local_path.startswith("/"):
                    local_path = local_path.lstrip("/")
                if local_path not in files and not (ROOT / local_path).exists():
                    errors.append(f"{path.name}: missing local {attr} target {url}")


def check_sitemap(errors: list[str]) -> None:
    sitemap_path = ROOT / "sitemap.xml"
    if not sitemap_path.exists():
        errors.append("sitemap.xml missing")
        return

    indexable = {
        path.name for path in html_files() if "noindex" not in read(path)
    }
    sitemap = read(sitemap_path)
    urls = set(re.findall(r"https://ferretorres\.eu/([^<]*)", sitemap))
    urls = {"index.html" if url == "" else url for url in urls}
    missing = sorted(indexable - urls)
    extra = sorted(urls - indexable)
    if missing:
        errors.append(f"sitemap missing: {', '.join(missing)}")
    if extra:
        errors.append(f"sitemap extra: {', '.join(extra)}")


def check_document_accessibility(errors: list[str]) -> None:
    for path in html_files():
        content = read(path)
        if content.count('class="skip-link"') != 1:
            errors.append(f"{path.name}: skip link count")
        if content.count('id="top"') != 1:
            errors.append(f"{path.name}: top id count")
        if '<html lang="en"' not in content:
            errors.append(f"{path.name}: html lang missing")
        if len(re.findall(r"<h1[\s>]", content)) != 1:
            errors.append(f"{path.name}: h1 count")


def main() -> int:
    errors: list[str] = []
    check_seo_metadata(errors)
    check_json_ld(errors)
    check_local_links(errors)
    check_sitemap(errors)
    check_document_accessibility(errors)

    if errors:
        print("Static site checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Static site checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
