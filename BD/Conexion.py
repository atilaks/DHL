import mysql.connector
from mysql.connector import Error

"""
Este apartado levanta la conexión con la base de datos y genera todas las interacciones con la misma.

Funciones:
    - __init__: Función principal que levanta el servicio de base de datos.
    - ListarPaquetes: Genera una lista actualizada de los registros en la tabla.
        - QUERY: "SELECT * FROM paquetes ORDER BY codigo ASC"
    - RegistrarPaquete: Registra una nueva entrada en la tabla.
        - QUERY: "INSERT INTO paquetes (Codigo, Direccion, Envio) VALUES ({0}, '{1}', {2})"
    - ActualizarPaquete: Recodifica un registro ya existente en la tabla.
        - QUERY: "UPDATE paquetes SET Direccion = '{0}', Envio = {1} WHERE codigo = '{2}'"
    - EliminarPaquete: Elimina un registro de la tabla.
        - QUERY: "DELETE FROM paquetes WHERE codigo = '{0}'"
"""

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '123456',
                db = 'central_logistica'
            )
        except Error as ex:
            print('Error al intentar la conexión: {0}'.format(ex))
    
    def ListarPaquetes(self):
        if self.conexion.is_connected():
            try:
                paquetador = self.conexion.paquetador()
                paquetador.execute("SELECT * FROM paquetes ORDER BY codigo ASC")
                resultados = paquetador.fetchall()
                return resultados
            except Error as ex:
                print('Error al intentar la conexión: {0}'.format(ex))

    def RegistrarPaquete(self, paquete):
        if self.conexion.is_connected():
            try:
                paquetador = self.conexion.paquetador()
                sql = "INSERT INTO paquetes (Codigo, Direccion, Envio) VALUES ({0}, '{1}', {2})"
                paquetador.execute(sql.format(paquete[0], paquete[1], paquete[2]))
                self.conexion.commit()
                print('Paquete registrado\n')
            except Error as ex:
                print('Error al intentar la conexión: {0}'.format(ex))
    
    def ActualizarPaquete(self, paquete):
        if self.conexion.is_connected():
            try:
                paquetador = self.conexion.paquetador()
                sql = "UPDATE paquetes SET Direccion = '{0}', Envio = {1} WHERE codigo = '{2}'"
                paquetador.execute(sql.format(paquete[1], paquete[2], paquete[0]))
                self.conexion.commit()
                print('Paquete actualizado\n')
            except Error as ex:
                print('Error al intentar la conexión: {0}'.format(ex))

    def EliminarPaquete(self, codigoPaqueteEliminar):
        if self.conexion.is_connected():
            try:
                paquetador = self.conexion.paquetador()
                sql = "DELETE FROM paquetes WHERE codigo = '{0}'"
                paquetador.execute(sql.format(codigoPaqueteEliminar))
                self.conexion.commit()
                print('Paquete eliminado\n')
            except Error as ex:
                print('Error al intentar la conexión: {0}'.format(ex))
    