class Password: #Clase Password que representa una contraseña
    def __init__(self, value): #Constructor de la clase que inicializa el valor de la contraseña
        self.value = value #Almacena el valor de la contraseña

    def __str__(self): #Metodo que retorna el valor de la contraseña como cadena de texto
        return self.value #Devuelve la contraseña como un string