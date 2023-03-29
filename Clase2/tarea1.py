#1. Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
#Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input('Ingresa tu edad'))
valor_mes = float(input('Ingresa tus ingreso mensuale'))



if edad >= 18 and valor_mes>= 1000:
    print('Tiene que tributar')
else:
    print('No tienes que tributar')
