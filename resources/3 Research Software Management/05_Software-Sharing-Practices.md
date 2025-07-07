---
title: "Module 5: Software Sharing Practices"
author: "Skills4EOSC T4.1"
tags:
    - Skills4EOSC
    - DataStewardship
    - Curriculum
    - Research Software Management
    - Software Development
---

# Module 5: Software Sharing Practices

!!! warning "This page is currently under construction"

    **The training curriculum is currently undergoing final revisions and quality checks.**
    **All materials will be released shortly.**
    **Until the official release, please refrain from using, distributing, or implementing any part of these resources.**


## Learning Objectives

- **Learning Objective 1 (LO1):** Advocate for the importance of applying software licences.
- **Learning Objective 2 (LO2):** Explain the relationship between copyright and software licences.
- **Learning Objective 3 (LO3):** Identify appropriate software licences to apply, taking into consideration the licences of reused pieces of code within a newly developed research software (like plugin or library).
- **Learning Objective 4 (LO4):** Identify the steps necessary to distribute research software.
- **Learning Objective 5 (LO5):** List the steps to publish research software.
- **Learning Objective 6 (LO6):** Describe practical steps to make research software citable.


## Total Module Duration

5 hours 35 minutes


## Learning Objective 1

LO1: Advocate for the importance of applying software licences.


### Learning Activities

- **Slide presentation** (30 mins): Lecture or presentation to go over what software licences are and the different permissions they grant, how they differ from copyright, and the importance of using them. A presentation from the Netherlands eScience Center training can be reused or adapted (Resource 1).
- **Applied learning activity** (30 mins): The learners should break up into groups of 3, and each access the website Choose a License (Resource 2). Each person in the group should imagine they are approached by a researcher who has requested advice on applying a software licence based on one of the three scenarios mentioned on the website: 1) I need to work in a community, 2) I want it simple and permissive, 3) I care about sharing improvements. Use the options of licences provided on the website to decide what advice you would give in each case. Share your reflections with the rest of the breakout group and note your observations together in a shared document.
- **Add-on applied learning activity** (15 mins): The learners can consider the following scenario (based on the 6<sup>th</sup> and final scenario mentioned in Resource 2): Discuss what would happen if you were approached by a researcher who does not want to use a software licence. What would you tell them about the implications of this for their research software? What advice would you give them? Discuss in your breakout groups.


### Materials to Prepare

- Presentation on software licences (Resource 1).
- Collaborative document such as HackMD or Google docs to note down observations from the activity (one document can be used for all the breakout groups).


### Instructor Notes

**All activities:**

- Broadly, this session addresses the different kinds of software licences, how they differ from copyright, and how and why to license research software created by researchers at a data steward's organisation.
- The hands-on activity is meant to give aspiring data stewards a feel for the different kinds of licences available and possible scenarios with researchers.
- Slide presentations and activity suggestions from the Netherlands eScience Center course are available to reuse and adapt, as long as they are properly cited, and attribution is given under CC BY 4.0 licence.


### Resources

**Slide presentation:**

1. *Software Licensing*. <https://esciencecenter-digital-skills.github.io/research-software-support/modules/licenses/slides/>. Accessed 25 Mar. 2025.

**Applied activities:**

2. "Choose an Open Source License." *Choose a License*, <https://choosealicense.com/>. Accessed 25 Mar. 2025.

**Further Reading:**

3. Salter, Jim. "Open Source Licenses: What, Which, and Why." *Ars Technica*, 24 Feb. 2020, <https://arstechnica.com/gadgets/2020/02/how-to-choose-an-open-source-license/>.



## Learning Objective 2

LO2: Explain the relationship between copyright and software licences.


### Learning Activities

- **Individual in-session activity** (40 mins): The learners should be given the following prompt to explore on their own: Look up the software policy of your research institution. What does it say about what software licences researchers should apply? What does it say about copyright? If there is no institutional policy, make a note of that, and try to see if there are any other guidelines (such as national laws or regulations) that are used instead. Each person should do a quick 2-minute summary about what they found.


### Materials to Prepare

- List of regulations or institutional software policies to study if there are no relevant context materials. Some suggestions (most relevant to the context of the Netherlands) are provided in the Resources.


