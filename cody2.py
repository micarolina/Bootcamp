import random

class NumeroMagico:
  
  def __init__(self):
    self.numero_magico = random.randint(1,10)

  def jugar(self):
    numero_usuario = int(input("Adivina del 1 al 10"))
    while numero_usuario != self.numero_magico:
      if self.numero_magico < numero_usuario:
        print("El número mágico es menor al que ingresaste")
      if self.numero_magico > numero_usuario:
        print("El número mágico es mayor al que ingresaste")
      
      numero_usuario = int(input("Adivina el número mágico entre 1 y 10: "))
    print("Ganaste!")

juego_magico = NumeroMagico()
juego_magico.jugar()