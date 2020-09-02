#----se crea ListaNombres----#
ListaNombres = []
ListaNombres = ["Melay" ,
        "Karla" ,
        "Laura Paredes" ,
        "Laura Montoya" ,
        "Juan Pablo" , 
        "Mario" ,
        "Valeria" ,
        "Santi" ]

listaEdades = [20,18,18,18,21,20,18,18]
print (ListaNombres)
print (ListaNombres [2])
print (ListaNombres [-1])
ListaNombres.append("Daniel")
print (ListaNombres[-1])
print (ListaNombres)

ListaNombres.pop(-1)
print (ListaNombres)
ListaNombres.append("Daniel")
listaEdades.append(27)
sizelist = len (ListaNombres)
print(sizelist)

for i in range (sizelist):
    print (f"hola soy {ListaNombres [1]} y estoy feliz programando")
print ("segundo metodo")

for nombre in ListaNombres:
    print (f"hola soy {nombre} y estoy feliz programando")


for i in range (sizelist):
    print (f"nombre : {ListaNombres [i]} Edad: {listaEdades [i]} ")

listaHobbies = []
decision = 0
while (decision == 0):
    hobbie = input("¿Cuál es tu hobbie favorito? : ")
    listaHobbies.append(hobbie)
    decision =int (input ("""Ingrese :
            0= Para seguir agregando Hobbies
            !0 = Para finalizar
    : """))
print(listaHobbies)
