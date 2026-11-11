import streamlit as st
import pickle
import numpy as np

import base64
  

def main():
    st.title(':blue[House Price Prediction]')
    bedrooms = st.number_input('Enter the number of bedrooms in the house.',min_value=1,max_value=9,step=1)
    bathrooms = st.number_input('Enter the number of bathrooms in the house',min_value=1,max_value=8)
    sqft_living = st.number_input('Enter the total living area of the house (in square feet).',min_value=500)
    sqft_lot = st.number_input('Enter the total lot size of the property (in square feet).',min_value=500)
    floors = st.number_input('Enter How many floors you want',min_value=1,max_value=5)
    waterfront = st.radio('Is the property located on a waterfront?',['Yes','No'],horizontal=True)
    view = st.selectbox('Select the quality of the view from the property',['No view','Fair view','Good view','Very good view','Excellent view'])
    condition = st.selectbox('Select the overall condition of the house',['Poor','Fair','Average','Good','Excellent'])
    grade = st.number_input('Enter the construction and design grade of the house (1 = Very Poor, 13 = Luxury).',min_value=1,max_value=13,step=1)
    sqft_above = st.number_input('Enter the above-ground living area (in square feet) ')
    sqft_basement = st.number_input('Enter the basement area (in square feet)')
    yr_built = st.number_input('Enter the year the house was built',max_value=2024,min_value=1890)
    yr_renovated = st.radio('Has the house been renovated?',['Yes','No'],horizontal=True)

    scaler = pickle.load(open('scaler.sav','rb'))
    model = pickle.load(open('model.sav','rb'))

    pred = st.button(':green[PREDICT]')

    if pred:
        if waterfront == 'Yes':
            waterfront_valid = 1
        else:
            waterfront_valid = 0

        if view == 'No view': 
            valid_view = 0
        elif view == 'Fair view':
            valid_view = 1
        elif view == 'Good view':
            valid_view = 2
        elif view == 'Very good view':
            valid_view = 3
        else :
            valid_view = 4

        if condition == 'Poor' :
            valid_condition = 1
        elif condition == 'Fair' :
            valid_condition = 2
        elif condition == 'Average':
            valid_condition = 3
        elif condition == 'Good' :
            valid_condition = 4
        else :
            valid_condition = 5

        if yr_renovated == 'Yes':
            valid_renovated = 1
        else :
            valid_renovated = 0

        data = [[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront_valid,valid_view,valid_condition,grade,sqft_above,sqft_basement,yr_built,valid_renovated]]
        data1 = scaler.transform(data)
        prediction = model.predict(data1)

        if prediction:
            st.write(f"Price : {int(prediction)}₹")
        
main()
