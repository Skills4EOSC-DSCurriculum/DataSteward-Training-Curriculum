---
title: "Module 8: Ontologies"
author: "Skills4EOSC T4.1"
tags:
    - Skills4EOSC
    - DataStewardship
    - Curriculum
    - Research Data Management
    - RDM
    - Ontologies
---

# Module 8: Ontologies

!!! warning "This page is currently under construction"

    **The training curriculum is currently undergoing final revisions and quality checks.**
    **All materials will be released shortly.**
    **Until the official release, please refrain from using, distributing, or implementing any part of these resources.**


## Learning Objectives

- **Learning Objective 1 (LO1):** Explain the concept of ontologies.
- **Learning Objective 2 (LO2):** Explain the concept of linked data.
- **Learning Objective 3 (LO3):** Apply ontologies to datasets.


## Total Module Duration

3 hours


## Learning Objective 1

LO1: Explain the concept of ontologies.


### Learning Activities

- **Lecture** (30 mins): Introduce the basics of ontologies (see Instructor Notes for detailed contents).
- **Research and group discussion** (30 mins): Search for ontologies, discover terms and relationships, and exchange with others (see "Instructor Notes" for a more detailed example).


### Materials to Prepare

- Lecture on introduction to ontologies (see Instructor Notes for detailed contents).
- Research and group work: exercise on investigating an ontology.


### Instructor Notes

**Lecture:**

- The learners should learn the definition and purpose of an ontology as well as the difference to similar concepts like a taxonomy. The most important concepts and languages/tools should be included (see Resources 1&ndash;6). The instructor can use the video from Resource 7 for a basic understanding of ontologies as well as examples.
- Content to include in lecture:
    - Basic concepts of ontologies (class, property, relationship)
    - Delimit use of ontology term from other usages (e.g. in philosophy)
    - Different types of controlled vocabularies (word list, taxonomy, thesaurus, ontology)
    - Relevant standards, technologies, and tools (e.g. RDF(a), SKOS, OWL, Turtle, SPARQL, JSON-LD, Protege, ...)
    - Benefits of using controlled vocabularies (for metadata)
- If possible, include examples where ontologies are important to find datasets, for example, World Protein Databank.
- For data stewards, ontologies help improve data interoperability and integration by using an established set of names and description of the knowledge from a discipline.
- If the audience is known, give hints about specific ontologies and adapt the examples to the domain of the learners (see Resources 8, 9 for some examples).

**Research and group discussion:**

- This is a practical exercise to enable learners to investigate an ontology: how it is structured, visualised and how it helps to find datasets.
- If there are learners from different research domains, build groups according to domain.

??? info "Detailed exercise description with examples"

    **Search for an ontology:**

    Visit an Ontology Repository that aligns with your interests, e.g. [BioPortal](bioportal.bioontology.org). Use the search bar to find an ontology related to a topic you care about. For example, you could search for "environment", "microbiology", "climate", "cancer", etc. BioPortal will show ontologies that have terms matching your query.

    **Investigate an Ontology:**

    - Identify its scope: What domain or subject does it cover? E.g., "This ontology describes plant phenotypes" or "This ontology lists climate observation properties."
    - Check the structure: Does it show a hierarchy or list of top-level categories? Click around to see if terms are organised (BioPortal often let you see a tree of classes).
    - Find a specific term (class): Pick a term that interests you and view its details. What is its definition? Does it have relationships listed (e.g. "Subclass of X", "Part of Y", or properties)? Does it have synonyms? For example, in ENVO, the term "Soil" might be under a broader term "environmental material" and overlap with concepts like "mineral material" or "clay".
    - Maintenance and source: Who created or maintains that ontology? (Often listed in description). This is just to remind you that ontologies are curated by organisations or communities in the scientific world.

    **Share & Discuss:**
    
    Have each person or pair briefly introduce the ontology or dataset they explored. Example: "We looked at ENVO (Environment Ontology). It's an ontology for environmental entities (like habitats, environmental features). It's structured hierarchically: e.g., 'human settlement' is a subclass of 'animal-associated environment' (but also of 'anthropised ecosystem' and 'environment associated with an animal part or small animal'). These relations are visualised in the Visualization tab. We found the class 'village' ('larger than a hamlet but smaller than a town'), which is also used in many other ontologies (see under Mappings). Using this ontology, someone annotating a dataset about ecosystems could tag 'village' in a standard way, which would help others find all data about villages even if they come from different sources."


