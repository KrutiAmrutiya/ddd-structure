from typing import List
from pypika import Table, PostgreSQLQuery
from adapters.db_adapters.db_query import QueryExecuter
from adapters.db_adapters.db_exeptions import CustomExeption
from modules.task_module.business.task_module.Dtos.task_dto import TaskDto
from modules.task_module.enterprise.validators.uniquevalidator import UniqueValidator


class TaskService:
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

    def create(self, data: TaskDto) -> TaskDto:
        """[summary]

        Args:
            data (TaskDto): [description]

        Raises:
            ValueError: [description]

        Returns:
            TaskDto: [description]
        """
        table = self.Table("task_task")
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

    def update(self, data: TaskDto, pk: int) -> TaskDto:
        """[summary]

        Args:
            data (TaskDto): [description]
            pk (int): [description]

        Returns:
            TaskDto: [description]
        """
        table = self.Table("task_task")
        q = (
            self.Query.update(table)
                .set(table.title, data.title)
                .set(table.description, data.description)
                .where(table.id == pk)
        )
        return self.query.execute(q.get_sql())

    def retrive(self, pk: int) -> TaskDto:
        """[summary]

        Args:
            pk (int): [description]

        Returns:
            TaskDto: [description]
        """
        table = self.Table("task_task")
        q = self.Query.from_(table).select("*").where(table.id == pk)
        return self.query.execute(q.get_sql())

    def retrive_title(self, pk: str) -> TaskDto:
        """[summary]

        Args:
            pk (str): [description]

        Returns:
            TaskDto: [description]
        """
        table = self.Table("task_task")
        q = self.Query.from_(table).select("*").where(table.title == pk)
        return self.query.execute(q.get_sql())

    def get_list(self) -> List[TaskDto]:
        """[summary]

        Returns:
            List[TaskDto]: [description]
        """
        table = self.Table("task_task")
        q = self.Query.from_(table).select("*")
        return self.query.execute(q.get_sql())
