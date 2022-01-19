from sqlalchemy.exc import ResourceClosedError


class CustomExeption(ResourceClosedError):
    """same as ResourceClosedError"""

    pass
