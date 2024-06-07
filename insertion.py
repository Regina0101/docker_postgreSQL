from faker import Faker
import random
import psycopg2
from psycopg2 import DatabaseError
from connection import create_connection

fake = Faker()


def insert_fake_data(conn):
    try:
        with conn.cursor() as cursor:
            for _ in range(3):
                group_name = fake.word()
                cursor.execute("INSERT INTO groups (name) VALUES (%s)", (group_name,))

            cursor.execute("SELECT id FROM groups")
            group_ids = [row[0] for row in cursor.fetchall()]

            for _ in range(50):
                student_name = fake.name()
                group_id = random.choice(group_ids)
                cursor.execute("INSERT INTO students (name, group_id) VALUES (%s, %s)", (student_name, group_id))

            for _ in range(5):
                teacher_name = fake.name()
                group_id = random.choice(group_ids)
                cursor.execute("INSERT INTO teachers (name, group_id) VALUES (%s, %s)", (teacher_name, group_id))

            cursor.execute("SELECT id FROM teachers")
            teacher_ids = [row[0] for row in cursor.fetchall()]

            for _ in range(8):
                subject_name = fake.word()
                teacher_id = random.choice(teacher_ids)
                cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)", (subject_name, teacher_id))

            for student_id in range(1, 51):
                for subject_id in range(1, 9):
                    grade = random.randint(0, 100)
                    grade_date = fake.date_between(start_date='-1y', end_date='today')
                    cursor.execute(
                        "INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s)",
                        (student_id, subject_id, grade, grade_date))

            conn.commit()
            print("Fake data inserted successfully.")
    except DatabaseError as e:
        conn.rollback()
        print(f"Error: {e}")


if __name__ == '__main__':
    conn = create_connection()

    if conn is not None:
        insert_fake_data(conn)
    else:
        print("Error: cannot create a database connection.")
