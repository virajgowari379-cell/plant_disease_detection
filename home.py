import streamlit as st
import requests

st.title("Plant Disease Detection")

file = st.file_uploader("Upload leaf image")

if file:
    st.image(file)

    if st.button("Predict"):
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            files={"file": file.getvalue()}
        )

        result = response.json()

        st.success(f"Prediction: {result['class']}")
        st.info(f"Confidence: {result['confidence']:.2f}")