# Proyecto final - Diseño de soluciones computacionales

### Reporte de consumos y devoluciones - Python 

## Instrucciones de ejecucion

### 1. Descargar codigo (o clonar repositorio)
### 2. Crear un virtual environment desde la raiz de la carpeta
<code>$ python -m venv pia_dsc_env</code>
### 3. Activar entorno virtual
<code>$ .\pia_dsc_env\Scripts\activate</code>
### 4. Instalar dependencias
<code>$ pip install -r requirements.txt</code>
### 5. Crear base de datos "pia_dsc" utilizando postgresql
Ej. Usando psql
<code>$ CREATE DATABASE pia_dsc;</code>
### 6. Conectarse a la base de datos
Ej. Usando psql </br>
<code>$ psql -U postgres</code></br>
<code>$ CREATE DATABASE pia_dsc;</code></br>
<code>$ \c pia_dsc;</code>
### 7. Ejecutar en postgres el codigo en: <code>base_de_datos/crear_tablas.sql</code>
Se crearán las tablas con registros de prueba
### 8. Crear archivo <code>base_de_datos/bd.init</code> siguiendo el formato de <code>base_de_datos/bd_ej.ini</code>
Asegurarse de cambiar la password
### 9. Ejecutar programa
<code>$ python cop_120.py</code>
