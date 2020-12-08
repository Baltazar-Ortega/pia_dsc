# -*-*-*-
"""
* Programa: identidades
* Objetivo: Proveer clases para representar la estructura de datos 'Identidad'
* Autor:    FCFM. GOAB. Gutiérrez Ortega Alberto Baltazar
* Fecha:    8/12/2020
"""

# -*-*-*- 
"""
* Clase       Función
* Identidad   Estructura básica de una identidad.
* IdPlaCon    Hereda de Identidad. Estructura para Id.Pla.Con
* IdDptCon    Hereda de Identidad. Estructura para Id.Dpt.Con
* IdCon       Hereda de Identidad. Estructura para Id.Con
* IdDev       Hereda de Identidad. Estructura para Id.Dev
"""

# -*-*-*-
"""
* (1) Las identidades nuevas deben de heredar de Identidad.
"""

class Identidad:
    def __init__(self, tipo):
        self.tipo = self.validar_tipo(tipo)

    def crear_identidad(self, elementos):
        self.id = " ".join(elementos)

    def validar_tipo(self, tipo):
        if tipo not in ['lectura', 'proceso', 'anterior']:
            return None
        else:
            return tipo
    
    def __str__(self):
        return self.id

class IdPlaCon(Identidad):
    def __init__(self, tipo, planta):
        super().__init__(tipo)
        self.planta = planta
        self.crear_identidad([planta])

class IdDptCon(Identidad):
    def __init__(self, tipo, planta, departamento):
        super().__init__(tipo)
        self.planta = planta
        self.departamento = departamento
        self.crear_identidad([planta, departamento])
    
class IdCon(Identidad):
    def __init__(self, tipo, planta, departamento, producto, clave_producto):
        super().__init__(tipo)
        self.planta = planta
        self.departamento = departamento
        self.producto = producto
        self.clave_producto = clave_producto
        self.crear_identidad([planta, departamento, producto, clave_producto])

class IdDev(Identidad):
    def __init__(self, tipo, planta, departamento, producto):
        super().__init__(tipo)
        self.planta = planta
        self.departamento = departamento
        self.producto = producto
        self.crear_identidad([planta, departamento, producto])
