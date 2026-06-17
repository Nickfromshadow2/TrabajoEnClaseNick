# Calcular ecuacion cuadratica
import os
os.system('cls' if os.name == 'nt' else 'clear')

def cuadratica(a,b,c):
    desc=b**2-4*a*c
    print("Solucion de ecuacion cuadratica")
    if a==0:
        print("no es una ecuacion lineal.")

    if desc>0:
        x1=(-b+desc**0.5)/(2*a)
        x2=(-b-desc**0.5)/(2*a)
        print(f"x1= {x1}")
        print(f"x2= {x2}")

        if desc<0:
            parteReal=-b/(2*a)
            parteCompleta=abs(desc)**0.5/(2*a)
            print(f"x= {parteReal} + {parteCompleta})i")
            print(f"x {parteReal} - {parteCompleta})i")

cuadratica(0,1,-4)



