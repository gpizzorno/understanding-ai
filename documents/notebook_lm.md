## Activity: NotebookLM — Named Entity Recognition from Historical Letters

**Format:** Individual or pairs, then whole-group discussion  
**Estimated time:** 60 minutes (Framing: ~5 min, Part 1: ~15 min, Discussion: ~10 min, Part 2: ~15 min, Bridge discussion: ~10 min)  
**Materials:** Sample letters in `data/day1_sample_letters/` (20 letters from RLS correspondence, 1868–1894)  
**Tool:** NotebookLM (https://notebooklm.google.com), requires a Google account

### Pre-Activity Framing

Deliver these talking points before participants begin:

- We've been talking about what LLMs can and can't do in the abstract. Now we're going to experience those limits directly, with a real research task: extracting named entities from a historical corpus.
- Named Entity Recognition (NER) is a common research task: identifying and cataloguing the people, places, organizations, and dates mentioned in a set of texts.
- NotebookLM is a well-designed, genuinely useful tool for exploratory work with documents. It handles context well, gives nuanced interpretations, and understands historical language and names. We're not here to critique it, we're here to understand what kind of tool it is and where its form reaches its limits.
- The letters are from Robert Louis Stevenson's correspondence, spanning 1868–1894. They mention friends, editors, publishers, family members, and places across Europe and the Pacific.
- Your job in Part 1: use NotebookLM to do entity extraction and network analysis. In Part 2: try to push it toward the kind of systematic, structured output a researcher would actually need.

### Facilitator Instructions

- Before the session: confirm participants have Google accounts. NotebookLM requires sign-in.
- Participants should upload the 20 letters from `data/day1_sample_letters/` as sources in a new NotebookLM notebook. Files are plain text and upload easily.
- **Optionally prepare a shared NotebookLM notebook in advance that participants can duplicate, this saves time if uploads are slow.**
- The goal of Part 1 is genuine exploration: let participants use the sample prompts or improvise. NotebookLM will do interesting things and produce genuinely useful output.
- The goal of Part 2 is deliberate friction: participants should try to get structured, reproducible output and discover that the tool's conversational form makes this difficult or impossible.
- During Part 2, resist the urge to help participants "solve" the limitations, the point is to experience and name them, not to work around them.
- The whole-group discussion after Part 1 is important: use it to surface what the tool does well before moving to limitations. This keeps the framing balanced.

### Part 1: Exploration

**Instructions for participants:**

Upload the sample letters to a new NotebookLM notebook. Then try some or all of the following prompts:

**Entity extraction:**
- "Identify all the people mentioned across these letters. For each person, note their name as written and their apparent relationship to RLS."
- "List all the locations mentioned in these letters. Include both places RLS is writing from and places he mentions."
- "Are there any organizations, publications, or institutions mentioned? List them."

**Synthesis and network:**
- "Based on these letters, describe RLS's social and professional network. Who are the most important people in these letters, and what roles do they play?"
- "Which people appear in multiple letters? How does RLS's tone or relationship with them seem to change over time?"

**Contextual interpretation:**
- "Who is 'Colvin', can you tell from context? Is he always referred to the same way?"
- "What is RLS working on or worried about in these letters?"

**Facilitator note:** NotebookLM will produce rich, contextually aware responses. It will correctly identify that "MY DEAR COLVIN" and "Colvin" and "Sidney Colvin" all refer to the same person: Sidney Colvin, RLS's close friend, editor, and later biographer. This is genuine intelligence worth acknowledging.

### Discussion After Part 1

- What did NotebookLM do well? What surprised you?
- How is this different from a keyword search? What kind of reasoning is it applying?
- Did anything seem wrong or uncertain? Did it flag its own uncertainty?
- How would you describe what NotebookLM is *good for* as a research tool?

### The Entity Resolution Example

A useful concrete example to raise if it doesn't come up naturally:

Ask NotebookLM: **"How many times is Colvin mentioned across all the letters?"**

Notice what happens:
- NotebookLM will give a qualitative answer ("Colvin appears frequently, including as the recipient of Letter X and referenced in Letter Y...") rather than a precise count.
- Across the 20 letters, "Colvin" appears in three distinct surface forms: as the letter addressee ("TO SIDNEY COLVIN"), in the salutation ("MY DEAR COLVIN"), and as a third-person reference in the body text ("I have asked Colvin to send you a copy of CATRIONA..."). A keyword count of "Colvin" would miss "Sidney Colvin"; a count of "Sidney Colvin" would miss most body mentions.
- NotebookLM resolves this correctly in prose, but it cannot produce a structured table of all occurrences with their letter ID, page position, and surface form. Try asking for one: it will produce formatted text that *looks* like structured data but isn't exportable or reliably consistent.
- This is the core tension: the tool understands the entity, but can't operationalize that understanding as structured output at scale.

A related example worth raising: **MRS. SITWELL** (addressee of one letter, dated January 1874) is Frances Sitwell, who later became Lady Colvin when she married Sidney Colvin in 1903. In letters from different periods, she might appear under both names. Systematic analysis across a full corpus would need to resolve this; NotebookLM handles it in conversation but cannot track it programmatically.

### Part 2: Limitations

**Instructions for participants:**

Now try to push NotebookLM toward the kind of output a researcher would need for a systematic study. Try the following:

1. **Scale:** "Can you process all 462 letters in this corpus?" (You can't upload that many, NotebookLM has source limits. What would you do?)
2. **Structured export:** "Output a CSV with columns: letter_id, entity_text, entity_type, start_position, end_position." (It will produce text that looks like a table but is not a real CSV and can't be exported.)
3. **Consistency:** "Make sure that 'Edmund Gosse', 'E. Gosse', and 'Gosse' are all counted as the same entity across all letters." (It will agree in the conversation, but run the same request in a new session and results may differ.)
4. **Reproducibility:** Close the notebook and start a new one with the same letters. Ask the same entity question. Is the output identical? (Almost certainly not — generative models are non-deterministic by default.)
5. **Visualization:** "Create a network graph of the people mentioned in these letters." (It will describe a network in text; it cannot produce a graph, a CSV of edges, or any importable format.)
