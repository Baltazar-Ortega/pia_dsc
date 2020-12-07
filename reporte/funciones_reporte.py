import sys
import re

# from fpdf import FPDF

# class Acumulador:
#     def generar_valor(self, elementos):
#         self.valor = sum(elementos)

# class AcumConProd(Acumulador):
#     def __init__(self, con_almacen=0, con_produccion=0):
#         self.con_almacen = con_almacen
#         self.con_produccion = con_produccion
#         self.generar_valor([con_almacen, con_produccion])

# class AcumTotDpt(Acumulador):
#     def __init__(self, imp_alm=0, imp_prod=0, dif_fav_alm=0, dif_fav_prod=0):
#         self.imp_alm = imp_alm
#         self.imp_prod = imp_prod
#         self.dif_fav_alm = dif_fav_alm
#         self.dif_fav_prod = dif_fav_prod

MAX_COLUMNAS = 114
MAX_LINEAS = 88

def imprimir_lineas_blanco(pdf, lineas_ya_impresas):
    # print("....**entra imprimir lineas blanco")
    # lineas_blanco = MAX_LINEAS - lineas_ya_impresas
    for num_linea in range(lineas_ya_impresas, MAX_LINEAS + 1):
        imprimir_linea(pdf, '', num_linea)

def imprimir_tot_dpt(pdf, num_linea, dpt_clave, dpt_nombre, acum_tot_dpt):
    linea_cve_nom = 'TOTAL DEL DPTO. '+dpt_clave+(' '*2)+formato_dpt_nombre(dpt_nombre)+\
        (' '*65)
    linea_almacen = 'ALMACEN' + (' '*5) + 'IMPORTE' + (' '*2) + \
        formato_prod_num(acum_tot_dpt.imp_alm) + (' '*4)+ \
        'DIFERENCIA A FAVOR ' + formato_prod_num(acum_tot_dpt.dif_fav_alm) + (' '*48)
    linea_produccion = 'PRODUCCION' + (' '*2) + 'IMPORTE' + (' '*2) + \
        formato_prod_num(acum_tot_dpt.imp_prod) + (' '*4)+ \
        'DIFERENCIA A FAVOR ' + formato_prod_num(acum_tot_dpt.dif_fav_prod) + (' '*48)
    if len(linea_cve_nom) == len(linea_almacen) == len(linea_produccion) == MAX_COLUMNAS:
        imprimir_linea(pdf, linea_cve_nom, num_linea)
        imprimir_linea(pdf, '', num_linea + 1)
        imprimir_linea(pdf, linea_almacen, num_linea + 2)
        imprimir_linea(pdf, '', num_linea + 3)
        imprimir_linea(pdf, linea_produccion, num_linea + 4)
        imprimir_linea(pdf, '', num_linea + 5)
    else:
        print("Formato incorrecto")


def imprimir_encabezado(pdf, prog_nom, fecha, planta_cve, planta_nombre, dpt_clave, dpt_nombre, num_hoja):
    MAX_COLUMNAS = 114
    dia, mes, anio = formato_fecha(fecha)
    fecha_imprimir = f"{dia}  {mes} {anio}"
    # print("fecha_imprimir: ", fecha_imprimir)
    # print("fecha_imprimir: ", len(fecha_imprimir))
    primer_linea = f'P-  {prog_nom}' + (' '*16) + 'R E P O R T E   C O M P A R A T I V O' + \
    (' '*3) + 'D E' + (' '*3) + 'C O N S U M O S' + (' '*9) + 'FECHA  '+fecha_imprimir
    # print("primer_linea: ", primer_linea)
    # print("len primer_linea: ", len(primer_linea))
    linea_num_hoja = 'ACME      DIV. NOMINA' + (' '*15) + 'P L A N T A  '+planta_cve+\
    (' '*2)+ ('x'*7)+(' '*2)+formato_planta_nombre(planta_nombre)+(' '*23)+'HOJA  '+formato_num_hoja(num_hoja)
    linea_contabilidad = 'CONTABILIDAD'+(' '*102)
    linea_departamento = 'DPTO. '+dpt_clave+(' '*4)+formato_dpt_nombre(dpt_nombre)+(' '*73)
    linea_producto = 'P R O D U C T O' + (' '*20) + 'REPORTE ALMACEN'+(' '*7)+'REPORTE PRODUCCION'+\
        (' '*10) + 'DIFERENCIA ENTRE REPORTES'+(' '*4)
    linea_campos = 'CODIGO' + (' '*6) + 'DESCRIPCION'+(' '*9)+'CONSUMO'+(' '*5)+\
        'IMPORTE'+(' '*6)+'CONSUMO'+(' '*5)+'IMPORTE'+(' '*6)+'CONSUMO'+(' '*5)+\
            'IMPORTE'+(' '*3)+'A FAVOR DE'
    linea_separacion = ('-'*6)+(' '*2)+('-'*20)+(' '*2)+ \
                       ( ('-'*11) + ' ' + ('-'*11)) + (' '*2) + \
                       ( ('-'*11) + ' ' + ('-'*11)) + (' '*2) + \
                       ( ('-'*11) + ' ' + ('-'*11)) + ' ' + ('-'*10)

    if len(primer_linea) == len(linea_num_hoja) == len(linea_contabilidad) == \
        len(linea_departamento) == len(linea_producto) == len(linea_campos) == \
        len(linea_separacion) == MAX_COLUMNAS: 
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

        # producto = {'Producto': 'P00001', 'Descripcion': 'Vaso de vidrio'}
        # linea_detalle = construir_detalle(producto)
        # imprimir_linea(pdf, linea_detalle, 11)
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
    return f"{cve_prod}  {descripcion}  {con_rep_alm} {imp_rep_alm}  {con_rep_produ} {imp_rep_produ}  {cons_dif} {imp_dif} {a_favor}"

