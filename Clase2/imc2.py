altura = float(input('Ingresa la estatura en metros'))
peso = int(input('Ingresa tu peso en kilogramos'))


estatura = altura * altura
print(estatura)
imc = peso / estatura
print(format(imc, '.2f'))
 
if(imc < 18.5):
    print('Tu rango es Delgadez', format(imc, '.1f'))
elif(imc >= 18.5 and imc <= 24.9):
    print('Tu rango es Normal', format(imc, '.1f'))
elif(imc >= 25.0 and imc <= 29.9):
    print('Tu rango es Obesidad', format(imc, '.1f'))
elif(imc >= 30.0):
    print('Obesidad', format(imc, '.1f'))
else:
    print('n/a')
