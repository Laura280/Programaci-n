#---Datos inicales---#
ListaPesos = [20000, 30000, 2500, 1000, 7600]

#--Pregntas al usuario--#
PreguntaMenu ="""
Por favor ingrese alguna de estas opciones:
            1- Convertir a pesos
            2- Añadir nuevo valor
            3- Ver máximo, mínimo y promedio de ingresos
            4- Eliminar un valor
            5- Salir del programa 
:"""
PreguntaConversionPesos= """
Por favor ingresa una de estas opciones:
            C-Convrtir a pesos colombianos
            D-Convertir a dolares
            E-Convertir a euros
:"""
PreguntaAgragarValor = "Por favor ingrese el valor que desea agregar"
PreguntaRemover = "Ingrese la posición que desee eliminar"

#---mensaje Error---#
mensajeErrorNumero = "Recuerde ingresar una opción válida 1,2,3,4,5"
mensajeErrorMoneda = "Recuerde ingresar una opción válida C,D,E"
#---Mensaje Informativo---#
mensajeOpcion = "Usted escogió la opción {} :"
mensajeSalida = "Gracias por usar el programa"
mensajePesos = "No es necesaria la conversión pero, se muestra la lista"

#---inicio---#
opcion = int (input(PreguntaMenu))
#-Calculos-#
ListaMonedaColombiana = ListaPesos
ListaDolares = []
ListaEuros = []
ListaClasificación = []

#--Conversión dolares a pesos--#
for elemento in ListaMonedaColombiana:
    dolares = elemento*0.00027
    ListaDolares.append(dolares) 

#--Conversión de euros a pesos--#
for elemnto in ListaMonedaColombiana:
    euros= elemento*0.00023
    ListaEuros.append(euros)

#--Cálculo máximo, mínimo y promedio--#
mayor=max(ListaMonedaColombiana)
menor=min(ListaMonedaColombiana)
acomulado= 0
for elemento in ListaMonedaColombiana:
    acomulado+=elemento
    promedio= acomulado/len(ListaMonedaColombiana)
promediopesos = round (promedio, 4)

while (opcion !=5) :
    if (opcion ==1):
        print(mensajeOpcion.format(1))
        conversion = input(PreguntaConversionPesos)
        if (conversion == "D"):
            print(ListaDolares)
        elif (conversion =="E") :
            print(ListaEuros)
        elif (conversion == "C") :
            print (mensajePesos)
            print (ListaPesos)
        else :
            print (mensajeErrorMoneda)
    elif (opcion ==2):
        print (mensajeOpcion.format(2))
        añadir = int(input(PreguntaAgragarValor))
        ListaMonedaColombiana.append(añadir)
        print (ListaPesos)
    elif (opcion ==3):
        print (mensajeOpcion.format(3))
        print ("El ingreso máximo fue", mayor)
        print ("El ingreso mínimo fue", menor)
        print ("El ingreso promedio fue", promediopesos)
    elif (opcion ==4):
        print (mensajeOpcion.format(4))
        print(ListaPesos)
        valorRemovido = int(input(PreguntaRemover))
        ListaPesos.pop(valorRemovido)
        print (ListaPesos)
    else:
        print (mensajeErrorNumero)
    opcion = int (input(PreguntaMenu))

#--Salida del programa--#
print (mensajeSalida)






