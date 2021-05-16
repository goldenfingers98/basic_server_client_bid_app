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

buyerRepository = BuyerRepository()
buyerRepository.save(buyer)

buyer.setId(1555)
buyerRepository.save(buyer)
