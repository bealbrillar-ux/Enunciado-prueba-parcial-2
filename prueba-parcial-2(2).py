import os
os.system("cls")
import random

num2 = 0
primerintento = 0
segundointento = 0

num1 =int(input("Ingrese límite inferior: \n"))

while num2 <= num1:
    num2 =int(input("Ingrese límite superior: \n"))

num_random = random.randint(num1,num2)
modulo_random = num_random % 2

if modulo_random == 0:
    numero_final = num_random
else:
    if num_random == 0 and num_random in range(num1,num2):
        numero_final = num_random
    elif num_random == 1 and num_random in range(num1,num2):
        numero_final = num_random
    elif num_random == 2 and num_random in range(num1,num2):
        numero_final = num_random
    elif (num_random + 1) in range(num1,num2):
        numero_final = num_random + 1
    else:
        numero_final = num_random - 1

for i in range(3):
    num_x = 0
    num_x = int(input("ingrese numero a ADIVINAR: \n"))
    if num_x == numero_final:
        print("Felicitaciones, pudiste adivinar.")
        print(f"Numero de intentos: {i+1}")
        break
    else:
        if i == 0:
            if num_x > numero_final:
                print("El numero es menor\n")
                primerintento += num_x
            else:
                print("El numero es mayor\n")
                primerintento += num_x
        elif i == 1:
            if num_x > numero_final:
                segundointento += num_x
                print("El numero es menor\n")
                resta1 = numero_final - primerintento
                resta1 *= -1
                resta2 = numero_final - segundointento
                resta2 *= -1
                if resta1 < resta2:
                    print(f"El numero que buscas esta mas cerca de {primerintento} que de {segundointento}\n")
                else:
                    print(f"El numero que buscas esta mas cerca de {segundointento} que de {primerintento}\n")
            else:
                segundointento += num_x
                print("numero random es mayor\n")
                resta1 = num_random - primerintento
                resta1 *= -1
                resta2 = num_random - segundointento
                resta2 *= -1
                if resta1 < resta2:
                    print(f"El numero que buscas esta mas cerca de {primerintento} que de {segundointento}\n")
                else:
                    print(f"El numero que buscas esta mas cerca de {segundointento} que de {primerintento}\n")
        else:
            print("perdiste")
            print(f"El numero era: {numero_final}")