import streamlit as st
import pandas as pd
import os
import pickle

data = pd.read_csv("plant_health_data.csv")


with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


with open('preprocessor.pkl', 'rb') as file:
    preposser =pickle.load(file)


df = data.drop(["Timestamp","Plant_ID","Plant_Health_Status"], axis=1)

st.write("plant health prediction")

with st.form(key="my_form"):
   Soil_Moisture=st.number_input("Enter Soil Moisture")
   Ambient_Temperature=st.number_input("Enter Ambient_Temperature")
   Soil_Temperature=st.number_input("Enter Soil_Temperature")
   Humidity=st.number_input("Enter Humidity")
   Light_Intensity=st.number_input("Enter Light_Intensity")
   Soil_pH=st.number_input("Enter Soil_pH")
   Nitrogen_Level=st.number_input("Enter Nitrogen_Level")
   Phosphorus_Level=st.number_input("Enter Phosphorus_Level")
   Potassium_Level=st.number_input("Enter Potassium_Level")
   Chlorophyll_Content=st.number_input("Enter Chlorophyll_Content")
   Electrochemical_Signal=st.number_input("Enter Electrochemical_Signal")
   submitted = st.form_submit_button("Submit")

data = {'Soil_Moisture': float(Soil_Moisture),
        'Ambient_Temperature': float(Ambient_Temperature),
        'Soil_Temperature': float(Soil_Temperature),
        'Humidity': float(Humidity),
        'Light_Intensity': float(Light_Intensity),
        'Soil_pH': float(Soil_pH),
        'Nitrogen_Level': float(Nitrogen_Level),
        'Phosphorus_Level': float(Phosphorus_Level),
        'Potassium_Level': float(Potassium_Level),
        'Chlorophyll_Content': float(Chlorophyll_Content),
        'Electrochemical_Signal': float(Electrochemical_Signal)
        } 
data = pd.DataFrame(data, index=[0])


st.write('---')

scaled = preposser.transform(data)
pred = model.predict(scaled)

st.header('Prediction of Plant Health')


if submitted:
  if pred == 0:
    st.write("High Stress")
  elif pred == 1:
    st.write("Moderate Stress")
  else:
    st.write("Healthy")