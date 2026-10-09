"""Helper script to select a diverse subset of RLS letters for the Unit 2 NotebookLM activity.

Selects ~15-20 letters that:
- Span different time periods
- Include different correspondents
- Vary in content (personal, literary, travel, professional)
- Are not too long (to avoid NotebookLM upload issues)
"""  # noqa: INP001

import random
import shutil
from pathlib import Path

import pandas as pd


def select_sample_letters(metadata_path, letters_dir, output_dir, n_letters=18):
    """Select a diverse sample of letters for the NotebookLM activity."""
    # load metadata
    metadata = pd.read_csv(metadata_path)
    metadata['year_num'] = pd.to_numeric(metadata['year'], errors='coerce')
    metadata = metadata.dropna(subset=['year_num'])

    # define time periods
    early = metadata[metadata['year_num'] <= 1870]  # noqa: PLR2004
    middle = metadata[(metadata['year_num'] > 1870) & (metadata['year_num'] <= 1880)]  # noqa: PLR2004
    late = metadata[metadata['year_num'] > 1880]  # noqa: PLR2004

    # key correspondents
    key_correspondents = [
        'SIDNEY COLVIN',
        'EDMUND GOSSE',
        'W. E. HENLEY',
        'MRS. THOMAS STEVENSON',
        'THOMAS STEVENSON',
        'CHARLES BAXTER',
        'HENRY JAMES',
    ]

    selected = []

    # sample from each time period
    if len(early) > 0:
        selected.extend(early.sample(min(2, len(early))).to_dict('records'))

    if len(middle) > 0:
        selected.extend(middle.sample(min(6, len(middle))).to_dict('records'))

    if len(late) > 0:
        selected.extend(late.sample(min(10, len(late))).to_dict('records'))

    # ensure we have key correspondents
    for correspondent in key_correspondents:
        if len(selected) >= n_letters:
            break
        corr_letters = metadata[metadata['addressee'] == correspondent]
        if len(corr_letters) > 0 and correspondent not in [s['addressee'] for s in selected]:
            selected.append(corr_letters.sample(1).to_dict('records')[0])

    # trim to desired number
    random.shuffle(selected)
    selected = selected[:n_letters]

    # create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # copy selected letters
    letters_path = Path(letters_dir)
    for letter in selected:
        src = letters_path / letter['file_name']
        dst = output_path / letter['file_name']
        if src.exists():
            shutil.copy2(src, dst)
            print(f'Copied: {letter["file_name"]} (to {letter["addressee"]}, {letter["date"]})')

    # save metadata for selected letters
    selected_df = pd.DataFrame(selected)
    selected_df.to_csv(output_path / 'selected_letters_metadata.csv', index=False)
    print(f'\nSelected {len(selected)} letters')
    print(f'Time range: {selected_df["year_num"].min():.0f} - {selected_df["year_num"].max():.0f}')
    print('\nCorrespondents included:')
    print(selected_df['addressee'].value_counts())

    return selected_df


if __name__ == '__main__':
    random.seed(42)  # for reproducibility

    metadata_path = 'data/letters_metadata.csv'
    letters_dir = 'data/letters'
    output_dir = 'data/sample_letters'

    selected = select_sample_letters(metadata_path, letters_dir, output_dir, n_letters=18)

    print(f'\nSample letters ready in {output_dir}/')
    print('Upload these to NotebookLM for the Unit 2 activity.')
