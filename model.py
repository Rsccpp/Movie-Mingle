import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load and preprocess data
def load_data(path='movies_metadata.csv'):
    df = pd.read_csv(path, low_memory=False)
    df = df[['title', 'overview']].dropna()
    df = df[~df['title'].duplicated()]
    return df

# Build the model
def create_model():
    df = load_data()
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['overview'])

    model = NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(tfidf_matrix)

    return df, tfidf, tfidf_matrix, model

# Recommend similar movies
def get_recommendations(title, num_recommendations=5):
    df, tfidf, tfidf_matrix, model = create_model()
    if title not in df['title'].values:
        return ["Movie not found. Please try another one."]

    idx = df[df['title'] == title].index[0]
    movie_vector = tfidf_matrix[idx]

    distances, indices = model.kneighbors(movie_vector, n_neighbors=num_recommendations + 1)

    rec_indices = indices.flatten()[1:]  # Skip the movie itself
    recommendations = df['title'].iloc[rec_indices].tolist()
    return recommendations

