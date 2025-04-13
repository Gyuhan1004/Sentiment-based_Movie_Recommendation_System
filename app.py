import streamlit as st
import pandas as pd
import os
import re
from src.data_preprocessing import load_data, preprocess_data
from src.sentiment_analysis import analyze_sentiment
from src.recommendation import create_score, get_top_recommendations, get_recommendations_by_preferences

# Set page config
st.set_page_config(page_title="🎬 Movie Recommendation App", layout="wide")

st.title("🎥 Smart Movie Recommender System")
st.markdown("##### Discover top-rated movies based on sentiment and smart scoring (TOPSIS)!")

# 🔁 Cache-heavy pipeline to prevent repeated processing
@st.cache_data
def load_and_prepare_data():
    print("🔄 Loading and processing data...")
    data_path = os.path.join("data", "imdb_tmdb_dataset.csv")
    df = load_data(data_path)
    df = preprocess_data(df)
    df = analyze_sentiment(df)
    df = create_score(df)
    return df

# Run once, cache result
df = load_and_prepare_data()

# Show Top 15 Recommendations
st.subheader("🔥 Top 15 Recommended Movies")
top_15 = get_top_recommendations(df, top_n=15)
st.dataframe(top_15.reset_index(drop=True), use_container_width=True)

# Prepare for next step (User Preferences)
st.markdown("---")
st.subheader("🎯 Want Personalized Picks?")
st.markdown("Tell us what you're into. We'll recommend movies that match your preferences!")

genre_input = st.text_input("Enter preferred genre (e.g., Action, Comedy, Thriller):")
language_input = st.text_input("Preferred language (e.g., en, hi, fr):")
min_rating = st.slider("Minimum IMDb Rating:", 1.0, 10.0, 6.0)

if st.button("🔍 Show Refined Recommendations"):
    @st.cache_data
    def get_filtered_recommendations(df, genre, language, min_rating, top_n=15):
        print("🎯 Filtering recommendations by user preferences...")
        return get_recommendations_by_preferences(
            df,
            genre=genre,
            language=language,
            min_rating=min_rating,
            top_n=top_n
        )

    filtered = get_filtered_recommendations(df, genre_input, language_input, min_rating, top_n=15)
    if not filtered.empty:
        st.success("🎯 Refined Recommendations Based on Your Preferences:")
        st.dataframe(filtered.reset_index(drop=True), use_container_width=True)
    else:
        st.warning("No movies found with your preferences. Try changing the filters!")

# --- Emotion-Aware Recommendations ---
st.markdown("---")
st.subheader("🧠 Emotion-Aware Recommendations")
mood = st.selectbox("What’s your mood today?", ["", "Happy", "Sad", "Adventurous", "Tense", "Romantic"])

mood_genre_map = {
    "Happy": ["Comedy", "Family", "Animation"],
    "Sad": ["Drama", "Romance"],
    "Adventurous": ["Action", "Adventure", "Fantasy"],
    "Tense": ["Thriller", "Mystery", "Crime"],
    "Romantic": ["Romance", "Drama"]
}

if mood:
    st.info(f"🎬 Finding movies to match your **{mood}** mood...")
    matched_genres = mood_genre_map.get(mood, [])
    mood_matches = df[
        df['genres_list'].apply(lambda g: any(genre in g for genre in matched_genres)) &
        ((df['overview_sentiment'] > 0.1) if mood == "Happy" else (df['overview_sentiment'] < 0.1))
    ]
    mood_top = mood_matches.sort_values(by="topsis_score", ascending=False).head(15)
    if not mood_top.empty:
        st.success("🌟 Here are some mood-matching movies:")
        st.dataframe(mood_top[["title", "genres_list", "overview_sentiment", "topsis_score"]].reset_index(drop=True), use_container_width=True)
    else:
        st.warning("No matching movies found for your mood. Try another mood?")

# --- Chat-style Natural Language Interface ---
st.markdown("---")
st.subheader("💬 Chat with the Recommender")
chat_input = st.text_input("Type your request (e.g., 'I want a romantic thriller with strong female leads'):")

def extract_preferences(text):
    text = text.lower()
    genre_keywords = ['action', 'comedy', 'drama', 'thriller', 'romance', 'horror', 'adventure', 'animation', 'fantasy', 'crime']
    matched_genres = [genre for genre in genre_keywords if genre in text]
    min_rating_match = re.search(r'rating\s*(\d+(\.\d+)?)', text)
    min_rating = float(min_rating_match.group(1)) if min_rating_match else 6.0
    return {
        "genre": matched_genres[0] if matched_genres else None,
        "min_rating": min_rating
    }

if chat_input:
    st.info(f"🧠 Interpreting your request: \"{chat_input}\"")
    prefs = extract_preferences(chat_input)
    filtered = df.copy()
    if prefs['genre']:
        filtered = filtered[filtered['genres_list'].str.contains(prefs['genre'], case=False, na=False)]
    if prefs['min_rating']:
        filtered = filtered[filtered['vote_average'] >= prefs['min_rating']]
    results = filtered.sort_values(by='topsis_score', ascending=False).head(15)
    if not results.empty:
        st.success("🤖 Here are your personalized movie picks:")
        st.dataframe(results[["title", "genres_list", "vote_average", "topsis_score"]].reset_index(drop=True), use_container_width=True)
    else:
        st.warning("No movies found. Try rephrasing or adding more details.")
