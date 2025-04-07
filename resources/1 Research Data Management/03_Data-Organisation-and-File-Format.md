---
title: "Module 3: Data Organisation and File Formats"
author: "Skills4EOSC T4.1"
tags:
    - Skills4EOSC
    - DataStewardship
    - Curriculum
    - Research Data Management
    - RDM
    - Data Organisation
    - File Format
---

# Module 3: Data Organisation and File Formats

!!! warning "This page is currently under construction"

    **The training curriculum is currently undergoing final revisions and quality checks.**
    **All materials will be released shortly.**
    **Until the official release, please refrain from using, distributing, or implementing any part of these resources.**


## Learning Objectives

- **Learning Objective 1 (LO1):** Describe the basic principles of file management.
- **Learning Objective 2 (LO2):** Set up a file structure for data files.
- **Learning Objective 3 (LO3):** Identify and distinguish between open and closed file formats.
- **Learning Objective 4 (LO4):** Explain the benefits and disadvantages of Open and closed file formats and.
- **Learning Objective 5 (LO5):** Explain the concept of obsolescence and identify factors that can contribute to obsolescence and how to mitigate them.


## Total Module Duration

9 &ndash; 9.5 hours (including preparatory exercises)


## Learning Objective 1

LO1: Describe the basic principles of file management.


### Learning Activities

- **Pre-reading** (45 mins): Before the lesson ask the learners to watch a short video about organising files and data (Resource 1) and read this webpage about file naming conventions (Resource 2).
- **Lecture** (120 mins): Introduce the basics of file management, building on the Carpentries lesson in File management (Resource 3).
- **(Optional) Supplementary activity** (120 mins): Follow the Library Carpentry lesson on Tidy Data (Resource 4) either as an in-class activity or self-paced option.


### Materials to Prepare

- Distribute the pre-reading and video prior to the session.
- Lecture on basis of file management and its importance.
- Optional activity &ndash; introduce and facilitate the carpentries lesson on Tidy data as a code along or self-paced activity or digital learning environment.


### Instructor Notes

**Lecture:**

- Give an introduction to the basics of file management (paths, trees and folders and naming conventions) to give an overview of why file management is important for data security, efficiency and collaboration. Introduce concepts and terminology, such as hierarchical, network and relational systems; file management tools such as organisational, search functions, version control, access management, collaboration and integration.
- Key takeaways to cover include:
  - Every computer has a file system used to keep track of the files on that machine. This system varies according to the computer. However, there is a common aim: The operational system (OS) allows the user to organize the contents of their computer in a hierarchical structure of directories that includes drives, folders, subfolders, and files.
  - File organization means the information/documents are organized so that a computer can read and understand it. This lets you use the full power of the computer for your analyses and stewardship.
  - Even though files are neatly organized, the content still might have errors or missing data or other problems. It's like you put all your data in the right drawers, but the drawers might still be messy.

**Optional Activity:**

- This activity follows the library carpentry lesson on file management. The Carpentry lessons include instructor notes and exercises and can be taught as "code-along" or self-paced activities. An optional hands-on activity is the Carpentry lesson about the Tidy Data principles. The Tidy Data activity would add another 120 mins to the lesson.


### Resources

**Resources for learning activities &ndash; instructor and learners:**

1. Ghent University. "RDM Knowledge Clips" *YouTube, * Seen 19 March 2025.
2. *File Naming Conventions \| Data Management*. <https://datamanagement.hms.harvard.edu/plan-design/file-naming-conventions>. Seen 19. March 2025.
3. *File Organization*. <https://datacarpentry.github.io/rr-organization1/>. Accessed 24 Mar. 2025.
4. *Optional activity: Tidy Data for Librarians: Summary and Setup*. <https://librarycarpentry.github.io/lc-spreadsheets/#setup>. Accessed 24 Mar. 2025.

**Inspiration to the slide deck &ndash; for instructors:**

