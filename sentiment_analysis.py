from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of a given text.
    Returns a tuple (polarity, subjectivity).
    Polarity is a float [-1.0, 1.0] where -1 means negative sentiment and 1 means positive sentiment.
    Subjectivity is a float [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
    """
    analysis = TextBlob(text)
    return analysis.sentiment.polarity, analysis.sentiment.subjectivity
