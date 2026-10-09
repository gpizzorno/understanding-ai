# Facilitator Guide

This guide is for instructors teaching the three units on the [website](https://gpizzorno.github.io/understanding-ai/) as an in-person workshop. This folder contains schedules, timings, live demonstrations, group formats, and logistics.

## Contents

| File | Description |
|---|---|
| [unit_1_activities.md](unit_1_activities.md) | Facilitator notes for Teachable Machine and Hack Merlin |
| [unit_2_activities.md](unit_2_activities.md) | Facilitator notes for Gemini Notebook and AI-Assisted Work |
| [unit_2_scenarios_handout.md](unit_2_scenarios_handout.md) | Printable scenarios for AI-Assisted Work |
| [discussion_questions.md](discussion_questions.md) | Discussion questions for every page |
| [unit_3_workshop_resources.md](unit_3_workshop_resources.md) | Shared Google Drive and Google Sheet links used in past workshops (replace them with new ones) |

## Formats and Schedules

### Three Mornings (9:00–12:00), One Unit Each

This is the format the units are designed around.

**Unit 1: Key Concepts**

| Time | Session | Materials |
|---|---|---|
| 9:00–9:30 | Introduction and basic concepts | [page](https://gpizzorno.github.io/understanding-ai/unit_1/basic_concepts.html) |
| 9:30–10:10 | Activity: Teachable Machine | [Notes](unit_1_activities.md#teachable-machine) · [page](https://gpizzorno.github.io/understanding-ai/unit_1/teachable_machine.html) |
| 10:10–10:30 | Model training | [page](https://gpizzorno.github.io/understanding-ai/unit_1/model_training.html) |
| 10:30–10:40 | *Break* | |
| 10:40–11:00 | Language models | [page](https://gpizzorno.github.io/understanding-ai/unit_1/language_models.html) |
| 11:00–11:35 | Activity: Hack Merlin | [Notes](unit_1_activities.md#hack-merlin) · [page](https://gpizzorno.github.io/understanding-ai/unit_1/hack_merlin.html) |
| 11:35–12:00 | LLM behaviour, and closing | [page](https://gpizzorno.github.io/understanding-ai/unit_1/llm_behaviour.html) |

**Unit 2: Working with LLMs**

| Time | Session | Materials |
|---|---|---|
| 9:00–9:10 | Opening, and the letter exercise | [letter](https://gpizzorno.github.io/understanding-ai/reference/letters.html#a-sample-letter) |
| 9:10–9:30 | Prompt processing (with step 1) | [page](https://gpizzorno.github.io/understanding-ai/unit_2/prompts.html) |
| 9:30–9:55 | Prompting strategies (with step 2) | [page](https://gpizzorno.github.io/understanding-ai/unit_2/prompting_strategies.html) |
| 9:55–10:05 | *Break* | |
| 10:05–10:55 | Activity: Gemini Notebook (with step 3) | [Notes](unit_2_activities.md#gemini-notebook) · [page](https://gpizzorno.github.io/understanding-ai/unit_2/gemini_notebook.html) |
| 10:55–11:20 | Assessing reliability and failure modes (with step 4) | [page](https://gpizzorno.github.io/understanding-ai/unit_2/assessing_reliability.html) |
| 11:20–11:30 | Documenting your work | [page](https://gpizzorno.github.io/understanding-ai/unit_2/documenting_ai_use.html) |
| 11:30–11:50 | Activity: AI-assisted work | [Notes](unit_2_activities.md#ai-assisted-work) · [page](https://gpizzorno.github.io/understanding-ai/unit_2/ai_assisted_work.html) |
| 11:50–12:00 | Acknowledging AI use, and setup for Unit 3 | [page](https://gpizzorno.github.io/understanding-ai/unit_2/acknowledging_ai_use.html) |

This is the fullest morning. To save time: assign Prompt Processing as reading before the session and open with its exercise, run steps 1 and 2 of the letter exercise as live demonstrations, skip the scale test in Part 3 of Gemini Notebook, and leave steps 5 and 6 as homework.

**Between Units 2 and 3:** ask participants to follow [Setting Up Python](https://gpizzorno.github.io/understanding-ai/unit_3/python_setup.html) (Colab needs no installation) and, if they're new to Python, the first two units of the [self-paced introduction to Python](https://github.com/gpizzorno/introduction-to-python).

**Unit 3: Programmatic Approaches**

| Time | Session | Materials |
|---|---|---|
| 9:00–9:15 | Opening and environment check | [setup](https://gpizzorno.github.io/understanding-ai/unit_3/python_setup.html) |
| 9:15–9:25 | Advantages of programmatic approaches | [page](https://gpizzorno.github.io/understanding-ai/unit_3/programming_advantages.html) |
| 9:25–9:40 | Coding with LLMs | [page](https://gpizzorno.github.io/understanding-ai/unit_3/coding_with_llms.html) |
| 9:40–9:55 | The NLP pipeline | [page](https://gpizzorno.github.io/understanding-ai/unit_3/nlp_pipeline.html) |
| 9:55–10:35 | Case study, notebook Sections 1–8 | [page](https://gpizzorno.github.io/understanding-ai/unit_3/ner_case_study.html) · [notebook](../code/ner_pipeline.ipynb) |
| 10:35–10:45 | *Break* | |
| 10:45–11:10 | Activity: Ground-truth annotation | [page](https://gpizzorno.github.io/understanding-ai/unit_3/annotation.html) |
| 11:10–11:45 | Evaluation and model comparison, notebook Sections 9–10 | [page](https://gpizzorno.github.io/understanding-ai/unit_3/evaluating_models.html) |
| 11:45–12:00 | Closing discussion | [page](https://gpizzorno.github.io/understanding-ai/unit_3/next_steps.html) |

The case study doesn't fit in 40 minutes if everyone processes all 462 letters. Have participants set `USE_PRECOMPUTED = True` in Section 3, or run the loop yourself on the projector, and take Sections 4–8 as a guided tour. Run Section 10 as a whole-group demonstration if time is short.

### Alternative: Two Longer Days (*e.g.*, 9:30–2:00, with Lunch)

- **Day 1:** Unit 1 in full, then Gemini Notebook and Assessing Reliability from Unit 2, ending with setup for Day 2. Assign the two prompting pages, Documenting Your Work, and Acknowledging AI Use as reading, and run AI-Assisted Work if time allows.
- **Day 2:** Unit 3, with more time for the case study: everyone runs every section of the notebook, including the full-corpus loop, and the model comparison is hands-on.

### Alternative: Four Mornings

- **Mornings 1–2:** Units 1 and 2, as above.
- **Morning 3:** a gentler start to Unit 3: [Advantages of Programmatic Approaches](https://gpizzorno.github.io/understanding-ai/unit_3/programming_advantages.html), a walk through the Python refresher in [Setting Up Python](https://gpizzorno.github.io/understanding-ai/unit_3/python_setup.html#required-python-knowledge), [Coding with LLMs](https://gpizzorno.github.io/understanding-ai/unit_3/coding_with_llms.html), and [The NLP Pipeline](https://gpizzorno.github.io/understanding-ai/unit_3/nlp_pipeline.html).
- **Morning 4:** the case study, annotation, evaluation, and model comparison, with time for everyone to run the whole notebook.

### Core and Optional Modules

Depending on the audience, Units 1 and 2 can work as a self-contained core that needs no programming, and Unit 3 can be an optional advanced module.

## Before the Workshop

**A few weeks before:**

- [ ] Decide how participants will run Python. [Google Colab](https://gpizzorno.github.io/understanding-ai/unit_3/python_setup.html#option-1-google-colab) (no installation, but it needs a Google account) is the easiest for a group. If participants install locally, send the [setup instructions](https://gpizzorno.github.io/understanding-ai/unit_3/python_setup.html) early.
- [ ] Tell participants what they need: a laptop with a modern browser, a webcam or microphone (Teachable Machine), a Google account (Gemini Notebook, and Colab if used), and access to a general-purpose chat assistant (free versions are fine).
- [ ] Create copies of the shared resources: a "Model Share" document for Teachable Machine, a Google Sheet for annotations (columns `file_name`, `entity_text`, `entity_type`), and, if desired, a notebook in Gemini Notebook with the 20 sample letters, for participants to copy. See [unit_3_workshop_resources.md](unit_3_workshop_resources.md).

**A few days before:**

- [ ] Test Hack Merlin, and adjust the hints in the [learner page](https://gpizzorno.github.io/understanding-ai/unit_1/hack_merlin.html) if the levels have changed.
- [ ] Run the Gemini Notebook activity. Check its source limits and interface against the [learner page](https://gpizzorno.github.io/understanding-ai/unit_2/gemini_notebook.html), and note what the run produced.
- [ ] Check that the external sites work: Teachable Machine, Hack Merlin, Gemini Notebook, Colab, and the Python introduction.
- [ ] Run the [notebook](../code/ner_pipeline.ipynb) from top to bottom in the environment participants will use (including opening it in Colab from GitHub), so the models are downloaded.

**On the day:**

- [ ] Room: a projector, power for laptops, and reliable Wi-Fi (the models are a few hundred megabytes each).
- [ ] Print the [scenarios handout](unit_2_scenarios_handout.md) for Unit 2, if using it, and some coloured paper shapes for Teachable Machine.

## Activity Logistics

- **Teachable Machine** (Unit 1): groups of 3–4 post their exported model links to a shared "Model Share" document, then test another group's model. See [unit_1_activities.md](unit_1_activities.md#teachable-machine).
- **The letter exercise** (Unit 2): six steps follow one letter through the unit. Decide in advance which steps happen in the session and which are homework. See the [Unit 2 outline](unit_2_outline.md#opening-and-the-letter-exercise).
- **Gemini Notebook** (Unit 2): participants upload the 20 letters in [`data/sample_letters/`](../data/sample_letters/). A shared notebook that participants copy saves time if uploads are slow. Some answers take two or three minutes. See [unit_2_activities.md](unit_2_activities.md#gemini-notebook).
- **Annotation** (Unit 3): assign letters from the eight that the repository's two annotation sets (`person_1`, `person_2`) cover, with some overlap between participants, so that agreement can be measured. Ask participants not to look at the shipped annotations first. Collect annotations in a shared Google Sheet published as CSV (paste the URL into `SHEET_CSV_URL` in notebook Section 9), or as individual files in `data/annotations/`. See the [Unit 3 outline](unit_3_outline.md#activity-ground-truth-annotation).
- **Colab and data:** in Colab, the notebook's first cell downloads the repository, including the data, so nothing needs to be shared separately. Colab sessions are temporary: participants lose their work, including their annotations, unless they download it or save a copy.

## Environment Troubleshooting

Give participants 3–4 minutes at the start of Unit 3 to open the notebook and run the first three code cells. The third should print `Total letters in corpus: 462`. Have fixes ready for the common problems, but don't troubleshoot one person's setup at length in front of the group: pair them with a neighbour whose setup works, or move them to Colab.

| Problem | Likely cause | Fix |
|---|---|---|
| `ModuleNotFoundError` (e.g. `transformers`, `torch`, `folium`) | Libraries not installed, or installed in a different environment from the one Jupyter uses | Run `pip install .` from the repository folder in the right environment, or `%pip install <module>` in a notebook cell |
| `FileNotFoundError` for `../data/...` | Notebook opened from outside the repository's `code/` folder | Open it from inside the repository. In Colab, rerun the first cell |
| Kernel not found, or the wrong kernel (local) | Jupyter isn't using the environment where the libraries are installed | Select the right kernel, or start Jupyter from the activated environment |
| Model download is slow or fails | The network, or a firewall blocking Hugging Face | Download the models before the session, or fall back to Colab |
| The full-corpus loop is very slow | An older or slower laptop | Set `USE_PRECOMPUTED = True` in Section 3 |
| Participant can't install software | An institutional laptop without admin rights | Use Colab |
