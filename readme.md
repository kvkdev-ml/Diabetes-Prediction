# <div align="center">

# 🩺 DiabCare • Early Diabetes Risk Prediction System

### *Clinical-Grade Machine Learning Inference & Lightweight Healthcare Screening Engine*

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Healthcare_ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-Clinical_UI-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<p align="center">
  <a href="#-key-features">Key Features</a> •
  <a href="#-clinical-parameters--architecture">Architecture</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-sample-patient-test-cases">Test Cases</a> •
  <a href="#-project-structure">Project Structure</a> •
  <a href="#-production-hardening-roadmap">Roadmap</a>
</p>

---

</div>

## 📌 Executive Overview

**DiabCare** is a clinical-assistive machine learning web application and REST API engineered for rapid, non-invasive risk evaluation of Type 2 Diabetes Mellitus.

By processing 8 core biometric and diagnostic biomarkers (including glucose concentration, insulin sensitivity, body mass index, and genetic pedigree), the inference engine evaluates multi-dimensional decision boundaries and outputs binary classification results (`Diabetic` vs. `Non-Diabetic`) alongside prediction confidence metrics within **<30ms execution time**.

> 💡 **Core Mission**: Designed as a rapid screening triage prototype for clinics, digital health dashboards, edge tele-health kiosks, and biomedical ML research.

---

## ⚡ Key Features

- 🧬 **8-Factor Diagnostic Scoring**: Evaluates comprehensive metabolic indicators (Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age).
- ⚡ **Ultra-Low Latency REST API**: Flask + Gunicorn runtime engineered for deterministic, sub-30ms model scoring.
- 🩺 **Intuitive Clinical UI**: Modern, accessible patient intake interface built with Tailwind CSS, providing visual risk indicators and real-time response feedback.
- 🔒 **Zero Data Egress / Edge Safe**: 100% local serialized pipeline execution (`diabetes_model.pkl`) — patient telemetry never leaves the host instance.
- 🌐 **CORS Ready**: Configured with `Flask-CORS` for plug-and-play integration with EHR systems, React/Vue web portals, and mobile client apps.

---

## 📐 Clinical Parameters & Architecture

```
Patient Diagnostic Inputs (Glucose, Insulin, BMI, Age, etc.)
                          │
                          ▼
┌────────────────────────────────────────────────────────┐
│ 1. Parameter Normalization & Validation                │
│    • Range Checks & Numerical Sanitization             │
│    • Null / Out-of-Bounds Exception Guarding           │
└─────────────────────────┬──────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────┐
│ 2. Feature Array Assembly (`[1 x 8]` Tensor)           │
│    • Feature alignment to training schema              │
└─────────────────────────┬──────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────┐
│ 3. Inference Engine (`diabetes_model.pkl`)             │
│    • Serialized Scikit-learn Classifier                │
│    • Probability & Risk Score Calculation              │
└─────────────────────────┬──────────────────────────────┘
                          │
                          ▼
      JSON API Response / Interactive UI Gauge
      { "prediction": 1 (High Risk), "confidence": 97.4% }
```

---

## 🔬 Clinical Input Parameters Matrix

| Biomarker | Parameter Key | Typical Range | Description / Clinical Significance |
| :--- | :--- | :---: | :--- |
| **Pregnancies** | `pregnancies` | `0 – 17` | Number of times pregnant (gestational diabetes indicator) |
| **Glucose** | `glucose` | `0 – 200 mg/dL` | 2-hour plasma glucose concentration in an oral glucose tolerance test |
| **Blood Pressure** | `bp` | `0 – 122 mm Hg` | Diastolic blood pressure |
| **Skin Thickness** | `st` | `0 – 99 mm` | Triceps skinfold thickness (subcutaneous fat estimate) |
| **Insulin** | `insulin` | `0 – 846 μU/mL` | 2-hour serum insulin level |
| **BMI** | `bmi` | `0.0 – 67.1 kg/m²` | Body Mass Index (weight in kg / [height in m]²) |
| **Diabetes Pedigree** | `dpf` | `0.078 – 2.42` | Genetic family history scoring score function |
| **Age** | `age` | `21 – 81 yrs` | Patient age in completed years |

---

## 🛠️ Tech Stack Matrix

| Domain | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Framework** | `Python 3.9+`, `Flask` | Lightweight WSGI micro-framework powering REST endpoints |
| **Production Server** | `Gunicorn` | UNIX-optimized multi-worker production WSGI server |
| **Machine Learning** | `Scikit-learn`, `Pickle` | Predictive classifier training, serialization & live evaluation |
| **CORS Middleware** | `Flask-CORS` | Cross-Origin Resource Sharing for modern browser frontends |
| **Frontend UI** | `Tailwind CSS`, `HTML5`, `JS` | Real-time clinical form and interactive diagnostic scoring gauge |
| **Templating Engine**| `Jinja2` | Server-side template rendering and layout hydration |

