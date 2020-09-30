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
        print (f"el número B {b} es mayor que A {a}")

infNumero (a,b)
infNumero (7,8)