def formato_a_favor_de(a_favor):
    # Necesito 10
    len_a_favor = len(a_favor)
    espacios_antes = 10 - len_a_favor
    res = (' '*espacios_antes) + a_favor
    return res

def formato_prod_num(num):
    # 11 espacios 
    # 9 numeros max (2 comas cada 3)
    max_espacios = 11
    res = ''
    if len(str(num)) > 6:
        # Necesita dos comas
        match = re.findall(r"[\d]{6}$", f'{num}')[0]
        primeros_numeros = str(num).replace(match, '')
        num_completo = primeros_numeros + ',' + match[0:3] + ',' + match[3:]
        res = res + ('.'*(max_espacios-len(num_completo))) + num_completo
    elif len(str(num)) > 3:
        # Necesita una coma
        match = re.findall(r"[\d]{3}$", f'{num}')[0]
        # print(match)
        primeros_numeros = str(num).replace(match, '')
        num_completo = primeros_numeros + ',' + match 
        res = res + ('.'*(max_espacios-len(num_completo))) + num_completo
    else:
        # No necesita comas
        len_num = len(str(num))
        puntos_antes = max_espacios - len_num
        res = ('.'*puntos_antes) + str(num)
    return res
          
def formato_prod_desc(descripcion):
    # 20
    len_prod_desc = len(descripcion)
    espacios_antes = 20 - len_prod_desc
    res = (' '*espacios_antes) + descripcion
    return res

def formato_planta_nombre(planta_nombre):
    # Ej. planta_nombre = Queretaro
    # Necesita 18 caracteres
    len_planta_nombre = len(planta_nombre)
    espacios_antes = 18 - len_planta_nombre
    res = (' '*espacios_antes)+planta_nombre
    # print("planta_nombre formateado: ", res)
    return res

def formato_dpt_nombre(dpt_nombre):
    # Ej. dpt_nombre = Articulos construccion
    # Necesita 25 caracteres
    len_dpt_nombre = len(dpt_nombre)
    espacios_antes = 25 - len_dpt_nombre
    res = (' '*espacios_antes)+dpt_nombre
    # print("dpt_nombre formateado: ", res)
    # print("len dpt_nombre formateado: ", len(res))
    return res

def formato_num_hoja(num_hoja):
    # 4 caracteres
    len_num_hoja = len(str(num_hoja))
    espacios_antes = 4 - len_num_hoja
    res = (' '*espacios_antes)+str(num_hoja)
    # print("num_hoja formateado: ", res)
    return res

def formato_fecha(fecha):
    anio = fecha[0:4]
    mes = fecha[4:6]
    dia = fecha[6:8]
    return dia, mes, anio
    # dia = fecha['dia']
    # mes = ''
    # if len(fecha['dia']) < 2:
    #     dia = '0' + fecha['dia']
    # if len(fecha['mes']) < 2:
    #     mes = ' 0'+fecha['mes']
    # else:
    #     mes = ' '+fecha['mes']
    # return dia, mes, fecha['anio']

def generar_numero_linea(numero_linea, cantidad_espacios):
    return str(numero_linea) + (' '*cantidad_espacios)

def generar_linea_imprimir(string_imprimir, numero_linea):
    if not string_imprimir:
        if numero_linea > 9:
            return generar_numero_linea(numero_linea, 115) + string_imprimir
        else: 
            return generar_numero_linea(numero_linea, 116) + string_imprimir
    else:
        if numero_linea > 9:
            return generar_numero_linea(numero_linea, 1) + string_imprimir
        else:
            return generar_numero_linea(numero_linea, 2) + string_imprimir
    
def imprimir_linea(pdf, string_imprimir, numero_linea):
    linea_reporte = generar_linea_imprimir(string_imprimir, numero_linea)
    pdf.cell(0, 3, linea_reporte, align='C', ln=1)

# if __name__ == '__main__':
#     # MAX_COLUMNAS = 114
#     # MAX_LINEAS = 88
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font('Courier', '', 8)

#     acum_tot_dpt = AcumTotDpt()
#     imprimir_tot_dpt(pdf, 5, 'DPT001', 'Articulos de construccion', acum_tot_dpt)

#     # fecha = {'dia':'20', 'mes':'11', 'anio':'1998'}

#     # imprimir_encabezado(pdf, fecha, 'PT1', 'Monterrey', 'DPT001', 'Articulos oficina', 45)

#     # producto = {'Producto':'P00001', 'Descripcion':'Vaso de vidrio', 'CostoUnitario':20}
#     # acum_con_prod = AcumConProd()
#     # gran = 321
#     # resultado = construir_detalle(producto, acum_con_prod, gran, gran, gran, gran, 'ALMACEN')
#     # print("Resultado de construir_detalle: ", resultado)
#     # print("Resultado de construir_detalle (len): ", len(resultado))
#     # imprimir_linea(pdf, resultado, 11)
#     # imprimir_linea(pdf, resultado, 12)


#     pdf.output('prueba.pdf', 'F')