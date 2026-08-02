import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ------------------------------------
# Configuration
# ------------------------------------
MODEL_PATH = "model/best_model_final.keras"   
IMG_SIZE = (224, 224)

# ------------------------------------
# Load Model
# ------------------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

# ------------------------------------
# Prediction Function
# ------------------------------------
def predict(image):

    image = image.convert("RGB")
    image = image.resize(IMG_SIZE)

    img = np.array(image).astype(np.float32)

    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)[0][0]

    if prediction >= 0.5:
        label = " Yellow (Ripe)"
        confidence = prediction
    else:
        label = " Green (Unripe)"
        confidence = 1 - prediction

    return label, confidence


# ------------------------------------
# Streamlit UI
# ------------------------------------
st.set_page_config(
    page_title="Banana Ripeness Classifier",
    page_icon="🍌",
    layout="centered",
)

st.title(" Banana Ripeness Classifier")

st.write(
    """
Upload an image of a banana and the model will predict whether it is:

-  Green (Unripe)
-  Yellow (Ripe)
"""
)

uploaded_file = st.file_uploader(
    "Choose a banana image",
    type=["jpg", "jpeg", "png", "webp"],
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict"):

        with st.spinner("Predicting..."):

            label, confidence = predict(image)

        st.success(f"Prediction: **{label}**")
        st.metric("Confidence", f"{confidence*100:.2f}%")

        st.progress(float(confidence))
