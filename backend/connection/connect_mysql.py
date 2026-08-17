import mysql.connector as ms

mycon=ms.connect(
    host='localhost',
    database='your_database_name',
    user='your_username',
    password='your_password'
)

mycursor=mycon.cursor()

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

        "Returns True if data is successfully created else False"

        try:
            query="""
            insert into  professors (
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
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
            mycursor.execute(query,(
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

        except:
            return False

    def find_by_email(self, email):
        pass

    def find_by_id(self, professor_id):
        pass

    def update(self,professor,**args):
        allowed_fields={
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
        values.append(professor.professor_id)
        set_clause= ", ".join(
        f"{field} = %s" for field in args

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
        pass

    