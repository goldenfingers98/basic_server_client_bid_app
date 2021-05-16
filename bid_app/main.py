from lib.server.Server import Server
# from src.models.models import *
from src.repositories.repositories import *


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

buyer = Buyer(0)
buyer.setBillAmmount(5455)
buyer1 = Buyer(1)
buyer1.setBillAmmount(6665)
buyerRepository = BuyerRepository()
buyerRepository.save(buyer)
buyerRepository.save(buyer1)

assetRepository = AssetRepository()
asset = Asset(150)
assetRepository.save(asset)

historyRepository = HistoryRepository()
# historyRepository.save(History(proposal=200,asset=asset,buyer=buyer))
# historyRepository.save(History(proposal=250,asset=asset,buyer=buyer1))
# historyRepository.save(History(proposal=300,asset=asset,buyer=buyer))
# historyRepository.save(History(proposal=450,asset=asset,buyer=buyer1))
# historyRepository.save(History(proposal=600,asset=asset,buyer=buyer))

l = historyRepository.findHistoriesByAsset(asset)
pass
