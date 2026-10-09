"""Check the links in the built website (docs/_site), and exit with an error if any are broken.

- Links between pages: the target page exists, and so does the #anchor, if there is one.
- Links to this repository on GitHub (e.g. data files, the facilitator guide): the file or folder
  exists in the repository.

Run after `quarto render docs`:   python3 docs/_scripts/check_links.py
"""

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urldefrag, urljoin, urlparse

DOCS = Path(__file__).resolve().parent.parent
SITE = DOCS / '_site'
REPO = DOCS.parent
SITE_URL = 'https://gpizzorno.github.io/understanding-ai/'
GITHUB_PREFIXES = (
    'https://github.com/gpizzorno/understanding-ai/blob/main/',
    'https://github.com/gpizzorno/understanding-ai/tree/main/',
)


class PageParser(HTMLParser):
    """Collect ids and link targets of a page."""

    def __init__(self):
        """Start with no ids and no links."""
        super().__init__()
        self.ids, self.links = set(), []

    def handle_starttag(self, tag, attrs):
        """Record tag id and target."""
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])


def parse(path):
    """Parse HTML page."""
    parser = PageParser()
    parser.feed(path.read_text(encoding='utf-8'))
    return parser


def check_link(page, href, pages):
    """Return error for link, or None if it works (or is external)."""
    if href.startswith(GITHUB_PREFIXES):
        repo_path = unquote(urldefrag(href)[0].split('/main/', 1)[1]).rstrip('/')
        return None if (REPO / repo_path).exists() else 'no such file in the repository'
    if href.startswith(SITE_URL):
        site_path, base = urljoin(SITE_URL, href)[len(SITE_URL) :], SITE
    elif urlparse(href).scheme or href.startswith(('mailto:', '//')):
        return None  # external link
    else:
        site_path, base = href, page.parent
    path, anchor = urldefrag(site_path)
    target = (base / unquote(path)).resolve() if path else page
    if target.is_dir():
        target = target / 'index.html'
    if not target.exists():
        return 'no such page'
    if anchor and target.suffix == '.html':
        ids = pages[target].ids if target in pages else parse(target).ids
        if anchor not in ids:
            return 'no such anchor'
    return None


def main():
    """Check every link on every page, print the broken ones, and return the exit status."""
    pages = {path: parse(path) for path in SITE.rglob('*.html') if 'site_libs' not in path.parts}
    problems = []
    for page, parsed in sorted(pages.items()):
        for href in parsed.links:
            problem = check_link(page, href, pages)
            if problem:
                problems.append(f'{page.relative_to(SITE)}: {href} ({problem})')
    for problem in problems:
        print(problem)
    print(f'{len(pages)} pages checked, {len(problems)} broken links')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
