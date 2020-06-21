---
layout: default
title: TILs
---

With the huge amount of information that is being published and put on the internet these days, I get very overwhelmed. To keep track, I end up journaling my "learnings" from papers/courses/blogs etc. Helps me track my progress. From now on, I'll document them here! It'll be a list of my TILs :)) I will journal these on my end throughout the week, and will post them out on the weekends!

> 20th June 2020

Read the paper ["Representation Learning for Information Extraction from Form-like Documents"]().

Problem Statement : Extracting structured information from "form" like documents i.e. given a set of fields for a particular domain, extract fields from unseen documents.

Key takeaways:

* the **type** of the target field is used to generate extraction candidates - eg: all date fields will have a date specific extractor, similarity for currency, addresses, email IDs etc.
* learning a **dense representation** for each of these candidates based on it's neighboring words in the document
* any field in a form will have some **structural / visual association** to the fields near by. eg: placement of the field of "due date" is x units away from the "number" field. As the paper says " an effective solution needs to combine the spatial information along with textual information "
* the pipeline has two steps : a. candidate generation - which is based on the type of field being extracted. b. scoring of the candidate w.r.t to the field
* one important point they did in their training was to **NOT** include the candidate text - but only the candidate position - this was done to avoid overfitting. Eg: if the model sees dates ranging from 2017 - 2020, it might not be able to generalize to dates in the future- or outside the range. So it's very important to not include the candidate text here..
* the other interesting part is the neural scoring model. Like you can see the architecture in the paper, it's been design to learn separate embeddings for the the field to which it belongs and a candidate embedding ( composed of candidate position, neighboring words + relative position ) and then combine these to get a score.
* the paper goes into more details about how they chose the spatial information of the candidate neighbors such that the neighborhood encoding is invariant of the order in which they are included..
* for the scoring they draw inspiration from work in metric learning (note to self: read more about this ).
* they use a "rectified adam" optimizer ( note to self: read about this )
* it's nice to see they talked about the precision/recall of their candidate generators, cause errors in the candidate generators will translate to errors in the entire pipeline


I'd like to see how this work can help in the following scenarios:
* when the documents are not templated
* when the documents are not forms, but still the information to be extracted is a. structured b. follows a type
* do we think a bag of words model can work decently well in the above case where the context is probably fixed but just the value to be extracted changes?
* they mentioned OCR errors, so trying to see how to get the model to learn better over OCR errors

Some questions I had :
* They mention that they downsample the negative samples to keep it to at most 40 negatives, but don't do so in the test and validation set - what was their thought process to do so? does this not change the distribution of the negative samples that the model sees during training?
