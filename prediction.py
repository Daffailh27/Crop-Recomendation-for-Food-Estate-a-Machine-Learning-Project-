import streamlit as st
import pandas as pd
import pickle
from PIL import Image

# Load Pipeline
with open('optimized_random_forest_model.pkl', 'rb') as file1:
    crop_recommendation_model = pickle.load(file1)

# Form for Crop Recommendation
def run():

    st.write('# Crop Recommendation for Sustainable Agriculture')
    st.write('###### Input the environmental parameters to get the crop recommendation.')

    image = Image.open('DALL·E-2023-12-28-14.01.59-An-illustrative-depiction-of-the-concepts-Food-Estate-Contract-Farming-and-Food-Security.-The-image-is-divided-into-three-sections_.png')
    st.image(image, caption='Sustainable Agriculture')

    with st.form('cropRecommendationForm'):
        # Assume that the form will capture environmental features such as N, P, K, temperature, humidity, pH, and rainfall
        N = st.number_input('Nitrogen', min_value=0)
        P = st.number_input('Phosphorus', min_value=0)
        K = st.number_input('Potassium', min_value=0)
        temperature = st.number_input('Temperature (in Celsius)', min_value=0)
        humidity = st.number_input('Humidity (%)', min_value=0)
        ph = st.number_input('pH Level', min_value=0.0, max_value=14.0)
        rainfall = st.number_input('Rainfall (mm)', min_value=0)
        rainfall_category = st.selectbox('Rainfall Category', ('low', 'medium', 'high'))
 

        # Submit button
        submitted = st.form_submit_button('Predict Crop')

    # DataFrame from input data
    input_data = pd.DataFrame({
        'N': [N],
        'P': [P],
        'K': [K],
        'temperature': [temperature],
        'humidity': [humidity],
        'ph': [ph],
        'rainfall': [rainfall],
        'rainfall_category': [rainfall_category]
    })

    # Prediction
    if submitted:
        crop_prediction = crop_recommendation_model.predict(input_data)
        st.write('## Recommended Crop:', crop_prediction[0])

if __name__ == '__main__':
    run()
