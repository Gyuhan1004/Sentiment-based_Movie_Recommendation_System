def filter_by_genre(df, genre):
    """Filter movies by genre."""
    return df[df['genres_list'].str.contains(genre, na=False)]

def filter_by_rating(df, min_rating, max_rating):
    """Filter movies by rating range."""
    return df[(df['vote_average'] >= min_rating) & (df['vote_average'] <= max_rating)]

# src/utils.py

def apply_user_preferences(df):
    print("\n✨ Set Your Preferences (Press Enter to skip any)")

    genre = input("Preferred genre (e.g. Action, Drama, Comedy): ").strip().lower()
    min_rating = input("Minimum IMDb rating (0-10): ").strip()
    min_sentiment = input("Minimum sentiment score (0-1): ").strip()
    language = input("Preferred language (e.g. en, hi): ").strip().lower()
    min_runtime = input("Minimum runtime in minutes: ").strip()
    max_runtime = input("Maximum runtime in minutes: ").strip()
    release_year = input("Release year (e.g. 2020): ").strip()

    filtered_df = df.copy()

    if genre:
        filtered_df = filtered_df[filtered_df['genres_list'].str.lower().str.contains(genre)]
    if min_rating:
        try:
            filtered_df = filtered_df[filtered_df['vote_average'] >= float(min_rating)]
        except:
            pass
    if min_sentiment:
        try:
            filtered_df = filtered_df[filtered_df['sentiment_score'] >= float(min_sentiment)]
        except:
            pass
    if language:
        filtered_df = filtered_df[filtered_df['original_language'] == language]
    if min_runtime:
        try:
            filtered_df = filtered_df[filtered_df['runtime'] >= int(min_runtime)]
        except:
            pass
    if max_runtime:
        try:
            filtered_df = filtered_df[filtered_df['runtime'] <= int(max_runtime)]
        except:
            pass
    if release_year:
        try:
            filtered_df = filtered_df[filtered_df['release_year'] == int(release_year)]
        except:
            pass

    # Sort by topsis_score again
    return filtered_df.sort_values(by='topsis_score', ascending=False).head(15)
