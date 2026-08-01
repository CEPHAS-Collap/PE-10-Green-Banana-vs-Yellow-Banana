import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ------------------------------------
# Configuration
# ------------------------------------
MODEL_PATH = "best_model_final.keras"   
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


