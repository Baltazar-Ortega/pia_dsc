# -*-*-*-
"""
* Programa: COP120
* Objetivo: Generar Reporte Comparativo de Consumos y devoluciones por Planta,
*           Departamento y Producto
* Autor:    FCFM. GOAB. Gutiérrez Ortega Alberto Baltazar
* Fecha:    8/12/2020
"""

# -*-*-*- (Estos son ejemplos)
"""Proceso         Función
* procesar:        Procesar corte
* terminar:        Cerrar ambiente y terminar programa
"""

# -*-*-*-
"""
* (1) Todas las variables deben tener valor inicial
* (2) Utilizar .startswith() y .endswith() en lugar de usar slicing
* (3) No comparar valores booleanos con '=='. Usar 'if'
* (4) El límite de una línea es de 79 caracteres
* (5) Los 'imports' de distintos modulos deben estar en líneas separadas
* (f) Si una sentencia de 'import' necesita mas espacio, utilizar parentesis
* (6) Cualquier sentencia 'return' donde no se tenga que retornar un
*     valor, explícitamente debe retornar 'None'
* (7) Añadir como última línea en el programa: # FIN DE PROGRAMA.
"""

import re
import sys

from estructuras_de_datos.identidades import IdPlaCon, IdDptCon, IdCon, IdDev
from estructuras_de_datos.acumuladores import AcumConProd, AcumTotDpt
from estructuras_de_datos.tablas import TablaProductos, TablaTablas
from base_de_datos.conexion import obtener_cursor

def procesa_planta():
    global num_lin
    # Hacer el Id.Pla.Con.Lei
    id_pla_con_lei = IdPlaCon('lectura', reg_con[0])
    # Id.Pla.Con.Proc = Id.Pla.Con.Lei
    id_pla_con_proc = IdPlaCon('proceso', id_pla_con_lei.planta)
    # Obtener nombre de planta
    # Si en el registro cambia la planta, break
    while True:
        if id_pla_con_lei.planta != id_pla_con_proc.planta:
            print('Cambio de planta')
            num_hoja = 0
            break
        else:
            resultado = procesa_departamento()
            if not resultado:
                print("procesa_planta EOF")
                return None
            planta_actual = reg_con[0]
            id_pla_con_lei.planta = planta_actual
            print("Planta actual: ", id_pla_con_lei.planta)
    num_lin = MAX_LIN

def procesa_departamento():
    print("Dpt actual: ", reg_con[1])
    total_consumo_departamento = 0
    # "Recorrer" productos en BD
    for i in range(1, 4):
        consumo_prod = procesa_producto(i)
        total_consumo_departamento = total_consumo_departamento + \
                                     consumo_prod
    print("\tTotal de consumo del departamento: ", total_consumo_departamento, '\n')
    if fin_con == 1:
        return None
    else:
        return True


    # Hacer el Id.Dpt.Con.Lei
    id_dpt_con_lei = IdDptCon('lectura', reg_con[0], reg_con[1])
    # Id.Dpt.Con.Proc = Id.Dpt.Con.Lei
    id_dpt_con_proc = IdDptCon('proceso', id_dpt_con_lei.planta,  
                                id_dpt_con_lei.departamento)
    print("Departamento actual: ", id_dpt_con_proc)
    # Obtener nombre de Departamento
    # Acum.Tot.Dpt = 0
    acum_tot_dpt = AcumTotDpt()
    # i_prod = 1
    i_prod = 1
    # Si id de lectura != id de proceso, y se recorrieron productos, break
    

    # Construir total del departamento
    # Si num_lin + 6 > MAX_LIN, encabezado
    # num_lin + 1
    # Escribir total del departamento
    # num_lin = MAX_LIN
    
