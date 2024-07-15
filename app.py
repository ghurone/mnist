import numpy as np
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from tensorflow.keras.models import load_model
from PIL import Image

st.set_page_config(page_title='Reconhecedor de Digitos',
                   page_icon='🔢',
                   layout="centered")


def load(model_path):
    try:
        model = load_model(model_path)
        return model
    except Exception as e:
        return None

# Carregar o modelo treinado
model = load('models/mnist.keras')

st.title('Reconhecedor de dígitos')
st.markdown('''
Desenhe um número de 0 a 9
''')

SIZE = 196
P_SIZE = 12
SCALE = 3

col1, col2, col3 = st.columns([1, 12, 1])

msg_place = col2.empty()

with col2:
    canvas_result = st_canvas(
        fill_color='#000000',
        stroke_width=P_SIZE*SCALE,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=SIZE*SCALE,
        height=SIZE*SCALE,
        drawing_mode="freedraw",
        key='canvas')

# Função para processar a imagem sem usar OpenCV
def preprocess_image(image_data):
    img = Image.fromarray(image_data.astype('uint8'), 'RGBA').convert('L')  # Convertendo para escala de cinza
    img = img.resize((28, 28))  # Redimensionar a imagem
    img = np.array(img).astype('float32') / 255.0  # Normalizar a imagem
    img = np.expand_dims(img, axis=-1)  # Adicionar a dimensão do canal
    img = np.expand_dims(img, axis=0)  # Adicionar a dimensão do batch
    return img

if col2.button('Predict', type='primary'):
    if canvas_result.image_data is not None:
        img = preprocess_image(canvas_result.image_data)
        
        attempts = 0
        total_attempts = 25
        success = False
        while attempts < total_attempts and not success:
            try:
                val = model.predict(img)[0]
                i = np.argmax(val)
                # Exibir mensagem de sucesso
                msg_place.success(f'Eu tenho {val[i]:.4%} de confiança que você desenhou o número {i}', icon="✅")
                success = True
            except:
                attempts += 1
                if attempts == total_attempts:
                    # Exibir mensagem de erro após tentativas
                    msg_place.error('Aconteceu algo inesperado, aperte o botão novamente.', icon="🚨")

st.markdown('<div style="text-align: center">Feito com ❤️ por <a href="https://www.github.com/ghurone">Erick Ghuron</a></div>', unsafe_allow_html=True)
