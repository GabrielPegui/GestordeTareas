class Tarea:
    def __init__(self,titulo,descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = 'no completada'

    def __str__(self):
        return f'{self.titulo} , {self.descripcion} , {self.estado}'
    

class AgregarTarea:

    def addtarea(self,tarea,diccionario):
        diccionario[tarea.titulo] = tarea

class EliminarTarea:
    
    def deletetarea(self,tarea,diccionario):
        diccionario.pop(tarea.titulo)

class MostrarTareas:

    def mostrartarea(self,diccionario):
        for nombretarea,tareadescripcion in diccionario.items():
            print(f'Tarea : {nombretarea} y descripcion: {tareadescripcion}')

class EstatusTarea:
    def cambiarestatus(self,tarea):
        if tarea.estado == 'no completada':
            tarea.estado = 'completada'
        else:
            print('su tarea cambio a no completada')
            tarea.estado = 'no completada'
      









    


        