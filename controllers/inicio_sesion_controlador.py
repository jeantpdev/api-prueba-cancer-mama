from models.iniciar_sesion_modelo import *

mod_inicio_sesion= Usuario()

class InicioSesionControlador():
    def iniciar_sesion(self):
        query=mod_inicio_sesion.login()
        return query
    
    def datos_usuario(self):
        query=mod_inicio_sesion.datos_usuario()
        return query
    
    def insertar_datos_paciente(self):
        query = mod_inicio_sesion.insertar_datos_paciente()
        return query