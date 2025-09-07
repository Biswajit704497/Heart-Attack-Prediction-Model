from flask import Flask,render_template, request
import joblib
model = joblib.load('polynomial_regression_model.joblib')

def heart_predict(demo):
    pre = model.predict([demo])
    return pre

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():

    if request.method == 'POST':
        age = int(request.form.get('age'))
        exercise= float(request.form.get('exercise'))
        bmi = float(request.form.get('bmi'))
        bp = float(request.form.get('bp'))
        cholesterol = float(request.form.get('cholesterol'))
        print(age, exercise, bmi, bp,cholesterol)
        pre = heart_predict([age,exercise,bmi,bp,cholesterol])

    return render_template("index.html", pre = pre)


app.run(debug=True)