#3. Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas
#ejemplo, al colocar numero 5, el resultado esperado es una lista

# Pedir numero positivo al usuario
numero = int(input('Ingresa un numero entero positivo\n'))

# cuenta regresiva desde el numero hasta 0
lista = ''
lista_real = []
while numero >= 1:
    # print(numero)
    lista += str(numero) + ', '
    lista_real.append(numero)
    numero -= 1
lista += str(numero)
lista_real.append(0)
# mostrar en pantalla separado por comas
print(lista)
print(f"Esta es la lista real {lista_real}")
print(type(lista), type(lista_real))