### Resources

**Training Materials:**

1. EMBL's European Bioinformatics Institute (EMBL-EBI). Bioinformatics for the Terrified: Controlled Vocabularies. <https://www.ebi.ac.uk/training/online/courses/bioinformatics-terrified/what-makes-a-good-bioinformatics-database/controlled-vocabularies/>. Accessed 12 Mar. 2025.
2. *Controlled Vocabularies & Ontologies -- Metadata*. <https://nbisweden.github.io/module-metadata-dm-practices/02-ontologies/index.html>. Accessed 12 Mar. 2025.
3. CFDE Data Resource Center. *CFDE Information Portal*. <https://info.cfde.cloud/documentation>. Accessed 12 Mar. 2025.
4. Cox, Simon, and Nick Car. *Vocabularies & Ontologies: Similarities & Differences, Definitions & Structures*. Australian Research Data Commons (ARDC), 2017. <https://av.tib.eu/media/36056>.
5. Aguilar Gómez, Fernando. Introduction to Ontologies. Sept. 2024. GitHub, <https://skills4eosc-dscurriculum.github.io/Pilot-Training-Ontologies/latest/>.

**Definition Ontology:**

6. *W3C. Semantic Web: Ontologies*. 9 Aug. 2018. <https://web.archive.org/web/20180809211622/http://www.w3.org/standards/semanticweb/ontology>.

**Videos:**

7. Ontologies. Directed by NFD4Cat, 2023. <https://www.youtube.com/watch?v=JUqicR4kmEI>.

**Discipline specific information:**

8. Jansen, Ludger. "Ontologies for the Digital Humanities: Learning from the Life Sciences?" *JOWO*, 2019. <https://ceur-ws.org/Vol-2518/paper-WODHSA5.pdf>.
9. *OBO Semantic Engineering Training*. <https://oboacademy.github.io/obook/>. Accessed 12 Mar. 2025.



## Learning Objective 2

LO2: Explain the concept of linked data.


### Learning Activities

- **Lecture** (30mins): Introduce the topic of linked data (see Instructor Notes for more detailed contents).
- **Exercise** (30 mins): The learners should modify some queries on linked datasets or create their own queries (see "Instructor Notes" for more detailed information).


### Materials to Prepare

- Prepare a presentation on Linked Data.
- Prepare notes and practice live demo on how to search/query. Prepare information for the learners how they can execute and modify or create the queries.


### Instructor Notes

**Lecture:**

- The lecture should contain the following contents (see Resources 1&ndash;3):
    - basic concepts of linked data,
    - relevant standards and technologies (such as URI, HTTP, ...), and
    - relationship between ontologies and linked data.

**Exercise:**

- First, the instructor should demonstrate how to execute queries on linked data, e.g. with SPARQL (see Resource 4 for an example service that can be run in the browser).
- Then, the learners should modify or create their own queries (see the info box below for example queries).
- Depending on the level of the learners, they should either modify only existing queries or create queries on their own.

??? info "Example SPARQL queries"

    Use <https://dbpedia.org/sparql/> for executing the queries.

    Start with this simple query 
    
    ```
    SELECT ?writer, ?name WHERE{?writer a dbo:Writer. ?writer foaf:name ?name .} LIMIT 5
    ```

    and then make some modifications:

    - Add additional column that prints the birth date (`dbo:birthDate`) or a picture (`foaf:depiction`) of the person.
    - Instead of writers, search for actors.

    Or, use a more advanced query for battles of Spain in the middle age:

    ```
    SELECT ?event ?eventLabel (str(?date) AS ?formattedDate)
    WHERE {
    ?event a dbo:Event .
    ?event rdfs:label ?eventLabel .
    FILTER (LANG(?eventLabel) = 'en')
    ?event dbo:date ?date ;
    dbo:place <http://dbpedia.org/resource/Spain> .
    FILTER (?date >= "0500-01-01"^^xsd:dateTime && ?date <= "1500-01-01"^^xsd:dateTime) .
    }
    ORDER BY ASC(?date)
    ```

    Possible modifications:

    - Change the country to France.
    - Modify the date of the battles that should be displayed.

    For more advanced users, the instructor can only write the requirements in plain language and let the learners create the query from scratch.


