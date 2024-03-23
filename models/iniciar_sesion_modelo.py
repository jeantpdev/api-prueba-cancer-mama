from config import *
from breast.knn import *
from flask import request, jsonify
from flask_jwt_extended import create_access_token
import json
import pandas as pd
import supabase
import requests

class Usuario():

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1tcGh6YXl4dnZoZHRydGN2anNxIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODI2MDY3NDYsImV4cCI6MTk5ODE4Mjc0Nn0.QZWfmiw-KMFgHOTSyxNGFlcOZvDRa305OkZH-YHTzDI',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1tcGh6YXl4dnZoZHRydGN2anNxIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODI2MDY3NDYsImV4cCI6MTk5ODE4Mjc0Nn0.QZWfmiw-KMFgHOTSyxNGFlcOZvDRa305OkZH-YHTzDI',
        'Content-Type' : 'application/json'
        }

    def login(self):
        username = request.json.get('usuario')
        password = request.json.get('contrasena')

        SUPABASE_URL = 'https://mmphzayxvvhdtrtcvjsq.supabase.co'
        SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1tcGh6YXl4dnZoZHRydGN2anNxIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODI2MDY3NDYsImV4cCI6MTk5ODE4Mjc0Nn0.QZWfmiw-KMFgHOTSyxNGFlcOZvDRa305OkZH-YHTzDI'
        # Conectamos con Supabase
        client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

        # Buscamos el usuario en la tabla 'users'
        query = client.table('usuario').select('*').eq('usuario', username).eq('contrasena', password)
        res = query.execute()
        # Si el usuario existe y la contraseña es correcta, se devuelve un token JWT
        if len(res.data) == 1:
            access_token = create_access_token(identity=username)
            print("access_token generado con éxito")

        return jsonify({"acceso": "AUTORIZADO" ,"access_token": access_token})
    
    def datos_usuario(self):
            
        response = requests.get('https://mmphzayxvvhdtrtcvjsq.supabase.co/rest/v1/usuario?select=*', 
                                headers= self.headers)
        return response.content

    # Realizar una solicitud POST a la API de SUPABASE
    def insertar_resultados_bd(self, datos_insertar):
        try:
           requests.post('https://mmphzayxvvhdtrtcvjsq.supabase.co/rest/v1/registros_prueba_usuario', 
                data = datos_insertar, 
                headers = self.headers)
        except requests.exceptions.HTTPError as err:
            print(err)
        return 201
    
    def convertir_a_string(self, resulatdo_prueba_sin_formatear):
        res = str(resulatdo_prueba_sin_formatear)
        x = res.replace("[", "")
        y = x.replace("]","")
        return y

    def convertir_a_json(self, edad, menopausia, tumorTamaño, invNodes, nodesCaps, gradoTumor, breast, breastQuead, irradiat, resultado_prueba, precision_modelo):

        rangos_edad = {
            0: "20-29",
            1: "30-39",
            2: "40-49",
            3: "50-59",
            4: "60-69",
            5: "70-79"
        }
        if edad in rangos_edad:
            edad = rangos_edad[edad]

        rangos_menopausia = {
            0: "ge40",
            1: "lt40",
            2: "premeno",  
        }
        if menopausia in rangos_menopausia:
            menopausia = rangos_menopausia[menopausia]

        rangos_tumorTamaño = {
            0: "0-4",
            1: "5-9",
            2: "10-14",
            3: "15-19",
            4: "20-24",
            5: "25-29",
            6: "30-34",
            7: "35-39",
            8: "40-44",
            9: "45-49",
            10: "50-54"
        }
        if tumorTamaño in rangos_tumorTamaño:
            tumorTamaño = rangos_tumorTamaño[tumorTamaño]

        rangos_invNodes = {
            0: "0-2",
            1: "3-5",
            2: "6-8",
            3: "9-11",
            4: "12-14",
            5: "15-17",
            6: "24-26"
        }
        if invNodes in rangos_invNodes:
            invNodes = rangos_invNodes[invNodes]

        rangos_nodesCaps = {
            0: "No",
            1: "Si"
        }
        if nodesCaps in rangos_nodesCaps:
            nodesCaps = rangos_nodesCaps[nodesCaps]

        rangos_gradoTumor = {
            0: "1",
            1: "2",
            2: "3"
        }
        if gradoTumor in rangos_gradoTumor:
            gradoTumor = rangos_gradoTumor[gradoTumor]

        rangos_breast = {
            0: "Izquierda",
            1: "Derecha"
        }
        if breast in rangos_breast:
            breast = rangos_breast[breast]

        rangos_breastQuead = {
            0: "central",
            1: "inferior izquierda",
            2: "superior izquierda",
            3: "inferior derecha",
            4: "superior izquierda"
        }
        if breastQuead in rangos_breastQuead:
            breastQuead = rangos_breastQuead[breastQuead]

        rangos_irradiat = {
            0: "No",
            1: "Si"
        }
        if irradiat in rangos_irradiat:
            irradiat = rangos_irradiat[irradiat]


        datos_json = {
            "age": edad,
            "menopause": menopausia,
            "tumor_size": tumorTamaño,
            "inv_nodes": invNodes,
            "nodes_caps": nodesCaps,
            "deg_malig": gradoTumor,
            "breast": breast,
            "breast_quead": breastQuead,
            "irradiat": irradiat,
            "class": resultado_prueba,
            "precision" : precision_modelo
        }
        datos_insertar = json.dumps(datos_json)

        return datos_insertar
    
    def insertar_datos_paciente(self):

        datos_usuario_temporal = []
        datos_usuario = {
        'edad': request.json['edad'],
        'menopausia': request.json['menopausia'],
        'tumorTamaño': request.json['tumorTamaño'],
        'invNodes': request.json['invNodes'],
        'nodesCaps': request.json['nodesCaps'],
        'gradoTumor': request.json['gradoTumor'],
        'breast': request.json['breast'],
        'breastQuead': request.json['breastQuead'],
        'irradiat': request.json['irradiat'],
        }

        datos_usuario_temporal.append(datos_usuario)
        edad = datos_usuario['edad']
        menopausia = datos_usuario['menopausia']
        tumorTamaño = datos_usuario['tumorTamaño']
        invNodes = datos_usuario['invNodes']
        nodesCaps = datos_usuario['nodesCaps']
        gradoTumor = datos_usuario['gradoTumor']
        breast = datos_usuario['breast']
        breastQuead = datos_usuario['breastQuead']
        irradiat = datos_usuario['irradiat']
        
        new_data = pd.DataFrame([[edad, menopausia, tumorTamaño, invNodes, nodesCaps, gradoTumor, breast, breastQuead, irradiat]], columns=['age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat'])

        resultado_prueba_sin_formatear, precision = knn_prediction(new_data)

        resultado_prueba = self.convertir_a_string(resultado_prueba_sin_formatear)

        precision_modelo = str(precision)

        datos_insertar = self.convertir_a_json(edad, menopausia, tumorTamaño, invNodes, nodesCaps, gradoTumor, breast, breastQuead, irradiat, resultado_prueba, precision_modelo)
        
        code = self.insertar_resultados_bd(datos_insertar)

        return jsonify({"status": code,"resultado_prueba": resultado_prueba, "precision": precision_modelo})
