import os
import mysql.connector as ms
from dotenv import load_dotenv

load_dotenv()

mycon = ms.connect(
    host="localhost",
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

mycursor = mycon.cursor()


class otp_operations:

    # Returns True if operations are completed without any problems
    # else False

    def __init__(self, email, otp, expiry=None):
        self.email = email
        self.otp = otp
        self.expiry = expiry

    def upload(self):

        try:
            # Check whether this email already has an OTP
            rq = """
                SELECT otp
                FROM email_verification
                WHERE email = %s
            """

            mycursor.execute(rq, (self.email,))
            available_otp = mycursor.fetchone()

            # Existing OTP found
            if available_otp is not None:
                if self.clear():
                    pass
                else:
                    return False

            query = """
                INSERT INTO email_verification
                (email, otp, expiry_date)
                VALUES (%s, %s, %s)
            """

            mycursor.execute(
                query,
                (self.email, self.otp, self.expiry)
            )

            mycon.commit()

            return True

        except ms.Error as e:
            mycon.rollback()
            print("Database error:", e)
            return False

    def verify(self, current_time):

        verify_query = """
            SELECT email, expiry_date
            FROM email_verification
            WHERE email = %s AND otp = %s
        """

        try:
            mycursor.execute(
                verify_query,
                (self.email, self.otp)
            )

            res = mycursor.fetchone()

            if res:

                if current_time > res[1]:
                    return (False, "otp_expired")

                else:
                    return (True, "otp_accepted")

            return (False, "invalid_otp")

        except ms.Error as e:
            print("Database error:", e)
            return (False, "database_error")

    def clear(self):

        try:

            delete_query = """
                DELETE FROM email_verification
                WHERE email = %s
            """

            mycursor.execute(
                delete_query,
                (self.email,)
            )

            mycon.commit()

            return True

        except ms.Error as e:
            mycon.rollback()
            print("Database error:", e)
            return False