5. *Paths and Trees and Folders - Ppt Download*. <https://slideplayer.com/slide/17369365/>. Accessed 24 Mar. 2025.



## Learning Objective 2

LO2: Set up a file structure for data files.


### Learning Activities

- **Presentation** (20 mins): Presentation to the practicalities of file-naming and version control.
- **Reflection activity** (45 mins): This activity is on the advantages and disadvantages the instructor and learners have experienced when storing files locally on their own computer and in a cloud solution (e.g. OneDrive, Dropbox, Google Drive).
    - The learners are encouraged to share in small groups how files on their computer are organised and assess & give feedback to each other on how they have named the files and worked with version control (as covered in LO1).
    - After the reflection activity, the learners can conduct an independent reflection to write a file naming convention using a project or files the learner has in their path finder. They formulate the naming convention and best practices for a fictive research group working with these files.


### Materials to Prepare

- Presentation on practicalities of file management and version control.
- Reflection activity: The instructor might have to bring their own examples and facilitate learns to share their own examples.


### Instructor Notes

**Presentation:**

- The instructor can provide practical instruction in and discussion on approaches to structuring and naming. Tips can be provided on creating a file naming convention that suits the discipline and data format requirements in research projects so that project members can navigate the data files.
- Allow time for your learners to create a file naming convention and structure and give feedback to someone else's work.
- Key take-aways:
    - The topics covered provide an introduction to the best ways of saving datafiles so they are not lost.
    - There can be disciplinary and project-level differences in file naming and organisation.
    - A slide deck on the practicalities of file management and version control (Resource 1). The instructor can cover information on sorting files, what is good information for file naming, and how to do version control.

??? info "Sample first slide"

    The presentation can be kicked off by the following two questions:

    1. Which filename is the most appropriate of the three below and why?
        - `2022-03-24_Attachment`
        - `24 marts 2022 Attachment`
        - `24032022attachment`
    2. Which file names is the most appropriate of the three below and why?
        - `labtox_recent_110810_old_version.sps`
        - `2010-08-11_bioasssay_tox_V1.sps`
        - `FFTX_3776438656.sps`

