"""Combine all the letters into a single Markdown file, for tools that limit the number of sources.

Run from the repository root:  python code/build_combined_letters.py
"""  # noqa: INP001

import re
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / 'data'
LETTERS_DIR = DATA_DIR / 'letters'
OUTPUT_PATH = DATA_DIR / 'stevenson_letters_combined.md'


def sort_key(file_name):
    """Order letters by volume, chapter, and letter number (numerically, so letter2 comes before letter10)."""
    volume, chapter, letter = map(int, re.findall(r'\d+', file_name))
    return volume, chapter, letter


def main():
    """Combine all the letters into a single Markdown file."""
    metadata = pd.read_csv(DATA_DIR / 'letters_metadata.csv').set_index('file_name')
    files = sorted((p.name for p in LETTERS_DIR.glob('*.txt')), key=sort_key)

    parts = [
        '# The Letters of Robert Louis Stevenson',
        '',
        (
            f"{len(files)} letters, one per section. Each section heading is the letter's file name in "
            'data/letters/, followed by the addressee and date from data/letters_metadata.csv. '
            'Text transcribed on Wikisource, public domain.'
        ),
    ]
    for name in files:
        row = metadata.loc[name].fillna('unknown')
        text = (LETTERS_DIR / name).read_text(encoding='utf-8').strip()
        parts += ['', f'## {name}', '', f'Addressee: {row["addressee"]}. Date: {row["date"]}.', '', text]

    OUTPUT_PATH.write_text('\n'.join(parts) + '\n', encoding='utf-8')
    words = sum(len(p.split()) for p in parts)
    print(f'Wrote {len(files)} letters ({words:,} words) to {OUTPUT_PATH.relative_to(DATA_DIR.parent)}')


if __name__ == '__main__':
    main()
