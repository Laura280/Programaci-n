class Persona:
    def __init__ (self, estaturaIngresado, pesoIngresado, 
    nombreIngresado,idIngresado,edadIngresado) :
        self.raza = "Humana"
        self.estatura = estaturaIngresado
        self.edad = edadIngresado
        self.nombre = nombreIngresado
        self.peso = pesoIngresado
        self.id = idIngresado
        print ("Hola mundo estoy viv@")
    def caminar (self):
        print("Hola voy a caminar")
    def saludo (self, saludoEspecial):
        print (saludoEspecial)
class Arquitecto (Persona):
    
    def dibujar_Planos (self):
        print (f"Hola soy {self.nombre} voy a dibujar un plano")

class Biomedico (Persona):
    
    def cultivar_Celulas (self):
        print (f"Hola soy {self.nombre} voy a cultivar celulas")

karla = Arquitecto (1.62,48, "Karla", 1000934654,18)
karla.caminar()
juan = Biomedico (1.76, 82, "Juan Pablo", 9876543867,23)
juan.caminar()
karla.saludo("HOLI CRAYOLI")
juan.saludo("HOLA COCACOLA")
karla.dibujar_Planos()
juan.cultivar_Celulas()