#esto es una prueba 
#class Personaje:
    # nombre='Default'
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0

#Abrimos función: constructor de la clase
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def imprimir_atributos(self):
        print("-Nombre: ",self.nombre)
        print("-Fuerza: ",self.fuerza)
        print("-Inteligencia: ",self.inteligencia)
        print("-Defensa: ",self.defensa)
        print("-Vida: ",self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0 
        print(self.nombre, "ha muerto")
        

    def dañar(self,enemigo):
            return self.fuerza - enemigo.defensa    

    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        if 0 >= daño:
            daño = 0
        enemigo.vida = enemigo.vida - daño
        print(self.nombre," ha realizado un ataque RAAAAAA. Ya muerete ", enemigo.nombre)
        print(self.nombre," ha realizado ", daño, " puntos de daño a ", enemigo.nombre)
        print("Vida restante de ", enemigo.nombre, " es de ", enemigo.vida)
        #RETO
        if (self.fuerza - enemigo.defensa)<=0:
            enemigo.morir()

#variable del constructor vacío en este momento
mi_personaje = Personaje("Isaac",40,3,70,100)
mi_personaje.imprimir_atributos()
# mi_personaje.subir_nivel(10,1,5)
# print("_________________")
# mi_personaje.imprimir_atributos()
# print (mi_personaje.esta_vivo())
# print (mi_personaje.morir())

mi_enemigo = Personaje("Vergil",70,30,70,100)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.imprimir_atributos()
#print(mi_personaje.dañar(mi_enemigo))
#mi_personaje.nombre = "MirosMage"
#mi_personaje.fuerza = "25"
# mi_personaje.inteligencia = "50"
# mi_personaje.defensa = "30"
# mi_personaje.vida = "5"

# print("El nombre del personaje es", mi_personaje.nombre)
# print("Estas son sus estadisticas:")
# print("     Fuerza:", mi_personaje.fuerza)
# print("     Inteligencia:", mi_personaje.inteligencia)
# print("     Defensa:", mi_personaje.defensa)
# print("     vida:", mi_personaje.vida)