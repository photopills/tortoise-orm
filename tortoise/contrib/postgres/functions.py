from pypika.terms import Function, Term

DEFAULT_TEXT_SEARCH_CONFIG = "pg_catalog.simple"


class ToTsVector(Function):  # type: ignore
    """
    to to_tsvector function
    """

    def __init__(self, field: Term, config_name: str = DEFAULT_TEXT_SEARCH_CONFIG):
        super(ToTsVector, self).__init__("TO_TSVECTOR", config_name, field)


class ToTsQuery(Function):  # type: ignore
    """
    to_tsquery function
    """

    def __init__(self, field: Term, config_name: str = DEFAULT_TEXT_SEARCH_CONFIG):
        super(ToTsQuery, self).__init__("TO_TSQUERY", config_name, field)


class PlainToTsQuery(Function):  # type: ignore
    """
    plainto_tsquery function
    """

    def __init__(self, field: Term, config_name: str = DEFAULT_TEXT_SEARCH_CONFIG):
        super(PlainToTsQuery, self).__init__("PLAINTO_TSQUERY", config_name, field)


class PlainToTsQuery(Function):  # type: ignore
    """
    plainto_tsquery function
    """

    def __init__(self, field: Term):
        super(PlainToTsQuery, self).__init__("PLAINTO_TSQUERY", field)


class Random(Function):  # type: ignore
    """
    Generate random number.

    :samp:`Random()`
    """

    def __init__(self, alias=None) -> None:
        super().__init__("RANDOM", alias=alias)
