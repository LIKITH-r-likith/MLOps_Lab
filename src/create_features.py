import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_features():
    df = pd.read_csv('data/processed/ratings_clean.csv')

    matrix = df.pivot_table(index='user_id', columns='movie_id', values='rating', fill_value=0)

    similarity = cosine_similarity(matrix)

    joblib.dump(similarity, 'models/user_similarity.pkl')

    print("Features created")

if __name__ == "__main__":
    create_features()