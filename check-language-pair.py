#!/usr/bin/env python3
"""Check the HTML and search metadata of an Arabic–English page pair."""

import argparse
from html.parser import HTMLParser
from urllib.request import Request, urlopen


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.language = ""
        self.direction = ""
        self.canonicals = []
        self.alternates = {}
        self.robots = []
        self.in_head = False
        self.feed(html)

    def handle_starttag(self, tag, attributes):
        values = {key: value or "" for key, value in attributes}
        if tag == "html":
            self.language = values.get("lang", "").lower().split("-", 1)[0]
            self.direction = values.get("dir", "ltr").lower()
        elif tag == "head":
            self.in_head = True
        elif self.in_head and tag == "link":
            relationships = values.get("rel", "").lower().split()
            if "canonical" in relationships:
                self.canonicals.append(values.get("href", ""))
            language = values.get("hreflang", "").lower()
            if "alternate" in relationships and language:
                self.alternates.setdefault(language, []).append(values.get("href", ""))
        elif self.in_head and tag == "meta":
            if values.get("name", "").lower() in {"robots", "googlebot"}:
                self.robots.append(values.get("content", ""))

    def handle_endtag(self, tag):
        if tag == "head":
            self.in_head = False


def blocks_google_indexing(value):
    parameter_directives = {"max-snippet", "max-image-preview", "max-video-preview", "unavailable_after"}
    applies = True
    for directive in value.lower().split(","):
        key, separator, argument = directive.strip().partition(":")
        if separator and key.strip() not in parameter_directives:
            applies = key.strip() == "googlebot"
            directive = argument
        if applies and directive.strip() in {"noindex", "none"}:
            return True
    return False


def check(url, language, expected):
    request = Request(url, headers={"User-Agent": "HululLocaleCheck/1.0"})
    with urlopen(request, timeout=15) as response:
        if response.status != 200 or response.geturl() != url:
            return [f"Expected HTTP 200 at {url}. Got {response.status} at {response.geturl()}"]
        if response.headers.get_content_type() != "text/html":
            return ["Expected an HTML response"]
        html = response.read().decode(response.headers.get_content_charset() or "utf-8", errors="replace")
        page = Page(html)
        directives = (response.headers.get_all("X-Robots-Tag") or []) + page.robots

    errors = []
    direction = "rtl" if language == "ar" else "ltr"
    if (page.language, page.direction) != (language, direction):
        errors.append(f"Expected lang={language} and dir={direction}. Got {page.language}/{page.direction}")
    if page.canonicals != [url]:
        errors.append(f"Expected one self-referencing canonical. Found {page.canonicals}")
    for tag, destination in expected.items():
        if page.alternates.get(tag) != [destination]:
            errors.append(f"Expected one hreflang={tag} to {destination}. Found {page.alternates.get(tag, [])}")
    if any(blocks_google_indexing(value) for value in directives):
        errors.append("Found a directive that prevents Google from indexing this page")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("arabic", help="Canonical URL of the Arabic page")
    parser.add_argument("english", help="Canonical URL of the English page")
    parser.add_argument("--default", help="Expected x-default URL, if the site publishes one")
    args = parser.parse_args()

    expected = {"ar": args.arabic, "en": args.english}
    if args.default:
        expected["x-default"] = args.default

    failed = False
    for language, url in (("ar", args.arabic), ("en", args.english)):
        try:
            errors = check(url, language, expected)
        except (OSError, ValueError, LookupError) as exc:
            errors = [str(exc)]
        if errors:
            failed = True
            for error in errors:
                print(f"FAIL {url}: {error}")
        else:
            print(f"OK   {url}")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
