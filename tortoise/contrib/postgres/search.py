from typing import Union
from pypika.enums import Comparator
from pypika.terms import BasicCriterion, Term, Function
from tortoise.contrib.postgres.functions import ToTsQuery, ToTsVector


class Comp(Comparator):  # type: ignore
    search = " @@ "


class SearchCriterion(BasicCriterion):  # type: ignore
    def __init__(self, field: Term, expr: Union[Term, Function]):
        if not isinstance(expr, Function):
            expr = ToTsQuery(expr)
        super().__init__(Comp.search, ToTsVector(config_name=expr.args[0].value, field=field), expr)
