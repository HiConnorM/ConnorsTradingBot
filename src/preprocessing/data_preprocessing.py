import numpy as np
from sklearn.preprocessing import MinMaxScaler
from benzinga_news import fetch_and_analyze_sentiment



def load_data(filename):
   def load_data(ticker, ...):  # Existing parameters
    # Existing code ...

    # Fetch and analyze sentiment for the ticker
    sentiment_data = fetch_and_analyze_sentiment(ticker)
    # You can now integrate this sentiment_data into your dataframe or dataset

    pass

def normalize_data(data):
    scaler = MinMaxScaler(feature_range=(0, 1))
    normalized_data = scaler.fit_transform(data)
    return normalized_data, scaler

def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        seq = data[i:i + seq_length]
        X.append(seq[:-1])
        y.append(seq[-1])
    return np.array(X), np.array(y)

def train_val_split(X, y, train_size=0.9):
    split = int(train_size * len(X))
    X_train = X[:split]
    y_train = y[:split]
    X_val = X[split:]
    y_val = y[split:]
    return X_train, y_train, X_val, y_val

