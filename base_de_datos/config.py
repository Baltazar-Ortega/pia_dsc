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