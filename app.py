from flask import Flask
from flask_cors import CORS
from config import *
from routes.inicio_sesion_rutas import inicio_sesion
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret' # Clave secreta para firmar los JWT
cors = CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5000"}})
jwt = JWTManager(app)


#El método register_blueprint se utiliza para conectar y activar un objeto Blueprint en la aplicación principal de Flask. Al registrar un blueprint, se pueden definir rutas, vistas, controladores y otros aspectos relacionados con esa parte específica de la aplicación.
app.register_blueprint(inicio_sesion)

def pagina_no_encontrada(error):
    return "<h1>La pagina a la que intentas acceder no existe...</h1>"

if __name__=="__main__":
    app.register_error_handler(404 , pagina_no_encontrada)
    app.run(port=5000, debug=True)
