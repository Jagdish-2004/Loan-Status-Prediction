from flask import Flask
from flask import request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app = application


##Import the model
model = pickle.load(open(r'model/model_df.pkl', 'rb'))
scaler = pickle.load(open(r'model/scaler.pkl', 'rb'))
label = pickle.load(open(r'model/label_encoder.pkl', 'rb'))



@app.route('/')
def home():
    return render_template('home.html')#Finds index.html in templates folder and renders it

@app.route('/predict', methods=['GET','POST'])#Get means when we click on the link, POST means when we submit a form
def predict():
    if request.method == 'POST':
        form_data = request.form

        # Collect all inputs as numeric
        applicant_income = float(form_data['applicant_income'])
        coapplicant_income = float(form_data['coapplicant_income'])
        loan_amount = float(form_data['loan_amount'])
        loan_amount_term = float(form_data['loan_amount_term'])
        credit_history = float(form_data['credit_history'])
        dependents = int(form_data['dependents'])
        gender = int(form_data['gender'])
        married = int(form_data['married'])
        education = int(form_data['education'])
        self_employed = int(form_data['self_employed'])
        property_area = int(form_data['property_area'])
        # Remove original property_area and extend with encoded values
        features = [
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_amount_term,
            credit_history,
            gender,
            married,
            dependents,
            education,
            self_employed,
            property_area
        ]
        
        # Engineered features
        total_income = applicant_income + coapplicant_income
        emi = loan_amount / loan_amount_term if loan_amount_term != 0 else 0
        loanbyincome = loan_amount / total_income if total_income != 0 else 0
        features.append(total_income)
        features.append(emi)
        features.append(loanbyincome)

        # Scale features
        numerical_features = ['applicant_income', 'coapplicant_income', 'loan_amount', 'loan_amount_term', 'total_income', 'emi', 'loanbyincome']
        final_features = np.array([features])

        # Prediction
        prediction = model.predict(final_features)
        predicted_label = 'Y' if prediction[0] == 1 else 'N'
        # Render the result on the home page
        return render_template('home.html', prediction='Accepted' if predicted_label == 'Y' else 'Rejected')
    else:
        return render_template('home.html')

#To run this type in terminal: python application.py
if __name__ == '__main__':
    app.run(host = "0.0.0.0",debug=True)#Host maps to the local address of the machine
    #to change the port number, add port=5001 (or any number) in the brackets