# Diabetes-Classification-Azure-Machine-Learning-End-to-End-ML-Pipeline-
Complete ML pipeline for Diabetes Classification using Azure Machine Learning Designer — including data preparation, normalization, logistic regression training, model evaluation, real-time inference pipeline creation, ACI deployment, and endpoint testing.
-This project follows Microsoft Learn's MLOps workflow and demonstrates practical Azure ML skills.

📌 Project Overview

The goal of this project is to build and deploy a classification model that predicts whether a patient is diabetic (1) or not (0) based on diagnostic measurements.

This project includes:

-Data exploration

-Column selection

-MinMax normalization

-Logistic regression classification

-Evaluation using metrics & confusion matrix

-Real-time inference with Web Service Input

-Deployment as a REST endpoint using ACI

-This is ideal for Data Scientist, ML Engineer, and Cloud AI Engineer roles.

📊 Dataset
Type: Tabular
Label column: Diabetic
Features:
Pregnancies, PlasmaGlucose, DiastolicBloodPressure, TricepsThickness, SerumInsulin, BMI, DiabetesPedigree, Age

Azure ML Explorer automatically shows:

-Missing values

-Histogram distributions

-Column statistics

🏗 Training Pipeline Architecture
-🔹 Steps Performed

-Select Columns in Dataset

-Removed: PatientID

-Normalize Data

-MinMax scaling applied to all numeric columns

-Split Data

-70% training / 30% testing

-Two-Class Logistic Regression

-Train Model

-Score Model

-Evaluate Model

📈 Evaluation Metrics

The Evaluate Model module provides:

-Accuracy, Precision, Recall, F1 Score, ROC Curve & AUC, Confusion Matrix

These metrics help assess model quality and classify diabetic conditions.

🟢 Inference Pipeline Architecture

The inference pipeline performs:

-Web Service Input

-Apply same transformations (Select Columns + Normalize)

-Score Model

-Execute Python Script (formats final output)

-Web Service Output

✔ Output Columns Returned

-PatientID

-DiabetesPrediction (0 / 1)

-Probability

🚀 Deployment
Compute Used

-Training: Azure ML Compute Cluster

-Deployment: Azure Container Instance (ACI)** (Free-tier friendly)

-Endpoint name: predict-diabetes

--Deployment Steps

-Created inference pipeline

-Replaced dataset with Enter Data Manually block

-Added Web Service Input

-Connected transformations → Model → Python Script → Output

-Published the pipeline

-Selected ACI

-Waited for deployment to finish

-Verified endpoint health in Details tab

-Tested endpoint successfully using JSON test input

🛠 Technologies & Tools Used
--Area	-Tools
--Cloud	-Microsoft Azure
--ML Platform	-Azure Machine Learning Studio (Designer)
--Transformation	-Select Columns, Normalize, Split
--Algorithms	-Two-Class Logistic Regression
--Deployment	-Azure Container Instance (ACI)
--Endpoint Type	-V1 Real-Time Endpoint
--Language	-Python (for endpoint testing)
