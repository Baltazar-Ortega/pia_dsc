# -*-*-*-
"""
* Programa: config
* Objetivo: Obtener parametros de conexion a BD desde el archivo bd.ini
* Autor:    FCFM. GOAB. Gutiérrez Ortega Alberto Baltazar
* Fecha:    8/12/2020
"""

# -*-*-*- 
"""
* Import          Funcion
* Libreria
* ConfigParser    Clase auxiliar para parsear archivos con cierto formato.
*  
* Proceso         Función
* configuracion:  Retorna parametros para la conexión a la BD postgresql.
"""

# -*-*-*-
"""
* (1) Utilizar instrucciones de reutilizacion del programa COP120.
"""

from configparser import ConfigParser

def configuracion(nombre_archivo='base_de_datos/bd.ini', 
                  seccion='postgresql'):
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