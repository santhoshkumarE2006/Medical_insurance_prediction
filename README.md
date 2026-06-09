# Medical Insurance Cost Prediction

## Overview

Medical Insurance Cost Prediction is a Machine Learning project that predicts a person's medical insurance charges based on demographic and health-related factors. The project uses a Random Forest Regressor model trained on a medical insurance dataset and provides predictions through a user-friendly Tkinter GUI.

---

## Features

* Data preprocessing using Pandas
* Categorical feature encoding
* Machine Learning model training using Random Forest Regressor
* Model evaluation using R² Score and MAE
* Model persistence using Pickle
* Interactive GUI built with Tkinter
* Real-time insurance cost prediction

---

## Dataset Information

The dataset contains the following attributes:

| Feature  | Description                               |
| -------- | ----------------------------------------- |
| age      | Age of the individual                     |
| sex      | Gender of the individual                  |
| bmi      | Body Mass Index                           |
| children | Number of dependents covered by insurance |
| smoker   | Smoking status                            |
| region   | Residential region                        |
| charges  | Medical insurance cost (Target Variable)  |

Dataset Size: 2772 Records

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Tkinter
* Pickle
* Jupyter Notebook

---

## Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Encoding
4. Train-Test Split
5. Model Training
6. Model Evaluation
7. Model Saving
8. GUI Development
9. Real-Time Prediction

---

## Model Performance

* Algorithm: Random Forest Regressor
* R² Score: 0.9507
* Mean Absolute Error (MAE): 1282.13
* ![model performance](https://github.com/santhoshkumarE2006/Medical_insurance_prediction/blob/main/images/Screenshot%202026-06-09%20100346.png?raw=true)

The model achieved approximately 95% prediction accuracy, demonstrating strong performance on unseen data.

---

## Project Structure

Medical_Insurance_Prediction/

├── Medical_Insurance_Prediction.ipynb

├── insurance_gui.py

├── insurance_model.pkl

├── medical_insurance.csv

├── requirements.txt

└── README.md

---

## How to Run

### 1. Install Required Libraries

pip install -r requirements.txt

### 2. Run the Application

python insurance_gui.py

### 3. Enter User Details

* Age
* BMI
* Number of Children
* Gender
* Smoking Status
* Region

Click **Predict Insurance Cost** to view the estimated insurance charge.

---

## Sample Prediction

Input:

* Age: 25
* BMI: 24.5
* Children: 1
* Gender: Male
* Smoker: No
* Region: Southeast

Output:

Predicted Insurance Cost: ₹7,528.77

---

![App Interface](https://github.com/santhoshkumarE2006/Medical_insurance_prediction/blob/main/images/Screenshot%202026-06-09%20115539.png?raw=true)

## Author

**Santhosh Kumar**

B.Sc Information Technology

Artificial intelligence Internship Project
