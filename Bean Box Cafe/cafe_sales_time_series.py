import pandas

data = {
    "date": pandas.date_range(start="2024-01-01", periods=30, freq="D"),
    "sales": [
        200, 220, 215, 230, 250, 245, 260, 270, 265, 280,
        300, 295, 310, 330, 325, 340, 360, 355, 370, 390,
        410, 405, 420, 440, 435, 450, 470, 465, 480, 500
    ]
}

df = pandas.DataFrame(data)





import pandas
import numpy 

# ==========================================
# Step 1 — Create the Daily Sales Dataset
# ==========================================
data = {
    "date": pandas.date_range(start="2024-01-01", periods=30, freq="D"),
    "sales": [
        200, 220, 215, 230, 250, 245, 260, 270, 265, 280,
        300, 295, 310, 330, 325, 340, 360, 355, 370, 390,
        410, 405, 420, 440, 435, 450, 470, 465, 480, 500
    ]
}

df = pandas.DataFrame(data)

# ==========================================
# Step 2 — Prepare the Time Series
# ==========================================
# Convert to datetime and set as index
df['date'] = pandas.to_datetime(df['date'])
df.set_index('date', inplace=True)
# Ensure data is sorted chronologically
df.sort_index(inplace=True)

# ==========================================
# Step 3 — Create Rolling Window Features
# ==========================================
# We shift by 1 to ensure we are using ONLY past data (t-1, t-2, t-3) 
# to predict the current day (t). This prevents data leakage.
df['rolling_mean_3'] = df['sales'].shift(1).rolling(window=3).mean()
df['rolling_std_3'] = df['sales'].shift(1).rolling(window=3).std()
df['rolling_max_3'] = df['sales'].shift(1).rolling(window=3).max()

# ==========================================
# Step 4 — Create Lag Features
# ==========================================
df['lag_1'] = df['sales'].shift(1)
df['lag_7'] = df['sales'].shift(7)

# ==========================================
# Step 5 — Build a Chronological Train-Test Split
# ==========================================
train_size = int(len(df) * 0.8)
train = df.iloc[:train_size]
test = df.iloc[train_size:].copy()

# ==========================================
# Step 6 — Compare Two Baseline Forecasts on the Test Data
# ==========================================
# Baseline 1: Naive Forecast (Yesterday's sales)
test['naive_forecast'] = test['lag_1']

# Baseline 2: Rolling Mean Forecast (Average of previous 3 days)
test['rolling_mean_forecast'] = test['rolling_mean_3']

# ==========================================
# Step 7 — Evaluate With MAPE
# ==========================================
def calculate_mape(actual, predicted):
    """Calculates Mean Absolute Percentage Error"""
    return numpy.mean(numpy.abs((actual - predicted) / actual)) * 100

mape_naive = calculate_mape(test['sales'], test['naive_forecast'])
mape_rolling = calculate_mape(test['sales'], test['rolling_mean_forecast'])

# ==========================================
# Step 8 — Print the Final Output
# ==========================================
print("--- FIRST 10 ROWS OF THE DATAFRAME ---")
print(df.head(10))
print("\n" + "="*50 + "\n")

print("--- DATE RANGES ---")
print(f"Train Date Range: {train.index.min().date()} to {train.index.max().date()}")
print(f"Test Date Range:  {test.index.min().date()} to {test.index.max().date()}")
print("\n" + "="*50 + "\n")

print("--- BASELINE EVALUATION (MAPE) ---")
print(f"Naive Forecast MAPE:        {mape_naive:.2f}%")
print(f"Rolling Mean Forecast MAPE: {mape_rolling:.2f}%")
print("\n" + "="*50 + "\n")

print("--- CONCLUSION ---")
if mape_naive < mape_rolling:
    print("The Naive Forecast performed better.")
else:
    print("The Rolling Mean Forecast performed better.")


