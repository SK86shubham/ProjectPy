import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("sleep_quality_smartphone_usage.csv")


# Step 2: Select features and target
features = ["screen_time_min", "blue_light_exposure_min", "sleep_duration_hr", "bedtime_24h"]
target = "sleep_quality_1_5"



X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)


y_pred = model.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))


user_input = {
    "screen_time_min": 80,
    "blue_light_exposure_min": 5,
    "sleep_duration_hr": 8.5,
    "bedtime_24h": 20.0
}
user_df = pd.DataFrame([user_input])
user_scaled = scaler.transform(user_df)




# Step 8: Predict sleep quality for user input
predicted_quality = model.predict(user_scaled)[0]
print(f"Predicted Sleep Quality (1-5): {predicted_quality}")