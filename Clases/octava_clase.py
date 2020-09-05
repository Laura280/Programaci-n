import random

dado = random.randint (1,6)
print(dado)

NumeroParticipante = int(input("Por favor ingrese un número: "))
while (NumeroParticipante != dado): 
    print("No adivinó el número")
    NumeroParticipante = int(input("Por favor ingrese un número: "))

print("Adivinó el número")

listaalimentos = []
decision =
