#Mostrar elemento a elemnto de una lista
def mostrarLista (lista):
    for elemento in lista:
        print (elemento)

profesiones = ["medico", "arquitecto", "ingeniero", "cajero", "carnicero", "docente"]
edades = [18,34,19,22,45,10,64]
mostrarLista (profesiones)
mostrarLista (edades)

#Número más grande, más pequeño, y promedio de lista.
def infolist(lista):
    mayor = max (lista)
    menor = min (lista)
    acumulador = 0
    for elemento in lista :
        acumulador += elemento
    sizelist = len (lista)
    promedio = acumulador / sizelist
    print (f"El número menor de la lista es {menor}, el más grande es {mayor} y el promedio es {promedio}")
edades = [18,34,19,22,45,10,64]
infolist(edades)

#Saludar n veces
def saludar (cantidad = 0):
    print ("¡Holaaa!  "* cantidad)
saludar (15)

#De la lista de número enteros devolver todos los números pares
def listapares(lista):
    pares = []
    for elemento in lista:
        if elemento % 2 == 0 :
            pares.append (elemento)
    return pares

edades = [18,34,19,13,22,45,10,64]
edadesPares = listapares(edades)
print(edadesPares)

#Devolver elementos mayores a 24
def mayoreslista(lista):
    mayores = []
    for elemento in lista:
        if elemento > 24 :
            mayores.append (elemento)
    return mayores

edades = [18,34,19,13,22,45,10,64]
edadesMayores = mayoreslista(edades)
print (edadesMayores)

#Función calcular IMC
def calcularIMC (peso,altura):
    return peso / (altura**2)
imc = calcularIMC (55, 1.52)
print (imc)

#Función despedida del programa
def despedida():
    print ("gracias por usar el programa, ¡hasta pronto!")
despedida()
