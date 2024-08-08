import streamlit as st
import numpy as np
import pickle

# Load the model once
clf = pickle.load(open("university.pkl", "rb"))

def predict(data):
    return clf.predict(data)

st.title("Case Study On University Admission Prediction")
st.markdown("Let's Predict Admission Chances")

st.header("")
col1, col2 = st.columns(2)

with col1:
    G = st.slider("GRE Score", 1.0, 340.0, 0.5)
    T = st.slider("TOEFL Score", 1.0, 120.0, 0.5)
    U = st.slider("University Rating", 1.0, 5.0, 1.0)
    S = st.slider("SOP", 1.0, 5.0, 1.0)
    L = st.slider("LOR", 1.0, 5.0, 1.0)
    C = st.slider("CGPA", 1.0, 10.0, 0.5)
    R = st.slider("Research", 0.0, 1.0, 0.5)

st.text('')
if st.button("Chance To Get Admission"):
    # Create a numpy array for the prediction
    input_data = np.array([[G, T, U, S, L, C, R]])
    # Get prediction
    result = predict(input_data)
    # Display result
    st.text(f"Admission Chance: {result[0]}")

st.markdown("Developed at Pratha Modasia")
