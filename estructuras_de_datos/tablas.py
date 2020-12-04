# Tablas

class Tabla:
    def __init__(self):
        self.indice = 1
        self.num_elementos = 0
        self.max_elem = 32
        self.registros = []
        self.formato_registro = None
    
    def llenar_tabla(self, registros):
        self.registros = registros
        
    def agregar_registro(self, registro):
        if self.num_elementos >= self.max_elem:
            print('Ya no caben mas registros')
        else:
            if registro.keys() == self.formato_registro.keys():
                self.registros.append(registro)
                self.num_elementos = self.num_elementos + 1
                # print('Registro insertado')
            else:
                print('Registro con formato incorrecto')

    def obtener_registro(self, indice):
        self.indice = indice
        return self.registros[self.indice]

    def existe_registro(self, clave):
        for registro in self.registros:
            if registro.clave == clave:
                return True
        return False

class TablaProductos(Tabla):
    def __init__(self):
        self.formato_registro = {
            'Producto': '',
            'Descripcion': '',
            'CostoUnitario': ''
        }

class TablaTablas(Tabla):
    def __init__(self):
        super().__init__()
        self.formato_registro = {
            'ClaveTabla': '',
            'LlaveTabla': '',
            'Informacion': ''
        }


    
    

# Ejemplo
# miregistro_tablas = {
#     'ClaveTabla': 'T04',
#     'LlaveTabla': 'PT1',
#     'Informacion': 'Queretaro'
# }

# tabla_tablas = TablaTablas()

# tabla_tablas.agregar_registro(miregistro_tablas)