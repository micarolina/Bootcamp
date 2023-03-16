def validar(mensaje):
    while True:
        try:
                dato = float(input(mensaje))
                return dato
        except:
                print('El dato debe ser un numero entero o decimal')
                

objetivo = input('Que compraras')
mesada = validar('De cuanto es tu mesada')
precio = validar('Coloca el precio que costara:')

meses = precio/mesada
ahorroActual = 0

while precio>ahorroActual:
        meses = meses-1
        mesadaActual = validar('mesada')
        ahorroActual = ahorroActual + mesadaActual
        restante = precio - ahorroActual

        print('Tiempo restante:', int(meses))
        print('AhorroP:', ahorroActual)
        print('Te falta: $', restante)
        
print('Felicitaciones llegaste a tu objetivo:', objetivo)
