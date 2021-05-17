from lib.repository.Repository import Repository
from src.models.models import *

class BuyerRepository(Repository):
    CLASS = Buyer

class AssetRepository(Repository):
    CLASS = Asset

class HistoryRepository(Repository):
    CLASS = History

    @staticmethod
    def findHistoriesByAsset(asset):
        return [item for item in HistoryRepository.entities if item and item.getAsset() == asset]
