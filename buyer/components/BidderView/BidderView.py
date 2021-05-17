from PySide2.QtWidgets import  QMainWindow
from .ui.ui_BidderView import Ui_BidderView
from components.BiddingRoom.BiddingRoom import BiddingRoom

class BidderView(QMainWindow, Ui_BidderView):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # Connecting signals to slots
        self.__connect_signals_to_slots()

        #########################
        self.show()


    def __connect_signals_to_slots(self):
        self.biddingRoomBtn.clicked.connect(self.__openBiddingRoom)

    def __openBiddingRoom(self):
        biddingWindow = BiddingRoom()
        self.setDisabled(True)
        biddingWindow.show()
        biddingWindow.exec_()
        self.setDisabled(False)
