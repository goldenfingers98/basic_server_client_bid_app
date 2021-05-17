from lib.server.Server import Server
from routes import *


# routes callbacks here


if __name__ == '__main__':
    # initializing server and routes
    Server.initialize(port=3000,pool_size=5)





    Server.run_application() 