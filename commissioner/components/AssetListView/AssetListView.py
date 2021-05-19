from PySide2 import QtGui
from .ui.ui_AssetListView import Ui_AssetListView
from PySide2.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from components.AssetDetails.AssetDetails import AssetDetails
from lib.client.Client import Client


class AssetListView(QDialog, Ui_AssetListView):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        # 
        self.__connect_signals_to_slots()
        # 
        # 
        self.__initialize()


    def __initialize(self):
        Client.get('/asset/all').then(self.__initialize_callback)

    def __create_tableEntry(self, **kwargs):
        row = self.assetTable.rowCount()
        self.assetTable.insertRow(row)
        data_list = list(kwargs.values())
        i = 0
        for item in data_list:
            self.assetTable.setItem(row,i,QTableWidgetItem(str(item)))
            i += 1

    def __connect_signals_to_slots(self):
        self.addBtn.clicked.connect(self.__addAsset)
        self.searchBtn.clicked.connect(self.__searchAsset)

    # Signals here
    def __addAsset(self):
        # Gathering data to send
        request_data = {
            'ref':self.assetRef.value(),
            'startingPrice':self.startingPrice.value()
        }
        # Sending request
        Client.post('/asset/add',request_data).then(self.__saveAsset)

    def __searchAsset(self):
        assetRef = self.idInput.value()
        Client.post('/asset/ref',{'ref':assetRef}).then(self.__searchAsset_result)

    # Callbacks here
    def __initialize_callback(self,res):
        assets = res['data']
        for asset in assets:
            # Create a table entry
            asset_buyerId = None
            if asset['_Asset__buyer'] is not None:
                asset_buyerId = asset['_Asset__buyer']['_Buyer__id']
            self.__create_tableEntry(
                _Asset__ref = asset['_Asset__ref'],
                _Asset__starting_price = asset['_Asset__starting_price'],
                _Asset__last_price = asset['_Asset__last_price'],
                _Asset__state = asset['_Asset__state'],
                _Asset__buyer = asset_buyerId
            )


    def __saveAsset(self,res):
        if res['status'] == 200:
            asset = res['data']
            self.__create_tableEntry(
                    _Asset__ref = asset['_Asset__ref'],
                    _Asset__starting_price = asset['_Asset__starting_price'],
                    _Asset__last_price = asset['_Asset__last_price'],
                    _Asset__state = asset['_Asset__state'],
                    _Asset__buyer = asset['_Asset__buyer']
                )
    
    def __searchAsset_result(self,res):
        if res['status'] == 200:
            assetDetails = AssetDetails(res['data'])
            assetDetails.show()
            assetDetails.exec_()