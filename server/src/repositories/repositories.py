from sys import set_asyncgen_hooks
from lib.repository.Repository import Repository
from src.models.models import *

class BuyerRepository(Repository):
    CLASS = Buyer

class AssetRepository(Repository):
    CLASS = Asset

    @staticmethod
    def exists(assetRef):
        try:
            AssetRepository.findById(assetRef)
            return True
        except Repository.RepositoryException as err:
            return False


    @staticmethod
    def findAssetsByState(state):
        return [asset for asset in AssetRepository.entities if asset.getState().upper() == state.upper()]

class HistoryRepository(Repository):
    CLASS = History

    @staticmethod
    def findHistoriesByAsset(asset):
        return [item for item in HistoryRepository.entities if item and item.getAsset() == asset]
