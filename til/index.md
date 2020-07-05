---
layout: default
title: TILs
---

With the huge amount of information that is being published and put on the internet these days, I get very overwhelmed. To keep track, I end up journaling my "learnings" from papers/courses/blogs etc. Helps me track my progress. From now on, I'll document them here! It'll be a list of my TILs :)) I will journal these on my end throughout the week, and will post them out on the weekends!

### 5th July 2020
##### Mostly ACL notes

Tutorial notes:
* interesting research question: interpretability analysis of multimodal documents. How do representations learn from different modalities?
* Only speech analysis: some things are directly applicable from images, because they are also continuous signals -  saliency maps, spectrograms etc.
* work on interpretability on formal languages. trade off between the interpretability of the model and it's quality, you can constraint the model and gain interpretability but might lose the learning power..
* What we want, ultimately is for interpretability to improve the model, and not constrain it..
* In some situations interaction between the system and the user is important, whereas in other cases it might not be desirable or possible.. in a radiology report you'd want it to be a interactive, but for an auto-driving car, you'd want the model to be very sure and maximize performance instead of having "doubts"
* In NLP the issue of learning can be multi-step: model, data, the human language is not supposed to learn it? from the scientific point as well as from a linguistic perspective..
* how infinitely recursive should language be??
* Question:which probing classifier to use? is it fair to compare two classifiers with different sizes?
** Idea: of using the minimum description length tells you not only the performance of the probe, but also how difficult it is to solve the task, a measure on how challenging it is to do?
* human error patterns vs model error patterns : any work? how do you differentiate - and how do you use them to make your model more faithful? before you fix the mistakes, you need to see how they arise. * look at generation track papers at ACL
* Brilliant BERT visualization demo [here](https://exbert.net/) [IMPORTANT]
* Another point for probing classifiers was to learn the "latent variable" that causes the model to perform well i.e. more in terms of the control experiments.
* what about carefully controlled test sets as used in psycho-linguistics human studies? can you transfer these evaluations to models?  
** idea is to eventually use these small sets. Look up paper on : posing fair generalization tasks, emnlp 2019. With small corpus, you get 1 or 0 answers as to whether the model does good on it or not, whereas with numbers on bigger corpus it's very difficult to gauge which quality of the model is being assessed. But again the trick is to ensure the very small targeted corpus is created properly?
* Q: What does it even mean to say that "a pretrained LM knows a task at 80%"? to me it sounds ;like the model DOES NOT know the phenomena :
** We want to go from not knowing it, to knowing it a little, saturating on the information. Similar to how it's in humans, kids might be not knowing a phenomena, and then they go on to knowing it properly. In models, the all or nothing doesn't happen, so how do you say is "80%" good enough? On going from 80 - 81% you dont know what the model learned in that 1%.... VERY VAGUE HERE.
* thoughts on probing for factual knowledge? decouple what the model can be trained on vs what the model can learn .. decouple memorization from reasoning .. memorization vs inference. The model needs to be more than a look up table, and more than just a replacement for a KB.
* What is your thought about configuring probes for fairness or privacy-preserving purposes, e.g. to show a model lacks interpretability wrt to gender or other protected attributes when it's trained to some reasonable degree for some designated prediction task?
** Very important, but how do you define biases? some exist in society and it is very difficult to get rid of them. It's definitely a good use case (look up references). Connects probing with the behavior side of inference.

Session 2 :
* disagreements in human judgements, how to handle these? inferences about meaning when there is no clear cut answer .. hard to say what behavior our model is supposed to have given these uncertainties.. challenge on how to design these sets
* do we always want to mimic human behavior? depends on the goal of the user creating the system .. eg: dialogue systems are difficult to evaluate, but for something like question answering you can still be more objective and try and achieve "super human" performance
* Q: Interpretability & subwords: how (if) do you think the fact that SOTA contextualization models use byte pairs affects their interpretability when compared to "standard" LSTMs + word-tokens
** we as humans don't use subwords and these don't necessarily adhere to the morphological information, and that makes it a little bit harder to interpret ( from a visualization perspective ). For behaviourial analysis : ends up being a part of the black box, the advantage of subwords is in the multi-lingual languages ( moving away from white space tokenization ). Investigation of how these different subwords change how the models performs ( subpiece vs word piece etc ).
* Q: Do any of you have thoughts like these? Are you tempted by models which can be better "guided"?  Any insights?
** with models now you try and build tasks into a model, which is mostly human guided < look up more about it later READ >
* Q : Which type of interpretability method (like post-hoc or model based) should be better for educational NLP areas like essay scoring, etc.
** Is the audience the engineers or the students? if it's the first, everything still remains the same, other than the document based models. If the audience is the students - still nervous using the tools - so mostly visualizations. The structural and behavior based methods are more for the machine learning engineers. Check for systematic biases while scoring students. What type of explanations to show to the students? ( from a user perspective )
* Q: Have you seen any work performing probing studies on document representation (say from BERT)?
** Not really. looked at discord representations, generation settings to say what are they sensitive to .. what sort of coherence chains to they have or not have .. You need adaptation to the model though.
* Q: How does one analyze a model architecture which transitions in terms of "what" it does [in terms of various linguistic properties] with increasing or decreasing training/finetuning sizes? [e.g it encodes property z only after a certain threshold of training examples N_min, or perhaps worse still, the behaviour is non-monotonic w.r.t encoding z]
** maybe by looking at different checkpoints, but at different points in training, diff datasets etc. Very complex to look at - can't just look at it post-hoc as an exploratory analysis.. probably better driven as hypothesis testing ( eg: Certain linguistic understanding gets better with training time etc )
* What's your thought on recent debiasing methods that work by downweighting potentially biased examples in the training data? They work well in improving the performance on some challenge datasets (e.g., HANS). But since new types of bias are still being discovered and these methods usually target a specific 'known' bias -- do you think these methods are the way to go for a better and more robust model of language?
** Similar to data augmentation, but skeptical of these kinds of methods - the concern is that these are too tight to the probing set - we need a much fuller picture of what did the downweighting change, but we need to look at a more holistic picture, what other heuristics it might be adapting.


### 4th July 2020
##### Mostly ACL notes
continuing on my TILs from "Interpretability and Analysis in Neural NLP" hosted by Yonatan Belinkov, Sebastian Gehrmann and Ellie Pavlick...


##### behavior analysis
the second way of understanding interpretability of these models is to a behavior analysis. In this method, you tend to look at  data points that are statistically less probable to be seen my the model during training, and then you try and see how your model generalizes to these points. This approach is very different from the probing or structural analysis approach.
* Some advantages: it's algorithm agnostic, practical, has an objective criteria for evaluating the representations.
* disadvantage: 1. if the model doesn't perform well on the curated dataset - do you debug the model or the data it's seen? 2. what level of generalization is considered to be fair? 3. you technically don't get much insights about WHY the model failed.

##### visualizations :
The third method for interpretability is via interfaces and visualizations. You try and understand the larger patterns by filtering noise.. this can help understand concepts in higher dimensions. It can be used for reducing exploration space ( eg; in model selection ), understand data, features, as well as important aspects of the modeling concetps ( eg: attention layer )

Can look at it in three perspectives:
* task : model selection , model decisions
* user : architect ( who sees just the model ), trained ( model + data ), end-user ( only sees the application )
* model involvement : interactive visualizations( with has the ability to change model parameters, links via interface ) , passive involvement ( eg: in tensorboard you only see the statistics, graphs etc but have no control over the actual underlying model  )

* difficulties: takes a lot of time and effort to build these interfaces especially to scale over multiple usecases
*  open research questions :
** how do these visualizations improve downstream trust?
** how do these insights improvement the model ? ( eg: visualizing the outliers )
** how to help understand causality?
** how to develop model interactive generic interfaces?



### 3rd July 2020
##### Mostly ACL notes
So I haven't posted in a while, because I was attending two conferences along with office work. I'll try and be more diligent this week, and write about my TILs regularly.  

In the coming week I'm attending ACL 2020! Seems very overwhelming given the number of tutorials, workshops and the sheer number of papers that have been accepted!  A lot of time this week has gone into trying to figure out what sessions I want to attend. Since the tutorials are recorded, I went through the tutorial on "Interpretability and Analysis in Neural NLP" hosted by Yonatan Belinkov, Sebastian Gehrmann and Ellie Pavlick.
Main takeaways:
* This tutorial focused on three ways for Interpretability : structural analysis,
* The first part of the talk focused on structural analysis via "probing classifier".

##### probing classifier

TLDR for a probing classifier:
```
Input: x, linguistic_ann(x)
F: f(x) -> rep(x)
G: g(rep(x)) -> g_output
evaluation g_output with linguistic_ann(x)
```
* In this model, you basically evaluate F, and the representations generated by model F on a dataset with has some linguistic annotations. Another model "g" is then trained using these representations to see how it performs on the same dataset. Model g is trained in a way to maximize the mutual information between the representations and the output annotations
* on looking at the performance of "f" i.e. representations from intermediate layers of "f" , we can conclude a hierarchy of tasks that each level would represent better.
* i.e. the lower layers of any NN model learn  more simple features like morphology, POS where as the upper layers can capture more complex concepts like dependencies, syntax and semantics etc. ( similar to as seen in CNNs for vision for example)
* shortcomings of this approach:
** even though we are comparing rep(x), but the performance is also based on how to choose "g", so the more complex "g" you choose, the better you are able to use the representation for the linguistic task. how does that play into comparing different "f"?
**  you need to have some standard models of "g" for comparison to say how the representations stand relative to a baseline
** the model "g" is being trained on a linguistic task which may be different from the actual task on which "f" is trained so even though "f" is performing well on the probing task, it might not perform well on the actual downstream task, how to resolve this?
** difference between "accuracy" and "selectivity" <--- (read about selectivity)  

continued ..

### 20th June 2020

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
