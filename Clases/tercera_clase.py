a = int (input("ingrese el primer número entero : "))
b = int (input("ingrese el segundo número entero : "))
print (a,b)

if (a == b ) :
    print("son números iguales")
elif (a>b) :
    print("El numero", a, "es mayor que el numero", b)
else:
    print(f"el numero B {b} es mayor que A {a}")

#Dada una temperatura determinar si el paciente esta sano o no
# Temperatura menor a 36 grados ipotermina
# Temperatura en el intervalo de 36.38 grados normal
# Temperatura en el intervalo de 37.5-38 grados normal
# Temperatura mayor a 38 grados fiebre
#Muestre el nombre del paciente y su estado

name = input("ingrese el nombre del paciente : ")
temperatura = float (input("ingrese la temperatura del pacente : "))
if (temperatura < 36) :
    print(f"El paciente llamado {name} se necuentra en estado de hipotermia")
elif (temperatura>=36 and temperatura< 37.5) :
    print(f"el paciente llamado {name} se encuentra en estado favorable")
elif (temperatura>=37.5 and temperatura< 38) :
    print(f"el paciente llamado {name} se encuentra en estado alerta")
else:
    print (f"el paciente llamado {name} se encuentra en estado de fiebre")