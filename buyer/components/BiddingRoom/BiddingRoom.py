from PySide2.QtWidgets import QApplication, QDialog
from .ui.ui_BiddingRoom import Ui_BiddingRoom
from lib.client.Client import Client

class BiddingRoom(QDialog,Ui_BiddingRoom):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        # 
        self.__connct_signals_to_slots()

    def __connct_signals_to_slots(self):
        self.bidBtn.clicked.connect(self.postBid)

    def postBid(self):
        Client.get("/hello",print)