??? info "Detailed key points to cover in the presentation"

    **Sorting files:** Computers often sort files alphabetically in the file browser. It is therefore a good idea to place the key information at the beginning of the file name. However, the sorting can be changed, e.g. to use the date the file was saved.

    **Sorting by date:** If you think you will need to find files by date, place the date the data were created at the start of the file name. The best date format is `YYYYMMDDhhmm`, as this ensures the files are sorted by year, then month, day and time. Use 24-hour format to avoid confusion about am/pm. When you use the date as the first element, the computer will be able to sort the files in correct chronological order, with either the newest or oldest first.

    **What information is good to include in the file name?** Think about what other information is good to include in the file name. For example, the initials of the person who conducted the experiment, performed the interview or collected the information in some other way. You might then add the experiment or interview number, if the data are collected in a specific order.

    Finally, you might add an abbreviation for the project or assignment. If you create a folder for data solely for a specific project, it might seem unnecessary to include the project name or abbreviation in the file name, but it may still be a good idea, as you might send a file to someone who has a different folder structure. In this case, it is good that they can see which project the file belongs to. Also, file names should be kept short. Try to limit them to 25-30 characters.

    **Elements that can be included in file names are:**

    - The date the file was created
    - Location (where the data were collected)
    - Project name or number
    - Sample number
    - Name of analysis or abbreviation
    - Version number
    - Name (or an abbreviation) of the person who collected the data, conducted the experiment or last worked on the file.

    File names must be readable, without compromising on precision. Some software does not like spaces in file names, so you should avoid them. You can replace spaces with `-` (hyphen) or `_` (underscore). Or you can start new words with a capital letter. For example:

    - `file-name.xxx`
    - `file_name.xxx`
    - `FileName.xxx`

    Where 'xxx' is the file extension, showing the file type (e.g. .txt, .doc, .csv, .pdf, .xlsx).

    Avoid special characters such as:  
    ``~ ! @ # $ % ^ & * ( ) ` ; : < > ? . , [ ] { } ' " |``

    DO NOT WRITE FILE NAMES ALL IN UPPER-CASE. IT MAKES THEM DIFFICULT TO READ.

    **Examples of good file names:**

    - `20190102_ac_smithlab_utra_exp01_gel_003.tiff`
    - date_experimentNumber_content_version.fileType:  
      `20190501_exp123_analysis_v01.pdf`
    - date_analysisMethod_topic_version.fileType:  
      `20190811_bioassay_toxicity_V1.sps`  
    - date_journalName_documentName_versionNumber.fileType:  
      `2020-plos-manuscript-v26.pdf`  

    **Examples of bad file names:**

    - `Test data 2016.xlsx`
    - `Meeting notes Jan 17.doc`
    - `Notes Eric.txt`
    - `Final FINAL last version.docx`

    **Sorting based on types of files and content:** If you work with different types of files or data from different sources, equipment or experiments, it is best to store them in separate folders. For example, you could store microscopy images in one folder, questionnaire responses in a second folder and audio files from interviews in a third. When naming your folders, it is important not to use the same subfolder names for different projects. If you send a subfolder containing files to another person, it could be unclear which project the folder belongs to, so include the project name or abbreviation in the name of subfolders.

    **Versions:** If you regularly add more data, it might be good to add a version identifier like 'v2' to the file name, e.g. filename_v2.xxx. If you include numbers in the file name, use leading 0s to ensure the files sort correctly (001, 002, 003). If you have a number of files with the following file names: 1, 246, 3, 111, 22, 33 and 2, older systems might sort them as follows: 1, 111, 2, 22, 246, 3, 33.

    **Naming conventions:** It is always a good idea to check whether particular naming conventions are used in your subject area. A naming convention is a standardised way of naming files. This is particularly relevant if you expect to share data publicly. If the data are to be kept private, you can name them in whatever way works best for you.

    Examples of naming conventions:

    - `[initials]_[method]_[topic]_[YYYYMMDD]_[version].[xxx]`
    - `[project#]_[method]_[version]_[YYYYMMDD].[xxx]`
    - `[fileType]_[initials]_[date].[xxx]`

**Reflection Activity:**

- Prepare instructions to the reflection activity. Include a case to exemplify file organisation and a codex for versioning.
- Prepare a checklist for file-naming using the information below developed by Copenhagen University working group for Digital Competences (Resource 3).


### Resources

**Input for the presentation &ndash; for instructors:**

1. Kjorveziroski, V. and Buss, M. Unit 3:*The Technical Aspect*s in: Wildgaard, Lorna, og Benjamin Derksen (Ed.):Technical Skills Are the Bridge to Reproducible Research: An Introduction for Data Librarians*.* Zenodo, 27 February 2025. *DOI.org (Datacite)*, <https://doi.org/10.5281/ZENODO.14936647>.

**Input for the reflection activity (file naming):**

2. 'Collecting and Organizing Data'. *Universiteit Gent*, <https://www.ugent.be/en/research/openscience/datamanagement/during-research/collection.htm>. Accessed 24 Mar. 2025.
3. Wildgaard, L. and Larsen, A.V. Save your data well - how to save data and find them again" *Copenhagen University, <https://absalon.ku.dk/courses/70701/pages/save-your-data-well-how-to-save-data-and-find-them-again?module_item_id=2053460.> Accessed 24. Mar. 2025*
4. *OSF*. How to name a file, <https://osf.io/dpu45/>. Accessed 24 Mar. 2025.
5. <https://authors.library.caltech.edu/records/mmnpf-cez11>

**Input for the reflection activity (data organisation and version control):**

6. 'Collecting and Organizing Data'. *Universiteit Gent*, <https://www.ugent.be/en/research/openscience/datamanagement/during-research/collection.htm>. Accessed 24 Mar. 2025.
7. *File Organization: File Organization: Naming*. <https://datacarpentry.github.io/rr-organization1/01-file-naming/index.html>. Accessed 24 Mar. 2025.



