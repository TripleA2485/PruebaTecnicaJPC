from flask import request, render_template, redirect, url_for, current_app as app #Importa funciones necesarias desde Flask
from Business_Logic import BusinessLogic, PasswordGenerator

password_generator = PasswordGenerator() #Instancia del generador de contraseñas
Business_Logic = BusinessLogic() #Instancia de la logica de negocio

@app.route('/') #Ruta para la pagina de inicio, renderiza el archivo index.html
def home():
    return render_template('index.html')

@app.route('/gen_password', methods=['POST']) #Ruta de la generacion de contrasenas, que acepta solo solicitudes POST
def gen_password():
    longitud = request.form.get('longitud', type=int)
    numeros = 'numeros' in request.form #Verifica si la casilla "numeros" esta marcada en el formulario
    caracteres_especiales = 'caracteres_especiales' in request.form #Verifica si la casilla "carac_especiales" esta marcada en el formulario

    try:
        password = password_generator.generate(longitud, numeros, caracteres_especiales) #Llama al metodo 'generate', pasando los parametros del formulario
        password_generada = password["random_password"] #Extrae la contraseña generada de la respuesta JSON de la API
        print("Contraseña generada:", password_generada)
        return render_template('index.html', password=password_generada) #Renderiza index.html
    except Exception as e:
        return render_template('index.html', error=str(e)) #Renderiza la plantilla index.html en caso de error