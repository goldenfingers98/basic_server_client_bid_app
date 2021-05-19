import sys
from PySide2.QtWidgets import QApplication, QDialog
from .ui.ui_BillView import Ui_BillView
from lib.client.Client import Client
from dotenv import dotenv_values


CONFIG = dotenv_values('./.env')
BUYER_ID = int(CONFIG["ID"])

class BillView(QDialog, Ui_BillView):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        Client.post('/buyer/data',({'id':BUYER_ID})).then(self.initiateData) # J'ai enlevé le args au niveau de get c prq j'ai utilsé post...
        # 
        self.payBtn.clicked.connect(self.pay)

    def initiateData(self,res):
        data = res['data']
        self.id.setText(str(data['_Buyer__id']))
        self.beforeTax.setText(str(data['_Buyer__bill_ammount']/1.2))
        self.afterTax.setText(str(data['_Buyer__bill_ammount']))
        # Testing if the bill is empty
        if data['_Buyer__bill_ammount'] == 0:
            self.payBtn.setEnabled(False)

    def pay(self):
        Client.post('/buyer/pay',({'id':BUYER_ID})).then(self.resetBill)

    def resetBill(self,res):
        if res['status'] == 200: # ie Sucess
            self.beforeTax.setText('0')
            self.afterTax.setText('0')
            self.payBtn.setEnabled(False)
