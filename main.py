""" 
Dado un listado de Strings, desarrolla un programa que imprima en consola la palabra con mas caracteres en el listado.
"""
max = 0
max_palabra = ''

palabras = [
    'Hola',
    'Live',
    'Ejercicios',
    'Python',
    'CodigoFacilito',
    'Example'
]


for palabra in palabras:
    size = len(palabra)
    
    if size > max:
        max = size
        max_palabra = palabra


print(max_palabra)