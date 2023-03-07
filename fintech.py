def transaccion(movimiento):
    # aqui va el codigo
    if movimiento > 0:
    #deposito
        print('Se ha realizado un deposito')
    elif movimiento == 0:
        print('Movimiento Invalido')
    else:
    #retiro
        print('Se ha realizado un retiro')

def modificar_saldo(movimiento):
    global saldo # magia
    if movimiento == 0:
        return
    
    movimiento_absoluto = abs(movimiento)
    if movimiento < 0 and movimiento_absoluto > saldo:
        print('No Tienes dinero suficiente')
        return

    saldo = saldo + movimiento


# saldo inicial
saldo = 0

transaccion(0)

# 5 transacciones
primer_movimiento = 100
transaccion(primer_movimiento)
modificar_saldo(primer_movimiento)


segundo_movimiento = 300
transaccion(segundo_movimiento)
modificar_saldo(segundo_movimiento)


tercer_movimiento = 500
transaccion(tercer_movimiento)
modificar_saldo(tercer_movimiento)

cuarto_movimiento = -200
transaccion(cuarto_movimiento)
modificar_saldo(cuarto_movimiento)

quinto_movimiento = -100
transaccion(quinto_movimiento)
modificar_saldo(quinto_movimiento)

sexto_movimiento = 0
transaccion(sexto_movimiento)
modificar_saldo(sexto_movimiento)

septimo_movimiento = 1000
transaccion(septimo_movimiento)
modificar_saldo(septimo_movimiento)

# saldo final
print(saldo)