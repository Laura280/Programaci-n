class TortaRedonda:
    def __init__ (self, saborIngresado):
        #Definiendo atibutos
        self.forma = "Redonda"
        self.sabor = saborIngresado
        #Acción al crear objeto
        print ("Soy una torta nueva")
    def motrar_atributos (self):
        print (f"soy de forma {self.forma} y de sabor {self.sabor}")


#Creó la torta
tortaChocolate = TortaRedonda("Chocolate")
tortaVainilla = TortaRedonda("Vainila")

#Se muestran atributos
print (tortaChocolate.sabor)
print (tortaVainilla.sabor)
print (tortaChocolate.forma)
print (tortaVainilla.forma)