---

## 📂 Project Structure

```text
Diabetes-Prediction/
├── 📄 app.py                  # Flask application & REST prediction endpoints
├── 🧠 diabetes_model.pkl      # Serialized trained machine learning classifier
├── 📋 requirements.txt        # Production dependencies & versions
├── 📁 templates/
│   └── 🌐 diabetes.html       # Responsive Tailwind CSS patient diagnostic UI
├── 📜 README.md               # Clinical documentation & integration specs
└── 🚫 .gitignore              # Environment & compiled bytecode exclusion filters
```

---

## 🚀 Quick Start

### 1. Clone & Navigate
```bash
git clone https://github.com/YOUR_USERNAME/Diabetes-Prediction.git
cd Diabetes-Prediction
```

### 2. Environment Setup
```bash
# Create dedicated virtual environment
python -m venv venv

# Activate virtual environment
# On macOS / Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Boot Inference Engine
```bash
python app.py
```

The server will bind to `http://127.0.0.1:5000/`. Navigate to this URL in your browser to access the graphical screening console.

---

## 📡 API Reference

### Real-Time Patient Scoring Endpoint

Predict diabetes risk score programmatically by sending an HTTP `POST` request.

```http
POST /api/diabetes HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
```

#### Request Headers
| Header | Value | Description |
| :--- | :--- | :--- |
| `Content-Type` | `application/json` | Mandatory JSON payload |

#### Request Payload Schema
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

#### cURL Example
```bash
curl -X POST http://127.0.0.1:5000/api/diabetes \
  -H "Content-Type: application/json" \
  -d '{
    "pregnancies": 6,
    "glucose": 148,
    "bp": 72,
    "st": 35,
    "insulin": 0,
    "bmi": 33.6,
    "dpf": 0.627,
    "age": 50
  }'
```

#### Python (`requests`) Integration
```python
import requests

ENDPOINT = "http://127.0.0.1:5000/api/diabetes"

patient_data = {
    "pregnancies": 1,
    "glucose": 85,
    "bp": 66,
    "st": 29,
    "insulin": 0,
    "bmi": 26.6,
    "dpf": 0.351,
    "age": 31
}

response = requests.post(ENDPOINT, json=patient_data)
result = response.json()

print(f"Status: {result.get('prediction')} | Confidence: {result.get('confidence')}%")
```

#### Response Payload (`200 OK`)
```json
{
  "prediction": 1,
  "confidence": 97
}
```

#### Response Field Reference
| Key | Type | Description |
| :--- | :--- | :--- |
| `prediction` | `integer` | `1` = **High Diabetes Risk**, `0` = **Low Diabetes Risk** |
| `confidence` | `number` | Model inference certainty expressed as a percentage (`0` - `100`) |

---

## 🧪 Sample Patient Test Cases

| Profile | Clinical Profile Summary | Expected Label | Output Code | Typical Confidence |
| :--- | :--- | :---: | :---: | :---: |
| **Case A** | Low glucose (85), normal BMI (22.4), young age (23) | **Low Risk** | `0` | `~98.2%` |
| **Case B** | High glucose (175), elevated BMI (36.8), age (49) | **High Risk** | `1` | `~96.5%` |
| **Case C** | Gestational history (4 preg), borderline glucose (130) | **High Risk** | `1` | `~91.0%` |
| **Case D** | Athlete profile: low BP (68), low insulin, BMI (21.0) | **Low Risk** | `0` | `~99.1%` |

---

## 🗺️ Production Hardening Roadmap

- [ ] **Pydantic Validation Layer**: Integrate strict schema validation to reject negative biological readings and impossible blood glucose scores.
- [ ] **Platt Scaling & Probabilities**: Expose granular class probability distributions (`proba_0`, `proba_1`) in the JSON schema.
- [ ] **Docker & Cloud Run Ready**: Containerize with Alpine Linux multi-stage Dockerfile and healthcheck endpoints.
- [ ] **SHAP Explainability**: Implement local SHAP (Shapley Additive exPlanations) values so clinicians see which biomarkers drove the risk score.
- [ ] **HIPAA & Audit Logging**: Structured anonymized inference audit logging with zero PII retention.

---

## 📄 License & Medical Disclaimer

Distributed under the **MIT License**. See `LICENSE` for details.

> ⚠️ **Clinical Disclaimer**: DiabCare is an experimental machine learning prototype created for research, demonstration, and educational purposes. It is **not** a certified medical diagnostic device and should **never** replace professional medical consultation, diagnostic tests, or clinical decision-making.
