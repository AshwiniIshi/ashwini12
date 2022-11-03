
from flask import Flask, jsonify, render_template, request
from models.utils import MedicalInsurance
import config

################ Create API ############

app = Flask(__name__) # Create Instance

############ Home API ##########

@app.route('/')
def flask():
    print("Welcome to Medicle Insurance Charges Prediction")
    # return "Success"
    return render_template("index.html")

############### predict_charges API ######### 

@app.route('/predict_charges', methods = ["POST", "GET"])
def get_insurance_charges():

    if request.method == "GET":
       
        age = int(request.args.get("age"))
        sex = request.args.get("sex")
        bmi = float(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")
        print("age, sex, bmi, children, smoker, region\n",age, sex, bmi, children, smoker, region)

        med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = med_ins.get_predicted_price()
        return render_template("index.html", prediction = charges)
    

    else:
        print("We are using POST Method")
        age = int(request.form.get("age"))
        sex = request.form.get("sex")
        bmi = float(request.form.get("bmi"))
        children = int(request.form.get("children"))
        smoker = request.form.get("smoker")
        region = request.form.get("region")
        print("age, sex, bmi, children, smoker, region\n",age, sex, bmi, children, smoker, region)

        med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = med_ins.get_predicted_price()
        return render_template("index.html", prediction = charges)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0' , port= config.PORT_NUMBER, debug=True)