import sqlite3


def create_student_table():
    conn = sqlite3.connect('universidad.db')
    c = conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS estudiantes(
              matricula TEXT PRIMARY KEY,
              nombre TEXT NOT NULL,
              apellido TEXT NOT NULL,
              promedio REAL
    )""")
    conn.close()


def insert_student(student):
    conn = sqlite3.connect('universidad.db')
    c = conn.cursor()
    c.execute("INSERT INTO estudiantes VALUES(?, ?, ?, ?)", 
              (student.matricula, student.nombre, student.apellido, student.promedio))
    conn.commit()
    conn.close()


def select_student(matricula):
    conn = sqlite3.connect('universidad.db')
    c = conn.cursor()
    c.execute("SELECT * FROM estudiantes WHERE matricula=?", (matricula,))
    estudiante = c.fetchone()
    conn.close()
    return estudiante


def update_prom(matricula, prom):
    conn = sqlite3.connect('universidad.db')
    c = conn.cursor()
    c.execute("UPDATE estudiantes SET promedio=? WHERE matricula=?", 
              (prom, matricula))
    conn.commit()
    conn.close()


def delete_student(matricula):
    conn = sqlite3.connect('universidad.db')
    c = conn.cursor()
    c.execute("DELETE from estudiantes WHERE matricula=?", (matricula))
    conn.commit()
    conn.close()


def select_all():
    conn = sqlite3.connect('universidad.db')
    c = conn.cursor()
    c.execute("SELECT * FROM estudiantes")
    print(c.fetchall())
    conn.close()

