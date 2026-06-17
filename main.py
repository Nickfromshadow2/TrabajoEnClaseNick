from clases import cuadratica
from clases import *
import numpy as np

import os
os.system("cls" if os.name=="nt" else "clear")
z=cuadratica(1,0,1)
z.raices()

#ecuacion cuadratica
respuesta=np.roots([1,0,1])
print(respuesta)

print(f"x1: {np.round(respuesta[0],3)}")

#ecuacion cuadratica
respuesta=np.roots([1,1,1,0,1])
print(respuesta)

print(f"x1: {np.round(respuesta[0],3)}    x2:{np.round(respuesta[1],20)}    x3:{np.round(respuesta[2],20)}")
