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
from datetime import datetime

from fpdf import FPDF

from estructuras_de_datos.identidades import IdPlaCon, IdDptCon, IdCon, IdDev
from estructuras_de_datos.acumuladores import AcumConProd, AcumTotDpt
from reporte.funciones_reporte import (imprimir_encabezado, construir_detalle, 
                                      imprimir_linea, imprimir_tot_dpt, 
                                      imprimir_lineas_blanco)
from base_de_datos.conexion import obtener_cursor
from funciones_auxiliares import (procesar_registro, procesar_registros, 
                                  mal_clasificado, crear_tabla)

def procesa_planta():
    global num_lin, num_hoja
    # Id.Pla.Con.Proc = Id.Pla.Con.Lei
    id_pla_con_lei = IdPlaCon('lectura', reg_con[0])
    id_pla_con_proc = IdPlaCon('proceso', id_pla_con_lei.planta)
    # Num.Hoja = 0
    num_hoja = 0
    # Si Id.Pla.Con.Lei NO es != Id.Pla.Con.Proc, 
    # entonces Procesa Departamento
    while True:
        if id_pla_con_lei.planta != id_pla_con_proc.planta:
            break
        else:
            continuar = procesa_departamento()
            if not continuar:
                return None
            id_pla_con_lei.planta = reg_con[0]
    # Si Id.Pla.Con.Lei es != Id.Pla.Con.Proc, continua
    # Num.Lin = Max.Lin
    num_lin = MAX_LIN

def procesa_departamento():
    global acum_tot_dpt, num_lin
    # Id.Dpt.Con.Proc = Id.Dpt.Con.Lei
    id_dpt_con_lei = IdDptCon('lectura', reg_con[0], reg_con[1])
    id_dpt_con_proc = IdDptCon('proceso', id_dpt_con_lei.planta,  
                                id_dpt_con_lei.departamento)
    # Obtener nombres de Planta y Departamento
    dpt_nom = obtener_nombre('departamento', id_dpt_con_proc)
    plt_nom = obtener_nombre('planta', id_dpt_con_proc)
    encabezado(pdf, fecha, id_dpt_con_proc.planta, plt_nom, 
               id_dpt_con_proc.departamento, dpt_nom)
    # Acum.Tot.Dpt = 0
    # I = 1
    acum_tot_dpt = AcumTotDpt()
    i_prod = 1
    # Si Id.Dpt.Con.Lei NO es != Id.Dpt.Con.Proc, 
    # entonces Procesa Producto
    while True:
        if (id_dpt_con_lei.departamento != id_dpt_con_proc.departamento or
            id_dpt_con_lei.planta != id_dpt_con_proc.planta) and \
            i_prod > tabla_productos.num_elementos:
            break
        else:
            procesa_producto(i_prod, id_dpt_con_proc)
            i_prod = i_prod+1
            if fin_con == 1 and i_prod > tabla_productos.num_elementos:
                break
            id_dpt_con_lei.departamento = reg_con[1]
            id_dpt_con_lei.planta = reg_con[0]
    # Imprimir linea blanco
    # Num.Lin + 1
    imprimir_linea(pdf, '', num_lin)
    num_lin = num_lin+1
    # Si Num.Lin + 6 > MAX_LIN, imprimir_encabezado
    espacio_necesario = 0
    espacio_necesario = num_lin+6
    if espacio_necesario > MAX_LIN:
        imprimir_lineas_blanco(pdf, num_lin)
        plt_nom = obtener_nombre('planta', id_dpt_con_proc)
        encabezado(pdf, fecha, id_dpt_con_proc.planta, plt_nom, 
                   id_dpt_con_proc.departamento, dpt_nom)
    # Escribir total del departamento
    imprimir_tot_dpt(pdf, num_lin, id_dpt_con_proc.departamento, dpt_nom, 
                     acum_tot_dpt)
    imprimir_lineas_blanco(pdf, num_lin+6)
    # Num.Lin = Max.Lin
    num_lin = MAX_LIN
    if fin_con == 1:
        return None
    else:
        return True

