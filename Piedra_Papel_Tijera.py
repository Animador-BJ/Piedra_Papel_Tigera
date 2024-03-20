import random

puntos_jugador = 0
puntos_computadora = 0

# imput
while True:
    print("--------------------------------")
    print("----Piedra, Papel o Tijeras----")
    print("--------------------------------")
    print("Escoja su opción:")
    print("  Piedra")
    print("  Papel")
    print("  Tijeras")
    print("--------------------------------")

    opciones = ["Piedra", "Papel", "Tijeras"]
    computadora = random.choice(opciones)
    jugador = input("Elija Piedra, Papel o Tijeras: ")

    print(f"------------------------------------")
    print(f"  La computadora eligió: {computadora}")

    # processing
    if jugador == "Piedra" or jugador == "Papel" or jugador == "Tijeras":
        print(f"Usted eligió: {jugador}")
    if jugador == computadora:
        print("¡Es un empate!")
    elif jugador == "Piedra" and computadora == "Tijeras":
        print("¡Ganaste!")
        puntos_jugador += 1
    elif jugador == "Papel" and computadora == "Piedra":
        print("¡Ganaste!")
        puntos_jugador += 1
    elif jugador == "Tijeras" and computadora == "Papel":
        print("¡Ganaste!")
        puntos_jugador += 1
    else:
        print("¡La computadora gana!")
        puntos_computadora += 1

    # output
    print(f"  - Tus puntos: {puntos_jugador}")
    print(f"  - Puntos de la computadora: {puntos_computadora}")

    continuar = input("-----------------------------------\n¿Desea continuar el juego? (si/no): ").lower()
    if continuar != "si":
        break
