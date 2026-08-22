import requests

url = "http://127.0.0.1:8000/create-account"

account = {
    "profile_id": "PROF002",
    "name": "John Doe",
    "email": "john@example.com",
    "password": "MyPassword123!",
    "phone_number": "9876543210",
    "university_id": 1,
    "department_id": 2,
    "designation": "Professor",
    "employee_id": "EMP001"
}

response = requests.post(url, json=account)

print("Status code:", response.status_code)
print("Response:", response.json())