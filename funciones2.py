largo = float(input('Ingresar el largo en metros'))
ancho = float(input('Ingresar el ancho en metros'))
m2XCaja = float(input('Ingresa el metro2 por caja'))
precioXm2 = float(input('Ingresar precio x m2'))

#calcular metros cuadrados de un cuarto
m2Cuarto = largo * ancho
#saber cuantas cajas se necesitan
cajas = m2Cuarto/m2XCaja

#calcular el precio de de cajas
#calcular el total de gastos
precioXcaja = (m2XCaja * precioXm2)
preciototal = cajas * precioXcaja

print('Total de cajas que se necesitan:',cajas)
print('Precio total:',preciototal)
