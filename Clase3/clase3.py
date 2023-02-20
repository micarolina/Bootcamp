num1 = 2.0
num2 = 5
resultado = num1 + num2
print(type(resultado))

#booleanos: true, false

mayor_edad = True

edad = int(input('ingresa tu edad'))

#comparacion de edad
#si (expresion)
if(edad >= 18 or edad <= 25):
    print('eres mayor de edad')
    #sino si (expresion - else significa sino)
elif (edad == 17):
    print('casi mayor de edad')
else:
    print('eres menor de edad')


