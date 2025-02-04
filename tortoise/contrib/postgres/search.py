from typing import Union

from pypika_tortoise.enums import Comparator
from pypika_tortoise.terms import BasicCriterion, Function, Term

from tortoise.contrib.postgres.functions import ToTsQuery, ToTsVector


class Comp(Comparator):
    search = " @@ "


class SearchCriterion(BasicCriterion):  # type: ignore
    def __init__(self, field: Term, expr: Union[Term, Function]) -> None:
        if not isinstance(expr, Function):
            expr = ToTsQuery(expr)
        super().__init__(Comp.search, ToTsVector(config_name=expr.args[0].value, field=field), expr)
