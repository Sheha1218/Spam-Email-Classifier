
from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)


if not os.path.exists('pred_model.pickle'):
    print("Error: pred_model.pickle file not found!")
else:
    
    with open('pred_model.pickle', 'rb') as file:
        pred_model = pickle.load(file)

@app.route('/', methods=['POST', 'GET'])
def index():
    pred = None

    if request.method == 'POST':
        msg = request.form['message']
        
        
        pred = pred_model.predict([msg])[0]  
        
       
        predict_result = "Spam" if pred == 1 else "Not Spam"
        
        return render_template('index.html', pred=predict_result)
    
    return render_template('index.html', pred=pred)

if __name__ == "__main__":
    app.run(debug=True)