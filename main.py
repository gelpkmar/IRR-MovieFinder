import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
movies = pd.read_csv('../movie_dataset/items.csv')
ratings = pd.read_csv('../movie_dataset/u.ratings.csv')
users = pd.read_csv('../movie_dataset/u.user.csv')

def clean_movies_date():
    movies['release date'] = pd.to_datetime(movies['release date'], format='%d-%b-%y')
    movies['year'] = movies['release date'].dt.strftime('%y')

clean_movies_date()

# Query 1: Action movies involving robberies and detective work
def query_1(movies):
    # Filter action movies
    action_movies = movies[movies['Action'] == 1]

    # Extract summaries containing "robberies" or "detective"
    keywords = ["robbery", "robberies", "detective"]
    filtered_movies = action_movies[action_movies['Summary'].str.contains('|'.join(keywords), case=False, na=False)]

    # Select top 10 movies
    return filtered_movies.head(10)['movie_title'].tolist()

# Query 2: Old movies for a family get-together
def query_2(movies):
    # Filter for children's or family genres
    family_movies = movies[(movies["Children's"] == 1) | (movies["Comedy"] == 1) | (movies["Musical"] == 1)]

    # Filter for older movies (released before 2000)
    old_family_movies = family_movies[family_movies['release date'].dt.year < 2000]

    # Select top 10 movies
    return old_family_movies.head(10)['movie_title'].tolist()

# Query 3: Popular movies by specific directors, excluding war movies
def query_3(movies):
    directors = ["Alfred Hitchcock", "Martin Scorsese", "Woody Allen", "Steven Spielberg"]
    filtered_movies = movies[movies['Director'].isin(directors)]

    # Exclude war movies
    non_war_movies = filtered_movies[filtered_movies["War"] == 0]

    # Sort by popularity (assuming 'popularity' is a column in the dataset)
    popular_non_war_movies = non_war_movies.sort_values(by='Rating', ascending=False)

    # Select top 10 movies
    return popular_non_war_movies.head(10)['movie_title'].tolist()

# Query 4: Movies similar to "Star Wars (1977)"
def query_4(movies):
    # Vectorize the summaries
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['Summary'].fillna(''))

    # Compute cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Get the index of "Star Wars (1977)"
    idx = movies[movies['movie_title'] == "Star Wars (1977)"].index[0]

    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Select top 10 similar movies
    similar_movies_indices = [i[0] for i in sim_scores[1:11]]
    return movies.iloc[similar_movies_indices]['movie_title'].tolist()

# Query 5: Movies similar to a given list of movies
def query_5(movies):
    liked_movies = ["Devil's Own, The (1997)", "Cable Guy, The (1996)", "Usual Suspects, The (1995)", "Godfather, The (1972)", "Young Frankenstein (1974)"]
    liked_indices = movies[movies['movie_title'].isin(liked_movies)].index

    # Aggregate similarity scores
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['Summary'].fillna(''))
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    sim_scores = cosine_sim[liked_indices].mean(axis=0)
    sim_scores = list(enumerate(sim_scores))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Select top 10 similar movies
    similar_movies_indices = [i[0] for i in sim_scores if i[0] not in liked_indices]
    return movies.iloc[similar_movies_indices]['movie_title'].tolist()[:10]

# Query 6: Movies about science, history, and the future for a young student
def query_6(movies):
    keywords = ["science", "history", "future"]
    filtered_movies = movies[movies['Summary'].fillna('').str.contains('|'.join(keywords), case=False, na=False)]

    # Select top 10 movies
    return filtered_movies.head(10)['movie_title'].tolist()

# Execute all queries
query_1_results = query_1(movies)
query_2_results = query_2(movies)
query_3_results = query_3(movies)
query_4_results = query_4(movies)
query_5_results = query_5(movies)
query_6_results = query_6(movies)

# Save results to .txt files
queries = [query_1_results, query_2_results, query_3_results, query_4_results, query_5_results, query_6_results]
for i, result in enumerate(queries, 1):
    with open(f'query_{i}.txt', 'w') as f:
        for movie in result:
            f.write("%s\n" % movie)
