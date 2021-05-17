from PySide2.QtWidgets import QApplication, QDialog
from .ui.ui_BiddingRoom import Ui_BiddingRoom
from lib.client.Client import Client

class BiddingRoom(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        ui = Ui_BiddingRoom()
        ui.setupUi(self)
