from PySide2 import QtGui
from .ui.ui_HistorySearch import Ui_HistorySearch
from PySide2.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from components.AssetDetails.AssetDetails import AssetDetails
from lib.client.Client import Client


class HistorySearch(QDialog, Ui_HistorySearch):

    def __init__(self,data):
        QDialog.__init__(self)
        self.setupUi(self)
        # 
        self.__initialize(data)


    def __initialize(self,data):
        for history in data:
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


    def __create_tableEntry(self, **kwargs):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        data_list = list(kwargs.values())
        i = 0
        for item in data_list:
            self.tableWidget.setItem(row,i,QTableWidgetItem(str(item)))
            i += 1

