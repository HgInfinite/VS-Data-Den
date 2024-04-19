# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


# %%
data = pd.read_parquet('sales_historic_1.parquet')

# %%
data['DATE_FIELD'] = pd.to_datetime(data['DATE_FIELD'])
data['YEARWEEK'] = data['DATE_FIELD'].dt.strftime('%Y-%U')

# %%
agg_data = data.groupby(['CHOICE_ID', 'YEARWEEK']).agg({
    'SALES': 'sum',
    'UNITS': 'sum'
}).reset_index()


# %%
features = ['SALES'] 

# %%
train_data, test_data = train_test_split(agg_data, test_size=0.2, random_state=42)


# %%
scaler = MinMaxScaler()
train_scaled = scaler.fit_transform(train_data[features])
test_scaled = scaler.transform(test_data[features])

# %%
def create_sequences(data, sequence_length):
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i+sequence_length])
        y.append(data[i+sequence_length])
    return np.array(X), np.array(y)

# %%
sequence_length = 10  #
X_train, y_train = create_sequences(train_scaled, sequence_length)
X_test, y_test = create_sequences(test_scaled, sequence_length)

# %%
model = Sequential([
    LSTM(64, input_shape=(X_train.shape[1], X_train.shape[2]), return_sequences=True),
    LSTM(64),
    Dense(2)  
])

# %%

model.compile(optimizer='adam', loss='mse')

# %%
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.1)

# %%
loss = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss}')


# %%
agg_data

# %%
def predict_demand(trend_start, trend_end):
    trend_data = agg_data[(agg_data['YEARWEEK'] >= trend_start) & (agg_data['YEARWEEK'] <= trend_end)]
    scaled_trend_data = scaler.transform(trend_data[features])
    X_trend, _ = create_sequences(scaled_trend_data, sequence_length)
    predictions = model.predict(X_trend)
    predictions = scaler.inverse_transform(predictions)
    return predictions

# %%
trend_start = '2024-01-01'
trend_end = '2024-12-31'  
predictions = predict_demand(trend_start, trend_end)
print(predictions)

# %%



