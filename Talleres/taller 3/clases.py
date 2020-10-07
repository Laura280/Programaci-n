#Clase paciente
class Paciente:
    def __init__ (self, idIng, sexoIng, nombreIng, afiliadoIng):
        self.id = idIng
        self.sexo = sexoIng
        self.nombre = nombreIng
        self.afiliado = afiliadoIng
    def atributos(self):
        print (f"Hola, soy la paciente {self.nombre} de sexo {self.sexo} con número de identificación {self.id} y afiliado a la eps {self.afiliado}")
    def sintomas (self, lista):
        for elemento in lista:
            print (elemento)

Paciente1 = Paciente (2345627476, "femenino", "Susana", "Confama")
listaSintomaas = ["Dolor de espalda", "Dolor de cabeza", "Dificultad para dormir", "Ansiedad"]
Paciente1.atributos()
Paciente1.sintomas(listaSintomaas)

#Clase estable
class Estable (Paciente):
    def __init__ (self, idIng, sexoIng, nombreIng, afiliadoIng, tiempoesperaIng, temperaturaIng, animoIng):
        Paciente.__init__(self, idIng, sexoIng, nombreIng, afiliadoIng)
        self.tiempodeespera = tiempoesperaIng
        self.temperatura = temperaturaIng
        self.animo = animoIng
    def atributos (self):
        print(f"Hola soy la paciente {self.nombre}, de sexo {self.sexo} con número de identificación {self.id} y afiliado a la eps {self.afiliado}, llevo un tiempo de espera de {self.tiempodeespera} minutos, mi temperatura es de {self.temperatura} °C y mi estado de ánimo es {self.animo}")
    def recomendaciones (self, lista):
        for elemento in lista:
            print(f"las recomendaciones a seguir son : {elemento}")
            print("Cumpliré las indicacines")

Paciente2 = Estable (5634864948, "femenino", "Mariana", "Salucop", 15, 36, "tranquilo")
listaRecomendaciones = ["tomar medicamento", "Tener buenas posiciones", "no estresarse", "Volver en un mes"]
Paciente2.atributos()
Paciente2.recomendaciones(listaRecomendaciones)

#Clase Crítico
class Critico (Paciente):
    def __init__ (self, idIng, sexoIng, nombreIng, afiliadoIng, habitacioninternadoIng, patologiaIng):
        Paciente.__init__(self, idIng, sexoIng, nombreIng, afiliadoIng)
        self.habitacióninternado = habitacioninternadoIng
        self.patologia = patologiaIng
    def atributos (self):
        print(f"Hola soy el paciente {self.nombre} de sexo {self.sexo} con número de identificación {self.id}, afiliado a la eps {self.afiliado}, me encuentro internado en la habitación {self.habitacióninternado}, y tengo {self.patologia}")
    def sintomas (self, lista):
        for elemento in lista:
            print (elemento)

Paciente3 = Critico (6576738746, "masculino", "Juan", "ConfaChocó", 107, "cáncer")
listaSintomas = ["No puede respirar sin ayuda de una máquina", "plaquetas muy bajitas"]
Paciente3.atributos()
Paciente3.sintomas(listaSintomas)