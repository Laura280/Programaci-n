#Dada una lista mosrrar en pantalla el número mayor, menor y el promedio.
def numerosLista(lista):
    mayor = max (lista)
    menor = min (lista)
    acomulador = 0
    for elemento in lista :
        acomulador += elemento
    sizelist = len(lista)
    promedio = acomulador / sizelist
    print (f"en la lista el número mayor es {mayor}, el menor es {menor} y el promedio de lista es {promedio}")
numeros = [3,5,4,7,3,5,9,5]
numerosLista(numeros)

#Dada una lista devolver unicamente los pares
def listaPares(lista):
    pares = []
    for elemento in lista:
        if elemento % 2 == 0 :
            pares.append (elemento)
    return pares

listaNumeros = [5,8,6,5,9,2,6,8,]
listaNumerosPares = listaPares(listaNumeros)
print (listaNumerosPares)

#Dado un mensaje mostrarlo en pantalla
def mensaje():
    print ("Hola, espero que se encuentre muy bien, gracias por visitarnos.")
mensaje()

#Dado un número le reste 12 y muestre el resultado
def numeroDado (numero):
    return numero-12
numero1 = numeroDado(36)
print(f"el resultado de la resta es {numero1} ")

#Dado un número lo multiplique por 12 y devuelva el resultado
def numeroFijo (numero):
    return numero*12
numero2 = numeroFijo(12)
print (f"El número multiplicado por doce da como resutado {numero2}")

#Dado un número dividirlo por 12 y devolver el resultado
def numerodado (numero):
    return numero/12
numero3 = numerodado(108)
print (f"el resultado de esta división es {numero3}")

#Dado un número sumarle 12 y devolver el resultado 
def numerofijo (numero):
    return numero+12
numero4 = numerofijo(320)
print(f"El resulatdo de la suma es {numero4}")

#Dada una de las funciones anteriores y su entrada mostrar en pantala el resultado
def operacionNumero (operacion, numero):
    print (operacion(numero))
operacionNumero (numeroDado, 44)
operacionNumero (numeroFijo, 6)
operacionNumero (numerodado, 273)
operacionNumero (numerofijo, 5)

