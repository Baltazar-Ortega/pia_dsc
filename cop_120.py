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

from estructuras_de_datos.identidades import IdPlaCon, IdDptCon, IdCon, IdDev
from estructuras_de_datos.acumuladores import AcumConProd, AcumTotDpt
from estructuras_de_datos.tablas import TablaProductos, TablaTablas
from base_de_datos.conexion import cursor 


def control():
    # Abrir archivo de consumos
    
    # Abrir archivo de devoluciones

    # Abrir reporte

    # Inicializacion de variables
    FinCon = 0
    FinDev = 0

    # Pintar encabezado

    # Leer consumo
    # Leer devolucion
    # Si FinCon NO es = 1, entonces procesa_planta
    # Si SI es 1, cerrar archivos y reporte

def lee_consumo(archivo_posicionado):
    # Id.Ant = Id.Lei
    pass









