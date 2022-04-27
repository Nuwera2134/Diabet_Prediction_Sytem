import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

model=load_model("model1.h5")

def diabet_prediction(input_data):
 
 input_data_as_numpy_array=np.asarray(input_data)
 input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

 prediction=model.predict(input_data_reshaped)
 print(prediction)
 if(prediction[0]== 0):
          return "this Person is not diabetic"
 else:
   return "this Person is diabetic"

def main():
    st.title("Diabets Prediction Web App")
   # Pregnacies,Glucose,BloodPressure,skinThickness,Insulin,BMI,DiabetsPedgreeFunction,Age

    Pregnacies=st.text_input("Number of Pregnacies")
    Glucose =st.text_input("Glucose Level")
    BloodPressure =st.text_input(" Blood Pressure value")
    skinThickness =st.text_input(" skin Thickness value")
    Insulin =st.text_input(" Insulin Level")
    BMI =st.text_input(" BMI  value")
    DiabetsPedgreeFunction=st.text_input(" Diabets Pedgree Function value")
    Age =st.text_input("Age of the Person ")

    
    diagnosis=''

    if st.button("Diabets Test Results"):
      diagnosis = diabet_prediction([Pregnacies,Glucose,BloodPressure,skinThickness,Insulin,BMI,DiabetsPedgreeFunction,Age])
      
      st.success(diagnosis)
    

if __name__ =='__main__':
    main()
