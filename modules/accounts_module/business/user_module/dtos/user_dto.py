class UserDto:
    """dto for task service"""

    id: int
    username: str
    first_name: str
    last_name: str
    password: str
    email: str
    gender: str
    date_of_birth: int
    phone_number: int

    def __init__(self, username: str, first_name: str, last_name: str, password: str, email: str,
                 gender: str, date_of_birth: int, phone_number: int, _id=None):

        """[summary]

        Args:
            username (str): [description]
            password (str): [description]
            email (str): [description]
            _id ([type], optional): [description]. Defaults to None.
        """
        self.id = _id if _id is not None else 0
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.gender = gender
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
