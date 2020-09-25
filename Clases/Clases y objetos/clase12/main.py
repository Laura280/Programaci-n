import persona as p
import estudiante as es
import egresado as eg
laura = p.Persona("Laura", 18, 10097865)
mario = p.Persona("Mario", 20, 23675489)
valeria = es.Estudiante("Valeria", 18, 21345432, "Biomedica", 3)
laura.hablar("Todo anda muy bien, me gusta aprender")
mario.comer("taco")
valeria.estudiar("cálculo")
melany = eg.Egresado("Melany",21,33568799,"Biomedica", "2023/12/12")
print (melany.semestre)
melany.trabajar ("MIT")