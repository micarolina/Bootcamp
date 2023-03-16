class Curso:
  # Crear atributos self
    def __init__(self, titulo, profesor, clases):
        self.titulo = titulo
        self.profesor = profesor
        self.clases = clases
  
  # Imprimir el titulo, el profesor, y las clases de este objeto
    def imprimir_detalles(self):
        print(self.titulo, self.profesor, self.clases)

    def cambiar_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo


python = Curso('Cursod e Python', 'Eduardo', 15)
javascript = Curso('Curso de JavaScript', 'Uriel', 20)
javascript.imprimir_detalles()
