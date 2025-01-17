class Personaje:
    #Atributos de la clase 
    #nombre = 'Default'
    #fuerza = 0
    #inteligencia = 0
    #defensa = 0
    #vida = 0

    #Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    #¿Qué significa self? Referencia al mismo objeto.
    #¿Qué es init? Constructor que inicializa el atributo del objeto
    #¿Por qué empieza con doble guión bajo? Porque es método mágico. Dunder
    #¿En qué momento se ejecuta el método init? Cuando se crea un objeto
    #snake_case y CamelCase
    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:",self.fuerza)
        print("-Inteligencia:",self.inteligencia)
        print("-Defensa:",self.defensa)
        print("-Vida:",self.vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        #self.fuerza += fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre,"ha muerto")
        #return self.vida <= 0
        
    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño=self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "Ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
             print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

class Guerrero (Personaje):
    #sobreescribir constructor
    def __init__ (self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
    #pass
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada: ", self.espada)

    def elegir_arma(self):
        opcion = int(input("Elige un arma: \n(1) Lanza de obsidiana, daño 10\n(2) Lanza de chaya, daño 5\n>>>>>>> "))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 5
        else:
            print("Opción no válida")
            self.elegir_arma()


    def daño(self,enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
class Mago (Personaje):
    #sobreescribir constructor
    def __init__ (self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    #pass
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-libro: ", self.libro)

    def elegir_arma(self):
        opcion = int(input("elige in arma: \n (1)Hechizos de programación, daño 10 \n(2) Recetario de chaya , daño 2 \n>>>>>>>"))
        if opcion == 1:
            self.libro = 10
        elif opcion == 2:
            self.libro = 2
        else:
            print("Opcion no valida")
            self.elegir_arma()
    def daño(self,enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

#Variable del constructor de la clase
michael_jackon = Personaje("Michael Jackson",20,15,10,100)
tlatoani = Guerrero("Apocalipto",50,70,30,100,5)
merlin=Mago("Merlin",20,15,10,100,6)
tlatoani.imprimir_atributos()
tlatoani.elegir_arma()
#tlatoani.imprimir_atributos()
merlin.imprimir_atributos()
merlin.elegir_arma()
#merlin.imprimir_atributos
michael_jackon.imprimir_atributos()

#ataques masivos
michael_jackon.atacar(tlatoani)
tlatoani.atacar(merlin)
merlin.atacar(michael_jackon)


# mi_personaje = Personaje("Dante",1000, 3,70,100)
# mi_personaje.imprimir_atributos()
# mi_enemigo = Personaje("Vergil",70,30,70,100)
# mi_personaje.atacar(mi_enemigo)
# mi_enemigo.imprimir_atributos()


#print(mi_personaje.dañar(mi_enemigo))
#print(mi_personaje.esta_vivo())
#mi_personaje.subir_nivel(10,1,5)
#print("---------------------")
#mi_personaje.imprimir_atributos()
#dmi_personaje.imprimir_atributos
# mi_personaje.nombre = "ChemaFighter"
# mi_personaje.fuerza = 30
# mi_personaje.inteligencia = 12
# mi_personaje.defensa = 28
# mi_personaje.vida = 3
# print("El nombre del personaje es ",mi_personaje.nombre)
# print("La fuerza del personaje es ",mi_personaje.fuerza)
# print("La inteligencia del personaje es ",mi_personaje.inteligencia)
# print("La defensa del personaje es ",mi_personaje.defensa)
# print("La vida del personaje es ",mi_personaje.vida)