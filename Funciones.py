"""
Este apartado implementa toda la lógica de las funcionalidades del programa.

Funciones:
    - ListarPaquetes: Tomando como imput los elementos existentes, genera una lista
        recorriendo un FOR para asignar cada valor.
    - PedirDatosPaquete: Hace una consulta al usuario para pedir datos del paquete.
        - Controla los errores de forma si no se ajusta al tamaño en código.
    - PedirDatosActualizacion: Hace una consulta al usuario para pedir el código del paquete.
        Verifica la existencia del mismo y consulta nuevamente para modificar los parámetros.
    - PedirDatosEliminacion: Hace una consulta al usuario para pedir el código del paquete. 
        Verifica la existencia del mismo y lo elimina.
"""

def ListarPaquetes(paquetes):
    print('\nPaquetes: \n')
    contador = 1
    for pac in paquetes:
        datos = '{0}. Código: {1} | Dirección: {2} | Envío: {3}'
        print(datos.format(contador, pac[0], pac[1], pac[2]))
        contador = contador + 1
    print(' ')

def PedirDatosPaquete():
    codigoCorrecto = False
    while(not codigoCorrecto):
        codigo = input('Ingresa el código: ')
        if len(codigo) == 6:
            codigoCorrecto = True
        else:
            print('Código incorrecto. Tiene que tener 6 dígitos')
    direccion = input('Ingresa la dirección: ')
    envio = float(input('Ingresa el envío: '))

    paquete = (codigo, direccion, envio)
    return paquete

def PedirDatosActualizacion(paquetes):
    ListarPaquetes(paquetes)
    CodigoEditar = input('Ingresa el código del paquete a editar')
    for paq in paquetes:
        if paq[0] == CodigoEditar:
            existeCodigo = True
            break
    if existeCodigo:
        direccion = input('Ingresa la dirección a modificar: ')
        envio = float(input('Ingresa el envío a modificar: '))
        paquete = (CodigoEditar, direccion, envio)
    else:
        paquete = None
    return paquete

def PedirDatosEliminacion(paquetes):
    ListarPaquetes(paquetes)
    CodigoEliminar = input('Ingresa el código del paquete a eliminar')
    for paq in paquetes:
        if paq[0] == CodigoEliminar:
            existeCodigo = True
            break
    if not existeCodigo:
        CodigoEliminar = ''
    return CodigoEliminar

