import requests
from config import BENZINGA_API_KEY
from sentiment_analysis import analyze_sentiment

def fetch_and_analyze_sentiment(ticker, count=5):
    """
    Fetch the latest news for a specific ticker from Benzinga and analyze their sentiment.
    Returns a list of dictionaries containing the title, content, and sentiment of each article.
    """
    news_data = fetch_benzinga_news(ticker, count)
    
    analyzed_data = []
    for article in news_data:
        sentiment = analyze_sentiment(article['description'])  # Analyzing sentiment of the article's description
        analyzed_data.append({
            'title': article['title'],
            'content': article['description'],
            'sentiment': sentiment
        })
        
    return analyzed_data
