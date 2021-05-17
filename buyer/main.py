from PySide2.QtWidgets import QApplication
from components.BidderView.BidderView import BidderView
from components.BiddingRoom.BiddingRoom import BiddingRoom
import sys
from dotenv import dotenv_values
from lib.client.Client import Client


# initializing host and port
CONFIG = dotenv_values('./.env')
HOST =  CONFIG["HOST"]
PORT = int(CONFIG["PORT"])
# Open a session
Client.openSession(HOST,PORT)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = BidderView()
    sys.exit(app.exec_())