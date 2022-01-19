from pinject import BindingSpec
from adapters.db_adapters.db_config import Config
from adapters.db_adapters.db_adapters import SqlConnectAdapter
from adapters.db_adapters.db_query import QueryExecuter
from modules.todo_module.enterprise.validators.uniquevalidator import UniqueValidator
from pinject import new_object_graph


class Mysec(BindingSpec):
    """[summary]

    Args:
        BindingSpec ([type]): [description]
    """

    def configure(self, bind):
        """[summary]

        Args:
            bind ([type]): [description]
        """
        bind("db_config", to_class=Config)
        bind("db_adapter", to_class=SqlConnectAdapter)
        bind("query", to_class=QueryExecuter)
        bind("validators", to_class=UniqueValidator)


obj_graph = new_object_graph(binding_specs=[Mysec()])
