# PE-10-Green-Banana-vs-Yellow-Banana


# 🍌 Green vs Yellow Banana Classifier

A deep learning web application that classifies whether a banana is **Green (Unripe)** or **Yellow (Ripe)** from an uploaded image. The model is built using **TensorFlow/Keras** with **MobileNetV2** transfer learning and deployed with **Streamlit**.

---

## Project Overview

Banana ripeness classification is useful in agriculture, food quality assessment, and supply chain management. This project uses a Convolutional Neural Network (CNN) based on MobileNetV2 to automatically identify whether a banana is:

* 🟢 **Green (Unripe)**
* 🟡 **Yellow (Ripe)**

Users can upload an image through a Streamlit web interface and receive an instant prediction with a confidence score.

---

##  Features

* Deep learning image classification
* MobileNetV2 transfer learning
* Streamlit web interface
* Confidence score for predictions
* Fast and lightweight inference
* Easy deployment

---

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* MobileNetV2
* Streamlit
* NumPy
* Pillow
* Matplotlib (for visualization)
* Jupyter Notebook

---

##  Project Structure

```text
green-vs-yellow-banana-classifier/
│
├── app.py                     # Streamlit application
├── green-vs-yellow-banana-classifier.ipynb
├── banana_classifier.keras    # Trained model
├── requirements.txt
├── README.md
└── dataset/
    ├── Green/
    └── Yellow/
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/green-vs-yellow-banana-classifier.git

cd green-vs-yellow-banana-classifier
```

### 2. Create a virtual environment (optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Application

Start the Streamlit app with:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

##  Model

The classifier uses **MobileNetV2** with transfer learning.

### Input

* Image size: **224 × 224**
* RGB images

### Output

*  Green (Unripe)
*  Yellow (Ripe)

---

##  How to Use

1. Launch the Streamlit app.
2. Upload a banana image (`.jpg`, `.jpeg`, `.png`, or `.webp`).
3. Click **Predict**.
4. View the predicted class and confidence score.

---

## Future Improvements

* Support multiple ripeness stages
* Improve model accuracy with more training data
* Deploy online using Streamlit Community Cloud
* Add Grad-CAM visualizations for explainability
* Enable real-time webcam predictions

---

## Requirements

Example `requirements.txt`:

```text
streamlit
tensorflow
numpy
Pillow
matplotlib
```

---

##  Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it for educational and commercial purposes.

---
