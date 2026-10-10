# Discussion Questions

Questions for group discussion, one set per page, in the order of the website. These questions are for facilitators who want to open up a discussion after a presentation or activity, or check what participants took away from it. Choose a few based on what came up, rather than working through them all.

## Unit 1

### [Basic Concepts](https://gpizzorno.github.io/understanding-ai/unit_1/basic_concepts.html)

- Before reading this, how would you have defined "AI"? What would you change about that definition now?
- Think of an AI tool you already use. Where does it sit in the hierarchy of terms: is it an LLM, another kind of machine learning model, or something else?
- If a model only learns patterns from its training data, what kinds of material from your own field might be poorly represented in that data?

### [Activity: Teachable Machine](https://gpizzorno.github.io/understanding-ai/unit_1/teachable_machine.html)

**About training:**

- How did you decide what classes to use? What assumptions did you build in?
- How did you collect your training data? Was it representative of what you'd test the model on?
- How did you decide how many samples were enough?

**About testing:**

- What did you expect before testing? Were you right?
- What did your model actually learn: the thing you meant, or something else that happened to separate your examples? How did you find out?
- What happened when you showed it something that belonged to none of your classes?

**Connecting to broader concepts:**

- In the shape-or-colour experiment, both explanations fit every training example. How would you design training data to rule one out?
- What are "good" training examples: good for whom, and in what context?
- How is what you just did similar to, and different from, how large language models are trained?

### [Model Training](https://gpizzorno.github.io/understanding-ai/unit_1/model_training.html)

- In your Teachable Machine model, where did bias enter? What shaped your choice of classes and examples?
- If you were building a model to classify historical documents, what training data would you need, and who would need to provide it?
- What does it mean for a model to "perform well"? Well for whom, and by what measure?
- For a research project of your own, would you care more about precision or recall? Why?
- How does the black box problem affect how you would use or report a model's outputs in your research?

### [Language Models](https://gpizzorno.github.io/understanding-ai/unit_1/language_models.html)

- What in your own sources (names, spellings, languages, scripts, transcription conventions) would a tokenizer built mostly from modern English handle badly?
- Embeddings place words close together when they appear in similar contexts. What assumptions from the training text might that build in, for the words that matter in your field?
- If an LLM picks each token with some randomness, what does that mean for using it in research that has to be repeatable?
- In the next-token example, the model expected "semester" in a sentence from the 1880s. Where else might a model's sense of what's "likely" be anachronistic for your material?

### [Activity: Hack Merlin](https://gpizzorno.github.io/understanding-ai/unit_1/hack_merlin.html)

- What surprised you most about what Merlin would and wouldn't do?
- Did you find yourself changing *what* you asked for, or mainly *how* you asked for it?
- At what point did the challenge stop being "ask for the password" and become "design a prompt that slips past a filter"?
- What does this suggest about the strengths and limits of system prompts, output filters, and input filters?
- If a research tool or institutional chatbot says it "cannot" do something, how much confidence should you place in that refusal?
- What would you worry about if you were building an LLM-based tool for archives, libraries, or classrooms, or using one on documents you hadn't read?

### [LLM Behaviour](https://gpizzorno.github.io/understanding-ai/unit_1/llm_behaviour.html)

- Which of these behaviours seems most relevant to the kind of research you do?
- Think of a time an AI tool gave you a confident answer. How could you have checked it?
- Where in your own field might a model's training data run thin, as it does for Stevenson's lesser-known correspondents?
- If a chat assistant explains how it reached an answer, what can you conclude from the explanation?
- Why might a model's refusal to answer be as untrustworthy as a confident answer?

## Unit 2

### [Prompt Processing](https://gpizzorno.github.io/understanding-ai/unit_2/prompts.html)

- When you've used a chat assistant, what made it feel intelligent? What made it feel unreliable?
- In step 1 of the letter exercise, what did the model add that wasn't in the letter? Did it tell you?
- What research tasks become harder if the model can only work with a limited slice of material at a time, or only sees the passages a search picked out?
- Which of your own research tasks are exploratory enough for an LLM to help usefully, and which demand a more reproducible method?

### [Prompting Strategies](https://gpizzorno.github.io/understanding-ai/unit_2/prompting_strategies.html)

- Think of a recent frustrating exchange with an LLM. Was the problem mainly the model, or was the task under-specified?
- Which of the four parts of a prompt (source, task, output, and standard) do you usually leave out?
- Which follow-up question would most improve a typical chatbot answer in your own work?
- In step 2 of the letter exercise, which decisions did the type column force that a summary would have glossed over?

### [Activity: Gemini Notebook](https://gpizzorno.github.io/understanding-ai/unit_2/gemini_notebook.html)

