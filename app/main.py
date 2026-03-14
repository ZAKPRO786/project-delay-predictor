from flask import Flask, request, jsonify
import joblib


app = Flask(__name__)

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "saved_model", "delay_model.pkl")

model = joblib.load(model_path)

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    features = [
        data["team_size"],
        data["tasks"],
        data["deadline_days"],
        data["complexity"]
    ]

    prediction = model.predict([features])[0]

    return jsonify({
        "delay_prediction": int(prediction)
    })


@app.route("/health")
def health():
    return {"status":"running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)