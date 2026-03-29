import pandas as pd
from pathlib import Path

def process_ratings():
    df = pd.read_csv('data/raw/ratings.csv')

    # remove duplicates
    df = df.drop_duplicates(subset=['user_id', 'movie_id'])

    Path('data/processed').mkdir(parents=True, exist_ok=True)

    df.to_csv('data/processed/ratings_clean.csv', index=False)

    print("Processed ratings:", len(df))

if __name__ == "__main__":
    process_ratings()