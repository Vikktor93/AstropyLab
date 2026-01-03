# 🔭 AstropyLab

**AstropyLab** es una aplicación desarrollada en Python que funciona como un observatorio astronómico personal. Se conecta a la API de la NASA para obtener imágenes del cosmos y utiliza técnicas de Visión por Computador (OpenCV) para realizar análisis automáticos de colorimetría y detección de cuerpos celestes.

## 🚀 Funcionalidades Actuales

* **Conexión API NASA:** Recupera automáticamente la "Imagen Astronómica del Día" (APOD) junto con su metada (título, fecha, explicación).
* **Gestión Inteligente de Descargas:** Descarga y almacena imágenes en alta definición localmente, organizándolas por fecha.
* **Análisis de Visión Artificial:**
    * 🎨 **Colorimetría:** Analiza los tonos predominantes para inferir características (nebulosas, filtros, etc.).
    * ✨ **Conteo de Estrellas:** Algoritmo de detección de puntos brillantes para estimar la densidad estelar en la imagen.
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
NASA_API_KEY=APIKEY
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
├── main.py                 # Punto de entrada de la aplicación
└── README.md               # Documentación
``` 

## ▶️ Uso
Asegúrate de tener el entorno activado y ejecuta el script principal:

```bash
python main.py
```

El sistema verificará la imagen del día, la descargará si es necesario y ejecutará el análisis visual, mostrando los resultados en la consola.

## 🔮 Roadmap (Próximos Pasos)
[ ] Interfaz Gráfica (GUI) para visualizar las imágenes y datos.

[ ] Integración con más APIs de la NASA (Mars Rover Photos, NeoWs).

[ ] Análisis más profundos (detección de constelaciones, clasificación de galaxias).

[ ] Automatización diaria (Cron jobs).


## 📄 Licencia
Este proyecto es de uso educativo y personal.