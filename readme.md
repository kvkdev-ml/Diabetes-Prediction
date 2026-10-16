# DiabCare: Diabetes Prediction System

A lightweight web application that predicts the likelihood of diabetes using a trained machine learning model and user-provided health data. The project combines a Flask backend, a responsive frontend, and a serialized machine-learning model to provide quick risk assessment in a browser.

## Overview

This project is designed for early diabetes screening by analyzing key health indicators such as:

- Pregnancies
- Glucose level
- Blood pressure
- Skin thickness
- Insulin level
- BMI
- Diabetes pedigree function
- Age

The application accepts these values through a simple form and sends them to a prediction API, which returns a risk result.

## Features

- Modern user interface for entering patient details
- Fast diabetes risk prediction using a trained model
- REST API endpoint for model inference
- Responsive frontend built with HTML, Tailwind CSS, and JavaScript
- Simple deployment-ready Flask app

## Tech Stack

### Backend
- Python
- Flask
- Flask-CORS
- Gunicorn
- Pickle (for loading the trained model)

### Frontend
- HTML5
- Tailwind CSS
- JavaScript
- Jinja2 templates

### Machine Learning
- Pre-trained diabetes prediction model stored as `diabetes_model.pkl`
- Model inference performed on user-submitted medical parameters

## Project Structure

```text
Diabetes-Prediction/
├── app.py                  # Flask app and prediction API
├── diabetes_model.pkl      # Serialized trained ML model
├── requirements.txt        # Python dependencies
├── templates/
│   └── diabetes.html       # Frontend UI
└── readme.md               # Project documentation
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd Diabetes-Prediction
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Linux/macOS
venv\Scripts\activate      # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Flask app:

```bash
python app.py
```

Then open the browser at:

```text
http://127.0.0.1:5000/
```

## API Endpoint

The project exposes a prediction endpoint:

```http
POST /api/diabetes
```

Example JSON payload:

```json
{
  "pregnancies": 2,
  "glucose": 120,
  "bp": 80,
  "st": 20,
  "insulin": 85,
  "bmi": 28.5,
  "dpf": 0.47,
  "age": 35
}
```

Example response:

```json
{
  "prediction": 1,
  "confidence": 97
}
```

## Notes

- The application loads the trained diabetes model from `diabetes_model.pkl` at runtime.
- The UI is designed for quick clinical screening and is intended for demonstration/prototype use.
- For production deployment, additional validation, model monitoring, and data security improvements should be considered.
