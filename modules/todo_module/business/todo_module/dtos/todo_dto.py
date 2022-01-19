class TodoDto:
    """dto for task service"""

    id: int
    title: str
    description: str

    def __init__(self, title: str, description: str, _id=None):
        """[summary]

        Args:
            title (str): [description]
            description (str): [description]
            _id ([type], optional): [description]. Defaults to None.
        """
        self.id = _id if _id is not None else 0
        self.title = title
        self.description = description
