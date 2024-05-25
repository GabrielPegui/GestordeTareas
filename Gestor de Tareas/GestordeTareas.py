# programa de gestor de tareas 

#importamos el archivo que necesitamos para el gestor
from Clases import clases_gestoras


#almacenador de tareas, en este caso un diccionario
Tareas = {}

#clases que tienen metodo para el gestor de tareas

AgregarTarea = clases_gestoras.AgregarTarea()
EliminarTarea = clases_gestoras.EliminarTarea()
MostrarTarea = clases_gestoras.MostrarTareas()
EstatusTarea = clases_gestoras.EstatusTarea() 

#ejecucion del gestor de tareas

print('Bienvenido a su Gestor de Tareas')
print()
print('A continuacion Elija una opcion: ')


while True:
        print('A continuacion Elija otra opcion si desea opcion: ')
        print()
        print('1.Agregar una Tarea')
        print('2.Eliminar una Tarea')
        print('3.Mostrar mis Tareas')
        print('4.completar una Tarea')
        print('5.Salir del gestor de Tareas')
        print()

        Seleccion = input('Que opcion Desea Elegir: ')

        while not Seleccion.isdigit():
            print('debe introducir un numero para poder continuar')
            print()
            Seleccion = input('Que opcion Desea Elegir: ')

        Seleccion = int(Seleccion)

        while Seleccion <= 0 or Seleccion > 5:
            print('elija una de las opciones disponible para poder continuar')
            print()
            Seleccion = input('Que opcion Desea Elegir: ')
            Seleccion = int(Seleccion)


      


        if Seleccion == 1: #procedimiento de agregar tarea
            print('A contiuacion creara su tarea')
            titulo = input('Escriba el Titulo de su tarea o Nombre: ')
            descripcion = input('Escriba la descripcion o en que consiste: ')
            Tarea = clases_gestoras.Tarea(titulo,descripcion)
            AgregarTarea.addtarea(Tarea,Tareas)
            print('Tarea creada y Agregada')
            print('asi quedaria: ')
            print()
            print(Tarea)
            print()
            print()
           
           

        elif Seleccion == 2: #procedimiento de eliminar tarea
        
            print('A contiuacion Eliminara una de sus tareas')
            print('Cual Tarea desea Eliminar ? ')
            MostrarTarea.mostrartarea(Tareas)
            Seleccion2 = input('Escriba el nombre de la Tarea a Eliminar: ')
            while not Seleccion2 in Tareas:
                print('La tarea que intentas eliminar no existe, debe ser uan tarea existente para eliminarla')
                Seleccion2 = input('Escriba el nombre de la Tarea a Eliminar: ')
            tareaaeliminar = Tareas[Seleccion2]
            EliminarTarea.deletetarea(tareaaeliminar,Tareas)
            print('Tarea Eliminada con exito!!!! ')
            print()
            print()


        elif Seleccion == 3: #procedimiento de mostrar tareas
            print('A contiuacion Mostraremos sus tareas')
            if not Tareas:
                print('Aun no tiene Tareas!')
                Seleccion3 = input('desde crear una ?? ')
                if Seleccion3.lower() == 'si':
                    print('A contiuacion creara su tarea')
                    titulo = input('Escriba el Titulo de su tarea o Nombre: ')
                    descripcion = input('Escriba la descripcion o en que consiste: ')
                    Tarea = clases_gestoras.Tarea(titulo,descripcion)
                    AgregarTarea.addtarea(Tarea,Tareas)
                    print('Tarea creada y Agregada')
                    print('asi quedaria: ')
                    print(Tarea)
                    print()
                    print()
                else:
                    pass
            else:
             MostrarTarea.mostrartarea(Tareas)
             print()
             print()
                    
                
        
            

        elif Seleccion == 4:
            print('Bienvenido al estatus de sus Tarea, donde puede cambiar el estado de sus tareas a -completado- una vez la haya terminado')
            print('por defecto el estado al crear una tarea es de -no completado- y aqui podra cambiarlo a -completado- una vez completada la tarea')
            print('solo hay 2 cambios, de completado a no completado y viceversa!')
            print('Asi que si la tarea esta en estado -completado- y procede a cambiar el estado o estatus sera a -no completado-')

            Seleccion4 = input('nombre de la tarea a cambiar de estado o estatus: ')

            while not Seleccion4 in Tareas:
                print('La tarea que intentas cambiar de estado/estatus no existe, debe ser uan tarea existente !.')
                Seleccion4 = input('Escriba el nombre de la Tarea a Eliminar: ')
            tareaacambiar = Tareas[Seleccion4]
            
            EstatusTarea.cambiarestatus(tareaacambiar)
            print(f'estatus de la tarea {Seleccion4} cambiada')
            print()
            print()
            






        else:
            print('has seleccionado la opcion de Salir. a continuacion el programa se cerrara y perdera sus tareas!')
            break












