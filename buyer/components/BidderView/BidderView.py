import threading
from PySide2 import QtWidgets
from PySide2.QtWidgets import  QMainWindow, QMessageBox, QWidget
from .ui.ui_BidderView import Ui_BidderView
from components.BiddingRoom.BiddingRoom import BiddingRoom
from lib.client.Client import Client

class BidderView(QMainWindow, Ui_BidderView):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # Connecting signals to slots
        self.__connect_signals_to_slots()
        #########################
        self.show()


    def __connect_signals_to_slots(self):
        self.biddingRoomBtn.clicked.connect(self.__openBiddingRoom)

    def __openBiddingRoom(self):
        Client.get("/assets/available").then(self.__openBiddingRoomCallback)

    # Callbacks here

    def __openBiddingRoomCallback(self,res):
        if len(res['data']) == 0:
            QtWidgets.QMessageBox.information(self,"Bidding Room","No assets to buy, try later.")
        else:
            asset = res['data'][0]
            biddingWindow = BiddingRoom(asset)
            self.setDisabled(True)
            biddingWindow.show()
            biddingWindow.exec_()
            self.setDisabled(False)
