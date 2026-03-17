import streamlit as st
import os

st.title("🌿 Grassland Monitoring AI")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Create uploads folder
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    filepath = os.path.join("uploads", uploaded_file.name)

    # Save file
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Dummy prediction
    prediction = "Grassland image uploaded successfully"

    st.success(prediction)
