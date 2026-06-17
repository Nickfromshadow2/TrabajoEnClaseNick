while True:
    print("""
    ========== MENÚ GENERAL ==========

    --- EJERCICIOS HECHOS EN CLASE ---
    1. Tipos de dato (Saludo)
    2. Ecuación lineal
    3. Variable booleana
    4. Promedio de 4 notas (Versión simple)
    5. Arreglo de 4 calificaciones
    6. Ejemplos de Ciclo For

    --- EJERCICIOS EXTRA ---
    7. Suma de enteros hasta 'n'
    8. Contar letras de un nombre
    9. Convertir vocal a mayúscula
    10. Verificar contraseña
    11. División de dos números
    12. Grupos A y B por nombre y sexo
    13. Invertir una frase
    14. lista de la compra
    15. Calcular paga por horas
    16. Contar años cumplidos

    0. SALIR DEL PROGRAMA
    """)

    opcion = input("Elige el número del ejercicio que deseas ejecutar del 1 al 16 y presione 0 para salir: ")
    print("\n")

    # SECCIÓN: HECHOS EN CLASE

    if opcion == '1':
        print("--- 1. Tipos de dato ---")
        nombre = input("Digita tu nombre: ")
        print("Hola " + nombre)

    if opcion == '2':
        print("--- 2. Ecuación lineal ---")
        print("ecuacion lineal:  ax+b")
        a = int(input("a: "))
        if a == 0:
            print("no es una ecucacion lineal")
        else:
            b = int(input("b: "))
            x = -b / a
            print("x: " + str(x))
            print("x es de tipo: " + str(type(x)))

    if opcion == '3':
        print("--- 3. Variable booleana ---")

        z = True
        if z:
            print("z: Verdadero ")
            print("z es del tipo: " + str(type(z)))
        else:
            print("z:  Falso " + str(z))
            print("z es del tipo: " + str(type(z)))

    if opcion == '4':
        print("--- 4. Calcular el promedio de 4 notas ---")
        nota1 = int(input("Ingrese la nota 1: "))
        nota2 = int(input("Ingrese la nota 2: "))
        nota3 = int(input("Ingrese la nota 3: "))
        nota4 = int(input("Ingrese la nota 4: "))
        if nota1 <= 0 or nota2 <= 0 or nota3 <= 0 or nota4 <= 0:
            print("No se puede sacar el promedio porque hay una nota inválida")
        else:
            r = (nota1 + nota2 + nota3 + nota4) / 4
            print("El promedio es: " + str(r))

    if opcion == '5':
        print("--- 5. Crear un arreglo de 4 calificaciones ---")
        notas = [0, 0, 0, 0]
        suma = 0
        promedio = 0
        resultado = True
        for i in range(4):
            notas[i] = int(input("Digite la nota " + str(i + 1) + ": "))
            if notas[i] <= 0:
                print("Nota no válida.")
                resultado = False
                break

            suma += notas[i]

        if resultado:
            promedio = suma / 4
            print("El promedio es: " + str(promedio))

    if opcion == '6':
        print("--- 6. Ciclo For (Ejemplos) ---")
        print("0 a 4 (range 5)")
        for i in range(5):
            print(i)
        print("\ndel 1 al 9 de 2 en 2")

        for i in range(1, 10, 2):
            print(i)
        print("\ndeletrear palabra")
        cadena = "Python"

        for letra in cadena:
            print(letra)
        print("\nindice de cada letra")

        for index, letra in enumerate(cadena):
            print(f"indice: {index} letra: {letra}")
        print("\nvalores dentro de un arreglo")
        arreglo = [10, 20, 30, 40, 50]

        for numero in arreglo:
            print(numero)
        print("\nArreglo de frutas")
        arregloFrutas = ["manzana", "banana", "pera"]

        for item in arregloFrutas:
            print(item)
        print("\nCambiando valor en índice 0:")
        arreglo[0] = 100
        print(arreglo)

    # SECCIÓN: LOS 10 EJERCICIOS EXTRA

    if opcion == '7':
        print("--- 7. Suma de enteros hasta 'n' ---")
        n = int(input("Introduce un número entero: "))
        suma_extra = n * (n + 1) / 2
        print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma_extra))

    if opcion == '8':
        print("--- 8. Letras del nombre ---")
        nombre_extra = input("¿Cómo te llamas? ")

        # el extra.upper de aca, es para que se vuelva mayuscula el nombre
        print(nombre_extra.upper() + " tiene " + str(len(nombre_extra)) + " letras")

    if opcion == '9':
        print("--- 9. Vocal a mayúscula ---")
        frase = input("Introduce una frase: ")
        vocal = input("Introduce una vocal en minúscula: ")

        # lo mismo aca el vocal.upper es para hacer una vocal mayuscula
        print(frase.replace(vocal, vocal.upper()))

    if opcion == '10':
        print("--- 10. Contraseña ---")
        key = "contraseña"
        password = input("Introduce la contraseña: ")

        # el password.lower es lo mismo solo que lo transforma a minuscula para evitar problemas
        if key == password.lower():
            print("La contraseña coincide")
        else:
            print("La contraseña no coincide")

    if opcion == '11':
        print("--- 11. División ---")
        ndiv = float(input("Introduce el dividendo: "))
        mdiv = float(input("Introduce el divisor: "))
        if mdiv == 0:
            print("¡Error! No se puede dividir por 0.")
        else:
            print("El resultado es:", ndiv / mdiv)

    if opcion == '12':
        print("--- 12. Grupos A y B ---")
        name = input("¿Cómo te llamas? ")
        gender = input("¿Cuál es tu sexo (M o H)? ")
        if gender.upper() == "M":
            if name.lower() < "m":
                group = "A"
            else:
                group = "B"
        else:
            if name.lower() > "n":
                group = "A"
            else:
                group = "B"
        print("Tu grupo es " + group)

    if opcion == '13':
        print("--- 13. Frase invertida ---")
        frase_inv = input("Introduce una frase: ")
        print(frase_inv[::-1])

    if opcion == '14':
        print("--- 14. lista de la compra ---")
        lista = input('Introduce los productos separados por comas: ')
        print(lista.replace(',', '\n'))

    if opcion == '15':
        print("--- 15. Paga por horas ---")
        horas = float(input("Introduce tus horas de trabajo: "))
        coste = float(input("Introduce lo que cobras por hora: "))
        paga = horas * coste
        print("Tu paga es", paga)

    if opcion == '16':
        print("--- 16. Años cumplidos ---")
        age = int(input("¿Cuántos años tienes? "))
        for i in range(age):
            print("Has cumplido " + str(i + 1) + " años")

    if opcion == '0':
        print("finalizando programa.")
        break