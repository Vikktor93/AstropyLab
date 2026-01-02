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
            response = requests.get(endpoint, params=params)
            response.raise_for_status() 
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error conectando a la NASA: {e}")
            return None