# -*-*-*-
"""
* Programa: funciones_reporte
* Objetivo: Proveer funciones para manipular reporte
* Autor:    FCFM. GOAB. Gutiérrez Ortega Alberto Baltazar
* Fecha:    8/12/2020
"""

# -*-*-*- 
"""
* Import                   Funcion
* Libreria
* re                       Módulo de la libreria estandar de python que
*                          sirve para trabajar con expresiones regulares.
* 
* Constantes               Funcion
* MAX_COLUMNAS             Numero columnas maximas en la hoja de pdf.
* MAX_LINEAS               Número de lineas maximas en la hoja de pdf.
* 
* Proceso                  Función
* imprimir_lineas_blanco:  Imprimir cierta cantidad de lineas en blanco antes
*                          de llegar al máximo.
* imprimir_tot_dpt:        Imprimir el total de departamento.
* imprimir_encabezado:     Imprimir encabezado.
* construir_detalle:       Retorna string con el detalle de producto.
* formato_a_favor_de:      Formato a string que indica la diferencia a favor.
* formato_prod_num:        Formato a número para que tenga las comas 
*                          necesarias si se necesita.
* formato_prod_desc:       Formato a descripcion del producto para utilizar el 
*                          espacio permitido.
* formato_planta_nombre:   Formato al nombre de la planta para utilizar el 
*                          espacio permitido.
* formato_dpt_nombre:      Formato al nombre de departamento para utilizar el 
*                          espacio permitido.
* formato_num_hoja:        Formato al numero de hoja para utilizar el 
*                          espacio permitido.
* formato_fecha:           Obtener dia, mes y año de string con fecha.
* generar_numero_linea:    Retorna string con el numero de linea y los 
*                          espacios en blanco necesarios a la derecha.
* generar_linea_imprimir:  Retorna string con formato listo para imprimir.
* imprimir_linea:          Imprime linea en reporte.
"""

# -*-*-*-
"""
* (1) Utilizar instrucciones de reutilizacion del programa COP120.
"""

import re

MAX_COLUMNAS = 114
MAX_LINEAS = 88

def imprimir_lineas_blanco(pdf, lineas_ya_impresas):
    for num_linea in range(lineas_ya_impresas, MAX_LINEAS + 1):
        imprimir_linea(pdf, '', num_linea)

def imprimir_tot_dpt(pdf, num_linea, dpt_clave, dpt_nombre, acum_tot_dpt):
    linea_cve_nom = 'TOTAL DEL DPTO. '+dpt_clave+(' '*2)+ \
                    formato_dpt_nombre(dpt_nombre)+(' '*65)
    linea_almacen = 'ALMACEN'+(' '*5)+'IMPORTE'+(' '*2)+ \
                    formato_prod_num(acum_tot_dpt.imp_alm)+(' '*4)+ \
                    'DIFERENCIA A FAVOR '+ \
                    formato_prod_num(acum_tot_dpt.dif_fav_alm)+(' '*48)
    linea_produccion = 'PRODUCCION'+(' '*2)+'IMPORTE'+(' '*2)+ \
                       formato_prod_num(acum_tot_dpt.imp_prod)+(' '*4)+ \
                       'DIFERENCIA A FAVOR '+ \
                       formato_prod_num(acum_tot_dpt.dif_fav_prod)+(' '*48)
    if len(linea_cve_nom) == len(linea_almacen) == \
        len(linea_produccion) == MAX_COLUMNAS:
        imprimir_linea(pdf, linea_cve_nom, num_linea)
        imprimir_linea(pdf, '', num_linea+1)
        imprimir_linea(pdf, linea_almacen, num_linea+2)
        imprimir_linea(pdf, '', num_linea+3)
        imprimir_linea(pdf, linea_produccion, num_linea+4)
        imprimir_linea(pdf, '', num_linea+5)
    else:
        print("Formato incorrecto")

def imprimir_encabezado(pdf, prog_nom, fecha, planta_cve, planta_nombre, 
                        dpt_clave, dpt_nombre, num_hoja):
    dia, mes, anio = formato_fecha(fecha)
    fecha_imprimir = f"{dia}  {mes} {anio}"
    primer_linea = 'P-  '+prog_nom + (' '*16)+ \
                   'R E P O R T E   C O M P A R A T I V O'+ \
                    (' '*3)+'D E'+(' '*3)+'C O N S U M O S'+(' '*9)+ \
                    'FECHA  '+fecha_imprimir
    linea_num_hoja = 'ACME      DIV. NOMINA'+(' '*15)+'P L A N T A  '+ \
                     planta_cve+(' '*2)+('x'*7)+(' '*2)+ \
                     formato_planta_nombre(planta_nombre)+(' '*23)+'HOJA  '+ \
                     formato_num_hoja(num_hoja)
    linea_contabilidad = 'CONTABILIDAD'+(' '*102)
    linea_departamento = 'DPTO. '+dpt_clave+(' '*4)+ \
                         formato_dpt_nombre(dpt_nombre)+(' '*73)
    linea_producto = 'P R O D U C T O'+(' '*20)+'REPORTE ALMACEN'+ \
                     (' '*7)+'REPORTE PRODUCCION'+(' '*10)+ \
                     'DIFERENCIA ENTRE REPORTES'+(' '*4)
    linea_campos = 'CODIGO'+(' '*6)+'DESCRIPCION'+(' '*9)+'CONSUMO'+(' '*5)+\
                   'IMPORTE'+(' '*6)+'CONSUMO'+(' '*5)+'IMPORTE'+(' '*6)+ \
                   'CONSUMO'+(' '*5)+'IMPORTE'+(' '*3)+'A FAVOR DE'
    linea_separacion = ('-'*6)+(' '*2)+('-'*20)+(' '*2)+ \
                       ( ('-'*11)+' '+('-'*11))+(' '*2)+ \
                       ( ('-'*11)+' '+('-'*11))+(' '*2)+ \
                       ( ('-'*11)+' '+('-'*11))+' '+('-'*10)

    if len(primer_linea) == len(linea_num_hoja) == \
        len(linea_contabilidad) == len(linea_departamento) == \
        len(linea_producto) == len(linea_campos) == len(linea_separacion) == \
        MAX_COLUMNAS: 
        imprimir_linea(pdf, primer_linea, 1)
        imprimir_linea(pdf, '', 2)
        imprimir_linea(pdf, linea_num_hoja, 3)
        imprimir_linea(pdf, '', 4)
        imprimir_linea(pdf, linea_contabilidad, 5)
        imprimir_linea(pdf, linea_departamento, 6)
        imprimir_linea(pdf, '', 7)
        imprimir_linea(pdf, linea_producto, 8)
        imprimir_linea(pdf, linea_campos, 9)
        imprimir_linea(pdf, linea_separacion, 10)
    else:
        print("Encabezado Formato incorrecto")

