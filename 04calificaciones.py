# crear un arreglo de 4 calificaciones

notas = [0,0,0,0]
suma = 0
promedio=0
resultado=True

for i in range(4):
    notas[i]=int(input("Digite la nota ")+str(i+1)+": ")

    if notas[i]<=0:
        print("Nota no valida.")
        resultado=False
        break

        suma+=notas[i]

if resultado:
    promedio=suma/4
    print("El promedio es: "+str(promedio))