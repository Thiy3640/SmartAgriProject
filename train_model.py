import pandas as pd
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from google.colab import files
import os

print(" Starting Specialized Training...")


# 1. CROP SYSTEM (Gaussian Naive Bayes)

# Naive Bayes is better here because it treats N, P, K as probabilities 
# rather than strict rules, preventing "weird" predictions.
if os.path.exists('Crop_recommendation.csv'):
    print("\n Training Crop Model (Naive Bayes)...")
    df_crop = pd.read_csv('Crop_recommendation1.csv')
    
    # Select Features
    X_crop = df_crop[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y_crop = df_crop['label']

    # Train
    crop_model = GaussianNB()
    crop_model.fit(X_crop, y_crop)
    
    print(f" Crop Accuracy: {crop_model.score(X_crop, y_crop)*100:.2f}%")

    with open('crop_model.pkl', 'wb') as f:
        pickle.dump(crop_model, f)
else:
    print(" Error: Crop_recommendation1.csv missing.")


# 2. FERTILIZER SYSTEM (Random Forest)

if os.path.exists('fertilizer_recommendation.csv'):
    print("\n Training Fertilizer Model (Random Forest)...")
    df_fert = pd.read_csv('fertilizer_recommendation.csv')

    # Encoders
    enc_soil = LabelEncoder()
    df_fert['Soil_Type'] = enc_soil.fit_transform(df_fert['Soil_Type'])
    
    enc_crop = LabelEncoder()
    df_fert['Crop_Type'] = enc_crop.fit_transform(df_fert['Crop_Type'])
    
    enc_fert = LabelEncoder()
    df_fert['Recommended_Fertilizer'] = enc_fert.fit_transform(df_fert['Recommended_Fertilizer'])

    # Features (Strict Order)
    X_fert = df_fert[['Soil_Type', 'Crop_Type', 'Nitrogen_Level', 'Phosphorus_Level', 
                      'Potassium_Level', 'Soil_pH', 'Soil_Moisture', 'Temperature', 
                      'Humidity', 'Rainfall']]
    y_fert = df_fert['Recommended_Fertilizer']

    # Train
    fert_model = RandomForestClassifier(n_estimators=100, random_state=42)
    fert_model.fit(X_fert, y_fert)
    
    print(f" Fertilizer Accuracy: {fert_model.score(X_fert, y_fert)*100:.2f}%")

    # Save Everything
    with open('fertilizer_model.pkl', 'wb') as f: pickle.dump(fert_model, f)
    with open('enc_soil.pkl', 'wb') as f: pickle.dump(enc_soil, f)
    with open('enc_crop.pkl', 'wb') as f: pickle.dump(enc_crop, f)
    with open('enc_fert.pkl', 'wb') as f: pickle.dump(enc_fert, f)

    # Download
    print("\n Downloading Files...")
    files.download('crop_model.pkl')
    files.download('fertilizer_model.pkl')
    files.download('enc_soil.pkl')
    files.download('enc_crop.pkl')
    files.download('enc_fert.pkl')