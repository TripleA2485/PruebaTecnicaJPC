from Data_Access import API_Client, DataAccess

class BusinessLogic: #Clase que presenta la capa de logica de negocio
    def __init__(self) -> None:
        self.data_access = DataAccess() #Instancia DataAccess para manejar el acceso a los datos dentro de la logica de negocio

class PasswordGenerator: #Clase PasswordGenerator, encargada de la generacion de contraseñas
    def __init__(self):
        self.api_client = API_Client() #Instancia API_Client, que es el cliente para interactuar con la API de generacion de contraseñas

    def generate(self, longitud, numeros, caracteres_especiales):
        return self.api_client.generate_password(longitud, numeros, caracteres_especiales) #Devuelve la contraseña generada por la API segun los parametros