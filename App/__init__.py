from flask import Flask

def create_app(): #Funcion que se encargada de crear e inicializar la aplicacion Flask
    app = Flask(__name__) #Instancia de la aplicacion Flask

    with app.app_context(): #Se usa un contexto de la aplicacion para asegurar de que se pueda acceder a ciertas variables de la aplicacion
        from . import Routes #Importa las rutas desde el modulo Routes
        return app #Retorna la instancia de la aplicacion