## Learning Objective 3

LO3: Identify and distinguish between open and closed file formats.


### Learning Activities

- **Lecture** (45 &ndash; 60 mins): on file formats, durability and recommended formats.
- **Q&A**: The walking questions (Resource 2) can be used for this activity between learners about image formats, formats that are best suited for short and medium term storage, file formats best suited for long term preservation and why use non-proprietary/open formats. The instructor can use Resource 1 where it discusses formats to facilitate the discussion.


### Materials to Prepare

- Lecture/slide deck on open and closed file formats and considerations to use each.
- Question prompts to facilitate the activity around file formats (Resources 1, 2).


### Instructor Notes

Consider letting the learners read or watch selected materials from the resource list before the lesson to encourage questions during the lecture. Pose questions and to and between the learners to discuss during the lecture.

**Lecture:**

- What are open and closed file formats? What are durable file formats? When would you use an open file format and when would you used a closed file format? What could the consequences of using a closed format be for Open Science?
- Key takeaways:
    - Selecting the right file format depends on the purpose, need for accessibility, and long-term preservation goals. Adhering to disciplinary standards and recommended practices ensures compliance and enhances the integrity and usability of digital data.
    - While Open file formats promote accessibility, interoperability, and long-term preservation, closed file formats can include robust security features, controlled by the owning company or have features that simply do not exist in open formats. However closed file formats can hinder data sharing and access, posing risks to the sustainability of digital information.
    - Different file formats offer varying levels of security and privacy protection.

**Q&A:**

- This activity helps learners to think and provide their own answers to questions they may have. The instructor facilitates this by having prompts ready as well as the answers ready for discussion (Resources 1, 2).


### Resources

**Input for the question and answer session:**

1. *FAQ*. <https://www.data.cam.ac.uk/faq>. Accessed 24 Mar. 2025.
2. 'Walking Questions'. *SessionLab*, <https://www.sessionlab.com/methods/walking-questions>. Accessed 24 Mar. 2025.

**Input for slide preparation (about file formats in data management):**

3. Teperek, Marta. *Choosing Formats*. 6 Mar. 2015, <https://www.data.cam.ac.uk/data-management-guide/creating-your-data/choosing-formats.>
4. Buttery, Hannah. *Expert Help Guides: Getting Your Data Organised: Durable File Formats*. <https://latrobe.libguides.com/dataorganisation/fileformats>. Accessed 24 Mar. 2025.
5. Lennertz, Lora. *Research Guides: Data File Management: File Formats*. <https://uark.libguides.com/c.php?g=947342&p=6830130>. Accessed 24 Mar. 2025.

**Examples for discussion &ndash; for instructors:**

6. *Recommended Formats Statement - Resources (Preservation, Library of Congress)*. <https://www.loc.gov/preservation/resources/rfs/>. Accessed 24 Mar. 2025.
7. *File Formats*. <https://opendatahandbook.org/guide/en/appendices/file-formats/>. Accessed 24 Mar. 2025.



## Learning Objective 4

LO4: Explain the benefits and disadvantages of Open and closed file formats.


### Learning Activities

- **Introduction** (20 mins): Introduction to the topic and the workshop and aligning expectations to learners 'participation.
- **Case Study** (60 mins): Case study where the learners suggest file formats for a fictional PI and research project. The aim is to get the learners to weigh the benefits and disadvantages of different formats in the context of the research field's traditions and requirements. Consequently, they will have to argue for and against open/closed format considering factors such as accessibility, longevity and data integrity. Resources 1 &ndash; 3 can be shared with learners to refer to during this activity.


### Materials to Prepare

- An introduction to the workshop which will be on the benefits and downsides of open and closed file formats through a case study.
- Present a fictitious case study as suggested in the instructor notes (or a real one if the instructor can present something from their own experience).


### Instructor Notes

**Introduction:**

