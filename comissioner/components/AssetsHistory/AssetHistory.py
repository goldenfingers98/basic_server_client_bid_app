from PySide2 import QtGui
from .ui.ui_AssetHistory import Ui_AssetHistory
from PySide2.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from components.HistorySearch.HistorySearch import HistorySearch
from lib.client.Client import Client


class AssetHistory(QDialog, Ui_AssetHistory):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        # 
        self.__connect_signals_to_slots()
        # 
        self.__initialize()


    def __connect_signals_to_slots(self):
        self.search.clicked.connect(self.__search)


    def __initialize(self):
        Client.get('/history/all').then(self.__initialize_callback)

    def __create_tableEntry(self, **kwargs):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        data_list = list(kwargs.values())
        i = 0
        for item in data_list:
            self.tableWidget.setItem(row,i,QTableWidgetItem(str(item)))
            i += 1



    # Slots here
    def __search(self):
        Client.post('/history/asset',{'id':self.idInput.value()}).then(self.__searchAsset_result)


    # Callbacks here
    def __initialize_callback(self,res):
        if res['status'] == 200:
            for history in res['data']:
                date = history['_History__date']
                try:
                    date = f"{date['day']}/{date['month']}/{date['year']} {date['time'].strip()}" # Whenever the parser doesn't work properly
                except:pass
                self.__create_tableEntry(
                    _History__date=date,
                    _History__buyer = history['_History__buyer']['_Buyer__id'],
                    _Asset__ref = history['_History__asset']['_Asset__ref'],
                    _History__proposal=history['_History__proposal'],
                    _History__result = history['_History__result']

                )
            self.show()
            self.exec_()

    def __searchAsset_result(self,res):
        if res['status'] == 200:
            historySearch = HistorySearch(res['data'])