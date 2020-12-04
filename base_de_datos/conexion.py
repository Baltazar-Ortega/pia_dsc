import psycopg2
from configparser import ConfigParser

def configuracion(nombre_archivo='bd.ini', seccion='postgresql'):
    parser = ConfigParser()
    parser.read(nombre_archivo)
    params_conexion = {}
    if parser.has_section(seccion):
        params_seccion = parser.items(seccion)
        for param in params_seccion:
            params_conexion[param[0]] = param[1]
    else:
        raise Exception('Seccion {0} no encontrada en el archivo {1}'.format(
                         seccion, nombre_archivo))
    return params_conexion

def conectar_postgres():
    params_conexion = configuracion()
    conn = psycopg2.connect(**params_conexion)
    print("La conexion ha sido exitosa")
    return conn

def cursor():
    conn = conectar_postgres()
    cursor = conn.cursor()
    return cursor

