from pypika_tortoise.terms import Function, Term

DEFAULT_TEXT_SEARCH_CONFIG = "pg_catalog.simple"


class ToTsVector(Function):
    """
    to to_tsvector function
    """

    def __init__(self, field: Term, config_name: str = DEFAULT_TEXT_SEARCH_CONFIG) -> None:
        super().__init__("TO_TSVECTOR", config_name, field)


class ToTsQuery(Function):
    """
    to_tsquery function
    """

    def __init__(self, field: Term, config_name: str = DEFAULT_TEXT_SEARCH_CONFIG) -> None:
        super().__init__("TO_TSQUERY", config_name, field)


class PlainToTsQuery(Function):
    """
    plainto_tsquery function
    """

    def __init__(self, field: Term, config_name: str = DEFAULT_TEXT_SEARCH_CONFIG) -> None:
        super().__init__("PLAINTO_TSQUERY", config_name, field)


class Random(Function):
    """
    Generate random number.

    :samp:`Random()`
    """

    def __init__(self, alias=None) -> None:
        super().__init__("RANDOM", alias=alias)