def procesa_producto(i_prod, id_dpt_con_proc):
    global acum_tot_dpt, num_lin
    # Con.Almacen(Acum) = 0
    # Con.Produccion(Acum) = 0
    acum_con_prod = AcumConProd()
    # Inicializacion de variables
    detalle = ''
    plt_nom = ''
    dpt_nom = ''
    pd_id = ''
    imp_rep_alm = 0
    imp_rep_produ = 0
    espacio_necesario = 0
    # Variables para crear reporte diferencia
    cons_dif = 0 
    imp_dif = 0 
    a_favor = ''

    prod_actual = tabla_productos.obtener_registro_por_indice(i_prod)
    if fin_con == 1:
        # Si existe el pd en bd, pero no hay pds en consumos
        # Terminó el archivo. Se quedó en P00001. 
        # Falta imprimir con 0 los otros
        if num_lin > MAX_LIN:
            plt_nom = obtener_nombre('planta', id_dpt_con_proc)
            dpt_nom = obtener_nombre('departamento', id_dpt_con_proc)
            # imprimir_lineas_blanco(pdf, num_lin + 1)
            encabezado(pdf, fecha, id_dpt_con_proc.planta, plt_nom, 
                       id_dpt_con_proc.departamento, dpt_nom)
        detalle = construir_detalle(prod_actual, acum_con_prod, 0, 0, 0, 0, 
                                    '   ')
        imprimir_linea(pdf, detalle, num_lin)
        num_lin = num_lin+1
        return

    # ¿Producto(ID) == Producto(I)?
    pd_id = reg_con[2]
    if pd_id == prod_actual['Producto']:
        # Calcular Reporte Almacen
        # Recorrer consumos hasta dejar de encontrar RA
        termina_con_ra = False
        acum_con_prod.con_almacen = calcular_reporte_almacen(prod_actual, 
                                                             id_dpt_con_proc)
        imp_rep_alm = acum_con_prod.con_almacen*prod_actual['CostoUnitario']
        if fin_con == 1:
            termina_con_ra = True
        # Calcular Reporte Produccion
        # Recorrer consumos hasta dejar de encontrar RP
        if not termina_con_ra:
            acum_con_prod.con_produccion = \
            calcular_reporte_produccion(prod_actual, id_dpt_con_proc)
            imp_rep_produ = acum_con_prod.con_produccion*\
            prod_actual['CostoUnitario']
        # Calcular Reporte Diferencia
        cons_dif = abs(acum_con_prod.con_almacen-acum_con_prod.con_produccion)
        imp_dif = cons_dif*prod_actual['CostoUnitario']
        if acum_con_prod.con_almacen > acum_con_prod.con_produccion:
            a_favor = 'ALMACEN'
        elif acum_con_prod.con_almacen < acum_con_prod.con_produccion:
            a_favor = 'PRODUCCION'
        elif acum_con_prod.con_almacen == acum_con_prod.con_produccion:
            a_favor = ''
        # Construir detalle
        detalle = construir_detalle(prod_actual, acum_con_prod, imp_rep_alm, 
                                    imp_rep_produ, cons_dif, imp_dif, a_favor)
        # Imprimir detalle
        imprimir_linea(pdf, detalle, num_lin)
    else:
        # ¿Producto(ID) no existe? Si es 0, significa que si.
        exi = tabla_productos.existe_registro(reg_con[2]) 
        if exi == 0:
            # Abortar
            print("\n\tEl producto no existe en la tabla Productos\n")
            print("\nAbortar")
            sys.exit(0)
        elif exi == 1:
            # Construir detalle de blancos y ceros
            # Cuando reg_con, por ej. pasó de P00001 a P00003
            detalle = construir_detalle(prod_actual, acum_con_prod, 0, 0, 0, 
                                        0, '   ')
            # Imprimir detalle
            imprimir_linea(pdf, detalle, num_lin)
    # Calcular Imp.Alm
    acum_tot_dpt.imp_alm = acum_tot_dpt.imp_alm+imp_rep_alm
    # Calcular Imp.Prod
    acum_tot_dpt.imp_prod = acum_tot_dpt.imp_prod+imp_rep_produ
    # Case A.Favor
    if a_favor == 'ALMACEN':
        acum_tot_dpt.dif_fav_alm = acum_tot_dpt.dif_fav_alm+imp_dif
    elif a_favor == 'PRODUCCION':
        acum_tot_dpt.dif_fav_prod = acum_tot_dpt.dif_fav_prod+imp_dif

    espacio_necesario = num_lin+1
    if espacio_necesario > MAX_LIN:
        plt_nom = obtener_nombre('planta', id_dpt_con_proc)
        dpt_nom = obtener_nombre('departamento', id_dpt_con_proc)
        # imprimir_lineas_blanco(pdf, num_lin + 1)
        encabezado(pdf, fecha, id_dpt_con_proc.planta, plt_nom, 
                   id_dpt_con_proc.departamento, dpt_nom)
    else:
        num_lin = num_lin+1

def encabezado(pdf, fecha, plt_cve, plt_nom, dpt_clave, dpt_nom):
    global num_hoja, num_lin
    num_hoja = num_hoja + 1
    imprimir_encabezado(pdf, NOMBRE_PROGRAMA, fecha, plt_cve, plt_nom, 
                        dpt_clave, dpt_nom, num_hoja)
    num_lin = 11

def lee_consumo():
    global reg_con, fin_con
    # Id.Ant = Id.Lei
    id_lei = IdCon('lectura', reg_con[0], reg_con[1], reg_con[2], reg_con[3])
    id_ant = id_lei
    # Lee registro (Si FinCon, FinCon = 1)
    linea_archivo = arch_con.readline()
    if linea_archivo == '':
        # Final de archivo "consumos"
        fin_con = 1
    else:
        reg_con = linea_archivo.rstrip().split(' ')
    # ¿FinCon = 1?
    if fin_con == 1:
        id_lei = IdCon('lectura', HV['pt'], HV['dpt'], HV['p'], HV['cvep'])
    else:
        id_lei = IdCon('lectura', reg_con[0], reg_con[1], reg_con[2], 
                       reg_con[3])
    # Si Id.Lei <= Id.Ant entonces es archivo mal clasificado, y aborta
    if mal_clasificado(id_ant, id_lei):
        print("\n\tArchivo 'consumos' mal clasificado")
        sys.exit(0)

