#Función por cada uno de los puntos#

##devolver número elevado al cuadrado
def numeroalCuadrado (numero):
    return numero**2
num1= numeroalCuadrado(6)
print (f"El número dado elevado a la dos es {num1}") 

##devolver número elevado a la 3
def numeroalCubo (numero):
    return numero**3
num2= numeroalCubo(6)
print (f"El número dado elevado a la tres es {num2}") 

##devolver número elevado a la 4
def numeroalaCuatro (numero):
    return numero**4
num3= numeroalaCuatro(6)
print(f"El número dado elevado a la cuatro es {num3}") 

##devolver número elevado a la 5
def numeroalaCinco (numero):
    return numero**5
num4= numeroalaCinco(6)
print(f"El número dado elevado a la cinco es {num4}") 

##Función dada otra función anterior muestre el resultado de las mismas
def operacionNueroElev (operacion, numero):
    print (operacion(numero))
operacionNueroElev (numeroalCuadrado,5)
operacionNueroElev (numeroalCubo,4)
operacionNueroElev (numeroalaCuatro,8)
operacionNueroElev (numeroalaCinco,9)

#Clases#

#Doctor

class Doctor:
    def __init__ (self, idIng, nombreIng, sexoIng, universidadIng) :
        self.id = idIng
        self.nombre = nombreIng
        self.sexo = sexoIng
        self.universidad = universidadIng
    def atributos(self):
        print(f"Hola soy el Doctor {self.nombre} de sexo {self.sexo} y soy egresado de la universidad {self.universidad}")
    def sintomas (self, lista):
        for elemento in  lista:
            print (elemento)

doctor1 = Doctor (21365289, "Felipe", "masculino", "Ces")
listaSintomas = ["tos", "dolor de cabeza", "fiebre", "malestar", "dolor de garganta"]
doctor1.atributos()
doctor1.sintomas(listaSintomas)

#Neurologo
class Neurologo (Doctor):
    def __init__ (self, idIng, nombreIng, sexoIng, universidadIng, experienciaIng, consultorioIng, salarioIng) :
        Doctor.__init__(self, idIng, nombreIng, sexoIng, universidadIng)
        self.experiencia = experienciaIng
        self.consultorio = consultorioIng
        self.salario = salarioIng
    def atributos (self):
        print(f"Hola soy el Doctor {self.nombre} de sexo {self.sexo} y soy egresado de la universidad {self.universidad} con experiencia de {self.experiencia}, trabajo en el consultorio {self.consultorio} y tengo un salario de {self.salario}")
    def pacientes (self, lista):
        for elemento in lista:
            print (f"el paciente a seguir es : {elemento}")

doctor1= Neurologo (682746834, "Felipe", "masculino", "ces", 5, 107, 7200000 )
listaPacientes = ["Camilo", "Esteban", "Julian", "Mariana"]
doctor1.atributos()
doctor1.pacientes(listaPacientes)

#Cárdiologo
class Cardiologo (Doctor):
    def __init__ (self, idIng, nombreIng, sexoIng, universidadIng, experienciaIng, consultorioIng, salarioIng, habitacionesIng) :
        Doctor.__init__(self, idIng, nombreIng, sexoIng, universidadIng)
        self.habitaciones = habitacionesIng
        self.experiencia= experienciaIng
        self.salario = salarioIng
        self.consultorio = consultorioIng
    def atributos (self):
        print (f"Hola soy el Doctor {self.nombre} de sexo {self.sexo} mi numero de identificación es {self.id} y soy egresado de la universidad {self.universidad} con experiencia de {self.experiencia}, trabajo en el consultorio {self.consultorio} y tengo un salario de {self.salario}, hay {self.habitaciones} disponibles")
    def sintomas (self, lista):
        for elemento in  lista:
            print (elemento)
            print ("Ya sé que tiene el paciente")

doctor3=Cardiologo (654348326, "Pedro", "Masculino", "UPB", 7, 23, 8000000, 7)
listaSintomas2 = ["tos", "dolor de cabeza", "fiebre", "malestar", "dolor de garganta"]
doctor3.atributos()
doctor3.sintomas(listaSintomas2)