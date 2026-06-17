import pandas as pd
from array import array

# arreglo

edades = array("i",[18,19,20,18])

# lista
estudiantes=["daniel","nick","angel","ever"]

# Diccionario

notas={
    "Carlos":85,
    "Ana":92,
    "Luis":78,
    "Maria":90
}
print("Lista de estudiantes")
print(estudiantes)

print("\n Diccionario de notas")
print(notas)

print("\n arreglo de edades")
print(edades)

print("\nrecorrido de datos")
for i in range(len(estudiantes)):
    nombre = estudiantes[i]
    nota=notas[nombre]
    edad=edades[i]
    print(f"Estudiante: {nombre} | Edad: {edad} |Nota: {nota}")


    print("Agregando un nuevo estudiante")

    estudiantes.apped("ale")
    nota["ale"]=88
    edades.append(21)

    for i in range(len(estudiantes)):
        nombre=estudiantes[i]
        nota=notas[nombre]
        edad=edades[i]

        print(f"Estudiante: {nombre} | Edad: {edad} |Nota: {nota}")

        panda_df = pd.DataFrame({"nota":notas.values()})

        print("\dataframe solo con notas")
        print(panda_df)