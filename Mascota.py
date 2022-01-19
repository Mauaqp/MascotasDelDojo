class Mascota:
    lista_mascotas = []
    def __init__(self,name, tipo, golosinas, salud, energia ):
        self.name = name
        self.tipo = tipo
        self.golosinas = salud
        self.energia = energia
        Mascota.lista_mascotas.append(self)
    
    def dormir(self):
        print(self.name + " ha tomado una siestecita")
    
    def comer(self):
        print(self.name + " ha comido")
        return self
    
    def jugar(self):
        print(self.name + " está jugando")
    
    def sonido (self):
        print(self.name + " ha emitido sonidos")