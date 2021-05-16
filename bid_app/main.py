from lib.server.Server import Server
# from src.models.models import *
from src.repositories.repositories import *
from time import sleep


# def logMessage(message):
#     print(message)
#     Server.send({
#         "response":"Hello there",
#         "status":200
#     })



# Server.initialize(port=3000,pool_size=5)
# Server.get(path='/log',callable=logMessage)
# Server.run_application()

###### test ######

# buyer = Buyer(0)
# buyer.setBillAmmount(5455)
# buyer1 = Buyer(1)
# buyer1.setBillAmmount(6665)
buyerRepository = BuyerRepository()
# buyerRepository.save(buyer)
# buyerRepository.save(buyer1)

assetRepository = AssetRepository()
asset = assetRepository.findById(150)

historyRepository = HistoryRepository()

l = historyRepository.findHistoriesByAsset(asset)
pass