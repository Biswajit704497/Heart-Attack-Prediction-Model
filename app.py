from flask import Flask,render_template, request
import os
from bmi_calculate import BMI_def
from heart_model import heart_def


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/heart_attack", methods=['GET', 'POST'])
def heart_attack():

    result = None  

    if request.method == 'POST':
        age = int(request.form.get('age',0))
        gender = int(request.form.get('gender',0))
        cholesterol = int(request.form.get('cholesterol',0))
        highBloodPressure = int (request.form.get('highBloodPressure',0))
        lowBloodPressure = int (request.form.get('lowBloodPressure',0))
        heartRate = int (request.form.get('heartRate',0))
        diabetes = int (request.form.get('diabetes',0))
        familyHistory = int (request.form.get('familyHistory',0))
        smoking = int (request.form.get('smoking',0))
        alcoholConsumption = int (request.form.get('alcoholConsumption',0))
        exerciseHours = int (request.form.get('exerciseHours',0))
        diet = int (request.form.get('diet',0))
        previousHeartProblems = int (request.form.get('previousHeartProblems',0))
        medicationUse = int (request.form.get('medicationUse',0))
        stressLevel = int (request.form.get('stressLevel',0))
        bmi=float(request.form.get('bmi',0))
        physicalActivityDays = int (request.form.get('physicalActivityDays',0))
        sleepHours = int (request.form.get('sleepHours',0))

        
        heart_rate_data_list =[[age,gender, cholesterol,highBloodPressure,lowBloodPressure,heartRate,diabetes,familyHistory,smoking,alcoholConsumption,
            exerciseHours,diet,previousHeartProblems,medicationUse,stressLevel,bmi,physicalActivityDays,sleepHours]]
        # print(dict(request.form))
        result = heart_def(heart_rate_data_list)
        
       

    return render_template("heart.html",result = result)


@app.route("/BMI", methods=['GET','POST'])
def BMI():
    person_bmi=[]
    if request.method == 'POST':
        weight = int(request.form.get('weight'))
        height =int(request.form.get('height'))
        person_bmi = BMI_def(height, weight)

           
    return render_template('BMI.html', person_bmi = person_bmi)


# main 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT env var
    app.run(host="0.0.0.0", port=port, debug=True)