import math
from tokenize import Double

while True:
    # Mostramos el menú
    print("""
    ========== MENÚ DE CONVERSIONES ==========
    1. Grados Celsius a Fahrenheit
    2. Grados Celsius a Kelvin
    3. Grados celsius a Rankine
    4. Grados Fahrenheit a Grados celsius
    5. Grados Fahrenheit a Kelvin
    6. Grados Fahrenheit a Rankine
    7. Kelvin a Grados celsius
    8. Kelvin a Grados fahrenheit
    
    0. SALIR
    ========================================
    """)

    opcion = input("Elige la conversion que deseas ejecutar (0-8): ")
    print("\n")

    if opcion == '1':
        print("--- Ejercicio 1: Grados Celsius a Fahrenheit ---")
        n = float(input("Introduce un número en grados celsius: "))
        r=n*1.8+32

        print("la conversion de °F a celsius es:" + str(r))

    if opcion == '2':
        print("--- Ejercicio 2: Grados Celsius a Kelvin ---")
        n = float(input("Introduce un número en Kelvin: "))
        r = n +273.15\

    if opcion == '3':
        print("--- Ejercicio 3: celsius a Rankine ---")
        n = float(input("Introduce un número en grados Celsius: "))
        r = (n+273.15)*1.8

    if opcion == '4':
        print("--- Ejercicio 4: Grados Fahrenheit a Grados celsius ---")
        n = float(input("Introduce un número en grados Fahrenheit: "))
        r = (n-32)/1.8

    if opcion == '5':
        print("--- Ejercicio 5: Grados Fahrenheit a Kelvin ---")
        n = float(input("Introduce un número en grados Fahrenheit: "))
        r = (n+459.67)/1.8

    if opcion == '6':
        print("--- Ejercicio 6: Grados Fahrenheit a Rankine ---")
        n = float(input("Introduce un número en grados Fahrenheit: "))
        r = n+459.67

    if opcion == '7':
        print("--- Ejercicio 6: Kelvin a Grados celsius ---")
        n = float(input("Introduce un número en Kelvin: "))
        r = n-273.15

    if opcion == '8':
        print("--- Ejercicio 6: Kelvin a Grados fahrenheit ---")
        n = float(input("Introduce un número en Kelvin: "))
        r = (n*9/5)-459.67

