import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_data(filename):
    # Load your data from CSV or any other format
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

