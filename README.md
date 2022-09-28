### DHL

## Objetivo
El objetivo de esta herramienta es crear una automatización de procesos CRUD (Create, Read, Update, Delete) ligamos a una base de datos.

## Herramientas
Se ha hecho uso de la herramienta "mysql-connector" para levantar el servicio local de base de datos.

## Contenido
    - Principal: Función main que coordina todas las funcionalidades para crear el servicio.
    - Funciones: Aplica la lógica del programa implementando funcionalidades muy concretas.
    - Conexion: Levanta el servicio de base de datos en MySQL y coordina las distintas consultas a la misma.

## Propuesta de mejora
    - Se podría implementar una interfaz para hacer las interacciones más amigables
    - El código podría reestructurarse en unidades más pequeñas, dividiendo más sus funcionalidades

## Comentarios
    - La lógica de las querys está planteada para un entorno de MySQL.
    - Está montado sobre un entorno virtual que implementa "mysql-connector".
    - Funciona en ámbito localhost en PhpMyAdmin. La base de datos tiene que tener configurada una tabla de "central_logistica" con la siguiente estructura:
        - id: int(11) / AUTO_INCREMENT
        - Codigo: int(6)
        - Direccion: varchar(35)
        - Envio: float
    - Se ha escrito y documentado en castellano, por estar orientada a la parte de un proceso de selección determinado.
    - Se ha utilizado la versión 3.10.1 de Python.
