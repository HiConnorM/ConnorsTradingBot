from preprocessing.data_preprocessing import load_stock_data, normalize_data, create_sequences, train_val_split
from models.lstm_model import create_lstm_model, train_model

# Parameters
ticker = 'AAPL'
start_date = '2010-01-01'
end_date = '2023-01-01'
seq_length = 60

# Load and preprocess data
stock_data = load_stock_data(ticker, start_date, end_date)
normalized_data, scaler = normalize_data(stock_data)
X, y = create_sequences(normalized_data, seq_length)
X_train, y_train, X_val, y_val = train_val_split(X, y)

# Build and train the LSTM model
model = create_lstm_model(input_shape=(X_train.shape[1], X_train.shape[2]))
history = train_model(model, X_train, y_train, X_val, y_val)

# Save the trained model
model.save('data/models/lstm_model.h5')

