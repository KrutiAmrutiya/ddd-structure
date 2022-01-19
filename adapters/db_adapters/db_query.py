from adapters.db_adapters.db_adapters import SqlConnectAdapter


class QueryExecuter:
    """executes sql query"""

    def __init__(self, db_adapter: SqlConnectAdapter) -> None:
        """[summary]

        Args:
            db_adapter  (SqlConnectAdapter): [description]
        """
        self.conn = db_adapter.connect()

    def execute(self, sqlquery: str):
        """[summary]

        Args:
            sqlquery (str): [description]

        Returns:
            [type]: [description]
        """
        return self.conn.execute(sqlquery)
