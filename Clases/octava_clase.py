import random

dado = random.randint (1,6)
print(dado)

NumeroParticipante = int(input("Por favor ingrese un número: "))
intentos = 1

while (NumeroParticipante != dado): 
    print("No adivinó el número")
    intentos =intentos + 1
    NumeroParticipante = int(input("Por favor ingrese un número: "))

print(f"Ha realizado {intentos} intentos antes de adivinar el número")
print("felicitaciones, adivinó el número")

listaalimentos = []
listaalimentos = ["pastas, papas fritas, carne, helado, empanadas,"]
sizelist =len (listaalimentos)
print (sizelist)

for i in range (sizelist):
    print(f"las {listaalimentos [i]} son de mis comidas favoritas")

print(listaalimentos[2])
