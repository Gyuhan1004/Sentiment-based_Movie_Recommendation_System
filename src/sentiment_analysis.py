from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(df):
    """Analyze sentiment of movie overviews and add sentiment scores."""
    analyzer = SentimentIntensityAnalyzer()
    df['sentiment_score'] = df['overview'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
    return df
