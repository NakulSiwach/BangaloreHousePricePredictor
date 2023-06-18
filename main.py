import pickle

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
data = pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open('newRidgeModel.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True,port=5000)