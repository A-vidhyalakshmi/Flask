from flask import Flask,request,jsonify
import pickle
import sklearn

app = Flask(__name__)

print(__name__)

model_pickle = open("./classifier.pkl",'rb')
clf = pickle.load(model_pickle)

@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping", methods=['GET'])
def pinger():
    return "<p>Hello i am under water!</p>"

@app.route("/json", methods=['GET'])
def json_check():
    return {"message": "Hi i am json!"}



@app.route('/predict' ,methods=['POST'])  #We give input to predict something , so its a POST method
def prediction():
    loan_req = request.get_json()

    if loan_req['Gender'] == 'Male':
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == 'Unmarried':
        Married = 0
    else:
        Married = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    Credit_History = loan_req['Credit_History']

    result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
    
    if result == 0:
        pred = 'REJECTED'
    else:
        pred = 'APPROVED'

    return {'loan_approval_status:',pred}



