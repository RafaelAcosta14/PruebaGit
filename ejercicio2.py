import math

OPCION_SUMAR = 1
OPCION_RESTAR = 2
OPCION_MULTIPLICAR = 3
OPCION_DIVIDIR = 4
OPCION_VER_HISTORIAL = 5
OPCION_SALIR = 6

MENSAJE_BIENVENIDA = "!Hola a la calculadora interactiva de python¡"
DIVISOR_LINEA = "--------------------------------------"
VALOR_INFINITO = math.inf

historial_operaciones = []
ejecutando_calculadora =True

def mostrar_menu():
    """Muestra las opciones disponibles de la calculadora."""
    print(DIVISOR_LINEA)
    print("Seleccione una operacion")
    print(f"{OPCION_SUMAR}.Sumar")
    print(f"{OPCION_RESTAR}.Restar")
    print(f"{OPCION_MULTIPLICAR}.Multiplicar")
    print(f"{OPCION_DIVIDIR}.Dividir")
    print(f"{OPCION_VER_HISTORIAL}.Ver historial")
    print(f"{OPCION_SALIR}.Salir")
    print(DIVISOR_LINEA)

    def obtener_numero_valido(mensaje):
        """Pedir al usuario un numero"""

        while True:
            Entrada = input(mensaje)
            try:
                numero = float(Entrada)
                return numero
            except ValueError:
                print("Entrada invalida")

    def sumar(num1, num2):
        resultado = num1 + num2
        return resultado
    
    def restar(num1, num2):
        resultado = num1 - num2
        return resultado
    
    def multiplicar(num1, num2):
        resultado = num1 * num2
        return resultado
    
    def dividir(num1, num2):
        if num2 == 0:
            return VALOR_INFINITO
        else:
            resultado = num1 / num2
            return resultado
        
    def agregar_a_historial(operacion_str):
        """Agregar la operacion al historial"""
        historial_operaciones.append(operacion_str)

    def mostrar_historial():
        print(DIVISOR_LINEA)
        if not historial_operaciones:
            print("Historial-vacio")
        else:
            print("Historial-de-operaciones")
            for i, operacion in enumerate(historial_operaciones):
                print(f"{i + 1}. {operacion}")
            print(DIVISOR_LINEA)

    print(MENSAJE_BIENVENIDA)

    while ejecutando_calculadora:
        mostrar_menu()

        opcion = obtener_numero_valido("Ingrese el numero de su opcion: ")

        if opcion == OPCION_SUMAR:
            num1 = obtener_numero_valido("Ingrese el primer numero: ")
            num2 = obtener_numero_valido("Ingrese el segundo numero: ")
            res = sumar(num1, num2)
            print(f"El resultado es: {res}")
            agregar_a_historial(f"{num1} + {num2} = {res}")

        elif opcion == OPCION_RESTAR:
            num1 = obtener_numero_valido("Ingrese el primer numero: ")
            num2 = obtener_numero_valido("Ingrese el segundo numero: ")
            res = restar(num1, num2)
            print(f"El resultado es: {res}")
            agregar_a_historial(f"{num1} - {num2} = {res}")

        elif opcion == OPCION_MULTIPLICAR:
            num1 = obtener_numero_valido("Ingrese el primer numero: ")
            num2 = obtener_numero_valido("Ingrese el segundo numero: ")
            res = multiplicar(num1, num2)
            print(f"El resultado es: {res}")
            agregar_a_historial(f"{num1} * {num2} = {res}")

        elif opcion == OPCION_DIVIDIR:
            num1 = obtener_numero_valido("Ingrese el primer numero: ")
            num2 = obtener_numero_valido("Ingrese el segundo numero: ")
            res = dividir(num1, num2)
            if res == VALOR_INFINITO:
                print("ERROR")
            else:
             print(f"El resultado es: {res}")
             agregar_a_historial(f"{num1} / {num2} = {res}")
        
        elif opcion == OPCION_VER_HISTORIAL:
         mostrar_historial()

        elif opcion == OPCION_SALIR:
            ejecutando_calculadora = False
            print("Gracias por usar la calculadora ¡Adios!")

        else:
            print("OPCION INVALIDA. INTENTE DE NUEVO")

        print("\n")



    
