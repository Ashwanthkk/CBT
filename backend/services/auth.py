import smtplib
import secrets
import os
from datetime import datetime, timedelta
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


class Email_verification:

    def __init__(self, email):
        self.email = email
        self.otp = None
        self.expiry_time = None

    def send_otp(self):

        self.otp = f"{secrets.randbelow(1000000):06d}"

        self.expiry_time = datetime.now() + timedelta(minutes=10)

        message = EmailMessage()

        message["Subject"] = "CBT Email Verification"
        message["From"] = os.getenv("Gmail")
        message["To"] = self.email

        message.set_content(
            f"""
            Hello,

            Your CBT email verification code is:

            {self.otp}

            This code will expire in 10 minutes.

            If you did not request this verification, ignore this email.

            Regards,
            CBT System
            """
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(
                os.getenv("Gmail"),
                os.getenv("password")
            )

            smtp.send_message(message)

        return True

    def verify(self, user_otp):

        if self.otp is None:
            return False

        if datetime.now() > self.expiry_time:
            self.otp = None
            self.expiry_time = None
            return False

        if self.otp == str(user_otp):
            self.otp = None
            self.expiry_time = None
            return True

        return False


if __name__ == "__main__":

    load_email = Email_verification(
        "soumyap952@gmail.com"
    )

    load_email.send_otp()

    ot = input("Enter 6 digit otp: ")

    if load_email.verify(ot):
        print("Email verified successfully!")

    else:
        print("Invalid or expired OTP.")