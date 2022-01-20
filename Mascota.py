class Mascota:
    lista_mascotas = []
    def __init__(self,name, tipo, golosinas, salud, energia ):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energia
        Mascota.lista_mascotas.append(self)
    
    def dormir(self):
        self.energia += 25
        print(self.name + " ha tomado una siestecita")
        return self
    
    def comer(self):
        self.energia += 50
        print(self.name + " ha comido")
        return self
    
    def jugar(self):
        self.energia -= 50
        print(self.name + " está jugando")
        return self

    def sonido (self):
        print(self.name + " ha emitido sonidos")
        return self

    def estado_mascota(self):
        print("---Estado de " + self.name + "---")
        print("Energía: " + str(self.energia))
        print("Salud: " + str(self.salud))