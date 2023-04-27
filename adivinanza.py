#Version 1.0
#Author: Armando Zuñiga.

import random

randon_num = random.randint(1,50)
intentos = 0

while True:
    intentos +=1
    numero = int(input("Ingresa un número para adivinar del 1 al 50: \n"))
    if randon_num == numero:
        print(f"Adivinaste el número!!!!\n Te tomó {intentos} lograrlo.")
        break
    elif numero > randon_num:
        print("El número es más pequeño.\n")
    else:
        print("El número es más grande.\n")
