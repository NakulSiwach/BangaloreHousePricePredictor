import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

data = pd.read_csv('Cleaned_data.csv')
# pipe = pickle.load(open('tryRidgeModel.pkl', 'rb'))
pipe = pd.read_pickle(open('tryRidgeModel.pkl', 'rb'))


@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html',locations=locations)


@app.route('/predict',methods=['POST'])
def predict():
    locations = request.form.get('location')
    bhk = int(request.form.get('BHK'))
    bath = int(request.form.get('bath'))
    sqft = int(request.form.get('total_sqft'))
    print(locations,bhk,bath,sqft)
    print(type(locations),type(bhk),type(bath),type(sqft))
    inputt = pd.DataFrame([[int(sqft),int(bath),int(bhk)]],columns=['total_sqft','bath','bhk'])
    print(inputt)
    prediction = pipe.predict(inputt)[0]
    print(prediction)
    return str(prediction)


if __name__ == "__main__":
    app.run(debug=True,port=5000)