#4. Escribir un programa que pida al usuario un número entero y muestre 
#por pantalla si es un número primo o no.#


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Solicitar al usuario un número entero
numero = int(input("Ingrese un número entero: "))

# Verificar si el número es primo o no
if es_primo(numero):
    print(numero, "es un número primo")
else:
    print(numero, "no es un número primo")