from database.models import AssetRealEstate
from project.core.repository import Repository


class AssetRealEstateRepos(Repository[AssetRealEstate, int]):
    ...
