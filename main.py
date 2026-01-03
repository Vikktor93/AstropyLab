import os
from dotenv import load_dotenv
from src.nasa_client import NasaClient
from src.image_manager import ImageManager
from src.analyzer import SpaceAnalyzer

load_dotenv()

def main():
    api_key = os.getenv("NASA_API_KEY")
    
    if not api_key:
        print("Falta la API Key en el archivo .env")
        return

    client = NasaClient(api_key)

    print("📡 Conectando con el observatorio AstropyLab...")
    
    data = client.get_apod()

    if data:
        print("\n--- REPORTE DEL OBSERVATORIO ---")
        print(f"Título: {data.get('title')}")
        print(f"Fecha: {data.get('date')}")
        print(f"URL: {data.get('url')}")
        
        explanation = data.get('explanation', '')
        print(f"\nDescripción: {explanation[:150]}...") 

        # --- Descarga y Análisis ---
        
        # Verificación de que sea una imagen (APOD a veces pone videos)
        if data.get('media_type') == 'image':
            print("\n Imagen detectada. Iniciando descarga...")
            
            manager = ImageManager()
            image_url = data.get('hdurl', data.get('url'))
            
            saved_path = manager.download_image(image_url, data.get('date'))
            
            if saved_path:
                print(f"✅ Guardado en: {saved_path}")
                print("\n Iniciando análisis de visión artificial...")
                
                try:
                    analyzer = SpaceAnalyzer(saved_path)
                    analyzer.analyze_colors()
                    analyzer.count_stars()
                except Exception as e:
                    print(f"⚠️ Error durante el análisis: {e}")
            else:
                print("❌ Error al guardar la imagen")
        
        else:
            print(f"\n El contenido de hoy es un {data.get('media_type')}, no se puede analizar con visión artificial")

    else:
        print("❌ No se pudieron obtener datos el día de hoy")

if __name__ == "__main__":
    main()