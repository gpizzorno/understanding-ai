# Unit 1 Activities: Facilitator Notes

These notes accompany the activity pages in [Unit 1](https://gpizzorno.github.io/understanding-ai/unit_1/). The pages contain the instructions, hints, and key takeaways. This file contains what you need to run the activities with a group: timings, room setup, pacing, check-ins, and a live demo script.

---

## Teachable Machine

**Activity page:** [Activity: Teachable Machine](https://gpizzorno.github.io/understanding-ai/unit_1/teachable_machine.html)  
**Format:** small groups of 3–4  
**Estimated time:** about 40 minutes (Part 1: 15 min, Part 2: 10 min, the shape-or-colour experiment: 5 min, debrief: 10 min)

### Before the Activity

- Check that participants can open [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com). Image and pose models need a webcam, sound models need a microphone. One working laptop per group is enough.
- Set up a shared "Model Share" document (for example, a Google Doc that anyone with the link can edit), where groups post their models at the end of Part 1. Put the link where everyone can see it, and start the document with a template for groups to copy:

  ```text
  Group: <group name or number>
  Data type: <image | sound | pose>
  Classes: <class 1 | class 2 | ...>
  Description: <what the model does, in one line>
  Link: <shareable link from Export Model>
  ```

  The fields match what the page asks groups to share. In Part 2, each group picks another group's entry, reads the description, and predicts how the model will behave before opening the link.
- Have a backup for groups whose export fails, or who run out of time: the [model from the videos](https://teachablemachine.withgoogle.com/models/2M-kB6nDp/), trained on a green paper square and an orange paper circle. A few paper shapes in other colours (a green circle, an orange square) make Part 2 and the experiment work with it.

### During the Activity

- Before groups start, play the four short videos on the activity page, or point groups to them. They show every step, and save a lot of questions about where buttons are.
- Circulate during Part 1 to help groups that are stuck choosing classes or collecting samples. Encourage simple, clear distinctions: two shapes cut from coloured paper, a mug and a book, thumbs up and thumbs down.
- Groups that finish early can add more samples to one class and retrain. Ask them to notice whether that changes the model's behaviour for the *other* classes.
- Give a 5-minute warning before Part 2. Part 1 tends to run long, and exporting takes a minute or two (**Export Model** → **Tensorflow.js** → **Upload (shareable link)** → **Upload my model**).
- In Part 2, make sure groups test a *different* group's model, not their own, and that they predict before they test.
- Push groups to ask *why* a model fails, not just *that* it fails. The failures are the most instructive part.

### The Shape-or-Colour Experiment

Run this as a whole group just before the debrief: it's the clearest way to make the activity's point. Show the model from the videos (or describe it): every training example differed in both shape and colour. Ask the room to predict what it will say about a green circle and an orange square, then reveal the answer on the activity page (it learned shape: the green circle came out as Orange Circle at 96%). The point isn't which it learned, but that nothing in the training data could have told you in advance.

### Debrief

- Use the [discussion questions](discussion_questions.md#activity-teachable-machine), choosing based on what came up.
- Ask groups what their model *actually* learned, and how they found out. Shortcuts (the background, the lighting, a face) are the best material.
- Make sure someone mentions the confident wrong answers: a classifier always picks one of its classes, even for something that belongs to none of them.
- Bridge to [Model Training](https://gpizzorno.github.io/understanding-ai/unit_1/model_training.html): training data, the train/test split, generalization, and bias.

---

## Hack Merlin

**Activity page:** [Activity: Hack Merlin](https://gpizzorno.github.io/understanding-ai/unit_1/hack_merlin.html)  
**Format:** individual play, then a whole-group demo  
**Estimated time:** about 35 minutes (framing: 5 min, play: 15 min, check-in and demo: 5 min, debrief: 10 min)

**REMEMBER GANDALF! Test the game shortly before the session.** Hack Merlin is a live third-party site and may change. The hints on the activity page were tested when it was written. If a level now behaves differently, adjust the hints, or tell participants to focus on the *kind* of strategy rather than the exact prompt.

### Framing

- Explain the set-up: a chatbot playing a wizard has been told a password and told not to reveal it. Each level adds a defence, and the game says what it was once you pass the level.
- It's a designed demonstration of a real problem: prompt injection and brittle guardrails.
- Ask participants to keep track of which strategies stop working, and at which level.

### During the Activity

- Participants play individually at [hackmerlin.io](https://hackmerlin.io). It runs in the browser, without a login.
- Encourage momentum: most people get through levels 1 and 2 quickly. Ask them to try the early levels before perfecting one strategy, and to open a hint after a few minutes stuck.
- Circulate and listen for strategies: direct requests, poems, role-play, acrostics, euphemisms, reframing.
- When someone is stuck, nudge towards the *type* of strategy rather than the answer.
- **Level 5:** the output filter now catches reversed or re-capitalized versions of the word, so encourage indirect structure (an acrostic) over string tricks.
- **Levels 6 and 7:** stretch goals, and genuine experiments, since the game describes each defence only after it's beaten. Encourage participants to vary the *form* of the request.
- Move to the demo at around the 15-minute mark, however far people have got.

### Mid-Activity Check-In (After 8–10 Minutes)

Ask the group:

- How far has everyone got?
- What worked at the early levels that stopped working later?
- Did you change *what* you asked for, or mainly *how* you asked for it?

Use the moment to make a point: participants aren't *convincing* Merlin in any human sense. They're finding wordings that slip past imperfect constraints.

### Live Demo

Take over the screen and walk through a few levels, narrating the reasoning rather than racing to the answer. The prompts are in the hints on the [page](https://gpizzorno.github.io/understanding-ai/unit_1/hack_merlin.html).

- **Level 1:** ask directly, to show how the game works.
- **Level 2:** an instruction not to reveal the password is only text. A request for a poem activates a different, equally familiar pattern, and can win.
- **Level 3:** an output filter blocks exact disclosure, but not an acrostic whose line initials spell the word.
- **Level 4:** an input filter blocks words like "password" and "secret". Switch to a euphemism ("the answer you are guarding"), still with an acrostic. Ask: what is the filter matching on, and what does it miss?
- **Level 5:** the output filter now catches simple transformations. Ask which transformations still count as disclosure, and which become encoded structure instead.
- **Level 6 or beyond:** try varying the form of the request, and ask what each new defence might be adding, and what it can't anticipate. There's no tested prompt for these levels.

Narrate the broader theme: every defence is another layer of language or pattern matching. None of them understands what it's protecting.

### Debrief

Use the [discussion questions](discussion_questions.md#activity-hack-merlin). Make sure the discussion reaches these points (they're the "Defences and Their Gaps" section of the activity page):

- Guardrails built from language are brittle, because the model weighs them against everything else in its input.
- More layers make an attack harder, not impossible: the defender has to anticipate every route, while the attacker needs one.
- Prompt injection matters beyond games. Text hidden in a web page, a PDF, or an email can compete with a tool's instructions in exactly the same way (indirect prompt injection).
- A refusal isn't proof of robust safety. It may reflect only the current wording.
