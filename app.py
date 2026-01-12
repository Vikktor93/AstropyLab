import streamlit as st
import os
from dotenv import load_dotenv
from src.nasa_client import NasaClient
from src.image_manager import ImageManager
from src.analyzer import SpaceAnalyzer

st.set_page_config(page_title="AstropyLab", page_icon="🔭", layout="wide")
load_dotenv()

# --- SIDEBAR ---
with st.sidebar:
    st.header("🛸 Panel de Control")
    
    # Selector de Modo
    mode = st.radio("Fuente de Datos:", ["📡 API NASA (Online)", "📂 Archivos Locales (Offline)"])
    
    analyze_btn = False
    selected_file = None
    
    if mode == "📂 Archivos Locales (Offline)":
        # Listar archivos en carpeta data/
        data_dir = "data"
        if os.path.exists(data_dir):
            files = [f for f in os.listdir(data_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
            if files:
                selected_file = st.selectbox("Selecciona una imagen guardada:", files)
            else:
                st.warning("No hay imágenes en la carpeta data/")
        else:
            st.error("La carpeta data/ no existe.")
            
    else:
        st.info("Conectado a API NASA")

    analyze_btn = st.button("🔍 Analizar Imagen")

# --- ÁREA PRINCIPAL ---
st.title("🔭 AstropyLab")
st.markdown(f"*Modo actual: {mode}*")

# Lógica Principal
image_path_to_analyze = None
image_title = ""
image_explanation = ""

if mode == "📡 API NASA (Online)":
    # LÓGICA ONLINE
    api_key = os.getenv("NASA_API_KEY")
    if not api_key:
        st.error("⚠️ Error: No se detectó la API KEY en .env")
    else:
        client = NasaClient(api_key)
        
        with st.spinner('Contactando al satélite...'):
            data = client.get_apod() # Aquí puede fallar si hay error 504
            
        if data:
            image_title = data.get('title', 'Sin título')
            image_explanation = data.get('explanation', '')
            
            if data.get('media_type') == 'image':
                st.image(data['url'], caption=data['date'], use_container_width=True)
                
                if analyze_btn:
                    # Descargar para analizar
                    manager = ImageManager()
                    image_path_to_analyze = manager.download_image(data['url'], data['date'])
            else:
                st.video(data['url'])
                st.info("El contenido de hoy es un video.")
        else:
            st.error("🚫 No se pudo conectar con la NASA (Error de Red). Prueba el Modo Offline.")

elif mode == "📂 Archivos Locales (Offline)" and selected_file:
    # LÓGICA OFFLINE
    image_path_to_analyze = os.path.join("data", selected_file)
    image_title = f"**Archivo Local:** {selected_file}"
    image_explanation = "Imagen cargada desde el almacenamiento local."
    
    # Mostrar la imagen local
    st.image(image_path_to_analyze, caption="Imagen Local", use_container_width=True)

# --- SECCIÓN DE ANÁLISIS ---
if analyze_btn and image_path_to_analyze:
    st.divider()
    st.subheader(f"🔬 Resultados del Análisis")
    st.write(f"{image_title}")

    try:
        analyzer = SpaceAnalyzer(image_path_to_analyze)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Conteo de Estrellas
            stars = analyzer.get_star_count()
            st.metric(label="✨ Cuerpos Celestes Detectados", value=stars)
        
        with col2:
            # Colorimetría
            rgb, label = analyzer.get_dominant_color()
            st.write(f"**Tonalidad:** {label}")
            hex_color = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
            st.markdown(f'<div style="background-color:{hex_color};width:100%;height:40px;border-radius:5px;"></div>', unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"Error analizando la imagen: {e}")