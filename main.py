import os
from dotenv import load_dotenv
from src.nasa_client import NasaClient
from src.image_manager import ImageManager
from src.analyzer import SpaceAnalyzer

load_dotenv()

def main():
    api_key = os.getenv("NASA_API_KEY")
    
    if not api_key:
        print("⚠️  Falta la API Key en el archivo .env")
        return

    # Instanciar el cliente
    client = NasaClient(api_key)

    print("📡 Conectando con el observatorio AstropyLab...")
    
    # Obtención de datos
    data = client.get_apod()

    if data:
        print("\n--- 🌌 REPORTE DEL OBSERVATORIO 🌌 ---")
        print(f"Título: {data.get('title')}")
        print(f"Fecha: {data.get('date')}")
        
        # --- Descarga y Análisis ---
        if data.get('media_type') == 'image':
            print("\n📸 Imagen detectada. Iniciando descarga...")
            
            manager = ImageManager()
            image_url = data.get('hdurl', data.get('url'))
            
            saved_path = manager.download_image(image_url, data.get('date'))
            
            if saved_path:
                print(f"✅ Guardado en: {saved_path}")
                print("\n🔬 Iniciando análisis de visión artificial...")
                
                try:
                    analyzer = SpaceAnalyzer(saved_path)
                    
                    # Obtener conteo de estrellas
                    num_stars = analyzer.get_star_count()
                    print(f"✨ Estrellas detectadas (aprox): {num_stars}")
                    
                    # Obtener color 
                    rgb, label = analyzer.get_dominant_color()
                    print(f"🎨 Colorimetría: {label} (RGB: {rgb})")
                    
                except Exception as e:
                    print(f"⚠️ Error durante el análisis: {e}")
            else:
                print("❌ Error al guardar la imagen.")
        else:
            print(f"\n🎥 El contenido es un video ({data.get('url')}), no se puede analizar.")

    else:
        # Si hay error de conexión (Timeout, etc)
        print("\n❌ No se pudieron obtener datos!")
        print("   -> Posible causa: La API de la NASA no responde (Timeout) o no hay internet")

if __name__ == "__main__":
    main()