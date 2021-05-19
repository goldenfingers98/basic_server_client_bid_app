from PySide2.QtWidgets import QDialog
from .ui.ui_AssetDetails import Ui_AssetDetails

class AssetDetails(QDialog, Ui_AssetDetails):

    def __init__(self,data):
        QDialog.__init__(self)
        self.setupUi(self)
        # 
        self.__initiate(data)


    def __initiate(self,data):
        buyer = data['_Asset__buyer']
        if buyer is not None:
            buyer = data['_Asset__buyer']['_Buyer__id']
        self.ref.setText(str(data['_Asset__ref']))
        self.startingPrice.setText(str(data['_Asset__starting_price']))
        self.lastPrice.setText(str(data['_Asset__last_price']))
        self.owner.setText(str(buyer))
        self.state.setText(str(data['_Asset__state']))