- Prepare a slide deck outlining the activity which will take the whole lesson and what you expect the learners to do. Prepare a list of recommended resources the learners can refer to during the case work.

**Case study:**

- Prepare/present the fictive case study below:
    - A Principle Investigator contacts the data steward (the learners) and requests help designing a file organisation to appropriately structure the project files and choosing appropriate file formats for the data, with preservation in mind. Find the metadata describing an open project in a repository relevant for the discipline or disciplines of the learners. Ensure the type or types of data collected in the project is described, the sources of the data, possible technical limitations, software to be used in analyses, and other relevant external data and information. Of course the instructor may have to manipulate the metadata, removing or adding information so the learners can come with ideas about which file organisation and formats they would suggest.
    - Discussion points can be prepared (e.g. on a digital discussion board) where discussion is facilitated so the learners respond to different prompts in their thought processes: Which format best ensures long-term preservation and accessibility? What are the trade-offs between advanced features in closed formats and the accessibility of open formats? How do ethical and legal considerations influence the choice of file format?


### Resources

**Input the learners can refer to during case work:**

1. *Format Description Categories - Sustainability of Digital Formats \| Library of Congress*. <https://www.loc.gov/preservation/digital/formats/fdd/descriptions.shtml>.
2. *Choosing The Right File Format/Quick Guide - Wikibooks, Open Books for an Open World*. <https://en.wikibooks.org/wiki/Choosing_The_Right_File_Format/Quick_Guide>.
3. Service, UK Data. 'Recommended Formats'. *UK Data Service*, <https://ukdataservice.ac.uk/learning-hub/research-data-management/format-your-data/recommended-formats/>.

**Input for datasets to use as cases &ndash; for instructors:**

4. *Datasets for Teaching and Learning*. <https://www.lib.ncsu.edu/formats/teaching-and-learning-datasets>. Accessed 24 Mar. 2025.
5. Huck, Jennifer. *LibGuides: Data and Statistics: Find Data for Teaching and Learning*. <https://guides.lib.virginia.edu/data/teachandlearn>. Accessed 24 Mar. 2025.
6. Data Education in School. *Useful datasets for data education in schools.* <https://dataschools.education/resource/useful-datasets-for-data-education-in-schools/>



## Learning Objective 5

LO5: Explain the concept of obsolescence and identify factors that can contribute to obsolescence and how to mitigate them.


### Learning Activities

- **Exercise** (45 mins): Learners will convert a provided file from a closed format (e.g., .docx) to various open formats (e.g., .pdf, .txt, .csv). They will note any data loss during conversion (e.g., formatting, embedded images, metadata) and prepare any questions they have about why certain data might not be preserved in the new format (Resource 1).
- **Lecture** (45 mins): Lecture about obsolescence, preservation and working open and FAIR.
- **(Optional) Module Assessment** (45 mins): Gage comprehension of LO1 &ndash; LO5.


### Materials to Prepare

- Providing a closed format file to learners.
- Slide deck on the implications of obsolescence and benefits of using open formats.
- Optional Module Assessment through the use of a real life case study or suggested examples given in the Instructor Notes.


### Instructor Notes

**Exercise:**

- The instructor provides learners with a closed format file and request that they convert from a closed format (e.g., .docx) to various open formats (e.g., .pdf, .txt, .csv).
- Ask learners to:
    1. Note any data loss during conversion (e.g., formatting, embedded images, metadata)
    2. Prepare any questions they have about why certain data might not be preserved in the new format.
- The instructor can end the exercise by summarising points raised from the questions above and discuss strategies for mitigating data loss in the conversion process.

**Slide deck:**

- Prepare a slide deck using the materials about the implications of obsolescence (Resources 2, 3) and the benefits of using open formats (Resources 4, 5) and (optionally) in line with FAIR, and OPEN principles.
- Points to present to and discuss with the learners during the presentation can be:
    - Data Integrity: How does the conversion process affect data integrity and usability?
    - Data ethics: Which considerations did you have about security, privacy and ethical/legal issues?
    - Long-Term Access: What measures can be taken to ensure long-term access and prevent obsolescence?
    - Preservation: Which strategies could be recommended to mitigate obsolescence?
    - Ethical Considerations: How do open formats align with ethical standards in their specific research field?
