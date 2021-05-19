from .ui.ui_BillDetails import Ui_BillDetails
from PySide2.QtWidgets import QDialog


class BillDetails(QDialog, Ui_BillDetails):

    def __init__(self,data):
        QDialog.__init__(self)
        self.setupUi(self)
        # 
        self.__initialize(data)

    
    def __initialize(self,data):
        self.id.setText(str(data['_Buyer__id']))
        self.foc.setText(str(data['_Buyer__bill_ammount']/1.2))
        self.ac.setText(str(data['_Buyer__bill_ammount']/1.2))
        

   

