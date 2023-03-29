#input() es la funcion que necesitamos pedir para un valor
#este valor lo recibe en cadena de caracteres

altura = float(input('ingresa la altura en metros'))
print(type(altura))
peso = input('ingresa tu peso en kilogramos')

#imc = peso / (altura*altura)
#      80 / 1.73 * 1.73
altura = float(altura)
peso = int(peso)
estatura = altura * altura
print(estatura)
imc = peso / estatura
print(imc)

# comparar los varos de IMC
if(imc < 18.5):
    print('delgadez')
elif(imc >= 18.5 and imc <=24.9):
    print('normal')
elif(imc >= 25.0 and imc <= 29.9):
    print('sobrepeso')
elif(imc >= 30.0):
    print('obesidad')
else:
    print('n/a')