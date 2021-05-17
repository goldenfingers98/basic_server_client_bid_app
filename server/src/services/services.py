from src.repositories.repositories import *
from threading import Semaphore,Lock


class BuyerService:
    __fileLock = Lock()
    __buyerRepository = BuyerRepository()

    def __init__(self):
        pass

    @classmethod
    def addBuyer(cls,buyer):
        try:
            # Getting permission
            cls.__fileLock.acquire()
            cls.__buyerRepository.save(buyer) # Critical ressource : file
        except Exception as err:
            pass
        finally:
            cls.__fileLock.release()

    @classmethod
    def getBuyers(cls):
        return cls.__buyerRepository.entities

    @classmethod
    def getBuyerById(cls,id):
        return cls.__buyerRepository.findById(id)

    @classmethod
    def updateBuyer(cls,buyer):
        # Retrieving the buyer
        try:
            temp = cls.__buyerRepository.findById(buyer.getId())
            temp.update(buyer)
            cls.__buyerRepository.save(temp)
        except Exception as err:
            # buyer doesn't exist
            pass

class AssetService:
    __fileLock = Lock()
    __assetRepository = AssetRepository()

    def __init__(self):
        pass

    @classmethod
    def addAsset(cls,asset):
        try:
            # Getting permission
            cls.__fileLock.acquire()
            cls.__assetRepository.save(asset) # Critical ressource : file
        except Exception as err:
            pass
        finally:
            cls.__fileLock.release()

    @classmethod
    def getAssets(cls):
        return cls.__assetRepository.entities

    @classmethod
    def updateAsset(cls,asset):
        # Retrieving the asset
        try:
            temp = cls.__assetRepository.findById(asset.getId())
            temp.update(asset)
            cls.__assetRepository.save(temp)
        except Exception as err:
            # asset doesn't exist
            pass

class HistoryService:
    __fileLock = Lock()
    __historyRepository = HistoryRepository()

    def __init__(self):
        pass

    @classmethod
    def addHistory(cls,history):
        try:
            # Getting permission
            cls.__fileLock.acquire()
            cls.__historyRepository.save(history) # Critical ressource : file
        except Exception as err:
            pass
        finally:
            cls.__fileLock.release()

    @classmethod
    def getHistorys(cls):
        return cls.__historyRepository.entities

    @classmethod
    def getHistoryByAsset(cls,asset):
        return cls.__historyRepository.findHistoriesByAsset()

    @classmethod
    def updatehistory(cls,history):
        # Retrieving the history
        try:
            temp = cls.__historyRepository.findById(history.getId())
            temp.update(history)
            cls.__historyRepository.save(temp)
        except Exception as err:
            # history doesn't exist
            pass