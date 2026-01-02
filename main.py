import os
from dotenv import load_dotenv
from src.nasa_client import NasaClient

load_dotenv()

def main():
    api_key = os.getenv("NASA_API_KEY")
    
    if not api_key:
        print("Falta la API Key en el archivo .env")
        return

    client = NasaClient(api_key)

    print("📡 Conectando con el observatorio...")
    
    data = client.get_apod()

    if data:
        print("\n--- REPORTE DEL OBSERVATORIO ---")
        print(f"Título: {data.get('title')}")
        print(f"Fecha: {data.get('date')}")
        print(f"URL Imagen: {data.get('url')}")
        
        explanation = data.get('explanation', '')
        print(f"\nDescripción: {explanation[:150]}...") 
    else:
        print("No se pudieron obtener datos el día de hoy")

if __name__ == "__main__":
    main()