import requests

class NasaClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.nasa.gov"
        
    # Obtiene la 'Astronomy Picture of the Day'. Retorna un diccionario con la data o None si falla.
    def get_apod(self, high_definition=True):
        endpoint = f"{self.base_url}/planetary/apod"
        
        params = {
            "api_key": self.api_key,
            "hd": high_definition
        }

        try:
            print(f"📡 Conectando a: {endpoint}")
            response = requests.get(endpoint, params=params, timeout=30) # Timeout para que no se quede pegado eternamente
            response.raise_for_status() # Esto salta si hay error 404, 500, 504, etc.
            return response.json()
            
        except requests.exceptions.HTTPError as e:
            print(f"❌ Error HTTP de la NASA: {e}")
            return None
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error de Conexión: {e}")
            return None