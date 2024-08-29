# **Heart Disease Prediction Project**

## **Table of Contents**
- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Features](#features)
- [Data Collection](#data-collection)
- [Data Preprocessing](#data-preprocessing)
- [Model Selection and Evaluation](#model-selection-and-evaluation)
- [Web Interface Details](#web-interface-details)
- [Installation](#installation)
- [Usage](#usage)
- [Project Architecture](#project-architecture)
- [Challenges Faced](#challenges-faced)
- [Future Work](#future-work)
- [Team Members](#team-members)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## **Project Overview**
The **Heart Disease Prediction** project is a machine learning-based application aimed at predicting the likelihood of heart disease in patients based on a variety of health metrics such as age, gender, blood pressure, cholesterol levels, and more. By leveraging data preprocessing techniques and model evaluation strategies, the project provides a robust solution that can aid in early diagnosis and potentially save lives. The application includes a user-friendly web interface that allows users to input their health data and receive real-time predictions.

## **Motivation**
Cardiovascular diseases are one of the leading causes of death globally. Early detection and prevention are key to reducing the mortality rate associated with heart diseases. This project was motivated by the need to create an accessible tool that can help in the early diagnosis of heart disease, especially in regions with limited access to healthcare professionals.

## **Features**
- **Data Preprocessing**: Includes handling of missing values, outlier detection, feature engineering, and data normalization to ensure the dataset is ready for model training.
- **Model Selection**: Evaluation of multiple machine learning models (e.g., Logistic Regression, Random Forest, SVM) to select the best-performing model.
- **Web Interface**: A responsive and intuitive web application built using Flask and Bootstrap.
- **Visualization**: Interactive data visualizations to help users understand their health metrics and the model's predictions.
- **Error Handling**: User-friendly error messages and validation to ensure proper data input.

## **Data Collection**
The dataset used in this project, `heart.csv`, contains historical medical data collected from various patients. The dataset includes the following features:
- **Age**: The age of the patient.
- **Gender**: Male or Female.
- **Chest Pain Type**: Type of chest pain experienced.
- **Resting Blood Pressure**: Patient's blood pressure at rest.
- **Cholesterol Level**: Serum cholesterol in mg/dl.
- **Fasting Blood Sugar**: Whether fasting blood sugar is > 120 mg/dl.
- **Resting ECG**: Results of the patient's resting electrocardiogram.
- **Maximum Heart Rate**: Maximum heart rate achieved during the stress test.
- **Exercise Induced Angina**: Whether exercise-induced angina occurs.
- **Oldpeak**: ST depression induced by exercise relative to rest.
- **Slope**: The slope of the peak exercise ST segment.
- **Number of Major Vessels**: Number of major vessels colored by fluoroscopy.
- **Thalassemia**: Blood disorder type.

## **Data Preprocessing**
### **1. Data Cleaning**
- **Missing Values**: Imputation techniques are applied to handle missing data, ensuring that the dataset remains complete.
- **Outlier Detection**: Statistical methods are used to detect and handle outliers that could skew model performance.

### **2. Feature Engineering**
- **Normalization**: Continuous variables are normalized to ensure that they contribute equally to the model training.
- **Categorical Encoding**: Categorical features are encoded using techniques like One-Hot Encoding to convert them into numerical values.

### **3. Splitting the Data**
- **Training and Testing**: The dataset is split into training and testing sets (typically 80%-20%) to evaluate the model's performance on unseen data.

## **Model Selection and Evaluation**
### **1. Model Selection**
Multiple machine learning algorithms are tested to identify the best model:
- **Logistic Regression**: A statistical method for binary classification.
- **Random Forest**: An ensemble method that uses multiple decision trees to improve accuracy.
- **Support Vector Machine (SVM)**: A powerful classifier that works well with high-dimensional data.
- **K-Nearest Neighbors (KNN)**: A simple algorithm that classifies data points based on their distance to nearest neighbors.

### **2. Model Evaluation**
Models are evaluated using performance metrics such as:
- **Accuracy**: The ratio of correctly predicted instances.
- **Precision and Recall**: Metrics that evaluate the balance between positive predictions and the number of relevant instances.
- **F1 Score**: The harmonic mean of precision and recall.
- **ROC-AUC Curve**: Evaluates the model's ability to distinguish between classes.

### **3. Model Deployment**
The best-performing model is serialized and saved as `model.pkl`, ready to be used for predictions in the web application.

## **Web Interface Details**
The web interface is developed using **Flask** and **Bootstrap**, offering the following features:
- **Input Form**: A form for users to input their health data.
- **Dynamic Predictions**: Real-time predictions displayed upon form submission.
- **Error Handling**: Alerts and Bootstrap toast messages for incorrect or missing inputs.
- **Visualization**: Graphical representation of data and predictions to provide users with insights.

### **Customization Options**
Users can modify the CSS to personalize the interface. Bootstrap allows easy customization to align with specific branding or aesthetic preferences.

## **Installation**
To set up the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/LoayElmokadem/Heart-Classfication
    ```

2. **Navigate to the project directory**:
    ```bash
    cd heart-disease-prediction
    ```

3. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

4. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask application**:
    ```bash
    python app.py
    ```

## **Usage**
1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Enter the required health metrics in the form provided.
3. Click on the **Submit** button to receive a heart disease prediction.
4. If the form is submitted without data or with incorrect data, a **Bootstrap toast error message** will appear to guide the user.

## **Project Architecture**
The project is organized as follows:

- **app.py**: The main Python script that runs the Flask application.
- **templates/**: Contains the HTML templates for the web pages.
- **model.pkl**: The serialized machine learning model used for predictions.
- **heart.csv**: The dataset used for training and evaluation.
- **Heart_Attack_Analysis_&_Prediction_Dataset.ipynb**: Jupyter notebook for data analysis and model selection.
- **Web_visual.ipynb**: Jupyter notebook for web-based visualizations.
- **requirements.txt**: Lists the Python packages required for the project.

## **Challenges Faced**
During the development of this project, several challenges were encountered:
- **Data Imbalance**: The dataset had an imbalanced class distribution, which required techniques like oversampling or class weighting to address.
- **Feature Selection**: Determining which features to include in the model was crucial for improving accuracy without overfitting.
- **Model Interpretability**: Balancing between model complexity and interpretability to ensure that the results were understandable for non-experts.

## **Future Work**
Potential improvements and extensions for the project include:
- **Integration with Electronic Health Records (EHR)**: To allow for automatic data extraction and prediction in clinical settings.
- **Mobile Application**: Developing a mobile app to make the predictions more accessible.
- **Enhanced Visualization**: Incorporating more advanced visualizations, such as interactive dashboards.
- **Deep Learning Models**: Experimenting with deep learning approaches to improve prediction accuracy.

## **Team Members**
This project was developed by the following team members:

- **Alaa Rafik**
- **Mariam Ali**
- **Mahmoud Ahmed Nasr**
- **Loay Waleed**
- **Ahmed Ali Elagamy**

we all worked together to build this project

## **Contributing**
We welcome contributions from the community. To contribute, please follow these steps:

1. **Fork the repository** to your own GitHub account.
2. **Create a new branch** for your feature or bug fix:
    ```bash
    git checkout -b feature-branch
    ```
3. **Make your changes** and commit them with clear and descriptive messages:
    ```bash
    git commit -m 'Add feature: X'
    ```
4. **Push your changes** to your branch on GitHub:
    ```bash
    git push origin feature-branch
    ```
5. **Submit a Pull Request** to have your changes reviewed and merged into the main branch.

## **License**
This project is licensed under the **Information Technology Institute (ITI) License**. You are free to use, modify, and distribute this software in any manner that complies with the license.

## **Acknowledgments**
We would like to thank our instructors, peers, and the open-source community for their support and resources that made this project possible. Special thanks to those who provided feedback during the development process, helping us refine and improve the project.
