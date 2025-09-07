import joblib

# Load your saved model
model = joblib.load("polynomial_regression_model.joblib")

# Example input: [age, exercise, bmi, bp, cholesterol]
sample = [45, 3, 26.5, 135, 220]

# Predict
prediction = model.predict([sample])

print("Input:", sample)
print("Predicted value:", prediction[0])
