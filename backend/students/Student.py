
class Students:
    def __init__(
        self,
        registration_id=None,
        full_name=None,
        email=None,
        mobile_number=None,
        board_name=None,
        roll_number=None,
        passing_year=None,
        percentage=None,
        is_declared=False,
        created_at=None
    ):
        self.registration_id = registration_id
        self.full_name = full_name
        self.email = email
        self.mobile_number = mobile_number
        self.board_name = board_name
        self.roll_number = roll_number
        self.passing_year = passing_year
        self.percentage = percentage
        self.is_declared = is_declared
        self.created_at = created_at