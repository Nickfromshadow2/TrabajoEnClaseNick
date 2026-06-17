while True:
    # Mostramos el menú
    print("""
    ========== MENÚ DE EJERCICIOS ==========
    1. Suma de enteros hasta 'n'
    2. Contar letras de un nombre
    3. Convertir vocal a mayúscula
    4. Verificar contraseña
    5. División de dos números
    6. Grupos A y B por nombre y sexo
    7. Invertir una frase
    8. Cesta de la compra
    9. Calcular paga por horas
    10. Contar años cumplidos
    0. SALIR
    ========================================
    """)

    opcion = input("Elige el número del ejercicio que deseas ejecutar (0-10): ")
    print("\n")

    # Usamos solo 'if' independientes para cada opción
    if opcion == '1':
        print("--- Ejercicio 1: Suma de enteros ---")
        n = int(input("Introduce un número entero: "))
        suma = n * (n + 1) / 2
        print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))

    if opcion == '2':
        print("--- Ejercicio 2: Letras del nombre ---")
        nombre = input("¿Cómo te llamas? ")
        print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")

    if opcion == '3':
        print("--- Ejercicio 3: Vocal a mayúscula ---")
        frase = input("Introduce una frase: ")
        vocal = input("Introduce una vocal en minúscula: ")
        print(frase.replace(vocal, vocal.upper()))

    if opcion == '4':
        print("--- Ejercicio 4: Contraseña ---")
        key = "contraseña"
        password = input("Introduce la contraseña: ")
        if key == password.lower():
            print("La contraseña coincide")
        else:
            print("La contraseña no coincide")

    if opcion == '5':
        print("--- Ejercicio 5: División ---")
        try:
            n = float(input("Introduce el dividendo: "))
            m = float(input("Introduce el divisor: "))
            if m == 0:
                print("¡Error! No se puede dividir por 0.")
            else:
                print("El resultado es:", n / m)
        except ValueError:
            print("¡Error! Debes introducir números, no letras.")

    if opcion == '6':
        print("--- Ejercicio 6: Grupos A y B ---")
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

    if opcion == '7':
        print("--- Ejercicio 7: Frase invertida ---")
        frase = input("Introduce una frase: ")
        print(frase[::-1])

    if opcion == '8':
        print("--- Ejercicio 8: Cesta de la compra ---")
        cesta = input('Introduce los productos separados por comas: ')
        print(cesta.replace(',', '\n'))

    if opcion == '9':
        print("--- Ejercicio 9: Paga por horas ---")
        horas = float(input("Introduce tus horas de trabajo: "))
        coste = float(input("Introduce lo que cobras por hora: "))
        paga = horas * coste
        print("Tu paga es", paga)

    if opcion == '10':
        print("--- Ejercicio 10: Años cumplidos ---")
        age = int(input("¿Cuántos años tienes? "))
        for i in range(age):
            print("Has cumplido " + str(i + 1) + " años")

    if opcion == '0':
        print("¡Gracias por usar el programa! Hasta luego.")
        break