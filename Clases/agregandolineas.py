import funciones_archivos as helper
namefile = "libro.txt"
helper.agregarLinea ("opinion.txt", "Nueva linea")
renglonesLibro = helper.leerArchivos(namefile) 
print (len(renglonesLibro))

if (len(renglonesLibro) == 0):
    print("Es la primera linea que se escribirá en el libro")
    helper.agregarLinea(namefile, "El día para programar es hoy")
else :
    linea = input ("ingrese la línea que desea agregar : \n")
    helper.agregarLinea (namefile, linea)







