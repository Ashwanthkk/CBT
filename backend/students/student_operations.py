
import os
import mysql.connector
from dotenv import load_dotenv

from students.Student import Students as Student

load_dotenv()

mycon = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

mycursor = mycon.cursor()


class StudentMethods:

    def create(
        self,
        full_name,
        email,
        mobile_number,
        board_name,
        roll_number,
        passing_year,
        percentage=None,
        is_declared=False
    ):
        try:
            query = """
                INSERT INTO students (
                    full_name,
                    email,
                    mobile_number,
                    board_name,
                    roll_number,
                    passing_year,
                    percentage,
                    is_declared
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                full_name,
                email,
                mobile_number,
                board_name,
                roll_number,
                passing_year,
                percentage,
                is_declared
            )

            mycursor.execute(query, values)
            mycon.commit()
            return True

        except mysql.connector.Error as e:
            mycon.rollback()
            print(f"Error creating student: {e}")
            return False

    def find_by_email(self, email):
        try:
            query = """
                SELECT
                    registration_id,
                    full_name,
                    email,
                    mobile_number,
                    board_name,
                    roll_number,
                    passing_year,
                    percentage,
                    is_declared,
                    created_at
                FROM students
                WHERE email = %s
            """

            mycursor.execute(query, (email,))
            row = mycursor.fetchone()

            if row is None:
                return None

            return Student(
                registration_id=row[0],
                full_name=row[1],
                email=row[2],
                mobile_number=row[3],
                board_name=row[4],
                roll_number=row[5],
                passing_year=row[6],
                percentage=row[7],
                is_declared=row[8],
                created_at=row[9]
            )

        except mysql.connector.Error as e:
            print(f"Error finding student by email: {e}")
            return None

    def find_by_id(self, registration_id):
        try:
            query = """
                SELECT
                    registration_id,
                    full_name,
                    email,
                    mobile_number,
                    board_name,
                    roll_number,
                    passing_year,
                    percentage,
                    is_declared,
                    created_at
                FROM students
                WHERE registration_id = %s
            """

            mycursor.execute(query, (registration_id,))
            row = mycursor.fetchone()

            if row is None:
                return None

            return Student(
                registration_id=row[0],
                full_name=row[1],
                email=row[2],
                mobile_number=row[3],
                board_name=row[4],
                roll_number=row[5],
                passing_year=row[6],
                percentage=row[7],
                is_declared=row[8],
                created_at=row[9]
            )

        except mysql.connector.Error as e:
            print(f"Error finding student by ID: {e}")
            return None

    def update(self, student, **kwargs):
        allowed_fields = {
            "full_name",
            "email",
            "mobile_number",
            "board_name",
            "roll_number",
            "passing_year",
            "percentage",
            "is_declared"
        }

        if not kwargs:
            return False

        if any(field not in allowed_fields for field in kwargs):
            raise ValueError("Invalid field provided for update")

        try:
            set_clause = ", ".join(
                f"{field} = %s" for field in kwargs
            )

            query = f"""
                UPDATE students
                SET {set_clause}
                WHERE registration_id = %s
            """

            values = tuple(kwargs.values()) + (
                student.registration_id,
            )

            mycursor.execute(query, values)
            mycon.commit()

            return mycursor.rowcount > 0

        except mysql.connector.Error as e:
            mycon.rollback()
            print(f"Error updating student: {e}")
            return False

    def delete(self, registration_id):
        try:
            query = """
                DELETE FROM students
                WHERE registration_id = %s
            """

            mycursor.execute(query, (registration_id,))
            mycon.commit()

            return mycursor.rowcount > 0

        except mysql.connector.Error as e:
            mycon.rollback()
            print(f"Error deleting student: {e}")
            return False

