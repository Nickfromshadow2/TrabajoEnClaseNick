# calcular el promedio de 4 notas

nota1=int(input("ingrese la nota 1: "))
nota2=int(input("ingrese la nota 2: "))
nota3=int(input("ingrese la nota 3: "))
nota4=int(input("ingrese la nota 4: "))

if nota1 <=0 or nota2<=0 or nota3<=0 or nota4<=0:
    print("no se puede sacar el promedio porque hay una nota invalida")
else:
    r=(nota1+nota2+nota3+nota4)/4
    print("el promedio es: "+ (str(r)))
