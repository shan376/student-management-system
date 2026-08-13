import mysql.connector
from config import Config

def get_connection():
    connection = mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DATABASE
    )

    return connection
def add_student(name, email, course):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO students (name, email, course)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, email, course))

    connection.commit()

    cursor.close()
    connection.close()
def get_all_students():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM students"

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return students
def delete_student(student_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM students WHERE id = %s"

    cursor.execute(query, (student_id,))
    connection.commit()

    cursor.close()
    connection.close()
def get_student_by_id(student_id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM students WHERE id = %s"

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    cursor.close()
    connection.close()

    return student
def update_student(student_id, name, email, course):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    UPDATE students
    SET name=%s,
        email=%s,
        course=%s
    WHERE id=%s
    """

    cursor.execute(query, (name, email, course, student_id))

    connection.commit()

    cursor.close()
    connection.close()
