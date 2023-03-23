import random

class NumeroMagico:
  def __init__(self):
    self.intentos = 0 # 0
    self.numero_magico = random.randint(1,10)

  def jugar(self):
    numero_usuario = int(input("Adivina del 1 al 10: "))
    self.intentos = self.intentos + 1 

    if self.numero_magico < numero_usuario:
      print("El número mágico es menor al que ingresaste") 
      self.jugar()
    elif self.numero_magico > numero_usuario:
      print("El número mágico es mayor al que ingresaste")
      self.jugar()
    else:
      print(f"Felicidades, adivinaste en {self.intentos} intentos")    
    
while True:
  print("Menú: ")
  print("Opción 1: Jugar")
  print("Opción 2: Salir")

  opcion_seleccionada = int(input("Escribe una opción: "))

  if opcion_seleccionada == 2:
    break
  if opcion_seleccionada == 1:
    juego_magico = NumeroMagico()
    juego_magico.jugar()