### Instructor Notes

- This learning activity builds on materials covered under LO1 and encourages the learner to think about software licences and copyright in the context of their own institutions, which may have differing policies.
- This activity is adapted from the Netherlands eScience Center course material in Resource 3 and can be reused, provided it is properly cited and attributes in accordance with the CC BY 4.0 licence.


### Resources

**Software policies of the institutions of the learner. For instance, in the context of the Netherlands, the following policies could be studied:**

1. Bazuine, M. TU Delft Guidelines on Research Software: Licensing, Registration and Commercialisation. Zenodo, 23 Mar. 2021, <https://doi.org/10.5281/zenodo.4629635>.
2. Akhmerov, A., et al. TU Delft Research Software Policy. Zenodo, 23 Mar. 2021, <https://doi.org/10.5281/zenodo.4629662>.
3. *Software Policies*. <https://esciencecenter-digital-skills.github.io/research-software-support/modules/licenses/university_policy/>. Accessed 3 Apr. 2025.



## Learning Objective 3

LO3: Identify appropriate software licences to apply, taking into consideration the licences of reused pieces of code within a newly developed research software (like plugin or library).


### Learning Activities

- **Reflection Activity** (40 mins): The instructor can use the software licensing compatibility tool in the EU Academy Licensing Assistant (Resource 1) to guide learners through assessing the compatibility of different software licences (use information from Resource 2 to get further information). Guidance from The Turing Way (Resource 3) can also be used to consider more detailed software licence compatibility scenarios.
    - Small breakout groups explore the following scenario: Consider 6 common open source software licences mentioned in the NL eScience Center module on Software Licensing (Resource 4):
        - GPL: GNU General Public License,
        - AGPL: Affero General Public License,
        - LGPL: GNU Lesser General Public License,
        - MPL: Mozilla Public License,
        - BSD: Berkeley Software Distribution, and
        - MIT: Massachusetts Institute of Technology.
    - Identifying combinations of these licences two at a time in the EU Academy Licensing Assistant (Resource 1), select one as the inbound licence (covering the third party source code that you plan to use in your project), and one as the outbound licence (already covering your main project source code and/or planned for the distribution of your project). Are these compatible with one another? Explore at least 3 different scenarios in your group and consider how the conditions of the inbound software licence affect your ability to use the licence of your choice on the outbound software.
    - Breakout groups should discuss in plenum their key takeaways from the activity, and whether they are common across groups.


### Materials to Prepare

- In order to get the activity started and familiarise learners with the process, the instructor could prepare one or two potential examples of licence compatibility to discuss while explaining the activity, or a demo of one or two licence combinations (using the Licensing Assistant or other relevant resources).


### Instructor Notes

- This activity looks at how to reuse other software, and how different software licences are compatible with each other (or not).
- The goal is to familiarise data stewards with some potential licence compatibility issues, even if they do not encounter them frequently. The activity also provides some resources and tools that could help explore licence compatibility issues.


### Resources

**To guide the activity:**

1. *Compatibility Checker | Interoperable Europe Portal*. <https://interoperable-europe.ec.europa.eu/collection/eupl/solution/licensing-assistant/compatibility-checker>. Accessed 1 Apr. 2025.
2. *Find and Compare Software Licenses | Interoperable Europe Portal*. <https://interoperable-europe.ec.europa.eu/collection/eupl/solution/licensing-assistant/find-and-compare-software-licenses>. Accessed 1 Apr. 2025
3. *License Compatibility - The Turing Way*. <https://book.the-turing-way.org/reproducible-research/licensing/licensing-compatibility#gplv3-vs-proprietary-license>. Accessed 1 Apr. 2025.
4. *Software Licenses*. <https://esciencecenter-digital-skills.github.io/research-software-support/modules/licenses/licenses/>. Accessed 1 Apr. 2025.



## Learning Objective 4

LO4: Identify the steps necessary to distribute research software.


### Learning Activities

