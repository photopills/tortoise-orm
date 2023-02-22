from typing import Optional
from pypika.terms import Function, Term


class ToTsVector(Function):  # type: ignore
    """
    to to_tsvector function
    """

    def __init__(self, field: Term, config_name: str = "pg_catalog.simple"):
        self.config_name = config_name
        super(ToTsVector, self).__init__("TO_TSVECTOR", config_name, field)


class ToTsQuery(Function):  # type: ignore
    """
    to_tsquery function
    """

    def __init__(self, field: Term, config_name: str = "pg_catalog.simple"):
        self.config_name = config_name
        super(ToTsQuery, self).__init__("TO_TSQUERY", config_name, field)


class PlainToTsQuery(Function):  # type: ignore
    """
    plainto_tsquery function
    """

    def __init__(self, field: Term, config_name: str = "pg_catalog.simple"):
        self.config_name = config_name
        super(PlainToTsQuery, self).__init__("PLAINTO_TSQUERY", config_name, field)


class Random(Function):  # type: ignore
    """
    Generate random number.

    :samp:`Random()`
    """

    def __init__(self, alias=None) -> None:
        super().__init__("RANDOM", alias=alias)
