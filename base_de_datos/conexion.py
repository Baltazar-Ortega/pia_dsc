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

