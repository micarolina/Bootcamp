#6. Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo#

palabra = input("Ingrese una palabra: ")
reverso = palabra[::-1]  # Invertir la palabra

if palabra == reverso:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
