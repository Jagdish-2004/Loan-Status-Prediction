# Loan Approval Prediction Web App

🏦 Loan Approval Prediction Web App

This project is a Loan Approval Prediction System built using Machine Learning and Flask. 
It predicts whether a loan application will be Approved or Rejected based on applicant details such as income, education, credit history, and more.  

The project includes a trained model, a Flask backend, and an interactive HTML frontend for easy use.

-------------------------------------------------------------
🚀 Features

- Machine Learning Model trained on loan applicant data  
- Flask Web Application for real-time predictions  
- Responsive HTML/CSS Frontend  
- Pre-trained Model Integration (model_df.pkl and scaler.pkl)  
- Predicts Loan Approval Status instantly  

-------------------------------------------------------------
🧩 Tech Stack

Backend: Python, Flask  
Frontend: HTML, CSS (Dark Theme UI)  
Modeling: Scikit-learn, Pandas, NumPy  
Data Preprocessing: StandardScaler, Label Encoding  
Deployment: Render / Heroku / AWS / Railway  

-------------------------------------------------------------
📁 Project Structure

Loan-Approval-Prediction/
│
├── model/
│   ├── model_df.pkl          
│   └── scaler.pkl            
│
├── templates/
│   └── index.html            
│
├── static/
│   ├── style.css             
│   └── images/               
│
├── Model Training.ipynb      
├── app.py / application.py   
├── requirements.txt          
└── README.md                 

-------------------------------------------------------------
⚙️ Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/<your-username>/Loan-Approval-Prediction.git
cd Loan-Approval-Prediction

2️⃣ Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (Mac/Linux)

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Flask Application
python app.py

Then open your browser and go to http://127.0.0.1:5000/

-------------------------------------------------------------
🧮 Model Details

- Trained on a loan dataset containing applicant demographic and financial details.  
- Preprocessing: Missing value handling, encoding, scaling.  
- Target: Loan_Status (Approved / Rejected).  
- Model: Logistic Regression / Random Forest / XGBoost (based on training).  

-------------------------------------------------------------
📊 Example Prediction

| Feature | Example Input |
|----------|----------------|
| Gender | Male |
| Married | Yes |
| Applicant Income | 5000 |
| Coapplicant Income | 2000 |
| Loan Amount | 150 |
| Credit History | 1 |
| Property Area | Urban |

Prediction → Loan Approved ✅

-------------------------------------------------------------
📦 Requirements

Flask, Pandas, NumPy, Scikit-learn, Pickle

-------------------------------------------------------------
📈 Future Enhancements

- Add authentication and database  
- Store predictions in a database  
- Add dashboard visualizations  
- Deploy using Docker / Render / AWS  

-------------------------------------------------------------
🤝 Contributing

1. Fork this repository  
2. Create a new branch (feature/new-feature)  
3. Commit your changes  
4. Open a Pull Request  

-------------------------------------------------------------
🧑‍💻 Author

Your Name  
GitHub: https://github.com/<your-username>  

-------------------------------------------------------------
🪪 License

This project is licensed under the MIT License.

