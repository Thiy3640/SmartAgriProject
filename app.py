from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# --- LOAD MODELS ONCE ---
try:
    crop_model = pickle.load(open('crop_model.pkl', 'rb'))
    fert_model = pickle.load(open('fertilizer_model.pkl', 'rb'))
    enc_soil = pickle.load(open('enc_soil.pkl', 'rb'))
    enc_crop = pickle.load(open('enc_crop.pkl', 'rb'))
    enc_fert = pickle.load(open('enc_fert.pkl', 'rb'))
    print(" Models Loaded!")
except:
    print(" Warning: Models not found. Upload .pkl files.")

@app.route('/', methods=['GET', 'POST'])
def index():
    res_crop = ""
    res_fert = ""
    
    # Dropdown options
    soils = sorted(enc_soil.classes_) if 'enc_soil' in globals() else []
    crops = sorted(enc_crop.classes_) if 'enc_crop' in globals() else []

    if request.method == 'POST':
        # --- CROP LOGIC ---
        if 'predict_crop' in request.form:
            try:
                features = [
                    float(request.form['N']), float(request.form['P']), float(request.form['K']),
                    float(request.form['temp']), float(request.form['hum']), 
                    float(request.form['ph']), float(request.form['rain'])
                ]
                res_crop = crop_model.predict([features])[0].upper()
            except Exception as e:
                res_crop = f"Error: {str(e)}"

        # --- FERTILIZER LOGIC ---
        elif 'predict_fert' in request.form:
            try:
                soil_id = enc_soil.transform([request.form['soil']])[0]
                crop_id = enc_crop.transform([request.form['crop']])[0]
                
                features = [[
                    soil_id, crop_id,
                    float(request.form['n_f']), float(request.form['p_f']), float(request.form['k_f']),
                    float(request.form['ph_f']), float(request.form['moist_f']),
                    float(request.form['temp_f']), float(request.form['hum_f']), float(request.form['rain_f'])
                ]]
                
                pred_id = fert_model.predict(features)[0]
                res_fert = enc_fert.inverse_transform([pred_id])[0]
            except Exception as e:
                res_fert = f"Error: {str(e)}"

    return render_template('index.html', res_crop=res_crop, res_fert=res_fert, soils=soils, crops=crops)

if __name__ == '__main__':
    app.run(debug=True)