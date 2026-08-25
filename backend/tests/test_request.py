"""This file contains llm generated code to test the backend"""

import requests


BASE_URL = "http://127.0.0.1:8000"


# --------------------------------
# 1. Send OTP
# --------------------------------

email = input("Enter professor email: ")

otp_response = requests.post(
    f"{BASE_URL}/send-otp",
    json={
        "email": email
    }
)

print("\nSend OTP")
print("Status code:", otp_response.status_code)
print("Response:", otp_response.json())


if otp_response.status_code != 200:
    print("Failed to send OTP.")
    exit()


# --------------------------------
# 2. Get OTP from user
# --------------------------------

user_otp = input("\nEnter the OTP received in email: ")


# --------------------------------
# 3. Verify OTP
# --------------------------------

verify_response = requests.post(
    f"{BASE_URL}/verify-otp",
    json={
        "email": email,
        "user_otp": user_otp
    }
)

print("\nVerify OTP")
print("Status code:", verify_response.status_code)
print("Response:", verify_response.json())


verify_data = verify_response.json()


# --------------------------------
# 4. Only create account if OTP
#    verification succeeds
# --------------------------------

if verify_response.status_code == 200 and verify_data["result"]:

    print("\nOTP verified successfully.")
    print("Creating professor account...")

    account = {
        "profile_id": "PROF002",
        "name": "John Doe",
        "email": email,
        "password": "MyPassword123!",
        "phone_number": "9876543210",
        "university_id": 1,
        "department_id": 2,
        "designation": "Professor",
        "employee_id": "EMP001"
    }

    account_response = requests.post(
        f"{BASE_URL}/create-account",
        json=account
    )

    print("\nCreate Account")
    print("Status code:", account_response.status_code)
    print("Response:", account_response.json())

else:

    print("\nOTP verification failed.")
    print("Account will NOT be created.")