- **Slide presentation** (20 mins): The importance of distributing research software, types of software and how to distribute them (can be adapted from Resource 1).
- **Discussion Activity** (40 mins): The learners are divided into small breakout groups of 3&ndash;4. The instructor should assign each group a case in which they give advice about distributing a particular kind of software (adapted from the suggested activity in Resource 2). Other case studies can be proposed by the instructor.
    - Case 1: A senior researcher who leads a group asks for advice on distributing some software that a junior researcher from their group has created. They say: "One of my people has made an amazing application for calculating where you can best put solar panels, and how much energy they will produce. We think there are lots of researchers studying the energy transition and working on solutions, and they should all use our program because it's just so great. We're submitting a paper on solar panels in the province next week, but how do we make the code available?"
    - Case 2: A historian who studies historical natural disasters wants to share code associated with a paper. They have a background in economics, and have taken a quantitative approach, working with a statistician to modify existing data analysis techniques and got some really good results. The author submitted a paper some time ago and have now been asked to share the code by the journal. What should they do?
    - The groups should present their approaches in a session in plenum, to see the different approaches taken by other learners.


### Materials to Prepare

- Slide presentation on distributing research software.
- Case studies or a prepared list of recommendations for the discussion activity.


### Instructor Notes

**Presentation/Discussion:**

- Content to cover in this activity:
    - What is software distribution and what aspects of it are important for research software?
    - What kinds of software exist and how are they best distributed?
    - What should you keep in mind when people ask for help on software distribution?
- Slide presentation and activities on research software distribution from the Netherlands eScience Center course are available to reuse and adapt, as long as they are properly cited and attribution is given under CC BY 4.0 licence.


### Resources

**Slide presentation:**

1. Distributing Software. <https://esciencecenter-digital-skills.github.io/research-software-support/modules/distributing/slides-distributing/>. Accessed 27 Mar. 2025.

**Case studies to guide the activity:**

2. *How to Distribute?* <https://esciencecenter-digital-skills.github.io/research-software-support/modules/distributing/exercise-distributing/>. Accessed 3 Apr. 2025.
3. Bazeley, Mikiko. "Understanding the 'Why' of VM's, Containers, & Virtual Environments." Ml Ops by Mikiko Bazeley, 20 May 2022, <https://medium.com/kitchen-sink-data-science/software-fundamentals-for-machine-learning-series-understanding-the-why-of-vms-containers-89621cf66d23>.



## Learning Objective 5

LO5: List the steps to publish research software.


### Learning Activities

