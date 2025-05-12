import requests as rq

class Iss:
    def __init__(self):  
        url = "http://api.open-notify.org/iss-now.json"
        try:
            response = rq.get(url, timeout=10)
            response.raise_for_status()  
            self.data = response.json()
        except rq.exceptions.RequestException as e:
            print(f"Error al obtener la posición de la ISS: {e}")
            self.data = None

    def getCoordinates(self):
        if self.data:
            return self.data['iss_position']['latitude'], self.data['iss_position']['longitude']
        else:
            return None, None
