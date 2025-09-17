from flask import Flask,render_template, request
import joblib
import os


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/heart_attack", methods=['GET', 'POST'])
def heart_attack():

    pre = None  # Initialize pre with a default value

    if request.method == 'POST':
        age = int(request.form.get('age',0))
        exercise= float(request.form.get('exercise',0))
        bmi = float(request.form.get('bmi',0))
        bp = float(request.form.get('bp',0))
        cholesterol = float(request.form.get('cholesterol',0))
        # print(age, exercise, bmi, bp,cholesterol)
       

    return render_template("heart.html",)


@app.route("/BMI", methods=['GET','POST'])
def BMI():
    bmi = None
    category=''
    if request.method == 'POST':
        weight = int(request.form.get('weight'))
        height =int(request.form.get('height'))

        height_m = height / 100
        bmi = weight /(height_m ** 2)
        bmi = round(bmi,2)
        # print(weight, height)
        
        if bmi < 18.5:
             category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
    
    return render_template('BMI.html', bmi = bmi , category = category)


# main 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT env var
    app.run(host="0.0.0.0", port=port, debug=True)