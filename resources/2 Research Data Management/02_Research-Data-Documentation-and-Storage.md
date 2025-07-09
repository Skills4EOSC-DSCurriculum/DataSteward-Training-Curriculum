---
title: "Module 2: Research Data, Documentation, and Storage"
author: "Skills4EOSC T4.1"
tags:
    - Skills4EOSC
    - DataStewardship
    - Curriculum
    - Research Data Management
    - RDM
    - Research Data
    - Documentation
    - Storage
---

# Module 2: Research Data, Documentation, and Storage


## Learning Objectives

- **Learning Objective 1 (LO1):** Recognise the responsibilities regarding Research Data Management during data collection and storage.
- **Learning Objective 2 (LO2):** Summarise the means to and benefits of organising and cleaning data.
- **Learning Objective 3 (LO3):** Apply documentation to data in accordance with policy and regulations relevant to the context of the Data Steward.


## Total Module Duration

3 hours 15 minutes


## Learning Objective 1

LO1: Recognise the responsibilities regarding Research Data Management during data collection and storage.


### Learning Activities

- **Practical Exercise&mdash;Data Flow Map** (45&nbsp;mins): Facilitate the data flow map exercise that is provided in Resource&nbsp;1.
- **Reflection activity** (45&nbsp;mins): Identify institutional data documentation and metadata documentation tools. Make this a think-pair-share exercise which is explained in more details in Resource&nbsp;3.


### Materials to Prepare

- Presentation on storing data and metadata.
- Reflection activity on institutional documentation tools.


### Instructor Notes

**Presentation:**

- Highlight the importance of storing contents of research as well as data and metadata (information about the data). The presentation can highlight which tools are available for data documentation. The facilitator can relate this to the local context by introducing (for example) different tools available according to the policies of their institutes or by initiating discussion among the learners.
- The instructor can introduce the data flow map at this stage and use this to facilitate a practical exercise or use parts of it in a presentation format (see Resource&nbsp;1).

**Reflection Activity:**

- For the reflection activity, the instructor can first introduce some of the possible tools that are available for data and metadata documentation: for instance, README files, Data Management Plans, Electronic Lab Notebooks. Discuss this and other tools, especially prescribed tools within the learners institutional or national context. Let participants discuss what they use in their local context.


### Resources

**Input for Presentation and discussion:**

1. Exercise 1. Data Flow Map. <https://tu-delft-library.github.io/rdm101-book/RDM101course-exercise1.pdf>.
2. Martinez-Lavanchy, P. M., et al. TU Delft Research Data Management 101 Course (Module 2). Zenodo, 1 Mar. 2024. DOI.org (Datacite). <https://doi.org/10.5281/ZENODO.10732095>.
3. Think, Pair, Share | Kent State University. <https://www.kent.edu/ctl/think-pair-share>. Accessed 15 Apr. 2025.



## Learning Objective 2

LO2: Summarise the means to and benefits of organising and cleaning data.


### Learning Activities

- **Lecture** (60&nbsp;mins): Introduce the concept of tidy data and the difficulties presented by untidy data.


### Materials to Prepare

- Slides for lecture on tidy data (defining tidy data and realising the F and A in FAIR).
- Optional Activity.


### Instructor Notes

**Lecture:**

- Findability and Accessibility can sometimes be impaired by sloppy data practices. This can have knock on effects to its reusability.
- Introduce the concept of tidy data as defined by Hadley Wickham, which states that each variable should have its own column, each observation should have its own row, and each type of observational unit should have its own table. Discuss the importance of tidy data for data analysis, visualisation, and reproducibility
- Summarise common difficulties encountered by untidy, incomplete, or other issues in data. For instance, missing entries can create issues in coding. Thus, part of curating a dataset may be filling missing entries with dummy values. Using uniform formats enables sorting, filtering and further analysis.
- Highlight the importance of documenting changes to datasets. A lack of documentation can impact the dataset's use for reproducibility tests and lower overall transparency. This can be done by documented versioning as well as other forms of logging within data repositories.
- Point towards further elements of automation that are enabled by way of coding, such as pulling data and checking it.

