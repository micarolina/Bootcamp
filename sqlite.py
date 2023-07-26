import sqlite3
from estudiantes import Estudiante
import estudiantesDB

conn = sqlite3.connect('universidad.db')
c = conn.cursor()

est_1 = Estudiante('222', 'Adriana', 'Cruz', '9.5')
est_2 = Estudiante('333', 'Marco', 'Rivas', '9.7')
est_3 = Estudiante('444', 'Adrian', 'Santacruz', '9.4')
est_4 = Estudiante('666', 'Roberto', 'Santacruz', '8.8')

many_students = [
    (est_1.matricula, est_1.nombre, est_1.apellido, est_1.promedio),
    (est_2.matricula, est_2.nombre, est_2.apellido, est_2.promedio),
    (est_3.matricula, est_3.nombre, est_3.apellido, est_3.promedio),
    (est_4.matricula, est_4.nombre, est_4.apellido, est_4.promedio)
]

def insertar_estudiante(estudiante):
    c.execute("INSERT INTO estudiantes VALUES (?, ?, ?, ?)", 
              (estudiante.matricula, estudiante.nombre, estudiante.apellido, estudiante.promedio))
    conn.commit()

# insertar_estudiante(est_4)

estudiantesDB.select_all()


conn.close()