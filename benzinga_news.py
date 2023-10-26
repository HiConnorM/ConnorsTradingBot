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


def fetch_benzinga_news(ticker, count=5):
    """
    Fetch the latest news for a specific ticker from Benzinga.
    Returns a list of dictionaries containing the title and description of each article.
    """
    # Define the endpoint URL, headers, and any other necessary information
    url = "https://api.benzinga.com/api/v2"
    headers = {
        "Authorization": f"Bearer {BENZINGA_API_KEY}"
    }
    params = {
        "ticker": ticker,
        "count": count
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from Benzinga: {response.text}")

    news_data = response.json()  # Assuming Benzinga returns data in JSON format

    return news_data
