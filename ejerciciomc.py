altura = float(input('Ingresa altura en metros: '))
peso = float(input('Ingresa tu peso en kilogramos: '))
imc = peso/(altura*altura)


if(imc < 18.5):
    print('IMC= ',imc,': Tu IMC es bajo')
elif(18.5 <= imc <= 24.9):
    print('IMC= ',imc,': Tu IMC es normal')
elif(24.9 < imc <= 29.9):
    print('IMC= ',imc,': Tu IMC es alto "sobrepeso"')
elif(29.9 < imc ):
    print('IMC= ',imc,': Tu IMC es muy alto "obesidad"')