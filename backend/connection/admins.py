class Professor:
    def __init__(
        self,
        professor_id=None,
        profile_id=None,
        name=None,
        email=None,
        phone_number=None,
        university_id=None,
        department_id=None,
        designation=None,
        employee_id=None,
        password_hash=None,
        role="PROFESSOR",
        status="ACTIVE",
        last_login_at=None
    ):
        self.professor_id = professor_id
        self.profile_id = profile_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.university_id = university_id
        self.department_id = department_id
        self.designation = designation
        self.employee_id = employee_id
        self.password_hash = password_hash
        self.role = role
        self.status = status
        self.last_login_at = last_login_at
