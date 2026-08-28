import os
import mysql.connector as ms
from dotenv import load_dotenv
from services.auth import Authentication

load_dotenv()

mycon = ms.connect(
    host="localhost",
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

mycursor = mycon.cursor()

class login_verify:

    def __init__(self,email,password):
        self.email=email
        self.password=password


    def verify(self):
        query="select password_hash from professors where email=%s"
        mycursor.execute(query,(self.email,))
        fetched_password=mycursor.fetchone()

        if not fetched_password:
            return False

        authenticator=Authentication(self.email)

        return authenticator.verify_hash(self.password,fetched_password[0])

