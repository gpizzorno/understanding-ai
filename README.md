# Understanding AI: A Practical Workshop for Humanities and Social Science Researchers

<img align="right" src="docs/assets/understanding_ai_thumb.png" width=300  />

These materials introduce researchers in the humanities and social sciences to how contemporary AI systems work, what they can and cannot do, and how to use them critically in research. They start from a single idea: AI models learn patterns from data, and both their usefulness and their characteristic failures follow from it.

The three units move from concepts to practice to method. Throughout, the question is not only whether a tool gives a good answer, but whether you could check it, repeat it, and report it. The materials are designed for self-study, and no technical background is assumed.

## The Materials

**The materials are published as a [website](https://gpizzorno.github.io/understanding-ai/).** They are organized into three units:

- **[Unit 1: Key Concepts](https://gpizzorno.github.io/understanding-ai/unit_1/)** covers what AI systems are, how they learn from data, and why they behave the way they do. You'll train a small model yourself with Teachable Machine, and try to talk a chatbot out of its secret password in Hack Merlin.
- **[Unit 2: Working with LLMs](https://gpizzorno.github.io/understanding-ai/unit_2/)** covers how large language models process your prompts, how to prompt them well, how to judge how far their output can be trusted, and how to be transparent about using them. You'll explore a set of historical letters with an AI research tool, and find out what it does well, and what it can't do reliably.
- **[Unit 3: Programmatic Approaches](https://gpizzorno.github.io/understanding-ai/unit_3/)** covers what to do when you need scale, structured data, and reproducible results. You'll run a pre-trained model over 462 letters by Robert Louis Stevenson, turn the results into charts, a network, a timeline, and a map, and then measure how accurate the results actually are when compared to annotations made by people, including your own.

Units 1 and 2 need a web browser, a webcam or microphone, a Google account, and access to a general-purpose AI chat assistant (free versions are fine). Unit 3 uses Python, in Google Colab or on your own computer: the first two units need no programming, and the third asks you to read and run code, not to write it.

## Teaching a Workshop

The [facilitator guide](facilitator_guide/README.md) has suggested schedules, notes for each activity, discussion questions for every page, a preparation checklist, and environment troubleshooting. It lives here in the repository so it can be edited directly on GitHub.

## Repository Contents

| Folder | Contents |
|--------|----------|
| [`docs/`](docs/) | The website: the pages for each unit, and the reference pages, written in [Quarto](https://quarto.org) |
| [`code/`](code/) | The Jupyter notebook for the Unit 3 case study, and the scripts used to prepare the data |
| [`data/`](data/) | The Robert Louis Stevenson letters and their metadata, a 20-letter sample and a single-file version for the Gemini Notebook activity, pre-computed NER output, annotations, and Gemini Notebook extractions (see the [data README](data/README.md)) |
| [`facilitator_guide/`](facilitator_guide/) | Schedules and facilitator notes for teaching the units as a workshop |

To preview the website locally, [install Quarto](https://quarto.org/docs/get-started/) and run `quarto preview docs`. The website is published by GitHub Actions ([`.github/workflows/website.yml`](.github/workflows/website.yml)) whenever `docs/` or the notebook changes on `main`.

## Licence

- **Code** is licensed under the [MIT License](LICENSE).
- **Written materials** are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE-docs). You may share and adapt them for any purpose, including in your own teaching, as long as you give appropriate credit.
- **Data** in `data/` comes from other sources with their own terms, see the [data README](data/README.md).

## Acknowledgements

- [James Capobianco](https://dsg.fas.harvard.edu/about/people/james-capobianco/) and [Tracy Stuber](https://dsg.fas.harvard.edu/about/people/tracy-stuber/) helped design and teach the original workshops these materials grew out of, as part of the programming of the [Digital Scholarship Group](https://dsg.fas.harvard.edu) at Harvard University.
- The letters were transcribed by the contributors to [Wikisource](https://en.wikisource.org/wiki/The_Letters_of_Robert_Louis_Stevenson_Volume_1).
- [Jeremy Guillette](https://atg.fas.harvard.edu/people/jeremy-guillette) scraped the letters from Wikisource, and split and parsed them into text files and metadata, in the [`stevenson_letters`](https://github.com/jaguillette/stevenson_letters) repository, created for an earlier workshop on web scraping.
- Place coordinates come from [OpenStreetMap](https://www.openstreetmap.org/copyright) via the [Nominatim](https://nominatim.org) geocoder (© OpenStreetMap contributors, [ODbL](https://opendatacommons.org/licenses/odbl/)).
- The case study uses the named-entity recognition models [`Davlan/bert-base-multilingual-cased-ner-hrl`](https://huggingface.co/Davlan/bert-base-multilingual-cased-ner-hrl) and [`dslim/bert-base-NER`](https://huggingface.co/dslim/bert-base-NER), via Hugging Face [Transformers](https://github.com/huggingface/transformers).
- Unit 1 uses [Teachable Machine](https://teachablemachine.withgoogle.com) (Google) and [Hack Merlin](https://hackmerlin.io), Unit 2 uses [Gemini Notebook](https://notebook.google) (Google). These are third-party services, not affiliated with these materials.

## Citation

If you use or adapt these materials, please cite them as:

> Pizzorno, Gabriel H. *Understanding AI: A Practical Workshop for Humanities and Social Science Researchers*. 2026. https://github.com/gpizzorno/understanding-ai
