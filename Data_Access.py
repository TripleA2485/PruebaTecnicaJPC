import requests #Modulo requests para realizar solicitudes HTTP
from Config import Config

class DataAccess: #Define clase DataAccess que se usa para manejo del acceso a datos en general
    def __init__(self):
        pass

class API_Client: #Define clase API_Client para interactuar con la API de generacion de contraseñas
    def __init__(self): 
        self.api_url = Config.NINJAS_API_URL #Asigna la URL de la API desde la configuracion
        self.headers = {'X-Api-Key': Config.API_KEY} #Configura los headers necesarios para la autenticacion en la API, y se utiliza la clave de la API

    def generate_password(self, longitud, numeros, caracteres_especiales): #Metodo para generar una contraseña a partir de la API
        
        try: #Realiza una solicitud GET a la API, pasando los parametros
            response = requests.get(f'{self.api_url}?length={longitud}&exclude_numbers={numeros}&exclude_special_chars={caracteres_especiales}', headers=self.headers)
            print(f"Respuesta de la API:", response.text)
            response.raise_for_status() #Verifica si la solicitud fue exitosa, sino se lanza una excepcion
            return response.json() #Retorna la respuesta en formato JSON
        except requests.exceptions.HTTPError as http_err: #Maneja errores HTTP
            raise Exception(f"Error en HTTP: {http_err}")
        except Exception as err: #Maneja otros tipos de errores
            raise Exception(f"Error al generar la contrasena: {err}")