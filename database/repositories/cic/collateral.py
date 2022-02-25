from sqlalchemy import CHAR, VARCHAR, Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel
from database.models import CreditCollateral
from project.core.repository import Repository


class CreditCollateralRepos(Repository[CreditCollateral, int]):
    ...
