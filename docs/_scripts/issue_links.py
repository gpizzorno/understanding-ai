"""Make each page's "Report an issue" link name the page it came from.

Quarto's issue link (repo-actions in _quarto.yml) opens a blank new issue. This adds the page's title as
the issue's title, and the page's address to its text, so readers don't have to say which page they mean.
"""

import os
import re
from html import unescape
from pathlib import Path
from urllib.parse import quote

SITE = Path(__file__).resolve().parent.parent / '_site'
SITE_URL = 'https://gpizzorno.github.io/understanding-ai/'
ISSUE_LINK = 'href="https://github.com/gpizzorno/understanding-ai/issues/new"'


def add_page(html, page):
    """Return the HTML with its issue link naming the page, and whether anything changed."""
    if ISSUE_LINK not in html:
        return html, False
    title = re.search(r'<title>(.*?)</title>', html, re.S)
    title = unescape(title[1]).split(' – ')[0].strip() if title else page.stem
    url = SITE_URL + page.relative_to(SITE).as_posix()
    query = f'title={quote(title)}&body={quote(f"Page: {url}" + chr(10) + chr(10))}'
    return html.replace(ISSUE_LINK, f'href="https://github.com/gpizzorno/understanding-ai/issues/new?{query}"'), True


def main():
    """Name the page in the issue links of the pages Quarto just rendered (or of every page, if run by hand)."""
    rendered = os.environ.get('QUARTO_PROJECT_OUTPUT_FILES')
    pages = [Path(f) for f in rendered.splitlines()] if rendered else SITE.rglob('*.html')
    total = 0
    for page in pages:
        if page.suffix != '.html' or not page.exists():
            continue
        html, changed = add_page(page.read_text(encoding='utf-8'), page.resolve())
        if changed:
            page.write_text(html, encoding='utf-8')
            total += 1
    print(f'Named the page in {total} issue links')


if __name__ == '__main__':
    main()
