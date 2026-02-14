Smart Farming AI: Precision Agriculture System
Overview
Smart Farming AI is a machine learning-based web application designed to assist farmers and agriculturalists in making data-driven decisions. The system provides two primary functionalities:

Crop Recommendation: Suggests the most suitable crop to grow based on soil nutrient levels (N, P, K) and climatic conditions.

Fertilizer Recommendation: Prescribes the correct fertilizer based on soil type, crop type, and current nutrient status.

The goal of this project is to optimize agricultural yield and reduce resource wastage through precision agriculture techniques.

Features
Crop Advisor: Uses the Gaussian Naive Bayes algorithm to analyze soil nutrients (Nitrogen, Phosphorus, Potassium), temperature, humidity, pH value, and rainfall to recommend the optimal crop.

Nutrient Calculator: Uses the Random Forest Classifier to analyze soil composition and crop requirements to suggest specific fertilizers.

User-Friendly Interface: A responsive web interface built with Bootstrap 5, featuring tab persistence and real-time input validation.

Robust Backend: Powered by Python Flask and Scikit-learn.

Technical Architecture
Machine Learning Models
Crop Prediction: Implements Gaussian Naive Bayes. This model was selected for its high accuracy in handling continuous environmental data (temperature, humidity) and its probabilistic nature.

Fertilizer Prediction: Implements Random Forest Classifier. This model handles categorical data (Soil Type, Crop Type) effectively and prevents overfitting through ensemble learning.

Tech Stack
Language: Python 3.x

Web Framework: Flask

Frontend: HTML5, CSS3, JavaScript, Bootstrap 5

Data Processing: Pandas, NumPy

Machine Learning: Scikit-learn

Project Structure
Plaintext
/smart-farming-ai
  ├── app.py                   # Main Flask application entry point
  ├── train_models.py          # Script to train ML models and generate .pkl files
  ├── requirements.txt         # List of dependencies
  ├── static/
  │    ├── css/
  │    │    └── style.css      # Custom styling
  │    └── js/
  │         └── script.js      # Client-side logic (Validation, Tab handling)
  ├── templates/
  │    └── index.html          # Main user interface
  ├── *.pkl                    # Serialized machine learning models and encoders
  └── README.md                # Project documentation
Installation and Setup
1. Prerequisites
Ensure you have Python installed on your system.

2. Clone the Repository
Bash
git clone https://github.com/yourusername/smart-farming-ai.git
cd smart-farming-ai
3. Install Dependencies
Create a virtual environment (recommended) and install the required libraries.

Bash
pip install flask pandas numpy scikit-learn
4. Model Generation (First Run Only)
If the .pkl files are not present, run the training script to generate the models.

Bash
python train_models.py
5. Run the Application
Start the Flask server.

Bash
python app.py
Open your web browser and navigate to: http://127.0.0.1:5000/

Usage Guide
For Crop Recommendation:
Navigate to the "Crop Advisor" tab.

Enter the N, P, K values of the soil.

Input the environmental conditions (Temperature, Humidity, pH, Rainfall).

Click "Predict Crop" to view the result.

For Fertilizer Recommendation:
Navigate to the "Fertilizer Doctor" tab.

Select the Soil Type and the Crop you intend to grow.

Enter the current nutrient levels and environmental data.

Click "Get Recommendation" to receive the prescription.

Datasets
The models were trained on the following datasets:

Crop Recommendation Dataset: Contains parameters for 22 different crops (N, P, K, temperature, humidity, pH, rainfall).

Fertilizer Prediction Dataset: Contains soil and crop-specific data mapped to suitable fertilizers.
