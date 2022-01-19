from Mascota import Mascota


class Ninja:
    lista_ninjas = []
    def __init__(self, nombre,apellido, mascota, premio, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascota
        self.premio = premio
        self.comida_mascota = comida_mascota
        Ninja.lista_ninjas.append(self)

    #Funciones
    def getNombre (self):
        print(self.nombre)
        return self.nombre
    
    def caminar(self):
        print(self.nombre + " sacó a pasear a " + Mascota.lista_mascotas[0].name)
        Mascota.lista_mascotas[0].jugar()
        return self

    def alimentar(self):
        print(self.nombre + " alimentó a " + Mascota.lista_mascotas[0].name)
        Mascota.lista_mascotas[0].comer()
        return self
    
    def bañar(self):
        print(self.nombre + " bañó a " + Mascota.lista_mascotas[0].name)
        Mascota.lista_mascotas[0].sonido()
        Mascota.lista_mascotas[0].dormir()
        return self

    