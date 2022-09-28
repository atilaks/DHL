from BD.Conexion import DAO
import Funciones

def MenuPrincipal():
    contituar = True
    while(contituar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print('===== MENÚ PRINCIPAL ====')
            print('1.- Lista de paquetes')
            print('2.- Registrar paquete')
            print('3.- Actualizar paquete')
            print('4.- Eliminar paquete')
            print('5.- Salir')
            print('=========================')
            opcion = int(input('Seleccione una opción: '))

            if opcion <1 or opcion> 5:
                print('Opción incorrecta')
            elif opcion == 5:
                contituar = False
                print('Hasta pronto')
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try: 
            paquetes = dao.ListarPaquetes()
            if len(paquetes) > 0:
                Funciones.ListarPaquetes(paquetes)
            else:
                print('No se encontraron paquetes')
        except:
            print('Ocurrió un error')
    elif opcion == 2:
        paquete = Funciones.PedirDatosPaquete()
        try:
            dao.RegistrarPaquete(paquete)
        except:
            print('Ocurrió un error')
    elif opcion == 3:
        try:
            paquetes = dao.ListarPaquetes()
            if len(paquetes) > 0:
                paquete = Funciones.PedirDatosActualizacion(paquetes)
                if paquete:
                    dao.ActualizarPaquete(paquete)
                else:
                    print('Código de paquete no encontrado')
            else:
                print('No se encontró el paquete')
        except:
            print('Ocurrió un error')
    elif opcion == 4:
        try:
            paquetes = dao.ListarPaquetes()
            if len(paquetes) > 0:
                CodigoEliminar = Funciones.PedirDatosEliminacion(paquetes)
                if not (CodigoEliminar == ""):
                    dao.EliminarPaquete(CodigoEliminar)
                else:
                    print('No se encontró el paquete')
            else:
                print('No se encontró el paquete')
        except:
            print('Ocurrió un error')

MenuPrincipal()