from database.models import CreditCard
from project.core.repository import Repository


class CreditCardRepos(Repository[CreditCard, int]):
    ...