def lee_devolucion():
    global reg_dev, fin_dev
    # Id.Ant = Id.Lei
    id_lei = IdDev('lectura', reg_dev[0], reg_dev[1], reg_dev[2])
    id_ant = id_lei
    # Lee registro (Si FinDev, FinDev = 1)
    linea_archivo = arch_dev.readline()
    if linea_archivo == '':
        # Final de archivo "devoluciones"
        fin_dev = 1
    else:
        reg_dev = linea_archivo.rstrip().split(' ')
    # ¿FinDev = 1?
    if fin_dev == 1:
        id_lei = IdDev('lectura', HV['pt'], HV['dpt'], HV['p'])
    else:
        id_lei = IdDev('lectura', reg_dev[0], reg_dev[1], reg_dev[2])
    # Si Id.Lei <= Id.Ant entonces es archivo mal clasificado, y aborta
    if mal_clasificado(id_ant, id_lei):
        print("\n\tArchivo 'devoluciones' mal clasificado")
        sys.exit(0)

#### Submodulos

def obtener_nombre(campo, identidad):
    if campo == 'planta':
        clave = 'T04'+identidad.planta
    elif campo == 'departamento':
        clave = 'T05'+identidad.planta+identidad.departamento
    exi = tabla_tablas.existe_registro(clave)
    if exi == 0:
        return ' '
    elif exi == 1:
        encontrado = tabla_tablas.obtener_registro(clave)
        return encontrado['Informacion']

def obtener_fecha():
    clave = 'F01'
    exi = tabla_tablas.existe_registro(clave)
    if exi == 0:
        return str(datetime.date(datetime.now())).replace('-', '')
    elif exi == 1:
        encontrado = tabla_tablas.obtener_registro(clave)
        if len(encontrado['Informacion']) != 8:
            return str(datetime.date(datetime.now())).replace('-', '')
        else:
            return encontrado['Informacion']

def calcular_reporte_almacen(producto, id_dpt_con_proc):
    suma_consumos = 0
    while True:
        if reg_con[3] != 'RA' or reg_con[2] != producto['Producto'] or \
            reg_con[1] != id_dpt_con_proc.departamento or \
            reg_con[0] != id_dpt_con_proc.planta:
            break
        else:
            suma_consumos = suma_consumos + int(reg_con[4])
            lee_consumo()
            if fin_con == 1:
                break
    suma_devoluciones = 0
    if fin_dev == 0:
        while True:
            if reg_dev[2] != producto['Producto'] or \
                reg_dev[1] != id_dpt_con_proc.departamento or \
                reg_dev[0] != id_dpt_con_proc.planta:
                break
            else:
                suma_devoluciones = suma_devoluciones+int(reg_dev[3])
                lee_devolucion()
                if fin_dev == 1:
                    break
    return suma_consumos-suma_devoluciones

def calcular_reporte_produccion(producto, id_dpt_con_proc):
    suma_consumos = 0
    while True:
        if reg_con[3] != 'RP' or reg_con[2] != producto['Producto'] or \
            reg_con[1] != id_dpt_con_proc.departamento or \
            reg_con[0] != id_dpt_con_proc.planta:
            break
        else:
            suma_consumos = suma_consumos+int(reg_con[4])
            lee_consumo()
            if fin_con == 1:
                break
    return suma_consumos

if __name__ == "__main__":
    ###### Control
    # Abrir archivo de consumos
    arch_con = open('tests/casos/caso1/consumos.txt', 'r')
    # Abrir archivo de devoluciones
    arch_dev = open('tests/casos/caso1/devoluciones.txt', 'r')
    # Abrir Base de datos
    cursor = obtener_cursor()
    tabla_productos = crear_tabla(cursor, 'Productos')
    tabla_tablas = crear_tabla(cursor, 'Tablas')
    # Abrir reporte
    num_lin = 0
    num_hoja = 0
    NOMBRE_PROGRAMA = 'COP120'
    MAX_LIN = 88
    MAX_COL = 114
    fecha = obtener_fecha()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Courier', '', 8)
    # Inicializacion de variables
    HV = {
        'pt': 'PT9',
        'dpt': 'DPT999',
        'p': 'P99999',
        'cvep': 'ZZ'
    }
    fin_con = 0
    fin_dev = 0
    acum_tot_dpt = AcumTotDpt()
    # Leer consumo
    reg_con = arch_con.readline().rstrip().split(' ')
    # Leer devolucion
    reg_dev = arch_dev.readline().rstrip().split(' ')
    # Si fin_con NO es = 1, entonces procesa_planta
    while True:
        if fin_con == 1:
            break
        else:
            procesa_planta()
    # Si SI es 1, cerrar archivos y reporte
    arch_con.close()
    arch_dev.close()
    pdf.output('reporte_final.pdf', 'F')