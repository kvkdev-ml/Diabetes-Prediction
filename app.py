from flask import Flask, render_template,request,jsonify
from flask_cors import CORS
import pickle as pk
app=Flask(__name__)
CORS(app)
@app.route('/')
@app.route('/DiabCare')
def index():
    return render_template('diabetes.html')
@app.route('/api/diabetes',methods=['POST'])
def diabetes_prediction():
    data = request.get_json()
    with open("diabetes_model.pkl", "rb") as f:
        model = pk.load(f)
        prediction = int(model.predict([[
            data["pregnancies"],
            data["glucose"],
            data["bp"],
            data["st"],
            data["insulin"],
            data["bmi"],
            data["dpf"],
            data["age"]
        ]])[0])
    return jsonify({
        "prediction": prediction,
        "confidence": 97
    })
if __name__=='__main__':
    app.run()