import requests as rq

class Coordinates:
    def __init__(self, address):
        headers = {"User-Agent": "MiApp"} 
        url = "https://nominatim.openstreetmap.org/search?"
        params = {
            "q": address,
            "format": "json",
            "limit": 1
        }
        try:
            response = rq.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()  
            data = response.json()
            if data:  
                self.data = data[0]
            else:
                print(f"No se encontraron coordenadas para '{address}'.")
                self.data = None
        except rq.exceptions.RequestException as e:
            print(f"Error al obtener coordenadas: {e}")
            self.data = None

    def getCoordinates(self):
        if self.data:
            return self.data['lat'], self.data['lon']
        else:
            return None, None  

