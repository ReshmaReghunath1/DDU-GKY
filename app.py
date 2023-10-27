import numpy as np
import pickle
import streamlit as st

# Load the XGBoost model
with open('MODEL.pkl', 'rb') as file:
    xgb = pickle.load(file)
file.close()


st.markdown(
    """
    <style>
        .stApp {
            background-image: url("https://redcliffelabs.com/myhealth/wp-content/uploads/2022/08/3.-Pay-attention-to-these-early-signs-of-heart-disease.jpg");
            background-size: cover;
    
        }
    </style>
    """,
    unsafe_allow_html=True
)

def make_prediction(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # Define dictionaries for categorical mappings
    sex_mapping = {
        'Male': 1,
        'Female': 0,
    }
    cp_mapping = {
        'Typical Angina': 1,
        'Atypical Angina': 2,
        'Non-Anginal Pain': 3,
        'Asymptomatic': 4,
    }
    restecg_mapping = {
        'Normal': 0,
        'Abnormality': 1,
        'Probable or Definite Left Ventricular Hypertrophy': 2
    }
    thal_mapping = {
        'Normal': 3,
        'Fixed defect': 6,
        'Reversible defect': 7
    }
    slope_mapping = {
        'Up Sloping': 1,
        'Flat': 2,
        'Down Sloping': 3
    }
    
    target = {
        1: 'Heart Patient',
        0: 'Normal'
    }

    # Map input values to numerical values
    sex = sex_mapping.get(sex, 0)
    cp = cp_mapping.get(cp, 1)  # You can set a default value (1) or handle this differently
    restecg = restecg_mapping.get(restecg, 0)
    thal = thal_mapping.get(thal, 3)  # You can set a default value (3) or handle this differently
    slope = slope_mapping.get(slope, 2)  # You can set a default value (2) or handle this differently

    # Create a NumPy array with the input data
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    # Make the prediction
    prediction = xgb.predict(input_data)
    output = target.get(prediction[0], 'Unknown')

    return output

def main():
    st.title("Heart Disease Prediction")
    with st.form('Heart Disease Prediction Form'):
        # Create a form to collect the user's input data
        age = st.number_input('Age')
        sex = st.selectbox('Gender', ['Male', 'Female'])
        cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)')
        chol = st.number_input('Serum Cholesterol (mg/dl)')
        fbs = st.selectbox('Fasting Blood Sugar', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
        restecg = st.selectbox('Resting ECG Results', ['Normal', 'Abnormality', 'Probable or Definite Left Ventricular Hypertrophy'])
        thalach = st.number_input('Maximum Heart Rate Achieved')
        exang = st.selectbox('Exercise-Induced Angina', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
        oldpeak = st.number_input('ST Depression')
        slope = st.selectbox('ST Segment Slope', ['Up Sloping', 'Flat', 'Down Sloping'])
        ca = st.number_input('Number of Major Vessels (0-3)')
        thal = st.selectbox('Thal', ['Normal', 'Fixed defect' ,'Reversible defect'])

        predict_button = st.form_submit_button("Predict")

    if predict_button:
        output = make_prediction(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
        st.write(f"Predicted Heart Disease: {output}")

if __name__ == "__main__":
    main()
