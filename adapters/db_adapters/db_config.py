import os


class Config:
    """Config Object"""

    db_name = os.getenv("db_name")
    db_host = os.getenv("db_host")
    db_user = os.getenv("db_user")
    db_password = os.getenv("db_password")
    db_driver = os.getenv("db_driver")

    @classmethod
    def db_uri(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        uri = "".join(
            [
                self.db_driver,
                "://",
                self.db_user,
                ":",
                self.db_password,
                "@",
                self.db_host,
                "/",
                self.db_name,
            ]
        )
        return dict(SQLALCHEMY_DATABASE_URI=uri)
