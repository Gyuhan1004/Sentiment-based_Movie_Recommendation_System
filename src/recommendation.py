import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Function to calculate the TOPSIS score for movie recommendations
def create_score(df):
    print("🎯 Applying TOPSIS for scoring...")
    
    # Select features for TOPSIS
    features = df[['vote_average', 'vote_count', 'sentiment_score']].copy()
    scaler = MinMaxScaler()
    norm_features = scaler.fit_transform(features)

    # Define weights: vote_average (0.4), vote_count (0.3), sentiment_score (0.3)
    weights = np.array([0.4, 0.3, 0.3])

    # Ideal best & worst
    ideal_best = np.max(norm_features, axis=0)
    ideal_worst = np.min(norm_features, axis=0)

    # Euclidean distances
    distance_best = np.linalg.norm(norm_features - ideal_best, axis=1)
    distance_worst = np.linalg.norm(norm_features - ideal_worst, axis=1)

    # TOPSIS score
    topsis_score = distance_worst / (distance_best + distance_worst)
    df['topsis_score'] = topsis_score

    # Sort by TOPSIS score in descending order
    df = df.sort_values(by='topsis_score', ascending=False)
    return df

# Function to get the top N recommendations based on TOPSIS score
def get_top_recommendations(df, top_n=10):
    print(f"📢 Top {top_n} movie recommendations:")
    return df[['title', 'vote_average', 'vote_count', 'sentiment_score', 'topsis_score']].head(top_n)

# Function to filter recommendations based on user preferences
def get_recommendations_by_preferences(df, genre=None, language=None, min_rating=None, top_n=15):
    print("🎯 Filtering recommendations by user preferences...")

    if genre:
        df = df[df['genres_list'].str.contains(genre, case=False, na=False)]

    if language:
        df = df[df['original_language'].str.lower() == language.lower()]

    if min_rating:
        df = df[df['vote_average'] >= min_rating]

    df = df.sort_values(by="topsis_score", ascending=False)

    return df[['title', 'vote_average', 'vote_count', 'sentiment_score', 'topsis_score']].head(top_n)
