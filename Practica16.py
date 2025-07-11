import random

# ---------------------------
# CONSTANTES
# ---------------------------
NUMERO_MINIMO = 1
NUMERO_MAXIMO = 100
INTENTOS_MAXIMOS = 7

# ---------------------------
# FUNCIONES
# ---------------------------

def generar_numero_secreto():
    return random.randint(NUMERO_MINIMO, NUMERO_MAXIMO)

def solicitar_adivinanza():
    while True:
        try:
            adivinanza = int(input(f"Adivina el número ({NUMERO_MINIMO}-{NUMERO_MAXIMO}): "))
            if NUMERO_MINIMO <= adivinanza <= NUMERO_MAXIMO:
                return adivinanza
            else:
                print(f"⚠️ Por favor ingresa un número entre {NUMERO_MINIMO} y {NUMERO_MAXIMO}.")
        except ValueError:
            print("❌ Entrada inválida. Debes escribir un número entero.")

def dar_pista(adivinanza, secreto):
    if adivinanza < secreto:
        print("🔻 Demasiado bajo.")
    elif adivinanza > secreto:
        print("🔺 Demasiado alto.")

def jugar():
    print("🎯 ¡Bienvenido al Juego de Adivinanza!")
    print(f"Adivina el número secreto entre {NUMERO_MINIMO} y {NUMERO_MAXIMO}. Tienes {INTENTOS_MAXIMOS} intentos.")

    secreto = generar_numero_secreto()
    adivinado = False
    intentos = 0

    while intentos < INTENTOS_MAXIMOS and not adivinado:
        print(f"\n🔄 Intento {intentos + 1} de {INTENTOS_MAXIMOS}")
        intento = solicitar_adivinanza()
        intentos += 1

        if intento == secreto:
            adivinado = True
        else:
            dar_pista(intento, secreto)

    # Resultado final
    if adivinado:
        print(f"\n🎉 ¡Felicidades! Adivinaste el número {secreto} en {intentos} intentos.")
    else:
        print(f"\n💀 Has perdido. El número secreto era: {secreto}")

# ---------------------------
# EJECUTAR JUEGO
# ---------------------------

if __name__ == "__main__":
    jugar()
