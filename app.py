import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("models/best_model.pkl", "rb"))

# Load encoder
encoder = pickle.load(open("models/target_encoder.pkl", "rb"))

# Load feature names
feature_names = pickle.load(open("models/feature_names.pkl", "rb"))

st.title("🌲 Forest Cover Type Prediction")

st.write("Enter the feature values to predict the forest cover type.")

st.subheader("Input Features")

inputs = []

for feature in feature_names:
    value = st.number_input(feature, value=0.0)
    inputs.append(value)

if st.button("Predict"):

    input_array = np.array(inputs).reshape(1, -1)

    prediction = model.predict(input_array)

    label = encoder.inverse_transform(prediction)

    st.success(f"Predicted Cover Type: {label[0]}")