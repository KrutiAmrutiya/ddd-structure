from adapters.db_adapters.db_query import QueryExecuter
from adapters.db_adapters.db_exeptions import CustomExeption
from modules.todo_module.business.todo_module.dtos.todo_dto import TodoDto
from pypika import Table, PostgreSQLQuery
from typing import List
from modules.todo_module.enterprise.validators.uniquevalidator import UniqueValidator


class TodoService:
    """[summary]"""

    def __init__(self, query: QueryExecuter, validators: UniqueValidator):
        """[summary]

        Args:
            query (QueryExecuter): [description]
            validators (UniqueValidator): [description]
        """
        self.query = query
        self.Table = Table
        self.Query = PostgreSQLQuery
        self.validators = validators

    def create(self, data: TodoDto) -> TodoDto:
        """[summary]

        Args:
            data (TodoDto): [description]

        Raises:
            ValueError: [description]

        Returns:
            TodoDto: [description]
        """
        table = self.Table("todo_todo")
        q = (
            self.Query.into(table)
                .columns("title", "description")
                .insert(data.title, data.description)
        )
        if self.validators.validate(self.retrive_title(data.title)):
            raise ValueError("not unique")
        try:
            self.query.execute(q.get_sql())
        except CustomExeption:
            return {"data": "created"}

    def update(self, data: TodoDto, pk: int) -> TodoDto:
        """[summary]

        Args:
            data (TodoDto): [description]
            pk (int): [description]

        Returns:
            TodoDto: [description]
        """
        table = self.Table("todo_todo")
        q = (
            self.Query.update(table)
                .set(table.title, data.title)
                .set(table.description, data.description)
                .where(table.id == pk)
        )
        return self.query.execute(q.get_sql())

    def retrive(self, pk: int) -> TodoDto:
        """[summary]

        Args:
            pk (int): [description]

        Returns:
            TodoDto: [description]
        """
        table = self.Table("todo_todo")
        q = self.Query.from_(table).select("*").where(table.id == pk)
        return self.query.execute(q.get_sql())

    def retrive_title(self, pk: str) -> TodoDto:
        """[summary]

        Args:
            pk (str): [description]

        Returns:
            TodoDto: [description]
        """
        table = self.Table("todo_todo")
        q = self.Query.from_(table).select("*").where(table.title == pk)
        return self.query.execute(q.get_sql())

    def get_list(self) -> List[TodoDto]:
        """[summary]

        Returns:
            List[TodoDto]: [description]
        """
        table = self.Table("todo_todo")
        q = self.Query.from_(table).select("*")
        return self.query.execute(q.get_sql())
