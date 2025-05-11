import joblib
import pandas as pd

model_decision = joblib.load(r'C:\FinalProject\semangatProject\anemia\Decision_model.pkl')
scaler = joblib.load(r'C:\FinalProject\semangatProject\anemia\Scaler.pkl')

# Data baru
new_data = {
        'Gender': 'male',  
        'Hemoglobin': 13,
        'MCH': 48.3,
        'MCHC':  30,
        'MCV': 73 


        # Gender	Hemoglobin	MCH	MCHC	MCV
}

# Convert new data ke DataFrame
new_data_df = pd.DataFrame([new_data])

# Mapping untuk Gender 
gender_map = {'male': 1, 'female': 0} 
new_data_df['Gender'] = new_data_df['Gender'].map(gender_map)

# SCalling dta numerik
new_data_scaled = scaler.transform(new_data_df)

# Prediksi
predicsi = model_decision.predict(new_data_scaled)
predict_hasil = predicsi[0]

label_map = {
        0: 'Tidak Anemia',
        1: 'Anemia'  
}
hasil_prediksi = [label_map[predict_hasil]]

print(f"Predict class (Encoded): {predict_hasil}")
print(f"Predict class (Decoded): {hasil_prediksi[0]}")