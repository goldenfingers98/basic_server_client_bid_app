from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_BiddingRoom(object):
    def setupUi(self, BiddingRoom):
        if BiddingRoom.objectName():
            BiddingRoom.setObjectName(u"BiddingRoom")
        BiddingRoom.resize(750, 450)
        BiddingRoom.setMinimumSize(QSize(750, 450))
        BiddingRoom.setMaximumSize(QSize(750, 450))
        self.gridLayout_3 = QGridLayout(BiddingRoom)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line = QFrame(BiddingRoom)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 2)

        self.groupBox = QGroupBox(BiddingRoom)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(250, 0))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.assetId = QLabel(self.groupBox)
        self.assetId.setObjectName(u"assetId")
        self.assetId.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.assetId)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(250, 0))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.assetStartingFrom = QLabel(self.groupBox)
        self.assetStartingFrom.setObjectName(u"assetStartingFrom")
        self.assetStartingFrom.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.assetStartingFrom)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(250, 0))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.AssetCurrentPrice = QLabel(self.groupBox)
        self.AssetCurrentPrice.setObjectName(u"AssetCurrentPrice")
        self.AssetCurrentPrice.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.AssetCurrentPrice)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 496, 271))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 25))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 25))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_8)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lastBidder = QLabel(self.scrollAreaWidgetContents)
        self.lastBidder.setObjectName(u"lastBidder")
        self.lastBidder.setMaximumSize(QSize(16777215, 25))
        self.lastBidder.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lastBidder)

        self.lastProposal = QLabel(self.scrollAreaWidgetContents)
        self.lastProposal.setObjectName(u"lastProposal")
        self.lastProposal.setMaximumSize(QSize(16777215, 25))
        self.lastProposal.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lastProposal)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.timeInput = QLabel(self.groupBox)
        self.timeInput.setObjectName(u"timeInput")
        self.timeInput.setFont(font1)

        self.gridLayout_2.addWidget(self.timeInput, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 2)


        self.retranslateUi(BiddingRoom)

        QMetaObject.connectSlotsByName(BiddingRoom)
    # setupUi

    def retranslateUi(self, BiddingRoom):
        BiddingRoom.setWindowTitle(QCoreApplication.translate("BiddingRoom", u"Bid application - Bidding Room", None))
        self.groupBox.setTitle(QCoreApplication.translate("BiddingRoom", u"Asset info", None))
        self.label_3.setText(QCoreApplication.translate("BiddingRoom", u"Asset ID", None))
        self.assetId.setText(QCoreApplication.translate("BiddingRoom", u"0", None))
        self.label_4.setText(QCoreApplication.translate("BiddingRoom", u"Starting from", None))
        self.assetStartingFrom.setText(QCoreApplication.translate("BiddingRoom", u"0", None))
        self.label_5.setText(QCoreApplication.translate("BiddingRoom", u"Current price", None))
        self.AssetCurrentPrice.setText(QCoreApplication.translate("BiddingRoom", u"0", None))
        self.label_6.setText(QCoreApplication.translate("BiddingRoom", u"Last bid", None))
        self.label_7.setText(QCoreApplication.translate("BiddingRoom", u"Bidder id", None))
        self.label_8.setText(QCoreApplication.translate("BiddingRoom", u"Proposal", None))
        self.lastBidder.setText(QCoreApplication.translate("BiddingRoom", u"None", None))
        self.lastProposal.setText(QCoreApplication.translate("BiddingRoom", u"0", None))
        self.label.setText(QCoreApplication.translate("BiddingRoom", u"Time remaininig:", None))
        self.timeInput.setText(QCoreApplication.translate("BiddingRoom", u"30 s", None))
    # retranslateUi

