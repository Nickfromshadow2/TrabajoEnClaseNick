def delta(self):
    return self.b**2-4*self.a*self.c

def raices(self):

 if self.a==0 and self.b>0:
     print("es una ecuacion lineal")
     print(f"x={self.c/self.b}")

 if self.c==0 and self.a>0:
     print("es una ecuacion lineal")
     print(f"c={self.b/self.a}")

 if self.a!=0 and self.c!=0:
    if self.delta()>0:
     x1 = (-self.b + self.delta() ** 0.5) / (2 * self.a)
     x2 = (-self.b - self.delta() ** 0.5) / (2 * self.a)
     print(f"x1= {x1}")
     print(f"x2= {x2}")
    else:
        parteReal=-self.b/(2*self.a)
        parteCompleja=abs(self.delta())**0.5/(2*self.a)
        print(f"x1={parteReal} + {parteCompleja}i")
        print(f"x2={parteReal} - {parteCompleja}i")


     
