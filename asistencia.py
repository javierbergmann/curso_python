print("GESTION DE ASISTENCIAS")
print("Ingrese cantidad de alumnos: ", end="")
cantAlumnos= int(input())
alumnos=[]
for i in range(cantAlumnos):
    print("Alumno " + str(i))
    print("Apellido: ", end="")
    apellido= input()
    print("Nombres: ", end="")
    nombres= input()
    print("Edad: ", end="")
    edad= input()
    asistencias=0
    newAlumn=[apellido, nombres, edad, asistencias]
    alumnos.append(newAlumn)
print("\n")
print("<<<<<<<<<<========== **Listado de Alumnos** ==========>>>>>>>>>>")
for al in alumnos:
    print(al)
