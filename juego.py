import sys
import random

turno = str(sys.argv[1])
opciones = ["piedra", "papel", "tijera"]
aleatorio = random.randint(0,2)
computador = opciones[aleatorio]


if turno == "tijera" and computador == "papel":
    print("Computador juega papel")
    print("ganaste")
elif turno == "tijera" and computador == "piedra":
    print("computador juega piedra")
    print("perdiste")

if turno == "papel" and computador == "piedra":
    print("computador juega piedra")
    print("ganaste")
elif turno == "papel" and computador == "tijera":
    print("computador juega tijera")
    print("perdiste")

if turno == "piedra" and computador == "tijera":
    print("computador juega tijera")
    print("ganaste")
elif turno == "piedra" and computador == "papel":
    print("computador juega papel")
    print("perdiste")

if turno != "tijera" or turno != "papel" or turno != "piedra":
    print("Argumento inválido: Debe ser piedra, papel o tijera.")

if turno == computador:
    print("empate")