- Help the learners assess the security and privacy of converted files. Consider how easily the data can be accessed, modified, or shared without authorization. Discuss the usability of the files in different formats after conversion. Consider aspects like ease of access, readability, and whether the essential data remains intact and functional. Identify challenges such as corrupted data, loss of functionality (e.g., formulas in spreadsheets), or incompatibility with commonly used software.

??? info "(Optional) Module Assessment"

    Prepare an assessment activity to gage the learners comprehension of LO1 &ndash; LO5.

    The instructor presents a research project they know well (such as one of their own) OR uses one of the project example below (Example 1, Example 2). Ensure the project description contains information about the type of data collected (e.g., qualitative interviews, quantitative measurements, images), software and file formats initially used, potential collaborators and stakeholders, ethical considerations and privacy issues and requirements for long-term preservation.

    **How to conduct the activity:**

    1. Divide students into small groups where the learners take on the role of a data steward and have to advise on the following aspects of the project:
        - Create a file organisation plan and a naming convention.
        - Selection of appropriate file formats (open vs. closed) and rationale for the choice.
        - Steps for converting closed formats to open formats.
        - Considerations of application of the FAIR principles (refer to the unit on FAIR data).
        - Strategies to mitigate obsolescence and ensure long-term preservation.
        - Consideration of security, privacy, and ethical issues.
    2. Groups will document their plan and prepare a brief presentation.
    3. Each group presents their plan.
    4. Class discussion and feedback on how to improve the plans.
    5. Conclusion and Reflection.

    ??? info "Example 1: Health and Lifestyle Survey"

        **Description:**

        A survey dataset collected from participants about their health and lifestyle habits, intended for research on public health trends.

        **Format:**

        SPSS files

        **Dataset Components:**

        1. Personal Information:
            - Participant ID: Unique identifier for each participant (e.g., P001, P002, ...)
            - Age: Age of the participant (e.g., 35, 42, ...)
            - Gender: Gender of the participant (e.g., Male, Female, Non-binary)
            - Location: City or region of residence (e.g., New York, London, Berlin)
        2. Health Information:
            - Chronic Conditions: Information on chronic conditions (e.g., diabetes, hypertension)
            - Medication: List of medications taken (e.g., insulin, antihypertensives)
            - Medical History: Any significant medical history (e.g., surgeries, hospitalisations)
        3. Lifestyle Information:
            - Diet: Information about dietary habits (e.g., vegetarian, high-protein diet)
            - Exercise: Frequency and type of exercise (e.g., daily jogging, weekly gym sessions)
            - Sleep Patterns: Average hours of sleep per night (e.g., 6 hours, 8 hours)
        4. Survey Responses:
            - Self-Rated Health: Participant's self-assessment of their health (e.g., Excellent, Good, Fair, Poor)
            - Health Goals: Personal health goals and aspirations (e.g., lose weight, managestress)
            - Barriers to Health: Challenges faced in maintaining a healthy lifestyle (e.g., lack of time, financial constraints)
        5. Data Sensitivity Considerations:
            - Sensitive Data:
                - o Personal Information: Location, gender, and age may be sensitive when combined with other data.
                - o Health Information: Chronic conditions and medication details are highly sensitive and should be handled with care.
            - Non-Sensitive Data:
                - Diet and Exercise Information: While still valuable, these data points are less sensitive compared to detailed health information.

    ??? info "Example 2: Handling Sensitive Data for a Mental Health and Wellbeing Study"

        **Description:** A research study aiming to explore the relationship between mental health and various lifestyle factors. The study collected detailed interview responses from participants on mental health symptoms, treatment history, and personal experiences.

        **Format:**

        - Interviews in MAC pages format
        - Coded interviews in an NVivo project format

        **Dataset Components:**

        1. Personal Information:
            - Participant ID: Unique identifier (e.g., P001, P002, ...)
            - Age: Age of the participant (e.g., 28, 45, ...)
            - Gender: Gender of the participant (e.g., Male, Female, Non-binary)
        2. Mental Health Information:
            - Symptoms: Self-reported symptoms (e.g., depression, anxiety, PTSD)
            - Treatment History: Details of mental health treatments (e.g., therapy sessions, medications)
            - Personal Experiences: Descriptions of significant life events impacting mental health
        3. Lifestyle Factors:
            - Social Support: Information on social support networks (e.g., friends, family)
            - Work-Life Balance: Participant's perception of their work-life balance (e.g., stress levels, job satisfaction)

        You are responsible for preparing this dataset for sharing with other researchers to facilitate further analysis while ensuring that sensitive information is adequately protected.

        1. Challenges:
            - Sensitive Data: Mental health symptoms, treatment history, and personal experiences are highly sensitive and must be handled with strict confidentiality.
            - Balancing Openness: The study aims to share valuable insights while protecting participant privacy.
        2. Solutions:
            - Anonymisation:
                - Remove Identifiers: Strip out or anonymise personal identifiers such as Participant ID and specific age or gender details.
                - Aggregate Data: Aggregate symptoms and treatment history into broader categories to minimise the risk of identification (e.g., generalising symptom categories instead of detailed descriptions).

    For the instructor the goal of this optional activity is that the learner think about the importance of file organization and choosing the right file formats as well as the broader implications of their choices in the context of open science and digital preservation.Give more time than you think for the case work and discussion afterwards, as there are many issues that can be discussed!

    **Key Take-aways:**

    - File management is the organization, structure, naming, accessing, and storing of documents. Good file management increases efficiency as information is easily found and understood.
    - Specific consequences of file mismanagement vary depending on the project; however, general risks include legal liability, regulatory non-compliance, duplication of efforts, misunderstanding of data, loss of knowledge during turnover, file obsolescence or corruption, inability to verify information, unclear provenance, and wasted time finding or accessing information.
    - Choosing the right file format is important. The benefits of Open File Formats are increased accessibility, interoperability, longevity and transparency. The disadvantages can be limited features and less technical support.
    - Benefits of Closed File Formats are the have sophisticated features and functionalities, integrate with other proprietary software's, there is good support. Disadvantages are restricted access, limited compatibility, risk of obsolescence and cost.
    - Effective preservation often requires specialized technical knowledge, which may be lacking in some organizations. Over time, data stored in certain formats can degrade, leading to loss of information and reduced usability.
    - Compatibility Issues: As new software and systems emerge, older formats may become incompatible, making data retrieval difficult. Data Sensitivity: Consider privacy and security implications, particularly for sensitive or confidential data.
    - Licensing: Be aware of any licensing restrictions that might affect the use and distribution of the chosen format. Consider who needs to access the data and ensure the format chosen facilitates broad accessibility and collaboration.


### Resources

**Input for file conversion exercise &ndash; resources for the instructor:**

1. *Converting from One File Type to Another \| Computing*. <https://www.maths.cam.ac.uk/computing/converting-one-file-type-another>.

**Resources about obsolescence &ndash; slide preparation for instructors:**

2. *Obsolescence: File Formats and Software \| Digital Preservation Management*. <https://dpworkshop.org/dpm-eng/oldmedia/obsolescence1.html>.

**Identifying a file extension and the software needed to open it:**

3. *FileInfo.Com - The File Format Database*. <https://fileinfo.com/>.

**Resources for slide development &ndash; for instructors:**

4. Administrator. 'DMP - Data Formats for Preservation'. *OpenAIRE*, <https://www.openaire.eu/data-formats-preservation-guide>.
5. 'Data Ethics Framework'. *GOV.UK*, 16 Sept. 2020, <https://www.gov.uk/government/publications/data-ethics-framework>.
