from PySide2.QtWidgets import  QMainWindow, QMessageBox
from .ui.ui_BidderView import Ui_BidderView
from components.BiddingRoom.BiddingRoom import BiddingRoom
from components.BillView.BillView import BillView
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
        self.billViewBtn.clicked.connect(self.__openBillView)

    def __openBiddingRoom(self):
        Client.get("/assets/available").then(self.__openBiddingRoomCallback)

    def __openBillView(self):
        billView = BillView()
        billView.show()
        billView.exec_()

    # Callbacks here

    def __openBiddingRoomCallback(self,res):
        if res['data'] is None:
            QMessageBox.information(self,"Bidding Room","No assets to buy, try later.")
        elif len(res['data']) == 0:
            QMessageBox.information(self,"Bidding Room","No assets to buy, try later.")
        else:
            asset = res['data']['asset']
            current_time = res['data']['current_time']
            biddingWindow = BiddingRoom(asset,current_time)
            self.setDisabled(True)
            biddingWindow.show()
            biddingWindow.exec_()
            self.setDisabled(False)
