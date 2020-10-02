#FUNCIONES#
#Devolver numero mayor o decir si son iguales
a = int(input("Pro favor ingrese el primer número entero :")) 
b = int(input("Por favor ingrese el segundo número entero :")) 
print (a,b)

def infNumero (numero1, numero2):
    if (a == b):
        print ("Estos dos números son iguales")
    elif (a>b):
        print ("El primer número ingresado", a, "es mayor que e segundo número ingresado", b)
    else :
        print (f"el número  {b} es mayor que {a}")

infNumero (a,b)
infNumero (7,8)


#En una lista, mostrar nombre por nombre
def mostrarLista (lista):
    for elemento in lista :
        print (elemento)

listaNombres = ["Laura", "Karla", "Juan", "Daniel"]
mostrarLista (listaNombres)


#Devolver el IMC
def calcularIMC (peso, altura):
    return peso / (altura**2)
imc = calcularIMC (56,1.52)
print (imc)


#Dada la función imc y los valores de peso y altura mostrar el IMC
def mostrarIMC (funcionIMC, estatura, peso):
    imc = funcionIMC (estatura,peso)
    print (f"el IMC calculado es {imc}")

mostrarIMC(calcularIMC, 1.52,56)


#CLASES Y OBJETOS#
#Objeto con id, nombre, peso, altura, sexo

class Persona:
    def __init__ (self, idIngresado, nombreIngresado, pesoIngresado, alturaIngresada, sexoIngresado):
        self.id = idIngresado
        self.nombre = nombreIngresado
        self.peso = pesoIngresado
        self.estatura = alturaIngresada
        self.sexo = sexoIngresado
        print ("Se ha creado un nuevo objeto persona")
    def atributos (self):
        print (f"Hola mi nombre es {self.nombre}, soy de sexo {self.sexo},")

