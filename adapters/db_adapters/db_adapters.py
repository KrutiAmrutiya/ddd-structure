from adapters.db_adapters.db_config import Config


class SqlConnectAdapter:
    """Sql Connector"""

    def __init__(self, db_config: Config) -> None:
        """[summary]

        Args:
            db_config (Config): [description]
        """
        self.db_config = db_config

    def connect(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        from sqlalchemy import create_engine

        conn = create_engine(self.db_config.db_uri().get("SQLALCHEMY_DATABASE_URI"))
        return conn
