def mesaje(nombre,apellido,descuento):
    resultado = operacion(descuento)
    print(nombre, apellido, 'tienes un',descuento,'% de descuento que es de',resultado)

def operacion(descuento):
    return (descuento * 2075)/100

def datos(nombre,apellido,anios):
        #2075
    if(anios==5):
        mesaje(nombre,apellido,50)
    elif(anios==3):
        mesaje(nombre,apellido,30)
    elif(anios==2):
        mesaje(nombre,apellido,20)
    else:
        print('Sin descuento')

datos('Mirian', 'Pico',2)
datos('Hector', 'Garcia',3)
datos('Hector', 'Ayres',5)