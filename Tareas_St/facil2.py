# haz un programa que pida un valor y muestre en la pantalla el valor positivo o negativo.

valor = float(input("Ingrese un valor: "))

if valor > 0:
    print("El valor es positivo.")
elif valor < 0:
    print("El valor es negativo.")
else:
    print("El valor es cero.")
