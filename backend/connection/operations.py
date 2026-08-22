import os
import mysql.connector as ms
from connection.admins import Professor
from dotenv import load_dotenv

load_dotenv()


mycon = ms.connect(
    host="localhost",
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

mycursor = mycon.cursor()


class ProfessorRepository:

    def create(
        self,
        profile_id,
        name,
        email,
        password_hash,
        phone_number=None,
        university_id=None,
        department_id=None,
        designation=None,
        employee_id=None
    ):
        """Returns True if data is successfully created, else False."""

        query = """
            INSERT INTO professors (
                profile_id,
                name,
                email,
                password_hash,
                phone_number,
                university_id,
                department_id,
                designation,
                employee_id
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
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
                designation,
                employee_id
            ))

            mycon.commit()
            return True

        except ms.Error as e:
            mycon.rollback()
            print("Database error:", e)
            return False


    def find_by_email(self, email):
        """
        Returns a Professor object if the email exists,
        otherwise returns None.
        """

        query = """
            SELECT
                professor_id,
                profile_id,
                name,
                email,
                phone_number,
                university_id,
                department_id,
                designation,
                employee_id,
                password_hash,
                role,
                status,
                last_login_at
            FROM professors
            WHERE email = %s
        """

        try:
            mycursor.execute(query, (email,))
            row = mycursor.fetchone()

            if row is None:
                return None

            return Professor(
                professor_id=row[0],
                profile_id=row[1],
                name=row[2],
                email=row[3],
                phone_number=row[4],
                university_id=row[5],
                department_id=row[6],
                designation=row[7],
                employee_id=row[8],
                password_hash=row[9],
                role=row[10],
                status=row[11],
                last_login_at=row[12]
            )

        except ms.Error as e:
            print("Database error:", e)
            return None


    def find_by_id(self, professor_id):
        """
        Returns a Professor object if the ID exists,
        otherwise returns None.
        """

        query = """
            SELECT
                professor_id,
                profile_id,
                name,
                email,
                phone_number,
                university_id,
                department_id,
                designation,
                employee_id,
                password_hash,
                role,
                status,
                last_login_at
            FROM professors
            WHERE professor_id = %s
        """

        try:
            mycursor.execute(query, (professor_id,))
            row = mycursor.fetchone()

            if row is None:
                return None

            return Professor(
                professor_id=row[0],
                profile_id=row[1],
                name=row[2],
                email=row[3],
                phone_number=row[4],
                university_id=row[5],
                department_id=row[6],
                designation=row[7],
                employee_id=row[8],
                password_hash=row[9],
                role=row[10],
                status=row[11],
                last_login_at=row[12]
            )

        except ms.Error as e:
            print("Database error:", e)
            return None


    def update(self, professor, **args):

        allowed_fields = {
            "profile_id",
            "name",
            "email",
            "phone_number",
            "university_id",
            "department_id",
            "designation",
            "employee_id",
            "password_hash",
            "role",
            "status"
        }

        for field in args:
            if field not in allowed_fields:
                raise ValueError(f"Cannot update field: {field}")

        if not args:
            return False

        values = list(args.values())

        # professor_id is used only to identify the professor
        values.append(professor.professor_id)

        set_clause = ", ".join(
            f"{field} = %s"
            for field in args
        )

        query = f"""
            UPDATE professors
            SET {set_clause}
            WHERE professor_id = %s
        """

        try:
            mycursor.execute(query, values)
            mycon.commit()

            return mycursor.rowcount > 0

        except ms.Error as e:
            mycon.rollback()
            print("Database error:", e)
            return False


    def delete(self, professor_id):
        """Deletes a professor using professor_id."""

        query = """
            DELETE FROM professors
            WHERE professor_id = %s
        """

        try:
            mycursor.execute(query, (professor_id,))
            mycon.commit()

            return mycursor.rowcount > 0

        except ms.Error as e:
            mycon.rollback()
            print("Database error:", e)
            return False