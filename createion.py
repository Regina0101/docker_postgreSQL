import logging
import psycopg2
from psycopg2 import DatabaseError
from connection import create_connection


logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(levelname)s:%(message)s')


def create_table(conn, sql_expression):
    try:
        with conn.cursor() as c:
            c.execute(sql_expression)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()


if __name__ == '__main__':
    sql_create_groups = """
        CREATE TABLE IF NOT EXISTS groups (
          id SERIAL PRIMARY KEY,
          name VARCHAR(50) NOT NULL
        );
        """
    sql_create_students = """
        CREATE TABLE IF NOT EXISTS students (
          id SERIAL PRIMARY KEY,
          name VARCHAR(100) NOT NULL,
          group_id INTEGER,
          FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE CASCADE
        );
        """
    sql_create_teachers = """
        CREATE TABLE IF NOT EXISTS teachers (
          id SERIAL PRIMARY KEY,
          name VARCHAR(100) NOT NULL,
          group_id INTEGER,
          FOREIGN KEY (group_id) REFERENCES groups(id) ON DELETE CASCADE
        );
        """
    sql_create_subjects = """
        CREATE TABLE IF NOT EXISTS subjects (
          id SERIAL PRIMARY KEY,
          name VARCHAR(175) NOT NULL,
          teacher_id INTEGER,
          FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        );
        """
    sql_create_grades = """
        CREATE TABLE IF NOT EXISTS grades (
          id SERIAL PRIMARY KEY,
          student_id INTEGER,
          FOREIGN KEY (student_id) REFERENCES students(id),
          subject_id INTEGER,
          FOREIGN KEY (subject_id) REFERENCES subjects(id),
          grade INTEGER CHECK (grade >= 0 AND grade <= 100),
          grade_date DATE NOT NULL
        );
        """

    try:
        conn = create_connection()

        if conn is not None:
            with conn:
                create_table(conn, sql_create_groups)
                create_table(conn, sql_create_students)
                create_table(conn, sql_create_teachers)
                create_table(conn, sql_create_subjects)
                create_table(conn, sql_create_grades)
        else:
            logging.error("Error! Cannot create the database connection.")
    except RuntimeError as e:
        logging.error(e)
