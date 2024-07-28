import streamlit as st
import pickle
import pandas as pd

# Loading new_df dataset and pipeline
cars_dict = pickle.load(open('Car_dict.pkl', 'rb'))
cars = pd.DataFrame(cars_dict)
pipe = pickle.load(open('Car_price_prediction.pkl', 'rb'))

# Title of the website
st.title("Car Price Predictor")

# Car name selection
selected_car = st.selectbox('Select the car model', cars['name'].values)

# Company selection
selected_company = st.selectbox('Select the company', cars['company'].unique())

# Year selection
year = st.number_input('Year of Manufacture', min_value=1990, max_value=2023, value=2010, step=1)

# Fuel type selection
fuel_type = st.selectbox('Select Fuel Type', cars['fuel_type'].unique())

# Kilometers driven input
kms_driven = st.number_input('Kilometers Driven', min_value=0, max_value=500000, value=10000, step=1000)


# Button for prediction
if st.button('Predict Price'):
    # Prepare the input DataFrame
    input_data = pd.DataFrame({
        'name': [selected_car],
        'company': [selected_company],
        'year': [year],
        'fuel_type': [fuel_type],
        'kms_driven': [kms_driven]
    })

    # Use the pipeline to predict the price
    predicted_price = pipe.predict(input_data)[0]

    # Display the predicted price
    st.write(f'The predicted price of the car is ₹ {predicted_price:.2f}')
