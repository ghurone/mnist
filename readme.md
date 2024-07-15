Aqui está uma descrição aprimorada para o seu projeto no GitHub:

---

# MNIST Digit Recognizer

This Streamlit application allows users to draw and recognize handwritten digits using a trained deep learning model. The app provides an interactive canvas where you can draw digits from 0 to 9 and get real-time predictions with confidence levels.

## Features

- **Interactive Drawing Canvas**: Easily draw digits with a smooth and responsive interface.
- **Real-Time Predictions**: Get instant predictions for your drawn digits with confidence percentages.
- **User-Friendly Interface**: Designed with simplicity and ease of use in mind.

## How to Use

1. **Draw a Digit**: Use the canvas to draw any digit from 0 to 9.
2. **Predict**: Click the 'Predict' button to see the model's prediction and confidence level.
3. **Clear and Retry**: Easily clear the canvas to draw another digit and make new predictions.

## Installation

To run this app locally, follow these steps:

1. Clone this repository:
   ```sh
   git clone https://github.com/ghurone/mnist-digit-recognizer.git
   ```
2. Navigate to the project directory:
   ```sh
   cd mnist-digit-recognizer
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## Dependencies

- Streamlit
- TensorFlow
- NumPy
- Pillow

## Model

The model used in this application is trained on the MNIST dataset, a well-known dataset of handwritten digits. It leverages a Convolutional Neural Network (CNN) to achieve high accuracy in digit recognition.

## Acknowledgements

- The MNIST dataset, provided by Yann LeCun, Corinna Cortes, and Chris Burges.
- Streamlit for making it easy to build and share custom web apps for machine learning and data science.

## Author

Developed with ❤️ by [Erick Ghuron](https://www.github.com/ghurone)
