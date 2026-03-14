import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

os.makedirs("../saved_model", exist_ok=True)

data = {
    "team_size":[3,5,2,8,6,4,7],
    "tasks":[20,50,10,80,60,40,70],
    "deadline_days":[10,30,5,60,45,20,50],
    "complexity":[2,3,1,4,3,2,4],
    "delay":[1,0,1,0,0,1,0]
}

df = pd.DataFrame(data)

X = df[["team_size","tasks","deadline_days","complexity"]]
y = df["delay"]

model = RandomForestClassifier()
model.fit(X,y)

joblib.dump(model, "../saved_model/delay_model.pkl")

print("Model saved")