- **Slide presentation** (20 mins): Short presentation on why research software should be published, and what steps can be taken to publish it (adapted from Resource 1).
- **Discussion activity** (40 mins): This activity is adapted from an activity from the Netherlands eScience Center Course in Resource 2.
    - Learners should be divided into small groups of 3 or 4, and be asked to choose a piece of research software that they know, or pick one of the packages from this list (source: Research Software Directory, Resource 3):
        - [ESMValTool](https://research-software-directory.org/software/esmvaltool)
        - [LitStudy](https://research-software-directory.org/software/litstudy)
        - [Haddock](https://research-software-directory.org/software/haddock3)
        - [worcs](https://cjvanlissa.github.io/worcs/index.html)
        - [democracy-topic-modelling](https://research-software-directory.org/software/democracy-topic-modelling)
    - They should then consider the following questions in their breakout groups.
        - Find out what the software is about.
        - Look individually in the [Research Software Registries Awesome List](https://github.com/NLeSC/awesome-research-software-registries) (Resource 4) for a registry that is suitable for the chosen piece of software. Discuss in the group which registry to choose. After choosing a software registry discuss in the group what further steps are required to publish research software (for instance, software repository, software paper).
    - Groups should then discuss in plenum how they made their choices of registries and key takeaways from the activity


### Materials to Prepare

- Slide presentation on publishing research software (can be reused or adapted from Resource 1).
- List of software to choose from for the discussion activity (can be chosen from Resource 4).


### Instructor Notes

**Presentation/Discussion:**

- Content covered in these learning activities:
    - What does publishing software mean?
    - Why should researchers publish their software?
    - Where should researchers publish their software?
    - What are the basic steps of publishing software?
    - How do I guide researchers through the steps of publishing software?
- A slide presentation on publishing research software from the Netherlands eScience Center course is available to reuse and adapt, as long as they are properly cited and attribution is given under CC BY 4.0 licence.
- The goal of the discussion activity is to imagine how learners would give advice to researchers about publishing software and familiarise themselves with some available software registries as a starting point.
- If the learners belong to a particular discipline and other registries are more suitable, those can be included in the discussion activity in addition to or in place of the existing examples.


### Resources

**Slide presentation:**

1. *Publishing Software*. <https://esciencecenter-digital-skills.github.io/research-software-support/modules/publication/slides-publication/>. Accessed 27 Mar. 2025.

**To facilitate the suggested activity:**

2. *Find Your Registry. <https://esciencecenter-digital-skills.github.io/research-software-support/modules/publication/ex_registries/>. Accessed 27 Mar. 2025.*
3. *Research Software Directory*. <https://research-software-directory.org/>. Accessed 24 Mar. 2025.
4. *"GitHub - NLeSC/Awesome-Research-Software-Registries: Awesome List of Research Software Registries."*, <https://github.com/NLeSC/awesome-research-software-registries>. Accessed 27 Mar. 2025.



## Learning Objective 6

LO6: Describe practical steps to make research software citable.


### Learning Activities

- **Slide presentation** (30 mins): Slide presentation on the principles of research software citation, and how and why to cite research software and make your own research software citable. Slides in Resource 1 can be reused or adapted with proper citation.
- **Discussion/Think-Pair-Share Activity** (30 mins): (Adapted from the activity in Resource 2) Learners should be given the following prompt to discuss with one another in pairs:
    - Suppose that a researcher approaches you to ask how to cite the software they have used for a research paper they have been writing and they provide you with the list below, which software would you recommend the researchers to cite and which not? Why?
        - Ubuntu - Operating System
        - Microsoft word - text editor (used to write the paper, take notes)
        - Git - Version control software
        - Numpy - Python math library (used in nearly all python-based research software)
        - ESMValTool - Diagnostic tool/library for Earth System Models (Used in many climate research projects)
        - ClimAnal - Their own domain specific python library (defines various analytical functions that they used in their climate research)
        - The original code on which they based their library ClimAnal
        - Their own local python script, used to execute the analysis


### Materials to Prepare

- Slide presentation on research software citation.


### Instructor Notes

**Presentation/Activity:**

- A slide presentation on research software citation from the Netherlands eScience Center course is available to reuse and adapt, as long as it is properly cited and attribution is given under CC BY 4.0 licence.
- Points to cover in the slide presentation:
    - Why is it important to cite research software?
    - What are the principles of software citation?
    - How do I communicate the importance of citing software to researchers?
    - How do I guide researchers through the steps of making their software citable?
- More information on Think-Pair-Share activities is available in Resource 6.
- One possible persistent identifier for software is the "SoftWare Heritage persistent IDentifier" (SWHID). More information can be found in Resource 8.


### Resources

**Slide presentation:**

1. *Software Citation*. <https://esciencecenter-digital-skills.github.io/research-software-support/modules/citation/slides-citation/>. Accessed 31 Mar. 2025.

**Guiding the discussion activity:**

2. *What to Cite?* <https://esciencecenter-digital-skills.github.io/research-software-support/modules/citation/ex_what-to-cite/>. Accessed 31 Mar. 2025.
3. *Should I Cite?* <https://mr-c.github.io/shouldacite/>. Accessed 31 Mar. 2025.
4. Chue Hong, Neil P., et al. *Software Citation Checklist for Authors*. Oct. 2019. *DOI.org (Datacite)*, <https://doi.org/10.5281/ZENODO.3479199>.
5. Smith, Arfon M., et al. "Software Citation Principles." *PeerJ Computer Science*, vol. 2, Sept. 2016, p. e86. *peerj.com*, <https://doi.org/10.7717/peerj-cs.86>.
6. *Think, Pair, Share | Kent State University*. <https://www.kent.edu/ctl/think-pair-share>. Accessed 10 Apr. 2025.

**Further reading:**

7. Di Cosmo, Roberto, et al. *Referencing Source Code Artifacts: A Separate Concern in Software Citation*. 2020. *DOI.org (Datacite)*, <https://doi.org/10.48550/ARXIV.2001.08647>.
8. *SoftWare Heritage persistent IDentifiers (SWHIDs)*. <https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html>. Accessed 07 Jul. 2025.
