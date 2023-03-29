num1 = 2.0
num2 = 5
resultado = num1 + num2
print(type(resultado))

#booleanos: True, False

mayor_edad = True

edad = int(input('Ingresa tu edad'))
genero = input('ingresa tu genero')

#comparacion de edad
if(genero == 'hombre' or genero == 'Hombre' or genero == 'Masculino'):
    print('eres hombre')
elif(genero == 'mujer'):
    print('eres mujer')
else:
    print('no definido')

#si (expresion)
if (edad >= 18 and edad <=25):
    print('eres mayor de edad')
#sino si (expresion)
elif(edad == 17):
    print('casi eres mayor de edad')
else:
    print('eres menor de edad')


