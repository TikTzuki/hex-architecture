from database.models.cic.credit_score import PersonCreditScore, PersonCreditScoreSegment
from project.core.repository import Repository


class PersonCreditScoreRepos(Repository[PersonCreditScore, int]):
    ...


class PersonCreditScoreSegmentRepos(Repository[PersonCreditScoreSegment, int]):
    ...
