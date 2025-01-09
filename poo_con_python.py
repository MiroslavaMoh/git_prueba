#esto es una prueba 
class Personaje:
    nombre='Default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

#Indicar que no haga nada de momento
    pass

#variable del constructor vacío en este momento
mi_personaje = Personaje()
mi_personaje.nombre = "MirosMage"
mi_personaje.fuerza = "25"
mi_personaje.inteligencia = "50"
mi_personaje.defensa = "30"
mi_personaje.vida = "5"

print("El nombre del personaje es", mi_personaje.nombre)
print("Estas son sus estadisticas:")
print("     Fuerza:", mi_personaje.fuerza)
print("     Inteligencia:", mi_personaje.inteligencia)
print("     Defensa:", mi_personaje.defensa)
print("     vida:", mi_personaje.vida)