# -*-*-*-
"""
* Programa: acumuladores
* Objetivo: Proveer clases para representar la estructura de datos 
*           'Acumulador'
* Autor:    FCFM. GOAB. Gutiérrez Ortega Alberto Baltazar
* Fecha:    8/12/2020
"""

# -*-*-*- 
"""
* Clase         Función
* Acumulador    Estructura básica de un acumulador.
* AcumConProd   Hereda de Acumulador. Estructura para Acum.Con.Prod
* AcumTotDpt    Hereda de Acumulador. Estructura para Acum.Tot.Dpt
"""

# -*-*-*-
"""
* (1) Los acumuladores nuevos deben de heredar de Acumulador.
* (2) Los acumuladores nuevos deben de inicializar sus valores a cero en
*     el constructor.
"""

class Acumulador:
    def generar_valor(self, elementos):
        self.valor = sum(elementos)

class AcumConProd(Acumulador):
    def __init__(self, con_almacen=0, con_produccion=0):
        self.con_almacen = con_almacen
        self.con_produccion = con_produccion
        self.generar_valor([con_almacen, con_produccion])

class AcumTotDpt(Acumulador):
    def __init__(self, imp_alm=0, imp_prod=0, dif_fav_alm=0, dif_fav_prod=0):
        self.imp_alm = imp_alm
        self.imp_prod = imp_prod
        self.dif_fav_alm = dif_fav_alm
        self.dif_fav_prod = dif_fav_prod


