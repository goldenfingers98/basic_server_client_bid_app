from src.services.services import *


class BuyerController:
    __buyerService = BuyerService()

    @classmethod
    def getBuyerById(cls,id):
        return cls.__buyerService.getBuyerById(id)

    @classmethod
    def updateBuyerData(cls,buyer):
        cls.__buyerService.updateBuyer(buyer)



class HistoryController:
    __historyService = HistoryService()

    @classmethod
    def pushHistory(cls,history):
        cls.__historyService.addHistory(history)

    @classmethod
    def getHistoriesByAsset(cls,asset):
        return cls.__historyService.getHistoryByAsset(asset)

    @classmethod
    def getLastHistoryByAsset(cls,asset):
        return cls.__historyService.getHistoryByAsset(asset)[-1]

    @classmethod
    def updateHistory(cls,history):
        cls.__historyService.updateHistory(history)



class AssetController:
    __assetService = AssetService()

    @classmethod
    def checkAvailableAssets(cls):
        return cls.__assetService.getAssetsByState('disponible')

    @classmethod
    def updateAsset(cls,asset):
        cls.__assetService.updateAsset(asset)