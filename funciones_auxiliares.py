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
        # Son iguales. Bien ordenado.
        return None
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
    registros_formateados = procesar_registros(registros, tabla.formato_registro)
    tabla.llenar_tabla(registros_formateados)
    return tabla