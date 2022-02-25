from database.models.cic.institution import CreditInstitutionLoan
from project.core.repository import Repository


class CreditInstitutionLoanRepos(Repository[CreditInstitutionLoan, int]):
    ...
