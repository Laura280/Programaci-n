#--Datos iniciales--#
ListaDolares = [20000, 30000, 4000, 2500,1000, 7600]

#--Preguntas al usuario--#
PreguntaMenú = """
Por favor ingrese una de las siguientes opciones : 
    1- Conversión dólares
    2- Mostrar clasificación de ingresos
    3- Mostrar minimo, máximo y promedio de ingresos
    4- Salir del programa
: """
PreguntaConversiónDolares  = """
Por favor ingrese una de las siguientes opciones :
    A- Convertir a peso Colombiano
    B- Convertir a dóares
    C- Convertir a euros
: """

#--Mensaje informativo--#
mensajeOpcion = "usted ha escogido la opcion {}"
mensajeDolares = "No es necesario hacer la conversión, pero se muestra la lista"
mensajeSalida = "Ha finalizado, gracias por usar el programa"
#--Mensaje Error--#
mensajeErrorNumero = "Recuerde ingresar una opción válida  4,3,2,1"
mensajeErrorMoneda = " REcuerde ingresar una opción válida A, B, C"


option = int (input(PreguntaMenú))
listaPesos= []
listaEuros = []
listaClasificación =[]

#-- 1 dolar = 3700 PesoColombiano--#
for elemento in ListaDolares:
    pesos = elemento * 3700
    listaPesos.append(pesos)
#--- 1 _Euro =(1Dolar.84)---#
for elemento in ListaDolares :
    euros = (elemento*0.84)
    listaEuros.append(euros)

#--Estados de Ingresos--#
for elemento in ListaDolares :
    clasificación = ""
    if (elemento < 1000 ):
        clasificación = "Bajos ingresos"
    elif (elemento > 1000 and elemento < 7000):
        clasificación = "Ingresos medios"
    elif (elemento >= 7000 and elemento < 20000):
        clasificación = "Ingresos altos"
    else:
        clasificación = "Ingresos muy altos"
    listaclasificación.append(clasificación)

#--Calcular máximo y minimo--#
superior = max (ListaDolares)
menor = min (ListaDolares)
acomulador = 0
for elemento in ListaDolares :
    acomulador += elemento
primedio= acomulador/len(ListaDolares)
promedioDolares = round (promedio,2)


while (opcion != 4) :
    if(opcion == 1):
        print(mensajeOpciion.format(1))
        if (conversión == "A"):
            print (listaPesos)
        elif (conversion == "C") :
            print (listaEuros)
        elif (conversion == "B") :
            print (mensajeDolares)
            print (ListaDolares)
        else:
            print (mensajeErrorMoneda)
    elif (opcion ==2):
        print(mensajeOpcion.format (2))
        print (listaClasificación)
    elif (opcion == 3):
        print(mensajeOpcion.format(3))
        print ("El máximo ingreso fue", superior)
        print ("El ingreso minimo fue", menor)
        print ("El promedio de ingreso fue", promedioDolares)
    else:
        print (mensajeErrorNumero)

#--Entrada variable opción--#
opcion = int (input(PreguntaMenú))

#--Salida--#
print (mensajeSalida)