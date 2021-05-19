from sys import path
from lib.server.Server import Server
from routes.routes import *

# routes callbacks here


if __name__ == '__main__':
    # initializing server and routes
    Server.initialize(port=3000,pool_size=5)

    Server.post(path="/asset/bid",callable=bid)
    Server.get(path="/assets/available",callable=checkAssetToBuy)
    Server.get(path="/asset/all",callable=getAssets)
    Server.post(path='/asset/add',callable=addAsset)
    Server.post('/asset/ref',callable=getAsset)

    Server.post(path="/buyer/data",callable=buyerData)
    Server.post(path="/buyer/pay",callable=pay)
    Server.post(path="/buyer/add",callable=addBuyer)
    Server.get(path='/buyer/all',callable=getBuyers)

    Server.get(path='/history/all',callable=getHistories)
    Server.post(path='/history/asset',callable=getHistoriyByAsset)

    Server.run_application() 