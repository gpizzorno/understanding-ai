"""Turn the bare URLs at the end of the rendered references into links on the publication details.

- Journal articles, and papers whose proceedings are given without "In": the whole publication
  details (journal, volume, issue, and pages).
- Chapters and papers "In" a book or proceedings: the title of the book or proceedings.
- "Paper presented at" a conference: the conference's name.
- Preprints: the repository ("Preprint, PsyArXiv" becomes "PsyArXiv"). arXiv preprints, and papers
  known only by their arXiv number, become a single link, "arXiv:2307.02483".
- Books, and works with no publication details: the title.

Pandoc builds the reference lists after every Lua filter has run, so this can't be done with a filter,
and a citation style can't choose a link's text. Quarto runs this script after rendering (post-render in
_quarto.yml). The hover previews read the same reference lists, so they show the links too. References
whose link text is already something other than the URL are left alone.
"""

import os
import re
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / '_site'

ENTRY = re.compile(r'(<div id="ref-[^"]*" class="csl-entry"[^>]*>)(.*?)(</div>)', re.S)
# the reference's final link, and whatever whitespace follows it
FINAL_LINK = re.compile(r'\s*<a href="(?P<url>[^"]+)">(?P<text>[^<]+)</a>\.(?P<end>\s*)$', re.S)
# the title of the work: in quotation marks (articles, chapters, papers) or in italics (books)
TITLE = re.compile(r'<span>“.*?”</span>|<em>.*?</em>', re.S)
ARXIV_URL = re.compile(r'https?://arxiv\.org/abs/(?P<id>[\w./-]+?)/?$')


def link(url, html):
    """Return the HTML as a link to the URL."""
    return f'<a href="{url}">{html}</a>'


def relink(entry):
    """Return the reference with its bare URL turned into a link."""
    final = FINAL_LINK.search(entry)
    if not final or final['text'] != final['url']:
        return entry
    url = final['url']
    title = TITLE.search(entry)
    if not title:
        return entry
    before, title_html = entry[: title.start()], title[0]
    italic_title = title_html.startswith('<em>')
    details = ' '.join(entry[title.end() : final.start()].split())
    if italic_title:
        details = details.removeprefix('.').strip()
    details = details.removesuffix('.')
    plain = re.sub(r'<[^>]+>', '', details)

    arxiv = ARXIV_URL.match(url)
    if arxiv and (not details or re.match(r'(arXiv:|Preprint, arXiv)', plain)):
        details = link(url, f'arXiv:{arxiv["id"]}')
    elif details.startswith('Preprint, '):
        details = link(url, details.removeprefix('Preprint, '))
    elif details.startswith('In <em>'):
        container = details[3 : details.index('</em>') + 5]
        details = 'In ' + link(url, container) + details[3 + len(container) :]
    elif details.startswith('<em>'):
        details = link(url, details)
    elif details.startswith('Paper presented at '):
        venue, sep, rest = details.removeprefix('Paper presented at ').partition('. ')
        details = 'Paper presented at ' + link(url, venue) + sep + rest
    else:
        # a book, or a work with no publication details: link its title
        title_html = link(url, title_html)

    if italic_title:
        reference = before + title_html + '.' + (f' {details}.' if details else '')
    else:
        reference = before + title_html + (f' {details}.' if details else '')
    return reference + final['end']


def relink_all(html):
    """Return the HTML with every reference relinked and the number of references changed."""
    count = 0

    def replace(m):
        nonlocal count
        new = relink(m[2])
        count += new != m[2]
        return m[1] + new + m[3]

    return ENTRY.sub(replace, html), count


def main():
    """Relink the references in the pages Quarto just rendered."""
    rendered = os.environ.get('QUARTO_PROJECT_OUTPUT_FILES')
    pages = [Path(f) for f in rendered.splitlines()] if rendered else SITE.rglob('*.html')
    total = 0
    for page in pages:
        if page.suffix != '.html' or not page.exists():
            continue
        html = page.read_text(encoding='utf-8')
        new, count = relink_all(html)
        if count:
            page.write_text(new, encoding='utf-8')
            total += count
    print(f'Linked the publication details of {total} references')


if __name__ == '__main__':
    main()
