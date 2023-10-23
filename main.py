import yfinance as yf
import pandas as pd
from preprocessing.data_preprocessing import load_data, normalize_data, create_sequences, train_val_split
from models.lstm_model import build_lstm_model, train_model


# Fetch Apple's stock data
apple_data = yf.download('AAPL', start='2010-01-01', end='2023-01-01')


# Load and preprocess data
data = load_data('data/raw_data/apple_stock_data.csv')
normalized_data, scaler = normalize_data(data)
X, y = create_sequences(normalized_data, seq_length=60)
X_train, y_train, X_val, y_val = train_val_split(X, y)

# Build and train the LSTM model
model = build_lstm_model(input_shape=(X_train.shape[1], X_train.shape[2]))
history = train_model(model, X_train, y_train, X_val, y_val)

# Save the trained model
model.save('data/models/lstm_model.h5')
