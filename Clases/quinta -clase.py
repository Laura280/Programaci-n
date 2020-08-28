#-----preguntas----#
preguntaNumero = "por favor ingrese un número del 1 al 10 : "
#-------Mensaje----#
mensajefallido = "Fallaste!!, no es número secreto"
mensajeExitoso = "felicitaciones has acertado el número en el que pensé"
mensajeDespedida = "gracias por jugar"
mensajeVida = "ten cuidado has perdido {} vida, te quedan {}"

#Ciclos while

numeroSecreto = 6
numeroIngresado = int(input(preguntaNumero))
vidasPerdidas = 0
while(numeroSecreto != numeroIngresado and vidasPerdidas<=2) :
    vidasPerdidas = vidasPerdidas +1
    print(mensajeVida.format(vidasPerdidas,3-vidasPerdidas))
    print (mensajefallido)
    if vidasPerdidas <3 :
        numeroIngresado = int(input(preguntaNumero)) 

if vidasPerdidas<3:
    print(mensajeExitoso)
else:
    print(mensajefallido)
print (mensajeDespedida)


#-----juegovocal----#
preguntaVocal ="Por favor ingrese una vocal en minúscula : "
mensajeExitoso = "felicidades, acertaste la vocal"
mensajeFallido = "lo siento, fallaste. Sigue intentando"
mensajeDespedida = "Chao, gracias por jugar"

vocalSecreta = "o"
vocalIngresada =input(preguntaVocal)
while(vocalSecreta != vocalIngresada) :
    print(mensajeFallido)
    vocalIngresada =input(preguntaVocal)
print(mensajeExitoso)
print(mensajeDespedida)




