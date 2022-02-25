from sqlalchemy import VARCHAR, Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel
from database.models import AssetOther
from project.core.repository import Repository


class AssetOtherRepos(Repository[AssetOther, int]):
    ...
