# Project Delay Prediction API

Machine Learning model deployed as a REST API to predict whether a project is likely to be delayed based on project parameters.

## Overview

This project demonstrates end-to-end ML deployment:

* Model training with Scikit-Learn
* Model serialization using Joblib
* Flask REST API for inference
* Docker containerization
* Git version control
* Ready for cloud deployment

The API receives project parameters and predicts whether the project will likely experience a delay.

---

## Project Structure

```
project-delay-predictor
│
├── app
│   └── main.py               # Flask API
│
├── model
│   └── train_model.py        # ML training script
│
├── saved_model
│   └── delay_model.pkl       # Trained model
│
├── Dockerfile                # Container configuration
├── requirements.txt          # Python dependencies
├── .gitignore
└── README.md
```

---

## Model Features

The model predicts delay based on:

* `team_size`
* `tasks`
* `deadline_days`
* `complexity`

Output:

```
0 = No Delay
1 = Delay Expected
```

---

## Running Locally

### 1 Install dependencies

```
pip install -r requirements.txt
```

### 2 Run the API

```
python app/main.py
```

Server runs at:

```
http://localhost:5000
```

---

## API Endpoints

### Health Check

```
GET /health
```

Response:

```
{
 "status": "running"
}
```

---

### Predict Delay

```
POST /predict
```

Example request:

```
{
 "team_size": 5,
 "tasks": 40,
 "deadline_days": 20,
 "complexity": 3
}
```

Response:

```
{
 "delay_prediction": 1
}
```

---

## Docker Deployment

Build image:

```
docker build -t delay-api .
```

Run container:

```
docker run -p 5000:5000 delay-api
```

---

## Tech Stack

* Python
* Flask
* Scikit-Learn
* Docker
* Git

---

## Use Case

This project demonstrates how machine learning models can be deployed as scalable services that integrate with backend systems for decision support in project management platforms.


