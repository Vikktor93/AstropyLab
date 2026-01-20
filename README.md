# 🔭 AstropyLab

**AstropyLab** es una aplicación desarrollada en Python que funciona como un observatorio astronómico personal. Se conecta a la API de la NASA para obtener imágenes del cosmos y utiliza técnicas de Visión por Computador (OpenCV) para realizar análisis automáticos de colorimetría y detección de cuerpos celestes.

Cuenta con una **Interfaz Gráfica (GUI)** moderna basada en Streamlit, gráficos interactivos y un **Modo Offline** para analizar imágenes locales.

## 🚀 Funcionalidades Actuales

* **Conexión API NASA:** Recupera automáticamente la "Imagen Astronómica del Día" (APOD) junto con su metadata (título, fecha, explicación).
* **Modo Offline:** Sistema de contingencia para cargar y analizar imágenes guardadas localmente en la carpeta `data/`.
* **Interfaz Interactiva:** Dashboard web para visualización de datos en tiempo real.
* **Gestión Inteligente de Descargas:** Descarga y almacena imágenes en alta definición localmente, organizándolas por fecha.
* **Análisis de Visión Artificial:**
    * 🎨 **Colorimetría:** Detección de tonalidades predominantes para inferir composición (ejemplo: nebulosas, presencia de oxígeno vs hidrógeno, etc.)
    * ✨ **Conteo de Estrellas:** Algoritmo de detección de puntos brillantes para estimar la densidad estelar en la imagen.
    * 📊 **Espectrómetro RGB:** Histograma interactivo que descompone la luz de la imagen en sus canales de color (Rojo, Verde, Azul) para análisis espectral.
* **Arquitectura Modular:** Estructura escalable basada en POO.

## 🛠️ Requisitos Previos

* **Python 3.10.19 o superior**
* **Anaconda** o Miniconda (Gestor de entornos)
* Una **API Key de la NASA** (Gratuita en [api.nasa.gov](https://api.nasa.gov/))

## ⚙️ Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/Vikktor93/AstropyLab
```
```bash
cd AstropyLab
```

### 2. Configurar el Entorno Virtual (Anaconda)
Se recomienda utilizar un entorno aislado para manejar las dependencias de ciencia de datos.
```bash
# Crear el entorno
conda create --name astropylab python=3.10.19

# Activar el entorno
conda activate astropylab

# Instalar dependencias
conda install -c conda-forge requests python-dotenv opencv matplotlib numpy
``` 

### 3. Configurar Variables de Entorno
Crea un archivo llamado ```.env``` en la raíz del proyecto.

```toml
NASA_API_KEY = AQUI_VA_API_KEY
``` 

## 📂 Estructura del Proyecto

``` 
AstropyLab/
│
├── data/                   # Almacenamiento local de imágenes descargadas
│   └── .gitkeep            # Mantiene la carpeta en git sin subir las fotos
│
├── src/                    # Código Fuente
│   ├── __init__.py
│   ├── nasa_client.py      # Cliente de conexión a la API
│   ├── image_manager.py    # Gestor de descargas y archivos
│   └── analyzer.py         # Módulo de Computer Vision (OpenCV)
│
├── .env                    # Credenciales 
├── .gitignore              # Configuración de exclusiones
├── app.py                  # Interfaz Gráfica (Streamlit)
├── main.py                 # Punto de entrada de la aplicación
├── environment.yml         # Dependencias
└── README.md               # Documentación
``` 

## ▶️ Uso
Asegúrate de tener el entorno activado y ejecuta el script principal:

```bash
streamlit run app.py
```

Se abrirá una pestaña en tu navegador donde podrás:  
📡 **Modo Online:** Consultar la APOD (Astronomy Picture of the Day) en tiempo real.  
📂 **Modo Offline:** Analizar imágenes de la colección local.  
🔬 **Analizar:** Ejecutar algoritmos de visión computacional para obtener conteo de estrellas, colorimetría y espectro RGB.  

## 🔮 Roadmap (Próximos Pasos)
✅ Interfaz Gráfica (GUI) para visualizar las imágenes y datos (Streamlit)

✅ Modo Offline (Análisis de Imágenes locales).

✅ Gráficos Interactivos (Histograma RGB).

[ ] Integración con más APIs de la NASA (Mars Rover Photos, NeoWs).

[ ] Deep Learning: Clasificación automática de galaxias (Espiral/Elíptica) usando Redes Neuronales.

[ ] Astrometría: Detección de constelaciones y patrones estelares.

[ ] Automatización diaria (Cron jobs).


## 📄 Licencia
Este proyecto es de uso educativo y personal.