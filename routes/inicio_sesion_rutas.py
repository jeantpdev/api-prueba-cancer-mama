from flask import Blueprint
from flask_cors import  cross_origin
from controllers.inicio_sesion_controlador import *


con_inicio_sesion= InicioSesionControlador()
inicio_sesion = Blueprint('inicio_sesion', __name__)

@inicio_sesion.route('/login', methods=['POST'])
@cross_origin()  
def login():
   return con_inicio_sesion.iniciar_sesion()

@inicio_sesion.route('/datos_usuarios', methods=['GET'])
@cross_origin()  
def datos_usuario():
   return con_inicio_sesion.datos_usuario()

@inicio_sesion.route('/insertar_datos_paciente', methods=['POST'])
@cross_origin()  
def insertar_datos_paciente():
   return con_inicio_sesion.insertar_datos_paciente()
