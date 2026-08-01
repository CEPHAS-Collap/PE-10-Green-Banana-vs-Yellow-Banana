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
