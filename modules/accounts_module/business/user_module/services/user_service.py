from adapters.db_adapters.db_query import QueryExecuter
from adapters.db_adapters.db_exeptions import CustomExeption
from modules.accounts_module.business.user_module.dtos.user_dto import UserDto
from pypika import Table, PostgreSQLQuery
from typing import List
# from modules.accounts_module.enterprise.validators.uniquevalidator import UniqueValidator


class UserService:
    """[summary]"""

    def __init__(self, query: QueryExecuter):
        """[summary]

        Args:
            query (QueryExecuter): [description]
            validators (UniqueValidator): [description]
        """
        self.query = query
        self.Table = Table
        self.Query = PostgreSQLQuery
        # self.validators = validators

    def create(self, data: UserDto) -> UserDto:
        """[summary]

        Args:
            data (TodoDto): [description]

        Raises:
            ValueError: [description]

        Returns:
            TodoDto: [description]
        """
        table = self.Table("accounts_user")
        q = (
            self.Query.into(table)
                .columns("username", "first_name", "last_name", "password", "email", "gender", "phone_number",
                         "date_of_birth", "is_superuser", "is_staff", "is_active", "date_joined")
                .insert(data.username, data.first_name, data.last_name, data.password, data.email,
                        data.gender, data.phone_number, data.date_of_birth, True, True, True, "1999-05-01 05:30:00+05:30")
        )
        # if self.validators.validate(self.retrive_title(data.title)):
        #     raise ValueError("not unique")
        try:
            self.query.execute(q.get_sql())
        except CustomExeption:
            return {"data": "created"}

    # def update(self, data: UserDto, pk: int) -> UserDto:
    #     """[summary]
    #
    #     Args:
    #         data (TodoDto): [description]
    #         pk (int): [description]
    #
    #     Returns:
    #         TodoDto: [description]
    #     """
    #     table = self.Table("accounts_user")
    #     q = (
    #         self.Query.update(table)
    #             .set(table.username, data.username)
    #             .set(table.password, data.password)
    #             .where(table.id == pk)
    #     )
    #     return self.query.execute(q.get_sql())
    #
    # def retrive(self, pk: int) -> UserDto:
    #     """[summary]
    #
    #     Args:
    #         pk (int): [description]
    #
    #     Returns:
    #         TodoDto: [description]
    #     """
    #     table = self.Table("accounts_user")
    #     q = self.Query.from_(table).select("*").where(table.id == pk)
    #     return self.query.execute(q.get_sql())
    #
    # def retrive_username(self, pk: str) -> UserDto:
    #     """[summary]
    #
    #     Args:
    #         pk (str): [description]
    #
    #     Returns:
    #         TodoDto: [description]
    #     """
    #     table = self.Table("accounts_user")
    #     q = self.Query.from_(table).select("*").where(table.username == pk)
    #     return self.query.execute(q.get_sql())

    def get_list(self) -> List[UserDto]:
        """[summary]

        Returns:
            List[TodoDto]: [description]
        """
        table = self.Table("accounts_user")
        q = self.Query.from_(table).select("*")
        return self.query.execute(q.get_sql())
