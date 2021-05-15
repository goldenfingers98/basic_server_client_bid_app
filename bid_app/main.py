from lib.Server.Server import Server


def logMessage(message):
    print(message)
    Server.send({
        "response":"Hello there",
        "status":200
    })



Server.initialize(port=3000,pool_size=5)
Server.get(path='/log',callable=logMessage)
Server.run_application()