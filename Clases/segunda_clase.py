nombre = input ("por favor ingrese su nombre : ")
print ("hola", nombre, "Eres bienvenido a este código")
edad = int (input ("por favor ingrese su edad : "))
estatura = float (input ("por favor ingrese su estatura : "))

print (edad)
print (estatura)

print (type(nombre))
print (type(edad))
print (type(estatura))

if  (edad >= 18) :
    print("usted es mayor de edad")
    print("ya eres todo un adult@")

    if (estatura>1.70):
        print("hola allá arriba eres muy alto")