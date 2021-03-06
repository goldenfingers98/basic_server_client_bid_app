from socket import NI_NAMEREQD
from time import sleep
from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QDialog
from .ui.ui_BiddingRoom import Ui_BiddingRoom
from lib.client.Client import Client
import threading

class BiddingRoom(QDialog, Ui_BiddingRoom):

    streamData = None
    biddingLock = threading.Lock() # Synchronizing chrono and stream listener

    def __init__(self,asset,current_time):
        QDialog.__init__(self)
        self.setupUi(self)
        # Setting the asset informations
        self.assetId.setText(str(asset['_Asset__ref']))
        self.assetStartingFrom.setText(str(asset['_Asset__starting_price']))
        self.AssetCurrentPrice.setText(str(asset['_Asset__last_price']))
        buyer = asset['_Asset__buyer']
        if buyer is not None:
            buyer = buyer['_Buyer__id']
        self.lastBidder.setText(str(buyer))
        self.timeInput.setText(str(current_time)+' s')
        # Setting decrementor
        self.__decrementor = threading.Thread(target=self.__decrement,name="decrementor")
        self.__decrementor.start()
        # Setting broadcast channel listener
        self.__listener = Client.set_listening_status(True)
        self.__listener_flag = True
        # Setting stream controller
        self.__stream_controller = threading.Thread(target=self.__control_stream,name="stream controller")
        self.__stream_controller.start()


    def __control_stream(self):
        while 1:
            self.__listener.streamLock.acquire() # Getting permission
            if self.__listener_flag:
                BiddingRoom.streamData = self.__listener.stream # Reading current data
                number = BiddingRoom.streamData['current_time']
                # Setting new asset info
                asset = BiddingRoom.streamData['asset']
                buyer_id = BiddingRoom.streamData['buyer_id']
                self.assetId.setText(str(asset['_Asset__ref']))
                self.assetStartingFrom.setText(str(asset['_Asset__starting_price']))
                self.AssetCurrentPrice.setText(str(asset['_Asset__last_price']))
                self.lastProposal.setText(str(asset['_Asset__last_price']))
                self.lastBidder.setText(str(buyer_id))
                # Setting chrono value
                BiddingRoom.biddingLock.acquire() # Getting permission
                print('current : ',number)
                self.timeInput.setText(str(number)+' s') # Critical ressource
                BiddingRoom.biddingLock.release()
            else:
                break

    def __decrement(self):
        while 1:
            # Setting chrono value
            sleep(1)
            BiddingRoom.biddingLock.acquire() # Getting permission
            current_time = int(self.timeInput.text().split(' ')[0]) # Reading from critical ressource
            if current_time > 0:
                self.timeInput.setText(f"{current_time-1} s")
                BiddingRoom.biddingLock.release()
            else:
                BiddingRoom.biddingLock.release()
                self.__listener_flag = False
                Client.set_listening_status(False)
                self.__listener.streamLock.release() # Bidding is finished and we must unleash the stream controller
                break

    def closeEvent(self, arg__1: QCloseEvent) -> None:
        self.__listener_flag = False
        Client.set_listening_status(False)
        self.__listener.streamLock.release()
        return super().closeEvent(arg__1)
    