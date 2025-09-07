from flask import Flask,render_template, request
import joblib
model = joblib.load('polynomial_regression_model.joblib')

def heart_predict(demo):
    prediction = model.predict([demo])
    return prediction

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():

    pre = None  # Initialize pre with a default value

    if request.method == 'POST':
        age = int(request.form.get('age',0))
        exercise= float(request.form.get('exercise',0))
        bmi = float(request.form.get('bmi',0))
        bp = float(request.form.get('bp',0))
        cholesterol = float(request.form.get('cholesterol',0))
        print(age, exercise, bmi, bp,cholesterol)
        pre = heart_predict([age,exercise,bmi,bp,cholesterol])

    return render_template("index.html", pre = pre)


app.run(debug=True)