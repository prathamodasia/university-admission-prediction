import streamlit as st
import pandas as pd
import numpy as np
import pickle

clf =pickle.load(open("university.pkl","rb"))

def predict(data):
    return clf.predict(data)

st.title("Case Study On University Admission Prediction")
st.markdown("Lets Predict Admission chances")

st.header("")
col1,col2 = st.columns(2)

with col1:
    G= st.sidebar.slider("GRE Score", 1.0, 340.0, 0.5)
    T= st.sidebar.slider("TOEFL Score", 1.0, 120.0, 0.5)
    U= st.sidebar.slider("University Rating", 1.0, 5.0, 1.0)
    S= st.sidebar.slider("SOP", 1.0, 5.0, 1.0)
    L= st.sidebar.slider("LOR", 1.0, 5.0, 1.0)
    C= st.sidebar.slider("CGPA", 1.0, 10.0, 0.5)
    R= st.sidebar.slider("Research", 0.0, 1.0, 0.5)
                          
st.text('')
if st.button("Chance To Get Admission"):
    result= clf.predict(np.array([[G,T,U,S,L,C,R]]))
    st.text(result[0])
    
st.markdown("Developed  at Pratha Modasia")
                  
