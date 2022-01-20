from Ninja import Ninja
from Mascota import Mascota

#Instrucciones
mascota1 = Mascota("Milly", "Perrito", "Galletitas", 100, 20)
mascota2 = Mascota("Brownie", "Perrito", "Galletitas de pollito", 200, 100)
ninja1 = Ninja("Mauri", "Peraltilla", mascota1, "Galletita", "Hueso")
ninja1.getNombre()
ninja1.caminar(0).alimentar(0).bañar(0)
mascota1.estado_mascota()