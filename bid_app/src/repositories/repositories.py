from lib.repository.Repository import Repository
from src.models.models import *

class BuyerRepository(Repository):
    CLASS = Buyer

class AssetRepository(Repository):
    CLASS = Asset