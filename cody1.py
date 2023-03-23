import random

def jugar_numero_magico(numero_magico):
  numero_usuario = int(input("Adivina el número mágico entre 1 y 10: ")) # 7
  if numero_magico < numero_usuario:
    print("El número mágico es menor al que ingresaste")
    jugar_numero_magico(numero_magico)
  elif numero_magico > numero_usuario:
    print("El número mágico es mayor al que ingresaste")
    jugar_numero_magico(numero_magico) # 7
  else:
    print("Felicidades, adivinaste")

numero_magico = random.randint(1,10) # 7
jugar_numero_magico(numero_magico) # 7