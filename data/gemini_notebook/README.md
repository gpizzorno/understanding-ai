# Gemini Notebook Extractions

This folder contains three sets of named entities, and a network graph, extracted from the 20 letters in [`sample_letters/`](../sample_letters/) by Gemini Notebook. They are used in Section 10 of the [case study notebook](../../code/ner_pipeline.ipynb) to compare a conversational AI tool with the pre-trained NER models, on accuracy and on reproducibility.

| File | Rows | Produced |
|---|---|---|
| `extraction_run1.csv` | 327 | 29 September 2026 |
| `extraction_run2.csv` | 325 | 29 September 2026, new notebook, same prompt |
| `extraction_run3.csv` | 320 | 6 October 2026, a new notebook, same prompt (recorded for the activity page) |

**Runs 1 and 2** were produced on new notebooks with the 20 sample letters (and `selected_letters_metadata.csv`) as sources, on a Google AI Plus account. 

**Run 3** was produced on a new notebook with the 20 letters only, on the same account. No model version was shown anywhere in the interface. Both files were produced with the same prompt, and downloaded from the Studio panel unchanged:

> Extract every named person, place, and organization mentioned in these letters. Output a CSV file with the columns: file_name, entity_text, entity_type. Use PER, LOC, and ORG as entity types. Record entity_text exactly as written in the letter. Include every mention, not just unique names.

The tool ran code to produce each file, but the code was not visible and could not be downloaded.

**The network graph** (run 3, same notebook). After the CSV, the tool was asked:

> Create a network graph of the people mentioned in these letters, connecting two people when they are mentioned in the same letter

and then:

> What exact steps did you take to produce the network graph? Could I reproduce them myself?

`network_graph.png` is the image it produced, downloaded from the Studio panel unchanged. `network_graph_code.py` is the script it gave in response to the second prompt, copied from the chat unchanged. Run on the 20 letters, the script draws a different graph: 14 people instead of 63, in one colour, with no legend. The run 3 CSV and the network files are not used by the notebook but are shown on the [activity page](https://gpizzorno.github.io/understanding-ai/unit_2/gemini_notebook.html#part-3-reliability).

**Columns:** `file_name`, `entity_text` (as written in the letter), and `entity_type` (PER, LOC, or ORG).
