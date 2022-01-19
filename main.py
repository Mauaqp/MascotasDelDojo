from Ninja import Ninja
from Mascota import Mascota

#Instrucciones
ninja1 = Ninja("Mauri", "Peraltilla", "Milly", "Galletita", "Hueso")
mascota1 = Mascota("Milly", "Perrito", "Galletitas ricas", "100", "50")
mascota2 = Mascota("Brownie", "Perrito", "Galletitas de pollito", "100", "100")
ninja1.getNombre()
ninja1.caminar().alimentar().bañar()