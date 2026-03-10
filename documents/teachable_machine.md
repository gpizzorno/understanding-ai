# Activity: Teachable Machine

**Format:** Small groups (3–4 participants)  
**Estimated time:** ~35 minutes (Part 1: ~15 min, Part 2: ~10 min, Debrief: ~10 min)  
**URL:** https://teachablemachine.withgoogle.com

## Facilitator Notes

- Before the activity: confirm all participants can access https://teachablemachine.withgoogle.com in their browsers. The tool requires a webcam or microphone for image/sound models, pose models require a webcam.
- Set up a shared "Model Share" document (*e.g.*, a Google Doc or shared slide deck) where groups will post their model information during Part 1.
- Circulate during Part 1 to help groups who are stuck choosing a concept or collecting samples. Encourage simple, clear distinctions (e.g., hat/no hat, thumbs up/thumbs down, loud noise/quiet).
- For Part 2, assign groups to test a *different* group's model, not their own.
- Keep an eye on time: Part 1 tends to run long. Give a 5-minute warning before transitioning to Part 2.
- During debrief, draw connections explicitly to the presentation concepts: training data, labels, generalization, overfitting.

## Part 1: Train a Model

**Instructions for participants:**

1. In groups of 3–4, go to https://teachablemachine.withgoogle.com and create a new project [Choose an image model?].
2. Define 2–3 categories (classes) for your model. Keep it simple and clearly distinguishable.
3. Collect training samples for each class using your webcam or microphone.
4. Train the model and test it in the preview panel.
5. Export your model: **Export Model → TensorFlow.js → Upload (cloud)** — save the link!
6. Add your model to the shared Model Share document with:
   - Group name or number
   - Data type (image / sound / pose)
   - Categories trained on
   - Brief description of what the model does
   - Link to your uploaded model
   - Do **not** upload images, share only the model link and weights.

**Facilitator note:** Encourage groups who finish early to keep collecting samples and retraining. Ask them to notice whether adding more examples in one class changes accuracy in others.

## Part 2: Test Another Group's Model

**Instructions for participants:**

1. Find another group's model in the Model Share document.
2. Read the description and predict how it will behave before testing.
3. Open the model link in your browser and test it with real-world input:
   - Does it work as described?
   - Try to fool it, find inputs it misclassifies. What does this reveal about the training data?
   - Explore the edges: what happens with ambiguous or unusual examples?

**Facilitator note:** Prompt groups to think about *why* the model fails when it does, not just *that* it fails. Failures are the most instructive part of this exercise.

## Debrief Discussion

Use the following prompts to guide a whole-group discussion. Not all need to be covered, choose based on what came up during the activity.

**About the training experience:**
- How did you decide what categories to use? What assumptions did you bake in?
- How did you collect your training data? Was it representative?
- How did you decide how many samples were enough?
- What unexpected things happened while training?

**About testing another group's model:**
- What were your expectations before testing? Were they correct?
- How did you decide what data to use to test the model?
- What problems came up? Were failures random or systematic?

**Connecting to broader concepts:**
- What are "good" training examples, good for whom, and in what context?
- What does the final model actually do, and what does it *not* do?
- What is the difference between a narrowly defined model and a generalizable one?
- How is what you just did similar to—and different from—how large language models are trained?
