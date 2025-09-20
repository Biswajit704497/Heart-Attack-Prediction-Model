from flask import Flask,render_template, request
import os
from bmi_calculate import BMI


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
        person_bmi = BMI(height, weight)

        
    
    return render_template('BMI.html', person_bmi = person_bmi)


# main 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT env var
    app.run(host="0.0.0.0", port=port, debug=True)