---
layout: default
title: TIL/August 2020

--

## August 17th 2020
* tbox vs abox
* how can tbox concepts be used to supplement NLP tasks more efficiently
* wikidata: you have crowd annotated samples with a Description. Entity, Aliases, Description
* knowledge: is specified by all the meta information associated with the entity
* KG Aliases: expand the entity with the aliases to make it more semantically rich.
Subject -> from DBPedia
Predicate -> from Oxford dictionary

* POS Tagging
* Tokenization nd Compounding ( always start with the longest word in the order of tokens )
* longest subsequence of the mention should match an entity in the DB
* three step process: CHOLAN:
* generating candidate: DCA Candidate -> pre calculated probability map , re-use the FALCON KG ( which as KG aliases), and added descriptions
* entity recognition -> plane BERT
* input: mention, sentence, candidate_context
* 




## August 12th 2020

* Logits - I think this is something very basic that I should have known, but today I learnt and properly read what a logit is.
* f_beta generic formula, just realized how stupid I am!!!!! Need to retake aa statistis course for sure.


---
## August 5th 2020
Attended a session on "Information-Theoretic Probing with Minimum Description Length" session hosted by NLP Friends. This was hosted by "Lena Voita" from Amsterdam and Edinburgh
* How to understand id a model captures a linguistic property?
* Probing Classifiers, sanity checks, information Theoretic point of view
* Sanity Checks: Accuracies  between pretrained vs random initialized models - Kelly Zhang and Sam Bowman - BlackBoxNLP2018
* Random labels : each type is assifned a random label - these labels are independent of contexts,
* differences in performance fails to capture differences in representations
* problems: random models as good as trained, models incode random labels not much worse than
* information Theoretic POV : what can be put between representations and labels to mesure the goodness?

* how can a probing classsifier be a compression algorithm?
* change the goal of predicting the classifier aim from predicting labels TO transmimtting the data / compressing data - it would become an MDL probe, and then the metric becomes codelength
* why is accuracy better than codelength - theoretical
* how is codelength = final quality + amount of effort
* Data part -> there is a probabilistic model
* shannon huffman code ( read  <- cross entropy loss of the data evaluated with the )
* Question: "What is regularity?"
* Strength of the regularity? looks the clustering of similar points together in space.

## 4th August 2020
* GPT-3 playground -- search end point, the similarity seems like
the document length for the documents is about 1000 words / 2000 documents, same for all applications
* text classification -- you can do it in the playground as a prompt - text classification / sentiment analysis
* you can fine tune models
* the initial prompt you send it will help determine the behavior of the bot - check Chat prompt
* "Parse unstructured data" :
* notion.so/OpenAI-API-Community-Examples
* GPT3 is a bunch of humans together, so youu nudge it in the dieection for the kind of human you want it to be
* explanation: maybe prompt it? "Why do you believe this?"
* Another way that it can be done - you can teach the model to say "i don't know" - in question answers
* is there some way to do a continuous learning pattern? reinforcement learning is possible
* temperature setting -> Q&A is very -> stochasticity of the output
* more useful if you want storetelling
* financial document analysis
* typically have fairly long pieces of formal english texts, - pick out those things relevant for analysis ; key value extracttions; simplification ; text correction -> form coherent sentences with ;
* multi-task : helps to have it one task

## 3d August 2020
https://www.youtube.com/watch?v=WVPE62Gk3EM&feature=youtu.be



## 1st August 2020

Sometimes I like to read blogs which are more focused towards the philosophy aspect of NLP - more like where is this community headed and what needs to be done in order to make things work and see if I agree/disagree with these things - also I think it makes me a better researcher in terms of getting to know a wider range of opinions, instead of just sticking with the knowledge. I personally believe that it is very important to know where this knowledge is headed or where it'll be progressing towards as well.

Today I read the blog "NLP beyond English"[this](https://ruder.io/nlp-beyond-english/) blog by Sebastian Ruder, and I am listing down my main takeaways from his blog.

* I personally think that the problem he expressed, which is that of, deep learning models only heading in the direction of English, or rather NN only heading in the direction of English, is very very relevant.

* Quoting directly from his blog :

```
A continuing lack of technological inclusion will not only exacerbate the language divide but it may also drive speakers of unsupported languages and dialects to high-resource languages with better technological support, further endangering such language varieties. To ensure that non-English language speakers are not left behind and at the same time to offset the existing imbalance, to lower language and literacy barriers, we need to apply our models to non-English languages.
```

* I think the above point is something i have thought of many times myself. Being from India, my parents speak in this dialect which is a form of one of the regional languages called *Punjabi*, the dialect in itself is called *Bhavalpuri*. I haven't expressed this concern to many people - but to me, I feel the language will eventually die off after my parents. None of my cousins or siblings ever learnt the language because of how the society was/is progressing. There is a so called "standardization" that came with the time - for India it was because of colonialism, and for the rest of the world, It is happening now, with other regions  being effected is cause of technology.

* From a very machine learning perspective, the NLP community has been working towards resources and methods that work well for English or high resource languages in general. A lot of the practices for these languages DO NOT work well or generalize to other languages. Some examples in the blog include - morphology  of language, reduplication which performs poorly  on languages with reduplication, languages with larger vocabularies.

* Quote from the blog which I found very true :

```
In the process, as a community we have overfit to the characteristics and conditions of English-language data. In particular, by focusing on high-resource languages, we have prioritised methods that work well only when large amounts of labelled and unlabelled data are available.
```

* From a common sense perspective, concepts of common sense are different for different cultures.

* Quoting from the blog :

```
As an NLP researcher or practitioner, we have to ask ourselves whether we want our NLP system to exclusively share the values of a specific country or language community.
```

* All in all, from a research standpoint I think the blog is very very very inspiring. Like, I myself would love to work on some low-resource languages from India, but I'm not sure how well that would translate to an industry application. It always for quite some time will go hand in hand with academic research. OR maybe - it has applications like regional language news, translation, or just the historical linguistic perspective of saving certain linguistics variety. It might be a little sad to see the world which has SO much variety right now converge to a point of 10 popular languages for which we were able to make chat bots! ( can't even )
