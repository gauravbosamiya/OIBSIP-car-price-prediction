import streamlit as st 
import pandas as pd 
import pickle 

model = pickle.load(open('car_price_model.pkl','rb'))

df = pd.read_csv('car data.csv')

st.set_page_config(page_title='Car Price Prediction')

st.title(':red[Car Price Prediction 🚗]')

car_name = st.selectbox(label='',options=df['Car_Name'].unique(),index=None,placeholder='Select Your Car Name')
present_price = st.number_input(label='',min_value=0,placeholder="Your car's present price in lacs",value=None)
year = st.selectbox(label='',options=df['Year'].unique(),index=None,placeholder='In Which year u purchased the car ?')
kms = st.number_input(label='',min_value=0,max_value=None,value=None,placeholder='Driven KMs...')
fuel_type = st.selectbox(label='',options=df['Fuel_Type'].unique(),index=None,placeholder='Petrol / Diesel / CNG')
selling_type = st.selectbox(label='',options=df['Selling_type'].unique(),index=None,placeholder='Dealer / Individual')
transmission = st.selectbox(label='',options=df['Transmission'].unique(),index=None, placeholder='Manual / Automatic')
owner = st.number_input(label='',min_value=0,max_value=None,value=None,placeholder='Owner')


input_data = {
    'Car_Name': [car_name],
    'Present_Price': [present_price],
    'Year': [year],
    'Driven_kms': [kms],
    'Fuel_Type': [fuel_type],
    'Selling_type': [selling_type],
    'Transmission': [transmission],
    'Owner': [owner]
}
input_df = pd.DataFrame(input_data)



if st.button('Predict'):
    try:
        prediction = model.predict(input_df)
        st.subheader(f'The predicted price of the car is: {prediction[0]:.2f}')
    except Exception as e:
        st.subheader(f"An error occurred: {e}")
else:
    st.subheader(":red[Please provide the input data and click 'Predict'.]")