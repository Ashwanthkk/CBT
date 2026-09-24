import os
import mysql.connector as ms
from students.Student import Students as Student
from dotenv import load_dotenv

load_dotenv()


mycon = ms.connect(
    host="localhost",
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

mycursor = mycon.cursor()


class StudentRepository:

    def create(
        self,
        profile_id,
        name,
        email,
        password_hash,
        phone_number=None,
        university_id=None,
        department_id=None,
        course=None,
        semester=None,
        roll_number=None
    ):
        """Returns True if data is successfully created, else False."""

        query = """
            INSERT INTO students (
                profile_id,
                name,
                email,
                password_hash,
                phone_number,
                university_id,
                department_id,
                course,
                semester,
                roll_number
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        try:
            mycursor.execute(query, (
                profile_id,
                name,
                email,
                password_hash,
                phone_number,
                university_id,
                department_id,
                course,
                semester,
                roll_number
            ))

            mycon.commit()
            return True

        except ms.Error as e:
            mycon.rollback()
            print("Database error:", e)
            return False


    def find_by_email(self, email):
        """
        Returns a Student object if the email exists,
        otherwise returns None.
        """

        query = """
            SELECT
                student_id,
                profile_id,
                name,
                email,
                phone_number,
                university_id,
                department_id,
                course,
                semester,
                roll_number,
                password_hash,
                status,
                last_login_at
            FROM students
            WHERE email = %s
        """

        try:
            mycursor.execute(query, (email,))
            row = mycursor.fetchone()

            if row is None:
                return None

            return Student(
                student_id=row[0],
                profile_id=row[1],
                name=row[2],
                email=row[3],
                phone_number=row[4],
                university_id=row[5],
                department_id=row[6],
                course=row[7],
                semester=row[8],
                roll_number=row[9],
                password_hash=row[10],
                status=row[11],
                last_login_at=row[12]
            )

        except ms.Error as e:
            print("Database error:", e)
            return None


    def find_by_id(self, student_id):
        """
        Returns a Student object if the ID exists,
        otherwise returns None.
        """

        query = """
            SELECT
                student_id,
                profile_id,
                name,
                email,
                phone_number,
                university_id,
                department_id,
                course,
                semester,
                roll_number,
                password_hash,
                status,
                last_login_at
            FROM students
            WHERE student_id = %s
        """

        try:
            mycursor.execute(query, (student_id,))
            row = mycursor.fetchone()

            if row is None:
                return None

            return Student(
                student_id=row[0],
                profile_id=row[1],
                name=row[2],
                email=row[3],
                phone_number=row[4],
                university_id=row[5],
                department_id=row[6],
                course=row[7],
                semester=row[8],
                roll_number=row[9],
                password_hash=row[10],
                status=row[11],
                last_login_at=row[12]
            )

        except ms.Error as e:
            print("Database error:", e)
            return None


    def update(self, student, **kwargs):

        allowed_fields = {
            "profile_id",
            "name",
            "email",
            "phone_number",
            "university_id",
            "department_id",
            "course",
            "semester",
            "roll_number",
            "password_hash",
            "status"
        }

        for field in kwargs:
            if field not in allowed_fields:
                raise ValueError(f"Cannot update field: {field}")

        if not kwargs:
            return False

        values = list(kwargs.values())

        # student_id is used only to identify the student
        values.append(student.student_id)

        set_clause = ", ".join(
            f"{field} = %s"
            for field in kwargs
        )

        query = f"""
            UPDATE students
            SET {set_clause}
            WHERE student_id = %s
        """

        try:
            mycursor.execute(query, values)
            mycon.commit()

            return mycursor.rowcount > 0

        except ms.Error as e:
            mycon.rollback()
            print("Database error:", e)
            return False


    def delete(self, student_id):
        """Deletes a student using student_id."""

        query = """
            DELETE FROM students
            WHERE student_id = %s
        """

        try:
            mycursor.execute(query, (student_id,))
            mycon.commit()

            return mycursor.rowcount > 0

        except ms.Error as e:
            mycon.rollback()
            print("Database error:", e)
            return False
