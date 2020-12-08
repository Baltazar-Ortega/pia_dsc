# -*-*-*-
"""
* Programa: funciones_auxiliares
* Objetivo: Proveer funciones secundarias al programa COP120
* Autor:    FCFM. GOAB. Gutiérrez Ortega Alberto Baltazar
* Fecha:    8/12/2020
"""

# -*-*-*- 
"""
* Import               Función
* Clase
* TablaProductos       Hereda de Tabla. Estructura para Tabla de BD 
*                      "Productos".
* TablaTablas          Hereda de Tabla. Estructura para Tabla de BD "Tablas".
* 
* Proceso              Función
* procesar_registros:  Retornar lista de registros ya formateados.
* procesar_registro:   Retorna registro formateado.
* mal_clasificado:     Retorna booleano para determinar si el orden del 
*                      registro es adecuado.
* crear_tabla:         Retorna una tabla de base de datos. La tabla 
*                      retornada depende de nombre_tabla.
"""

# -*-*-*-
"""
* (1) Utilizar instrucciones de reutilizacion del programa COP120.
"""

from estructuras_de_datos.tablas import TablaProductos, TablaTablas

def procesar_registros(registros, formato):
    return [procesar_registro(registro, formato) for registro in registros]

def procesar_registro(registro, formato):
    reg_dict = {}
    for campo, valor in zip(formato.keys(), registro):
        reg_dict[campo] = valor
    return reg_dict

def mal_clasificado(id_ant, id_lei):
    if id_lei.id < id_ant.id:
        return True
    elif id_ant.id == id_lei.id:
        return False
    else:
        return False

def crear_tabla(cursor, nombre_tabla):
    cursor.execute(f'SELECT * FROM "{nombre_tabla}"')
    registros = cursor.fetchall()
    tabla = None
    if nombre_tabla == 'Productos':
        tabla = TablaProductos()
    else:
        tabla = TablaTablas()
    registros_formateados = procesar_registros(registros, 
                                               tabla.formato_registro)
    tabla.llenar_tabla(registros_formateados)
    return tabla