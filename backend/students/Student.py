class Students:
    def __init__(
        self,
        student_id=None,
        profile_id=None,
        name=None,
        email=None,
        phone_number=None,
        university_id=None,
        department_id=None,
        course=None,
        semester=None,
        roll_number=None,
        password_hash=None,
        status="ACTIVE",
        last_login_at=None
    ):
        self.student_id = student_id
        self.profile_id = profile_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.university_id = university_id
        self.department_id = department_id
        self.course = course
        self.semester = semester
        self.roll_number = roll_number
        self.password_hash = password_hash
        self.status = status
        self.last_login_at = last_login_at