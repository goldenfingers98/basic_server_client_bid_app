from sys import path
from lib.server.Server import Server
from routes.routes import *

# routes callbacks here


if __name__ == '__main__':
    # initializing server and routes
    Server.initialize(port=3000,pool_size=5)

    Server.post(path="/asset/bid",callable=bid)
    Server.get(path="/assets/available",callable=checkAssetToBuy)

    Server.post(path="/buyer/data",callable=buyerData)
    Server.post(path="/buyer/pay",callable=pay)



    Server.run_application() 