### Resources

**Information for creating the presentation:**

1. data.europa.eu. Linking Data: What Does It Mean? 1 Aug. 2022. <https://data.europa.eu/en/publications/datastories/linking-data-what-does-it-mean>.
2. *W3C Wiki: Linked Data*. <https://www.w3.org/wiki/LinkedData>. Accessed 12 Mar. 2025.
3. Aguilar Gómez, Fernando. Introduction to Ontologies. Sept. 2024. GitHub, <https://skills4eosc-dscurriculum.github.io/Pilot-Training-Ontologies/latest/>.

**Services for conducting queries on ontologies in your browser:**

4. OpenLink Software. SPARQL Query Editor. <https://dbpedia.org/sparql/>. Accessed 12 Mar. 2025.



## Learning Objective 3

LO3: Apply ontologies to datasets.


### Learning Activities

- **Lecture** (10 mins): Introduce the exercises to be done by the learners (for example, show them how to search for terms and ontologies and introduce them to the sample dataset).
- **Exercise** (50 mins): Apply ontology terms to metadata from a dataset.


### Materials to Prepare

- Presentation slides as introduction to the exercise.
- Metadata from a dataset to be extended by the learner.

??? info "Sample Metadata"

    Use [https://bioportal.bioontology.org](https://bioportal.bioontology.org/) to search for the corresponding ontology terms.

    | Field             | Original Value     | Ontology Term (ID) |
    |-------------------|--------------------|--------------------|
    | Sample Type       | Lake water         | ENVO:04000007      |
    | Chemical          | Nitrate            | CHEBI:17632        |
    | Measurement Type  | Concentration      | PATO:0000033       |


### Instructor Notes

**Lecture:**

- This LO builds on the knowledge from LO1/LO2 and demonstrates the practical use case.
- The instructor should quickly introduce in the task to be done by the students.
- The instructor can use Resource 1 and 2 to prepare for this presentation.

**Exercise:**

- Create or find a dataset with metadata. If the metadata is not already linked to an ontology, then conduct this task.
- The learners get the dataset without the values from the ontology and should then find the relevant entries in the ontology and map the values to these terms.
- The services in Resources 3&ndash;7 can be used for finding ontologies.
- If a specialised software is available (and useful for the learners), then the exercise can be conducted using this software. Otherwise, this can be done manually e.g. using a spreadsheet software.
- If the audience is known, adapt the dataset and/or ontology to the domain of the learners.


### Resources

**Examples for an exercise:**

1. Aguilar Gómez, Fernando. Introduction to Ontologies. Sept. 2024. GitHub, <https://skills4eosc-dscurriculum.github.io/Pilot-Training-Ontologies/latest/>.
2. OBO Semantic Engineering Training: Getting Hands on with Ontologies. <https://oboacademy.github.io/obook/lesson/getting-hands-on/>. Accessed 12 Mar. 2025.

**Services for finding ontologies:**

3. TIB -- Leibniz Information Centre for Science and Technology and University Library. TIB Terminology Service. <https://terminology.tib.eu/ts/>. Accessed 12 Mar. 2025.
4. EMBL's European Bioinformatics Institute (EMBL-EBI). Ontology Lookup Service (OLS). <https://www.ebi.ac.uk/ols4/index>. Accessed 12 Mar. 2025.
5. Linked Open Vocabularies (LOV). <https://lov.linkeddata.es/dataset/lov/>. Accessed 12 Mar. 2025.
6. CLARIAH. Awesome Ontologies for Digital Humanities Awesome. 2019. <https://github.com/CLARIAH/awesome-humanities-ontologies>. Accessed 12 Mar. 2025.
7. ISTEX Le socle de la bibliothèque scientifique numérique nationale. Loterre (Linked Open Terminology Resources). <https://loterre.istex.fr/en/>. Accessed 12 Mar. 2025.