??? info "Optional Activity"

    The activity can focus on the following aspects: Automating boring tasks with Python and Pandas: Loops and Conditionals, Pandas and DataFrames, Aggregating data, Dealing with empty values and incomplete data, Type conversion, Unique and standard values, best practices and documentation.

    The instructor can use Python as an example of a tool to use for data cleaning. Recommendation of how one can go on to work with this concretely:

    - Go through the basics of Python automation; loops and conditionals.
    - Go through the Pandas library for Python, covering crucial functions for tidy data such as `pd.melt()`, `pd.pivot_table()`, `pd.concat()`, `dropna()`, `fillna()`, `astype()`, and `drop_duplicates()`.
    - Make clear that this is not only work that the data steward may be called on to do, but might also be something that they teach.


### Resources

**Lecture:**

1. Wickham, Hadley. "Tidy Data". Journal of Statistical Software, bd. 59, nr. 10, 2014. DOI.org (Crossref). <https://doi.org/10.18637/jss.v059.i10.Recommendations>.
2. For engaging directly with cleaning data: Tidy data: <https://vita.had.co.nz/papers/tidy-data.pdf>.
3. Copenhagen University Library Datalab intros to Python Pandas. <https://kubdatalab.github.io/python/docs/intro.html>.
4. Melanie Walsh's introduction to Cultural Analytics and Python. <https://melaniewalsh.github.io/Intro-Cultural-Analytics/welcome.html>.
5. Library Carpentries: Tidy data with Pandas. <https://librarycarpentry.github.io/lc-python-intro/tidy.html>.



## Learning Objective 3

LO3: Apply documentation to data in accordance with policy and regulations relevant to the context of the Data Steward.


### Learning Activities

- **Discussion** (45&nbsp;mins): Participants list their institutional policies (if any) that outline RDM. They discuss the best practices for data documentation and storage within these policies. This discussion can be done in small groups. At the end of the discussion, each group can present/summarise documentation/storage practices highlighted in the policy they discussed OR if they have real life examples to showcase the practice this would be even better. If there is no institutional policy in place then they can discuss what are the current RDM practices within their institute and what a policy document should take into account or the trainer can provide them with an existing RDM policy.


### Materials to Prepare

- Facilitate discussion by having one or two institutional policies to share with the group (refer to Resources&nbsp;1&ndash;4 for some examples).


### Instructor Notes

**Discussion:**

- The instructor can introduce the goal of an institutional policy to outline how researchers are provided support to implement good RDM practices as well as data documentation and storage practices. Such a policy helps an institute to identify and address gaps and challenges in infrastructure, resources and other practices related to RDM.
- The instructor should outline the key elements of an RDM policy concerning data documentation and storage which includes:
    - the goal of a policy as well as definitions,
    - scope of policy (which data it is dealing with),
    - roles and responsibilities of various stakeholders with regards to data documentation and storage, and
    - any compliance or recommendations that have to be adhered to or other practices to be followed (Resources&nbsp;3, 4).
- The instructor can find many institutional data policies online by doing an online search. Some links have been provided in the resource.


### Resources

**Input for Discussion:**

1. "Research Data Management Code of Conduct." Maastricht University Library, 3 Jul. 2024. <https://library.maastrichtuniversity.nl/research/rdm/rdm-policies/research-data-management-code-of-conduct/>.
2. "RDM Policies." Vrije Universiteit Amsterdam. <https://vu.nl/en/about-vu/more-about/rdm-policies>. Accessed 25 Mar. 2025.
3. "TU Delft & Faculty Policies." TU Delft. <https://www.tudelft.nl/en/library/current-topics/research-data-management/r/policies/tu-delft-faculty-policies>. Accessed 25 Mar. 2025.
4. Policies and Guidelines for Research Data Management - For Employees - University of Oslo. <https://www.uio.no/english/for-employees/support/research/research-data-management/policies-guidelines.html>. Accessed 25 Mar. 2025.
