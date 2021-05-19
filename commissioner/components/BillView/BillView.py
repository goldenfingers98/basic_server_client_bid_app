from PySide2 import QtGui
from .ui.ui_BillView import Ui_BillView
from PySide2.QtWidgets import QDialog, QTableWidgetItem
from lib.client.Client import Client
from components.BillDetails.BillDetails import BillDetails


class BillView(QDialog, Ui_BillView):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        # 
        self.__connect_signals_to_slots()
        # 
        Client.get('/buyer/all').then(self.__initialize)
        # 

    def __connect_signals_to_slots(self):
        self.search.clicked.connect(self.__search)
        self.addBtn.clicked.connect(self.__addBuyer)

    def __create_tableEntry(self, **kwargs):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        data_list = list(kwargs.values())
        i = 0
        for item in data_list:
            self.tableWidget.setItem(row,i,QTableWidgetItem(str(item)))
            i += 1


    def __initialize(self,res):
        if res['status'] == 200:
            for bill in res['data']:
                self.__create_tableEntry(
                    _Buyer__id = bill['_Buyer__id'],
                    _Buyer__bill_ammountFOC = bill['_Buyer__bill_ammount']/1.2,
                    _Buyer__bill_ammount = bill['_Buyer__bill_ammount'],
                )
            self.show()
            self.exec_()

    # Slots here

    def __search(self):
        Client.post('/buyer/data',{'id':self.idInput.value()}).then(self.__search_result)

    def __addBuyer(self):
        # Gathering data to send
        request_data = {
            'id':self.bidderId.value(),
        }
        # Sending request
        Client.post('/buyer/add',request_data).then(self.__saveBidder)

    # Callbacks here
    def __search_result(self,res):
        if res['status'] == 200:
            billDetails = BillDetails(res['data'])
            billDetails.show()
            billDetails.exec_()


    def __saveBidder(self,res):
        if res['status'] == 200:
            bill = res['data']
            self.__create_tableEntry(
                    _Buyer__id = bill['_Buyer__id'],
                    _Buyer__bill_ammountFOC = 0,
                    _Buyer__bill_ammount = 0,
                )