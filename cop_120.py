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

from estructuras_de_datos.identidades import IdPlaCon, IdDptCon, IdCon, IdDev
from estructuras_de_datos.acumuladores import AcumConProd, AcumTotDpt
from estructuras_de_datos.tablas import TablaProductos, TablaTablas
from base_de_datos.conexion import cursor

def procesa_planta():
    global fin_con, num_lin, registro_con
    # Hacer el Id.Pla.Con.Lei
    id_pla_con_lei = IdPlaCon('lectura', registro_con[0])
    # Id.Pla.Con.Proc = Id.Pla.Con.Lei
    id_pla_con_proc = IdPlaCon('proceso', id_pla_con_lei.planta)
    num_hoja = 0
    # Obtener nombre de planta
    # Si en el registro cambia la planta, break
    while True:
        if id_pla_con_lei.planta != id_pla_con_proc.planta:
            print('Cambio de planta')
            break
        else:
            resultado = procesa_departamento()
            if not resultado:
                print("not resultado")
                return None
            planta_actual = registro_con[0]
            id_pla_con_lei.planta = planta_actual
            print("Planta actual: ", id_pla_con_lei.planta)
    num_lin = MAX_LIN

def procesa_departamento():
    global registro_con
    print("Dpt actual: ", registro_con[1])
    total_consumo_departamento = 0
    # "Recorrer" productos en BD
    for i in range(1, 4):
        consumo_prod = procesa_producto(i)
        if not consumo_prod: # Se llegó al EoF
            print("not consumo_prod")
            return None
        total_consumo_departamento = total_consumo_departamento + \
                                     consumo_prod

    print("Total de consumo del departamento: ", total_consumo_departamento, '\n')
    return True
    # Hacer el Id.Dpt.Con.Lei
    # Id.Dpt.Con.Proc = Id.Dpt.Con.Lei
    # Obtener nombre de Departamento
    # Acum.Tot.Dpt = 0
    # i_prod = 1
    # Si id de lectura != id de proceso, y se recorrieron productos, break


    # Construir total del departamento
    # Si num_lin + 6 > MAX_LIN, encabezado
    # num_lin + 1
    # Escribir total del departamento
    # num_lin = MAX_LIN
    
def procesa_producto(indice_prod):
    global registro_con, archivo_consumos, fin_con
    total_consumo = 0
    cambia_producto_en_registro = False
    while not cambia_producto_en_registro:
        print("Valor de consumo registro_con actual: ", registro_con[4])
        total_consumo = total_consumo + int(registro_con[4])

        # Leo el siguiente registro
        lectura = archivo_consumos.readline()
        if lectura == '':
            print("Ha llegado al final del archivo")
            fin_con = 1
            return None
        else:
            registro_con = lectura.rstrip().split(' ')

        # Convertir 'P00001' a i
        match_obj = re.search('[\d]+', registro_con[2])
        num_prod = int(match_obj.group())
        print("num_prod sig.registro: ", num_prod)
        if num_prod != indice_prod:
            cambia_producto_en_registro = True
    print(f"Total consumo de producto {indice_prod}: ", total_consumo, '\n')
    return total_consumo
        

    # print(f"Consumo de registro2 de producto {i}: ", registro_con[4])
    # sig_registro = archivo_consumos.readline().rstrip().split(' ')
    # print(f"Consumo de registro2 de producto {i}: ", sig_registro[4])


def lee_consumo():
    pass

if __name__ == "__main__":
    # Abrir archivo de consumos
    archivo_consumos = open('consumos_test_3.txt', 'r')
    # Abrir archivo de devoluciones
    archivo_devoluciones = open('devoluciones.txt', 'r')
    # Abrir Base de datos
    # Abrir reporte
    num_lin = 0
    MAX_LIN = 88
    # Inicializacion de variables
    fin_con = 0
    fin_dev = 0
    # Pintar encabezado
    # Leer consumo
    registro_con = archivo_consumos.readline().rstrip().split(' ')
    # Leer devolucion
    registro_dev = archivo_devoluciones.readline().rstrip().split(' ')
    # Si fin_con NO es = 1, entonces procesa_planta
    while True:
        if fin_con == 1:
            break
        else:
            procesa_planta()

    # Si SI es 1, cerrar archivos y reporte
    archivo_consumos.close()
    archivo_devoluciones.close()