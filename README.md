# Web Login Attack Simulation and Machine Learning-based Request Classification System

This project is a prototype web security system that simulates human and automated login attempts on a Flask web application and classifies incoming requests using a Machine Learning model.

The goal is to study the difference between legitimate user behavior and automated brute-force attacks, and to explore how simple ML models can assist in identifying suspicious request patterns.

---

## Project Overview

The application consists of a Flask-based web login system integrated with:

* Selenium scripts to simulate different types of traffic (human vs automated)
* A Machine Learning model (Logistic Regression) trained on a custom dataset
* A request scoring mechanism that classifies requests as safe or unsafe

This project demonstrates a basic pipeline for detecting potential automated login attacks in a controlled environment.

---

## Key Components

### 1. Flask Web Application

* Provides signup and login functionality
* Uses SQLAlchemy for database management
* HTML templates with embedded CSS and JavaScript for the frontend

Main entry point:

```bash
python run.py
```

---

### 2. Traffic Simulation using Selenium

Two scripts are used to generate different types of login traffic:

* `human_traffic.py`
  Simulates realistic user interaction with natural typing delays for username and password fields.

* `brute_force.py`
  Simulates automated brute-force login attempts by rapidly submitting multiple credential combinations.

These scripts help create controlled datasets representing both legitimate and malicious behaviors.

Note: A compatible Selenium WebDriver (e.g., ChromeDriver or GeckoDriver) must be installed separately and added to the system PATH.

---

### 3. Machine Learning Model

* Algorithm: Logistic Regression
* Purpose: Classify login request patterns as safe or unsafe
* Dataset: Custom handmade dataset generated from simulated traffic
* Data preprocessing and labeling scripts are included in the repository

The model outputs a score that helps identify whether a request resembles normal human behavior or automated attack behavior.

---

## Technology Stack

* Backend: Flask
* Database: SQLAlchemy
* Frontend: HTML, CSS, JavaScript (Flask Templates)
* Automation: Selenium WebDriver
* Machine Learning: scikit-learn (Logistic Regression)
* Data Processing: pandas, joblib

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Shadow-Sensei/ai-web-defender.git
cd ai-web-defender
```

### 2. Create and activate a virtual environment

Create the virtual environment:

```bash
python -m venv venv
```

Activate the environment based on your operating system:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows (Command Prompt)**

```bash
venv\Scripts\activate
```

**Windows (PowerShell)**

```bash
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Selenium WebDriver

Install the appropriate driver for your browser (ChromeDriver for Chrome or GeckoDriver for Firefox) and ensure it is available in your system PATH.

### 5. Run the application

```bash
python run.py
```

The web application will start locally, allowing interaction with the login system and testing via the simulation scripts.

---

## Current Scope and Limitations

* The ML model is trained on a handcrafted dataset generated from simulated traffic
* The system is intended as a proof-of-concept prototype, not a production-ready security solution
* Classification is based on basic behavioral features and may not generalize to real-world large-scale attacks

---

## Future Improvements

* Real-time monitoring dashboard for request analysis
* Integration with live web servers
* Use of more advanced anomaly detection or deep learning models
* Adaptive rate limiting and automated blocking mechanisms

---

## Author

Developed as a hackathon project to explore the integration of web security concepts, traffic simulation, and basic machine learning for request classification.
