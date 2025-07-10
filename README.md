💤 [Sleep Quality Prediction Using Smartphone 🔗]([https://colab.research.google.com/drive/1wsHDEYnpsCOGtLHOs1vG8g_MbxCbgTX-#scrollTo=Je8a8WuYermZ])



📌 Project Overview
This project aims to predict a person's sleep quality (scale: 1–5) based on their smartphone usage behavior before bedtime. It explores how screen time, blue light exposure, and bedtime habits impact sleep and uses machine learning to make accurate predictions.

🎯 Objective
To analyze smartphone usage data and build a machine learning model that can classify sleep quality using features like:

Screen time before sleep

Blue light exposure duration

Sleep duration

Bedtime (24-hour format)

🧠 Problem Statement
With increasing dependence on smartphones, especially at night, sleep quality is being affected. This project identifies patterns in usage that influence sleep and leverages these insights to make predictions that can help promote healthier digital habits.

🧰 Tech Stack
Category	Tools/Tech
Language	Python
Libraries	Pandas, Scikit-learn
Algorithms	Logistic Regression, Random Forest (initial test)
Evaluation	5-Fold Cross Validation
Preprocessing	StandardScaler

📊 Dataset
A synthetic dataset was created with the following columns:

screen_time_min: Total screen time before sleep (in minutes)

blue_light_exposure_min: Time exposed to blue light

sleep_duration_hr: Total sleep duration in hours

bedtime_24h: Bedtime in 24-hour format

sleep_quality_1_5: Target variable (1 = poor sleep, 5 = excellent sleep)

🛠️ Methodology
Data Preparation

Handled missing values and selected relevant features.

Feature Scaling

Used StandardScaler to normalize features.

Model Selection & Training

Compared Random Forest and Logistic Regression.

Final model: Logistic Regression (simpler and better for small datasets).

Model Evaluation

Applied 5-Fold Cross Validation to assess model performance.

✅ Results
Model	Accuracy
Random Forest	49.9%
Logistic Regression	62.5% ✅

Logistic Regression outperformed Random Forest on the dataset due to its simplicity and effectiveness on structured, small-scale data.

🔮 Future Improvements
Collect real-world data via tracking apps or surveys.

Add more features like caffeine intake, stress level, physical activity.

Try advanced models: Decision Trees, XGBoost, or Deep Learning.

