# data_preprocessing.py

import pandas as pd

def load_data(filepath):
    print(f"🔄 Loading data from {filepath}...")
    return pd.read_csv(filepath)

def preprocess_data(df):
    print("🧹 Preprocessing data...")

    # Drop rows with missing essential info
    df.dropna(subset=['title', 'overview', 'vote_average', 'vote_count'], inplace=True)

    # Remove duplicates
    df.drop_duplicates(subset=['title'], inplace=True)

    # Remove pornographic content using keyword-based filtering
    porn_keywords = [
        'porn', 'xxx', 'erotic', 'adult film', 'softcore', 'hardcore', 'explicit', 'fetish', 'sex tape',
        'stripper', 'sensual', 'bdsm', 'orgy', 'incest', 'hentai', 'camgirl'
    ]

    def is_pornographic(text):
        """Checks if the text contains any pornographic keyword"""
        if pd.isna(text): return False
        text = str(text).lower()
        return any(keyword in text for keyword in porn_keywords)

    # Apply the filter to title, overview, and keywords
    df = df[~df['overview'].apply(is_pornographic)]
    df = df[~df['keywords'].apply(is_pornographic)]
    df = df[~df['title'].apply(is_pornographic)]

    print(f"✅ Dataset cleaned. Remaining movies: {len(df)}")
    return df
