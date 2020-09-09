#ENTRADAS
Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

#preguntas
preguntaMenu = """
Por favor ingrese alguna de las opciones : 
            1- Convertir temperturas
            2- Estado de salud de cada una de las emperaturas
            3- Ver máximo y minimo de temperaturas
            4- Para salir del programa 
"""
preguntaConversionTemperatura = """
Por favor ingrese alguna de las opciones : 
            F- Convertir temperturas fahrenheit
            K- Convertir temperaturas Kelvin
            C- Convertir temperaturas Celcius
:"""

#----Mensajes Error----#
mensajeEntradaNoValidaN = "recuerde ingresar una opción válida 1,2,3,4"
mensajeEntradaNoValidaT = "recuerde ingresar una opcion válida F,K,C"
#----mensaje Informativo----#
mensajeOpcion =  "usted escogió la opción {}"
mensajeSalida = "Gracias por usar el programa"
mensajeCelcius = "No es necesaria la conversión, pero se muestra la lista"


#Inicio Código
opcion = int (input(preguntaMenu))
#calculos preliminares
listaGradosK = []
listaGradosF = []
listaGradosC = Temperatura_Corporal
listaEstadosSalud = []
#----Pasando a Kelvin xC + 273.15----#
for elemento in listaGradosC:
    kelvin = elemento + 273.15
    listaGradosK.append(kelvin)

#----Pasando a Fahrenheit (xC* 1.8) + 32----#
for elemento in listaGradosC:
    Fahrenheit = (elemento*1.8) + 32
    listaGradosF.append(Fahrenheit)

#----Dectetando los estados de salud----#
for elemento in listaGradosC:
    estado = ""
    if (elemento < 36 ):
        estado = "Hipotermia"
    elif (elemento >= 36 and elemento <37.6):
        estado = "Normal"
    else:
        estado = "Fiebre"
    listaEstadosSalud.append(estado)
#---Calcular maximo & minimo---#
mayor = max (listaGradosC)
menor = min (listaGradosC)
frecuencia = round(len (listaGradosC)/24,2)



#Menu
while(opcion != 4) :
    if (opcion ==1):
        print(mensajeOpcion.format(1))
        #Pregunta
        conversion = input(preguntaConversionTemperatura)
        if (conversion == "K"):
            print(listaGradosK)
        elif (conversion == "F") :
            print(listaGradosF)
        elif (conversion == "C") :
            print (mensajeCelcius)
            print(listaGradosC)
        else :
                print (mensajeEntradaNoValidaT)


    elif (opcion == 2):
        print(mensajeOpcion.format(2))
        print(listaEstadosSalud)
    elif (opcion ==3):
        print(mensajeOpcion.format(3))
        print("la temperatura máxima fue", mayor)
        print("la temperatura minima fue", menor)
        print ("la temperatura fue tomada con una frecuencia de", frecuencia)
    else:
        print (mensajeEntradaNoValidaN)



    #Entrada de la variable opcion
    opcion = int (input(preguntaMenu))


#Salida del programa 
print (mensajeSalida)
