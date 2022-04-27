import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

model=load_model("model1.h5")

input_data=(5,166,72,19,175,25.8,0.587,51)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

prediction=model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]==0):
    print("this Person is not diabetic")
else:
    print("this Person is diabetic")


