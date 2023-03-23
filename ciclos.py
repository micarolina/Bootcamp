import random

partida_menos_intentos = False

while True:
  print("Menú: ")
  print("Opción 1: Jugar")
  print("Opción 2: Salir")  

  opcion_seleccionada = int(input("Escribe una opción: "))

  if opcion_seleccionada == 2:
    break

  if opcion_seleccionada == 1:
    # 1. Generar un número aleatorio
    numero_magico = random.randint(1,10) #  5

    intentos = 1
    # 2. Intentar adivinar el número generado
    numero_usuario = int(input("Adivina el número mágico entre 1 y 10: ")) # 5

    while numero_usuario != numero_magico:
      # 3. Si no adivino, darle pistas al usuario hasta que adivine
      intentos = intentos + 1

      if numero_magico < numero_usuario:
        print("El número mágico es menor al que ingresaste")
      if numero_magico > numero_usuario:
        print("El número mágico es mayor al que ingresaste")
      
      numero_usuario = int(input("Adivina el número mágico entre 1 y 10: "))

    # 4. Cuando adivine, mensaje de felicitación
    print(f"Felicidades, adivinaste en {intentos} intentos") # Interpolacion
    
    if intentos < partida_menos_intentos:
      partida_menos_intentos = intentos

print(f"La mejor partida fue en {partida_menos_intentos} intentos") # Interpolacion