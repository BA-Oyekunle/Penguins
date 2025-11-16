#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import joblib
import numpy as np


# In[2]:


model = joblib.load("model/kmeans_model.pkl")


# In[ ]:


st.title("Penguin Species Predictor")
st.write("Enter measurements to predict Species")


# In[ ]:


# Field input
culmen_length_mm= st.number_input("Culmen length (mm)", value= 0.0)
culmen_depth_mm = st.number_input(" Culmen Depth (mm)" , value =0.0)
flipper_length_mm =st.number_input(" Flipper length(mm)", value =0.0)
body_mass_g = st.number_input("Body mass (g)", value =0.0)


# In[ ]:


# prediction 
if st.button("Predict"):
    features = np.array([[culmen_length_mm, culmen_depth_mm,flipper_length_mm,body_mass_g]])
    try:
        prediction = model.predict (features)[0]
        st.success(f"Predicted species: {prediction}")
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(features)[0]
            st.write("Prediction probabilities:", probd)
    except Expection as e:
        st.error(f"Error in prediction: {e}")


# In[ ]:


import nbformat
from nbconvert import PythonExporter
with open("streamlit_app.ipynb") as f:
    notebook = nbformat.read(f, as_version =4)
exporter = PythonExporter()
script, _= exporter.from_notebook_node(notebook)

with open ("streamlit_app.py", "w") as f:
    f.write(script)


