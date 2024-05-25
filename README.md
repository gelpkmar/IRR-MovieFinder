# IRR Assignment03 - Finding Relevant Movie

|| |
|-----------|--------------|
|**Author:**| Marlon Gelpke|
|**Matriculation Number:**|15-532-849|
|**Date of Submission:**| 25.05.2024|

The submission to this project contains the following files:
```
.
└── IRR_assignment01_Marlon_Gelpke
    ├── code.zip
    ├── query_results/
    │   ├── query_01.csv
    │   ├── query_02.csv
    │   ├── query_03.csv
    │   ├── query_04.csv
    │   ├── query_05.csv
    │   ├── query_06.csv
    └── IRR_assignment03_approach.pdf
````

>The submission contains `query_0x.txt` files per query requested (1-6). These files were produced using the data provided by the teaching team.

## 1. Introduction
This document describes the approach and setup of the Movie Recommender System that was developed in scope of assignment 03 of the University of Zurich Computer Science course "Introduction to Retrieval and Recommendation".

The following materials were supplied to us:
- 5 documents in .csv format providing information about movies, users and users' ratings of movies.
- items.csv: Detailed information on movies incl. link to IMDB database and movie summary, cast, etc.

The goal was to create a system that will reliably answer the following queries:
1. I like to watch action movies that involve robberies and detective work. Tell me what I can
watch.
2. I want recommendation of old movies that I can watch during a family get together.
3. I want to watch the most popular movies by Alfred Hitchcock, Martin Scorsese, Woody Allen,
or Steven Spielberg. I do not like to watch movies about wars. Tell me what could be relevant
for me.
4. I liked the movie “Star Wars (1977)”. Show me similar ones.
5. I liked the movies “The Devil’s Own”, “The Cable Guy”, “The Usual Suspects”, “The Godfather”,
and “Young Frankenstein”. Show me similar ones.
6. I’m a young student. I like watching movies about science, history, and future, with as many
different topics as possible. Tell me what I can watch.

## 2. Approach
The below describes the technical approach and outlines the design decisions taken to solve this project.

### 2.1 Technical Implementation
The technical execution of this project relies heavily on the following third party libraries:
- scikit-learn - TFIDF vectorization, cosine similarity, score normalization
- pandas - reading of the `.csv` files
- json - writing and reading of the inverse document index
- NLTK - all natural language processing (e.g., tokenization, lemmatization, calculation of similarity, etc.)

The project is spread over two different Python files. A quick overview and explanation of the different files:
- `main.py`: Main execution of the program.
- `offline_preprocessing.py`: Script used to run the preprocessing functions to generate the input data required for the individual recommendation methods.

#### 2.1.1 Preprocessing and preparation
>Code to be found in `offline_preprocessing.py`

The largest part of the offline preprocessing is the harmonization of the data files to use common delimeters and to add the respective headers describing the column names as indicated in the README file. The result are three files with `.csv` suffix containing user information, movie item information and information on individual movie ratings.

>In this particular project, the common delimeter ";" was chosen for the output files. This was done as a work around to avoid the fact that some URL's contain commas within them.

#### 2.1.2 Creation of the movie recommendations
>Code to be found in `main.py`

The provided code is a Python prototype script designed to address a movie recommendation task based on user preferences and specifications outlined in the exercise. The objective is to recommend relevant movies for different user profiles by leveraging information about users (age, gender, occupation) and movie items (genre, summary, visual features).

To accomplish this task, the code utilizes the pandas library to load and manipulate datasets, and scikit-learn for text vectorization and similarity computation. Let's break down how each query function in the code aligns with the exercise requirements:

- Action Movies Involving Robberies and Detective Work (Query 1):
    - This query filters action movies from the dataset and then further refines the selection to include those with summaries containing keywords related to robberies and detective work.

- Old Movies for Family Get-Together (Query 2):
    - Here, the code identifies older movies suitable for family gatherings by filtering for children's or family genres and movies released before the year 2000.

- Popular Movies by Specific Directors, Excluding War Movies (Query 3):
    - This query selects popular movies directed by specific directors (Alfred Hitchcock, Martin Scorsese, Woody Allen, Steven Spielberg) while excluding those categorized as war movies.

- Movies Similar to "Star Wars (1977)" (Query 4):
    - Using cosine similarity based on TF-IDF vectorization of movie summaries, this query finds movies similar to "Star Wars (1977)".

- Movies Similar to a Given List of Movies (Query 5):
    - For users who liked specific movies, this query computes the average similarity scores between the liked movies and all other movies in the dataset, recommending similar ones.

- Movies about Science, History, and the Future for a Young Student (Query 6):
    - Targeting young students interested in science, history, and the future, this query identifies movies containing relevant keywords in their summaries.

Each query function returns a list of 10 relevant movies based on the specified criteria. Finally, the script saves the results of each query to separate text files.

In summary, the provided code implements a movie recommendation system tailored to diverse user preferences and specifications, ranging from genre preferences to specific movie preferences and demographic considerations. By leveraging text analysis and similarity computation techniques, it aims to provide personalized and relevant movie recommendations for various user profiles.

## 3. Conclusion
In context of this assignment, the provided code serves as a prototype for a movie recommendation system catering to specific user preferences and specifications. While it demonstrates the capability to generate recommendations for predefined queries, there exists substantial room for improvement to enhance the system's effectiveness in handling custom requests beyond the six queries requested in this exercise. To achieve this, an advanced recommendation pipeline integrating various techniques in retrieval, recommendation, natural language processing (NLP), similarity calculations, and AI models is proposed.

Pipeline for Improving the Movie Recommendation System:

1. **Data Enrichment and Feature Engineering**:
   - Incorporate additional metadata such as user demographics, movie tags and user reviews to enrich the dataset.
   - Utilize advanced feature engineering techniques to extract meaningful representations from visual features (e.g., movie trailers).

2. **Advanced NLP Preprocessing**:
   - Implement advanced NLP preprocessing techniques such as sentiment analysis to extract deeper insights from textual data.

3. **Personalized User Profiling**:
   - Develop user profiling mechanisms leveraging collaborative filtering, content-based filtering, and hybrid approaches to capture individual preferences and behavior patterns.
   - Incorporate contextual information such as user context (e.g., time of day, location).

4. **Enhanced Similarity Computation**:
   - Explore similarity metrics beyond cosine similarity, such as Jaccard similarity, BM25, or embedding-based metrics, to capture diverse aspects of movie similarity.
   - Utilize semantic similarity measures to account for latent relationships between movies based on their semantic meaning.

5. **Deep Learning Models for Recommendation**:
   - Integrate deep learning functionalities to model complex user-item interactions and capture long-term dependencies.

6. **Real-Time Query Handling and Adaptation (for more advanced applications beyond this class)**:
   - Implement a real-time recommendation engine capable of processing ad-hoc user queries in a scalable and efficient manner.
   - Utilize reinforcement learning or bandit algorithms to optimize recommendation policies and adapt to evolving user preferences over time.

7. **Evaluation and Model Fine-Tuning**:
   - Conduct comprehensive evaluation experiments using metrics such as precision, recall, and F1-score to assess the performance of the recommendation system.

By following this step-by-step pipeline and incorporating advanced techniques in retrieval, recommendation, NLP, similarity calculations, and AI models, the movie recommendation system can evolve into a robust system capable of handling diverse user requests and delivering highly personalized movie recommendations.