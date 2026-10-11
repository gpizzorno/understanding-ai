"""Report titles that don't follow the site's Title Case rule, with the suggested fix.

Checks page titles (front matter), headings and callout titles in every .qmd page, the sidebar labels in
_quarto.yml, and the headings in the case study notebook. It only reports: nothing is changed, and it
isn't part of the build.

The rule: capitalize the first and last words, every word after a colon, and all major words (nouns,
pronouns, verbs including Is/Are/Be, adjectives, adverbs including Not, and particles such as Up in
"Setting Up"). Lowercase articles, coordinating conjunctions, "as", "to", and prepositions of four letters
or fewer. In hyphenated compounds, capitalize each major part ("Pre-Trained", but "All-or-Nothing").
Words with capitals or digits inside them (LLMs, NER, F1), inline code, and link targets are left alone.

Run from anywhere:   python3 docs/_scripts/check_titlecase.py
"""

import json
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
REPO = DOCS.parent
NOTEBOOK = REPO / 'code' / 'ner_pipeline.ipynb'

MINOR = {
    'a', 'an', 'the', 'and', 'or', 'but', 'nor', 'as', 'at', 'by', 'for', 'from', 'in', 'into', 'of', 'off',
    'on', 'onto', 'over', 'per', 'to', 'via', 'vs.', 'vs', 'with', 'up',
}
# a minor word after one of these verbs is a particle, and is capitalized ("Setting Up")
PARTICLE_AFTER = {'set', 'setting', 'follow', 'writing', 'write', 'look', 'pick', 'break', 'sign'}
PARTICLES = {'up', 'out', 'off', 'on', 'in'}


def cap(word):
    """Capitalize the first letter, leaving the rest as it is."""
    return word[:1].upper() + word[1:]


def title_word(word, first, last, prev):
    """Return one word in title case, given its position and the word before it."""
    core = word.strip('*"“”‘’\'()[]?!.,:;')
    if (
        not core
        or core.startswith(('`', '{', '<', 'http'))
        or any(c.isupper() or c.isdigit() for c in core[1:])
        or (core.isupper() and len(core) > 1)
    ):
        return word
    if '-' in core:
        parts = core.split('-')
        new = '-'.join(p if (i > 0 and p.lower() in MINOR) else cap(p) for i, p in enumerate(parts))
        return word.replace(core, new, 1)
    lower = core.lower()
    particle = lower in PARTICLES and prev.lower().strip('*') in PARTICLE_AFTER
    if lower in MINOR and not first and not last and not particle:
        return word.replace(core, lower, 1)
    return word.replace(core, cap(core), 1)


def titlecase(title):
    """Return the title in title case, leaving inline code, link targets, attributes, and HTML alone."""
    pieces = re.split(r'(`[^`]*`|\{[^}]*\}|\]\([^)]*\)|<[^>]+>)', title)
    positions = [(i, j) for i, piece in enumerate(pieces) if i % 2 == 0 for j, w in enumerate(piece.split(' ')) if w]
    out, seen = [], []
    for i, piece in enumerate(pieces):
        if i % 2:
            out.append(piece)
            continue
        words = piece.split(' ')
        for j, word in enumerate(words):
            if not word:
                continue
            k = positions.index((i, j))
            prev = seen[-1] if seen else ''
            words[j] = title_word(word, k == 0 or prev.endswith(':'), k == len(positions) - 1, prev)
            seen.append(word)
        out.append(' '.join(words))
    return ''.join(out)


def titles():
    """Yield (file, line number, kind, title) for every title on the site and in the notebook."""
    for page in sorted(DOCS.rglob('*.qmd')):
        if '_site' in page.parts:
            continue
        lines = page.read_text(encoding='utf-8').split('\n')
        fence, front_matter = False, 0
        for n, line in enumerate(lines, 1):
            if line.strip() == '---' and front_matter < 2 and n < 15:
                front_matter += 1
                continue
            if front_matter == 1:
                if m := re.match(r"^title: '(.*)'$", line):
                    yield page, n, 'title', m[1].replace("''", "'")
                continue
            if line.lstrip().startswith(('```', '~~~')):
                fence = not fence
            elif not fence and (m := re.match(r'^#{1,6} (.+)$', line)):
                yield page, n, 'heading', m[1]
    config = DOCS / '_quarto.yml'
    for n, line in enumerate(config.read_text(encoding='utf-8').split('\n'), 1):
        if m := re.match(r"^\s*-? ?(?:text|section): '?(.*?)'?$", line):
            yield config, n, 'sidebar', m[1]
    cells = json.loads(NOTEBOOK.read_text(encoding='utf-8'))['cells']
    for n, cell in enumerate(cells, 1):
        if cell['cell_type'] == 'markdown':
            for line in ''.join(cell['source']).split('\n'):
                if m := re.match(r'^#{1,6} (.+)$', line):
                    yield NOTEBOOK, n, 'notebook cell', m[1]


def main():
    """Print every title that differs from its title-case form."""
    count = 0
    for path, n, kind, title in titles():
        suggestion = titlecase(title)
        if suggestion != title:
            print(f'{path.relative_to(REPO)}:{n} [{kind}]  {title}  →  {suggestion}')
            count += 1
    print(f'{count} titles to check')


if __name__ == '__main__':
    main()