def procesa_producto(i_prod):
    global reg_con, arch_con, fin_con
    total_consumo = 0
    id_hv = IdCon('lectura', HV['pt'], HV['dpt'], HV['p'], HV['cvep']).id
    cambia_producto_en_registro = False
    while not cambia_producto_en_registro:
        print("V.consumo reg_con actual: ", reg_con[4])
        total_consumo = total_consumo + int(reg_con[4])

        id_lei = lee_consumo()
        if id_lei.id == id_hv:
            break

        # Convertir 'P00001' a i
        match_obj = re.search('[\d]+', reg_con[2])
        num_prod = int(match_obj.group())
        # print("num_prod sig.registro: ", num_prod)
        if num_prod != i_prod:
            cambia_producto_en_registro = True
    print(f"Total consumo de producto {i_prod}: ", total_consumo, '\n')
    return total_consumo

def lee_consumo():
    global reg_con, fin_con
    # Id.Ant = Id.Lei
    id_lei = IdCon('lectura', reg_con[0], reg_con[1], reg_con[2], reg_con[3])
    id_ant = id_lei
    # Lee registro (Si FinCon, FinCon = 1)
    lin_arch = arch_con.readline()
    if lin_arch == '':
        print("Final de arch consumos")
        fin_con = 1
    else:
        reg_con = lin_arch.rstrip().split(' ')
    # Condicion
    if fin_con == 1:
        id_lei = IdCon('lectura', HV['pt'], HV['dpt'], HV['p'], HV['cvep'])
    else:
        id_lei = IdCon('lectura', reg_con[0], reg_con[1], reg_con[2], reg_con[3])
    # Si Id.Lei <= Id.Ant entonces es archivo mal clasificado, y aborta
    if mal_clasificado(id_ant, id_lei):
        print("\n\tArchivo consumos mal clasificado")
        sys.exit(0)
    return id_lei

def lee_devolucion():
    global reg_dev, fin_dev
    # Id.Ant = Id.Lei
    id_lei = IdDev('lectura', reg_dev[0], reg_dev[1], reg_dev[2])
    id_ant = id_lei
    # Lee registro (Si FinDev, FinDev = 1)
    lin_arch = arch_dev.readline()
    if lin_arch == '':
        print("Final de arch devoluciones")
        fin_dev = 1
    else:
        reg_dev = lin_arch.rstrip().split(' ')
    # Condicion
    if fin_dev == 1:
        id_lei = IdDev('lectura', HV['pt'], HV['dpt'], HV['p'])
    else:
        id_lei = IdDev('lectura', reg_dev[0], reg_dev[1], reg_dev[2])
    # Si Id.Lei <= Id.Ant entonces es archivo mal clasificado, y aborta
    if mal_clasificado(id_ant, id_lei):
        print("\n\tArchivo devoluciones mal clasificado")
        sys.exit(0)
    return id_lei

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


def procesar_registros(registros, formato):
    return [procesar_registro(registro, formato) for registro in registros]

def procesar_registro(registro, formato):
    reg_dict = {}
    for campo, valor in zip(formato.keys(), registro):
        reg_dict[campo] = valor
    return reg_dict

if __name__ == "__main__":
    # Abrir archivo de consumos
    arch_con = open('consumos_test_3.txt', 'r')
    # Abrir archivo de devoluciones
    arch_dev = open('devoluciones.txt', 'r')
    
    # Abrir Base de datos
    cursor = obtener_cursor()
    tabla_productos = crear_tabla(cursor, 'Productos')
    tabla_tablas = crear_tabla(cursor, 'Tablas')

    # Abrir reporte
    num_lin = 0
    MAX_LIN = 88
    # Inicializacion de variables
    HV = {
        'pt': 'PT9',
        'dpt': 'DPT999',
        'p': 'P99999',
        'cvep': 'ZZ'
    }
    fin_con = 0
    fin_dev = 0
    num_hoja = 0
    # Pintar encabezado
    # Leer consumo
    reg_con = arch_con.readline().rstrip().split(' ')
    # Leer devolucion
    reg_dev = arch_dev.readline().rstrip().split(' ')

    # Si fin_con NO es = 1, entonces procesa_planta
    # while True:
    #     if fin_con == 1:
    #         break
    #     else:
    #         procesa_planta()

    # # Si SI es 1, cerrar archivos y reporte
    arch_con.close()
    arch_dev.close()