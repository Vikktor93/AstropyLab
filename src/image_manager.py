import requests
import os
from datetime import datetime

class ImageManager:
    def __init__(self, storage_path="data"):
        self.storage_path = storage_path
        # Crear la carpeta data si no existe
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)
    
    # Descarga la imagen desde la URL y la guarda. Retorna la ruta del archivo guardado.
    def download_image(self, url, date):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                file_name = f"{date}_astropylab.jpg"
                file_path = os.path.join(self.storage_path, file_name)

                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                
                print(f"Imagen guardada en: {file_path}")
                return file_path
            else:
                print("No se pudo descargar la imagen.")
                return None
        except Exception as e:
            print(f"Error en la descarga: {e}")
            return None