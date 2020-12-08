# -*-*-*-
"""
* Programa: conexion
* Objetivo: Proveer funciones para utilizar la base de datos de postgresql
* Autor:    FCFM. GOAB. Gutiérrez Ortega Alberto Baltazar
* Fecha:    8/12/2020
"""

# -*-*-*- 
"""
* Import              Funcion
* Libreria
* psycopg             Libreria externa para facilitar conexion a postgresql.
* Proceso
* configuracion       Módulo local para obtener los datos para conectarse a la
*                     base de datos
*  
* Proceso             Función
* conectar_postgres:  Retorna conexión a la base de datos.
* obtener_cursor:     Retorna cursor de la conexion. 
"""

# -*-*-*-
"""
* (1) Utilizar instrucciones de reutilizacion del programa COP120.
"""

import psycopg2

from base_de_datos.config import configuracion

def conectar_postgres():
    params_conexion = configuracion()
    conn = psycopg2.connect(**params_conexion)
    return conn

def obtener_cursor():
    conn = conectar_postgres()
    cursor = conn.cursor()
    return cursor

