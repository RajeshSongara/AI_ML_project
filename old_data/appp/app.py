import sys
import os

# 🔥 VERY IMPORTANT (top me hi hona chahiye)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, request, render_template
from db import create_table, insert_data
import pickle
from db import create_table, insert_data,fetch_data


app = Flask(__name__)

# Model load
model = pickle.load(open('model.pkl', 'rb'))

# Table create (app start pe)
create_table()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    hours = float(request.form['hours'])
    attendance = float(request.form['attendance'])

    prediction = model.predict([[hours, attendance]])

    # 🔥 SAVE DATA HERE
    insert_data(hours, attendance, float(prediction[0]))

    return f"Predicted Marks: {prediction[0]}"

@app.route('/history')
def data():
    rows= fetch_data()
    return render_template('history.html',data=rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)