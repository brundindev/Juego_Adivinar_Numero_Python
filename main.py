# @brundindev - 2025/01/16
import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinanza de numero!")
    print("Hecho por: @brundindev")
    print("Debes adivinar un número del 1 al 100")
    print("¡Intenta adivinarlo!")

    while not adivinado:
        adivinanza = input("Introduzca un número del 1 al 100: ")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(
                    "Felicidades has ganado! El número válido entre el 1 al 100"
                )
        else:
            print("Por favor, introduzca un número válido entre el 1 al 100")

juego_adivinanza()