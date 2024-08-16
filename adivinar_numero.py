import random

maximo = input("Type Max number: ")

if maximo.isdigit():
    maximo = int(maximo)

    if maximo <= 0:
        print('El numero debe ser mayor a 0.')
        quit()
else:
    print('Ingrese un numero entero.')
    quit()

random_number = random.randint(0, maximo)
intento = 0


while True:#mala practica, hehco para probar el break y el continue
    intento += 1
    user_guess = input("Adivina: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Ingrese un numero entero.')
        continue

    if user_guess == random_number:
        print("Correcto!")
        break
    elif user_guess > random_number:
        print("Te pasaste!")
    else:
        print("Te quedaste corto!")

print("You got it in", intento, "guesses")