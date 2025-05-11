import joblib
import pandas as pd
import sys

model_decision = joblib.load(r'C:\FinalProject\semangatProject\anemia\Decision_model.pkl')
scaler = joblib.load(r'C:\FinalProject\semangatProject\anemia\Scaler.pkl')

 # cd "C:\FinalProject\semangatProject\anemia"
# python Anemia_cmd.py male 13 48.3 30 73
if len(sys.argv) != 6:
         print ("Usage: Anemia_cmd.py <Gender> <Hemoglobin> <MCH> <MCHC> <MCV>")
         sys.exit(1)

new_data = {
        "Gender" : str(sys.argv[1]),
        "Hemoglobin" : int(sys.argv[2]),
        "MCH" : float(sys.argv[3]),
        "MCHC" : int(sys.argv[4]),
        "MCV" : int(sys.argv[5]),
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

# print(f"Predict class (Encoded): {predict_hasil}")
# print(f"Predict class (Decoded): {hasil_prediksi[0]}")

print(f" {hasil_prediksi[0]}")