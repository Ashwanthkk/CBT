import requests

BASE_URL = "http://127.0.0.1:8000"

email=input("Enter email:")
password=input("Enter password:")

otp_response=requests.post(
    f"{BASE_URL}/verify_credentials",
    json={
        "email":email,
        "password":password
    }
    
)

print("Verifying")
print("Status code:", otp_response.status_code)
print("Response:", otp_response.json())


if otp_response.status_code != 200:
    print("Failed to send data.")
    exit()
