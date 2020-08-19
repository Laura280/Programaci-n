nombre = input("por favor ingrese su nombre : ")
peso = float(input("por favor ingrese su peso en kilogramos : "))
estatura = float(input("por favor ingrese su estatura en metros : "))

imc = peso/estatura**2
if (imc <18.5) :
    print(f"{nombre} tiene infrapeso")
elif (imc>=18.5 and imc<25) :
    print(f"{nombre} esta con un peso normal")
elif(imc>=25 and imc<30) :
    print(f"{nombre} tiene sobrpeso")
elif (imc>=30 and imc<35) : 
    print(f"{nombre} tiene obesidad")
else:
    print (f"{nombre} tiene obesidad morbida")