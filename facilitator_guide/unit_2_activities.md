# Unit 2 Activities: Facilitator Notes

These notes accompany the activity pages in [Unit 2](https://gpizzorno.github.io/understanding-ai/unit_2/). The pages contain the instructions, expected results (in collapsed callouts), and key takeaways. This file contains what you need to run the activities with a group.

---

## Gemini Notebook

**Activity page:** [Activity: Gemini Notebook](https://gpizzorno.github.io/understanding-ai/unit_2/gemini_notebook.html)  
**Format:** individually or in pairs, with whole-group discussion between the parts  
**Estimated time:** 50–60 minutes (framing: 5 min, Part 1: 10 min, discussion: 5 min, Part 2: 10 min, Part 3: 15 min, bridge discussion: 10 min)  
**Materials:** the 20 letters in [`data/sample_letters/`](../data/sample_letters/) and, for the scale test in Part 3, [`data/stevenson_letters_combined.md`](../data/stevenson_letters_combined.md)

### Before the Session

- Participants need a Google account. Gemini Notebook requires sign-in.
- Run the activity yourself shortly before the session, with the prompts on the activity page. The tool changes often: check the source limits, where files appear in the **Studio** panel, and how to download them. Note what *your* run produced (row counts, the Colvin count, what the network looks like), since participants' results will differ from the activity page's.
- If uploads might be slow, prepare a notebook with the 20 letters and share it, so participants can make their own copy.
- Some answers take two or three minutes to generate. Plan for it: the videos on the activity page show what the waits look like, and participants can read ahead or compare notes while they wait.

### Framing

Deliver these points before participants begin (the activity page's introduction covers the same ground):

- The task is a real research task: finding the people, places, and organizations in a set of letters (named-entity recognition), a common first step for indexing, mapping, or network analysis.
- Gemini Notebook is a genuinely capable tool, and participants will find it does most of what they ask. The point isn't to catch it out. It's to find out what its output *is*: could you check it, and could you get the same result again?
- Three parts: explore (Part 1), ask for structured data (Part 2), and then ask the questions a reviewer would ask about that data (Part 3).

### During the Activity

- **Part 1** is genuine exploration: let participants use the sample prompts or their own. Make sure everyone asks the Colvin count question, and looks in the **Thoughts** panel for `Executed code`.
- **Pause after Part 1 for a short whole-group discussion.** Draw out what the tool does well before moving to its limits, which keeps the framing balanced. The `S. C.` example (initials resolved to Sidney Colvin from context) is the one to highlight: it's the entity resolution problem, and it returns in Unit 3.
- **Part 2:** the CSV export and the network graph. Participants who are following the letter exercise do step 3 here: filter the spreadsheet to the letter to Colvin, and compare its rows with their step-2 table. Ask them to **save the CSV**: Part 3 needs it.
- **Part 3:** ask participants to try each question and note what happens *before* opening the expected results. If time is short, have different pairs take different questions, and report back. The scale test (item 5) takes longest, so skip it, or demonstrate it, if needed.
- Resist the urge to help participants work around the limits. The point is to experience and name them.

### Typical Findings

The activity page's expected results come from the authors' test runs. Things to be ready for:

- The second run of the CSV prompt gives a different file: in our tests, 327 and 325 rows, of which only 288 matched, and a third run, a week later, gave 320. Accuracy was almost the same, but the *data* wasn't.
- The code behind `Executed code` isn't shown and can't be downloaded.
- The "steps" the tool gives for its network graph are a reconstruction. In our test, the script it offered drew 14 people in one colour, while its own image had 63 people in three colour-coded groups. The two images are side by side on the activity page.
- No model name or version is shown anywhere.
- A notebook holds 50 sources on the free plan (100 on paid plans), so the 462 letters don't fit as separate files. The combined file works around it, but raises the question of whether the whole corpus was really covered.

Participants' own results will differ in the details. That's the point, and worth saying out loud.

### Bridge Discussion

Close with the "Implications" section of the activity page and the [discussion questions](discussion_questions.md#activity-gemini-notebook). The four things research data needs on top of accuracy (reproducibility, transparency, a fixed version, and verifiability) are the thread that runs into [Assessing Reliability](https://gpizzorno.github.io/understanding-ai/unit_2/assessing_reliability.html) and all of Unit 3. Frame them as properties of conversational tools in general, not flaws in this product: Unit 3 builds a pipeline that gives up some accuracy in exchange for all four, and evaluates it against these same exports.

---

## AI-Assisted Work

**Activity page:** [Activity: AI-Assisted Work](https://gpizzorno.github.io/understanding-ai/unit_2/ai_assisted_work.html)  
**Format:** pairs or small groups, then whole-group discussion  
**Estimated time:** 20–30 minutes (framing: 3 min, scenarios: 10–15 min, debrief: 10 min), plus 5–10 minutes for the optional writing exercise  
**Materials:** the [printable scenarios](unit_2_scenarios_handout.md), or the scenarios projected

### Framing

- This is a discussion, not a test. Norms differ across disciplines, institutions, publishers, and classrooms, and they're still changing. There's no answer key.
- Introduce the four lenses from the activity page, which structure the discussion: **source or tool?**, **light assistance or substantive contribution?**, **private or public?**, and **what does the relevant policy say?**

### During the Activity

- Hand out the scenarios (or project them). If participants use the activity page instead, ask them not to open **Things to Consider** until their group has discussed the scenario.
- For each scenario, groups decide: is it acceptable, and under what conditions? Is the AI a tool, a source, or both? What should be checked, and what, if anything, said about the AI's role? What would change their answer?
- With six scenarios and limited time, assign two or three to each group, making sure every scenario is covered by someone.
- Encourage disagreement. The point is explicit reasoning, not unanimity: when a group disagrees, ask which lens explains it.

### Debrief

- Walk through the scenarios using the "Looking Across the Scenarios" questions on the activity page. The **Things to Consider** notes under each scenario are your reference.
- Don't collapse the discussion into a single rigid answer. Emphasize trade-offs, and the reasons for stronger or weaker transparency requirements.
- Scenarios 4 and 6 connect directly to the morning: an unchecked bibliography is a hallucination risk passed on to readers, and an AI-generated dataset raises every question from the Gemini Notebook activity.
- Scenario 3 is the one most likely to raise questions of *authorship* rather than citation, and it's worth discussing the difference.
- Let the discussion lead into [Acknowledging AI Use](https://gpizzorno.github.io/understanding-ai/unit_2/acknowledging_ai_use.html): cite sources, not the model; acknowledge material tool use, in proportion; say what you checked; and follow the relevant policy.
- If time allows, run the writing exercise: each participant writes a two- or three-sentence disclosure statement for one scenario, and the group discusses a few.

