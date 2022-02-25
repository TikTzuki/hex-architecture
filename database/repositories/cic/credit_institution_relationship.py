from database.models.cic.credit_institution_relationship import PersonCreditInstitutionRelationship
from project.core.repository import Repository


class PersonCreditInstitutionRelationshipRepos(Repository[PersonCreditInstitutionRelationship, int]):
    ...
