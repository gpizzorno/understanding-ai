"""Build data/place_coordinates.csv: coordinates for the most-mentioned locations in the corpus.

Takes the most frequent LOC entities in data/extracted_entities.csv and looks each one up
with OpenStreetMap's Nominatim geocoder (https://nominatim.org).

Usage (from the repository root):
    python code/build_place_coordinates.py [number_of_places]

Nominatim's usage policy: https://operations.osmfoundation.org/policies/nominatim/)
"""  # noqa: INP001

import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import pandas as pd

ENTITIES_PATH = Path('data/extracted_entities.csv')
OUTPUT_PATH = Path('data/place_coordinates.csv')
USER_AGENT = 'understanding-ai-teaching-materials (https://github.com/gpizzorno/understanding-ai)'


def geocode(place):
    """Return (latitude, longitude, display_name) for a place name."""
    query = urllib.parse.urlencode({'q': place, 'format': 'json', 'limit': 1})
    request = urllib.request.Request(
        f'https://nominatim.openstreetmap.org/search?{query}',
        headers={'User-Agent': USER_AGENT},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        results = json.load(response)
    if not results:  # if not found return (None, None, None)
        return None, None, None
    return float(results[0]['lat']), float(results[0]['lon']), results[0]['display_name']


def main(n_places=60):
    """Build the place coordinates CSV for the most-mentioned locations."""
    entities = pd.read_csv(ENTITIES_PATH)
    top_places = entities[entities['entity_group'] == 'LOC']['text'].value_counts().head(n_places)

    # keep any review already done by hand
    reviews, notes = {}, {}
    if OUTPUT_PATH.exists():
        previous = pd.read_csv(OUTPUT_PATH).set_index('place')
        reviews = previous['review'].dropna().to_dict()
        notes = previous['note'].dropna().to_dict()

    rows = []
    for place, mentions in top_places.items():
        latitude, longitude, geocoded_as = geocode(place)
        print(f'{place:<30} {mentions:>4}  ->  {geocoded_as}')
        rows.append(
            {
                'place': place,
                'mentions': mentions,
                'latitude': latitude,
                'longitude': longitude,
                'geocoded_as': geocoded_as,
                'review': reviews.get(place, ''),
                'note': notes.get(place, ''),
            },
        )
        time.sleep(1.1)  # Nominatim usage policy: max one request per second

    pd.DataFrame(rows).to_csv(OUTPUT_PATH, index=False)
    print(f'\nWrote {len(rows)} places to {OUTPUT_PATH}')


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 60)
