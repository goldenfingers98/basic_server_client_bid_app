from PySide2.QtWidgets import QMainWindow, QMessageBox
from .ui.ui_comissionerView import Ui_ComissionerView
from components.BiddingRoom.BiddingRoom import BiddingRoom
from components.AssetListView.AssetListView import AssetListView
from components.BillView.BillView import BillView
from lib.client.Client import Client

class ComissionerView(QMainWindow, Ui_ComissionerView):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # 
        self.__connect_signals_to_slots()
        # 
        self.show()


    def __connect_signals_to_slots(self):
        self.biddingRoom.clicked.connect(self.__open_biddingRoom)
        self.assetListView.clicked.connect(self.__open_assetListView)
        self.buyersBillView.clicked.connect(self.__open_billView)


    def __open_biddingRoom(self):
        biddingRoom = BiddingRoom()
        biddingRoom.show()
        biddingRoom.exec_()

    def __open_assetListView(self):
        assetListView = AssetListView()
        assetListView.show()
        assetListView.exec_()


    
    def __open_biddingRoom(self):
        Client.get("/assets/available").then(self.__openBiddingRoomCallback)

    def __open_billView(self):
        billView = BillView()
    # Callbacks here

    def __openBiddingRoomCallback(self,res):
        if res['data'] is None:
            QMessageBox.information(self,"Bidding Room","No assets to sell, try later.")
        elif len(res['data']) == 0:
            QMessageBox.information(self,"Bidding Room","No assets to sell, try later.")
        else:
            asset = res['data']['asset']
            current_time = res['data']['current_time']
            biddingWindow = BiddingRoom(asset,current_time)
            self.setDisabled(True)
            biddingWindow.show()
            biddingWindow.exec_()
            self.setDisabled(False)

    