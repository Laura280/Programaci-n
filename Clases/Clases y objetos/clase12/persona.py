class Persona():
    def __init__ (self, nombreIn, edadIn, idIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.id = idIn
    #Acciones
    #Hablar
    def hablar (self, mensaje) :
        print(f"Hola soy {self.nombre} y teno algo que deir : {mensaje}")
    #Comer
    def comer (self, plato):
        print (f"Hola soy {self.nombre} y voy a comer un delicioso {plato} ")

