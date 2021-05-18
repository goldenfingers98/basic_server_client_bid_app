from PySide2.QtWidgets import QApplication, QDialog
from .ui.ui_BiddingRoom import Ui_BiddingRoom
from lib.client.Client import Client

class BiddingRoom(QDialog,Ui_BiddingRoom):

    def __init__(self,asset):
        QDialog.__init__(self)
        self.setupUi(self)
        # Setting the asset informations
        self.assetId.setText(str(asset['_Asset__ref']))
        self.assetStartingFrom.setText(str(asset['_Asset__starting_price']))
        self.AssetCurrentPrice.setText(str(asset['_Asset__last_price']))
        self.lastBidder.setText(str(asset['_Asset__buyer']))
        self.proposalValue.setMinimum(asset['_Asset__last_price'])
        # 
        self.__connct_signals_to_slots()

    def __connct_signals_to_slots(self):
        self.bidBtn.clicked.connect(self.postBid)

    def postBid(self):
        Client.post("/asset/bid",[self.proposalValue.value()]).then(print)