def construir_detalle(producto, acum_con_prod, imp_rep_alm, 
                      imp_rep_produ, cons_dif, imp_dif, a_favor):
    cve_prod = producto['Producto']
    descripcion = formato_prod_desc(producto['Descripcion'])
    con_rep_alm = formato_prod_num(acum_con_prod.con_almacen)
    imp_rep_alm = formato_prod_num(imp_rep_alm)
    con_rep_produ = formato_prod_num(acum_con_prod.con_produccion)
    imp_rep_produ = formato_prod_num(imp_rep_produ)
    cons_dif = formato_prod_num(cons_dif)
    imp_dif = formato_prod_num(imp_dif)
    a_favor = formato_a_favor_de(a_favor)
    return f"{cve_prod}  {descripcion}  {con_rep_alm} {imp_rep_alm}  "+ \
           f"{con_rep_produ} {imp_rep_produ}  {cons_dif} {imp_dif} {a_favor}"

def formato_a_favor_de(a_favor):
    car_necesarios = 10
    len_a_favor = len(a_favor)
    espacios_antes = car_necesarios-len_a_favor
    resultado = (' '*espacios_antes)+a_favor
    return resultado

def formato_prod_num(num):
    max_espacios = 11
    resultado = ''
    if len(str(num)) > 6:
        # Necesita dos comas
        match = re.findall(r"[\d]{6}$", f'{num}')[0]
        primeros_numeros = str(num).replace(match, '')
        num_completo = primeros_numeros+','+match[0:3]+','+match[3:]
        resultado = resultado+('.'*(max_espacios-len(num_completo)))+ \
                    num_completo
    elif len(str(num)) > 3:
        # Necesita una coma
        match = re.findall(r"[\d]{3}$", f'{num}')[0]
        primeros_numeros = str(num).replace(match, '')
        num_completo = primeros_numeros+','+match 
        resultado = resultado+('.'*(max_espacios-len(num_completo)))+ \
                    num_completo
    else:
        # No necesita comas
        len_num = len(str(num))
        puntos_antes = max_espacios-len_num
        resultado = ('.'*puntos_antes)+str(num)
    return resultado
          
def formato_prod_desc(descripcion):
    car_necesarios = 20
    len_prod_desc = len(descripcion)
    espacios_antes = car_necesarios-len_prod_desc
    resultado = (' '*espacios_antes)+descripcion
    return resultado

def formato_planta_nombre(planta_nombre):
    # Ej. planta_nombre = Queretaro
    car_necesarios = 18
    len_planta_nombre = len(planta_nombre)
    espacios_antes = car_necesarios-len_planta_nombre
    res = (' '*espacios_antes)+planta_nombre
    return res

def formato_dpt_nombre(dpt_nombre):
    # Ej. dpt_nombre = Articulos construccion
    car_necesarios = 25
    len_dpt_nombre = len(dpt_nombre)
    espacios_antes = car_necesarios-len_dpt_nombre
    resultado = (' '*espacios_antes)+dpt_nombre
    return resultado

def formato_num_hoja(num_hoja):
    car_necesarios = 4
    len_num_hoja = len(str(num_hoja))
    espacios_antes = car_necesarios-len_num_hoja
    resultado = (' '*espacios_antes)+str(num_hoja)
    return resultado

def formato_fecha(fecha):
    anio = fecha[0:4]
    mes = fecha[4:6]
    dia = fecha[6:8]
    return dia, mes, anio

def generar_numero_linea(numero_linea, cantidad_espacios):
    return str(numero_linea)+(' '*cantidad_espacios)

def generar_linea_imprimir(string_imprimir, numero_linea):
    if not string_imprimir:
        if numero_linea > 9:
            return generar_numero_linea(numero_linea, 115)+string_imprimir
        else: 
            return generar_numero_linea(numero_linea, 116)+string_imprimir
    else:
        if numero_linea > 9:
            return generar_numero_linea(numero_linea, 1)+string_imprimir
        else:
            return generar_numero_linea(numero_linea, 2)+string_imprimir
    
def imprimir_linea(pdf, string_imprimir, numero_linea):
    linea_reporte = generar_linea_imprimir(string_imprimir, numero_linea)
    pdf.cell(0, 3, linea_reporte, align='C', ln=1)
