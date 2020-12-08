# -*-*-*-
"""
* Programa: tablas
* Objetivo: Proveer clases para representar la estructura de datos 'Tabla'
* Autor:    FCFM. GOAB. Gutiérrez Ortega Alberto Baltazar
* Fecha:    8/12/2020
"""

# -*-*-*- 
"""
* Clase             Función
* Tabla             Estructura básica de una tabla.
* Tabla_Productos   Hereda de Tabla. Estructura para Tabla de BD "Productos".
* Tabla_Tablas      Hereda de Tabla. Estructura para Tabla de BD "Tablas".
"""

# -*-*-*-
"""
* (1) Las tablas nuevas deben de heredar de Tabla.
* (2) Las tablas nuevas deben crear un formato de registro. 
"""

class Tabla:
    def __init__(self):
        self.indice = 1
        self.num_elementos = 0
        self.max_elem = 100
        self.registros = []
        self.formato_registro = None
    
    def llenar_tabla(self, registros):
        self.registros = registros
        self.num_elementos = len(self.registros)
        
    def agregar_registro(self, registro):
        if self.num_elementos >= self.max_elem:
            print('Ya no caben mas registros')
        else:
            if registro.keys() == self.formato_registro.keys():
                self.registros.append(registro)
                self.num_elementos = self.num_elementos + 1
            else:
                print('Registro con formato incorrecto')

    def obtener_registro_por_indice(self, indice):
        self.indice = indice - 1
        return self.registros[self.indice]

class TablaProductos(Tabla):
    def __init__(self):
        super().__init__()
        self.formato_registro = {
            'Producto': '',
            'Descripcion': '',
            'CostoUnitario': ''
        }

    def obtener_registro(self, clave):
        for registro in self.registros:
            if registro['Producto'] == clave:
                return registro
        return False
    
    def existe_registro(self, clave):
        for registro in self.registros:
            if registro['Producto'] == clave:
                return 1
        return 0

class TablaTablas(Tabla):
    def __init__(self):
        super().__init__()
        self.formato_registro = {
            'ClaveTabla': '',
            'LlaveTabla': '',
            'Informacion': ''
        }

    def obtener_registro(self, clave):
        for indice, registro in enumerate(self.registros, 1):
            reg_clave = registro['ClaveTabla'] + registro['LlaveTabla']
            if reg_clave == clave:
                return registro
        return 0

    def existe_registro(self, clave):
        for indice, registro in enumerate(self.registros, 1):
            reg_clave = registro['ClaveTabla'] + registro['LlaveTabla']
            if reg_clave == clave:
                return 1
        return 0