- The tool was more accurate than the specialized model in Unit 3, at least on people and organizations. Why isn't that enough for research data?
- Which of the questions in Part 3 (repeating it, the code, the steps, the version, the scale) would matter most for a research project of your own?
- If you wanted to count every mention of every person across all 462 letters, what would you need that Gemini Notebook can't provide?
- Which [failure modes](https://gpizzorno.github.io/understanding-ai/reference/failure_modes.html) did you see in action?
- What would you still use Gemini Notebook for, knowing what you know now?

### [Assessing Reliability](https://gpizzorno.github.io/understanding-ai/unit_2/assessing_reliability.html)

- Which failure mode concerns you most for your own research area? Why?
- Which tasks in your own work can tolerate approximation, and which can't?
- What kinds of mistakes could still happen even if the model is quoting the source text?
- In step 4 of the letter exercise, what did your check find? What would you have decided about the post-office?
- Pick one task from your own work. What level of verification would it require?

### [Documenting Your Work](https://gpizzorno.github.io/understanding-ai/unit_2/documenting_ai_use.html)

- Think of the last time you used an AI tool for research. Could you reconstruct now exactly what you asked, what you got, and what you checked?
- What would proportionate documentation look like for the way you use AI tools at the moment?
- When would you ask a tool for the script rather than the result? What would you do with a script you couldn't read yourself?

### [Activity: AI-Assisted Work](https://gpizzorno.github.io/understanding-ai/unit_2/ai_assisted_work.html)

The "Looking Across the Scenarios" questions on the learner page work well for the whole-group debrief. In addition:

- Which of the four lenses explained most of the disagreements in your group?
- Which scenario is closest to something you've done, or seen a colleague do? What would you do differently now?
- Where does your own institution, journal, or funder stand on these questions? Do you know?

### [Acknowledging AI Use](https://gpizzorno.github.io/understanding-ai/unit_2/acknowledging_ai_use.html)

- When would you cite an AI tool's output as a source, rather than acknowledging the tool?
- Read your disclosure statement from step 6 of the letter exercise. Would a reader know whether the table could be trusted?
- What standard of transparency would you be comfortable defending, where no policy exists?

## Unit 3

### [Advantages of Programmatic Approaches](https://gpizzorno.github.io/understanding-ai/unit_3/programming_advantages.html)

- On these letters, the NER model was less accurate than Gemini Notebook on people and organizations. When would you still choose it, and why?
- Is there a task in your own research that needs code? Which of the signs on the page does it show: scale, structured output, rerunning, knowing what was done to every document, or privacy?
- What would you want to do with structured data about your sources that you can't do now?

### [Coding with LLMs](https://gpizzorno.github.io/understanding-ai/unit_3/coding_with_llms.html)

- Have you ever used code, or a spreadsheet formula, that you didn't fully understand? How did you decide whether to trust the result?
- The letters-per-year chart looked right, but silently dropped a letter. How would you have noticed?
- Which of the five habits would be hardest for you to keep up, and why?
- If an LLM wrote code that produced a result you published, what would you need to be able to say about that code?

### [The NLP Pipeline](https://gpizzorno.github.io/understanding-ai/unit_3/nlp_pipeline.html)

- What kinds of names in your own sources would a model trained on modern news text struggle with?
- When would you choose a narrow, specialized model over a general-purpose LLM, and when the other way round?
- What would you look for in a model card before trusting the model's output in your research?

### [Case Study: Named Entities in Stevenson's Letters](https://gpizzorno.github.io/understanding-ai/unit_3/ner_case_study.html)

- What patterns emerged that would be hard to see by reading the letters one by one?
- What questions do the visualizations raise that you'd want to answer by going back to the letters?
- Where did the pipeline need human judgement? Could any of those decisions be automated safely?
- If nobody had checked the geocoding, would you have trusted the map?

### [Activity: Ground-Truth Annotation](https://gpizzorno.github.io/understanding-ai/unit_3/annotation.html)

- How long did it take to annotate one letter? What does that imply for annotating all 462?
- Which cases were you unsure about? What made them hard?
- How consistent do you think your annotations would be if you did the same letters again in two weeks?
- If your annotations are the ground truth, what happens to the evaluation when *you* made a mistake?

### [Evaluating and Comparing Models](https://gpizzorno.github.io/understanding-ai/unit_3/evaluating_models.html)

- Was your prediction about the second model right? What does that tell you about choosing a model?
- How did the model's score change when you switched the reference annotator? What does that mean for reporting a single number?
- What F1 would you consider acceptable to report in a published study? What would you need to document alongside it?
- You can't open the model to see why it missed `COLVIN` in a salutation. What can you do instead?
- Gemini Notebook scored highest but couldn't be reproduced. If you had to choose one approach for a project, which would it be?

### [Next Steps](https://gpizzorno.github.io/understanding-ai/unit_3/next_steps.html)

- What is one task in your own research that you could now approach differently?
- Which step of the pipeline would be hardest to get right for your own sources?
- What question are you leaving with that you didn't have when you started?

## Reference

### [Failure Modes](https://gpizzorno.github.io/understanding-ai/reference/failure_modes.html)

- Which failure mode have you met most often in your own use of AI tools? Did you notice it at the time?
- Which are hardest to spot in humanities work, and why?
- For one failure mode, what would a check built into your workflow look like?
