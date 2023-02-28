clientes = ['Lorena', 'Julian', 'Karla']

clientes.remove('Julian')
clientes.append('Luis')

for cliente in clientes:

    if(cliente == 'Julian'):
        print('No puede entrar', cliente)
    else:
        print('Si puede entrar', cliente)