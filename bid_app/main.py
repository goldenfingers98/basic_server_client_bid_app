from lib.server.Server import Server
# from src.models.models import *
from src.repositories.repositories import *
from time import sleep


def logMessage():
    Server.send({
        "data":"Hello there",
        "status":200
    })

def postTest(message):
    print(message)
    Server.send({
        "data":"Hello from post test!",
        "status":200
    })



Server.initialize(port=3000,pool_size=5)
Server.get(path='/log',callable=logMessage)
Server.post(path='/postTest',callable=postTest)
Server.run_application() 