# Acumuladores

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
        self.generar_valor({imp_alm, imp_prod, dif_fav_alm, dif_fav_prod})


