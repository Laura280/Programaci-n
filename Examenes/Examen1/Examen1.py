nombre = input("por favor ingrese su nombre : ")
procedencia = input("por favor ingrese su procedencia : ")

if (procedencia == "china" or procedencia == "iran" or procedencia == "italia") :
    print(f"{nombre} de procedencia de {procedencia} debe ir a estado de observación")
else:
    temperatura = float(input("por for ingrese su temperatura en grados celcius : "))
    if (temperatura <36) :
        print(f"{nombre} se encuentra en estado de hipotermia")
    elif (temperatura >=36 and temperatura <=38.4) :
        print(f"{nombre} se encuentra en estado saludable")
    elif (temperatura >=38.5 and temperatura <=40) : 
        print(f"{nombre} esta en estado de alerta")
    else:
        print(f"{nombre} se encuentra en estado de peligro")
