from App import create_app

app = create_app() #Instancia de la aplicacion

if __name__ == '__main__': #Este bloque se ejecuta solo si este archivo se ejecuta directamente
    app.run(debug = True) #Esto permite mostrar errores detallados en el navegador y reinicia el servidor automáticamente si se hacen cambios en el código