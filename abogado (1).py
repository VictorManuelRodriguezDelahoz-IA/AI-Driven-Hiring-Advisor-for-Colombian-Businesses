import streamlit as st
import google.generativeai as genai
import json
from PIL import Image

background_color = "#192734"

text_color = "white"  # Color de texto para contrastar con el fondo

st.markdown(f"""
    <style>
        body {{
            background-color: {background_color} !important;
            color: {text_color} !important; /* Establece el color del texto */
        }}
        .main .block-container {{ /* Ajusta el ancho del contenido principal */
            max-width: 1200px; /* Ancho máximo en píxeles */
            padding-top: 3rem; /* Espacio superior */
            padding-bottom: 3rem; /* Espacio inferior */
        }}
        h1, h2, h3 {{ /* Estilos para los encabezados (opcional) */
            color: #66B3FF; /* Un azul más claro para los títulos */
        }}
        .stButton>button {{ /* Estilos para los botones */
             background-color: #007bff; /* Un azul para los botones */
             color: white;
        }}
    </style>
    """, unsafe_allow_html=True)

# Reemplaza con tu API Key
api_key = ""  
genai.configure(api_key=api_key)

generation_config = genai.GenerationConfig(
    temperature=0.7,
    top_p=0.95,
    max_output_tokens=2048,
)

model = genai.GenerativeModel(
  model_name="gemini-exp-1206", 
  generation_config=generation_config,
)

# Título de la aplicación
st.title("Asesor legal IA")

# Obtener la entrada del usuario
user_input = st.text_input("Introduce tu texto aquí:")

# Guardar la entrada del usuario en una variable
texto_usuario = user_input

input = {"prompt":"Eres un asistente de IA especializado en la asesoría legal para empresarios colombianos que necesitan ayuda sobre que hacer con sus trabajadores.",
         "user_input":texto_usuario}

input_str = json.dumps(input)

# Mostrar la entrada del usuario y procesarla solo si hay entrada
if st.button("Generar"):
    response = model.generate_content(
    input_str)
    st.write(response.text)

input2 = {"prompt":"Eres un asistente de IA especializado en la asesoría legal para generar contratos a empresarios colombianos que dejan sus necesidades con los empleados.",
         "user_input":texto_usuario }

input_str2 = json.dumps(input2)

file_name = "contrato"
if st.button("Generar contrato"):
    response2 = model.generate_content(
    input_str2)
    st.write(response2.text)
    st.download_button(
            label="Descargar Archivo",
            data=response2.text.encode("utf-8"),
            file_name=file_name,
            mime="text/plain"  # Especifica el tipo MIME para archivos de texto
        )
