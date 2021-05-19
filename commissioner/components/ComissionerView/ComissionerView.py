from PySide2.QtWidgets import QMainWindow
from .ui.ui_comissionerView import Ui_ComissionerView
from components.BiddingRoom.BiddingRoom import BiddingRoom

class ComissionerView(QMainWindow, Ui_ComissionerView):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # 
        self.__connect_signals_to_slots()
        # 
        self.show()


    def __connect_signals_to_slots(self):
        self.biddingRoom.clicked.connect(self.__open_biddingRoom)


    def __open_biddingRoom(self):
        biddingRoom = BiddingRoom()
        biddingRoom.show()
        biddingRoom.exec_()
    