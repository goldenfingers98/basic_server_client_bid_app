from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_ComissionerView(object):
    def setupUi(self, ComissionerView):
        if ComissionerView.objectName():
            ComissionerView.setObjectName(u"ComissionerView")
        ComissionerView.resize(697, 508)
        self.centralwidget = QWidget(ComissionerView)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(7, 50, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.assetListView = QPushButton(self.centralwidget)
        self.assetListView.setObjectName(u"assetListView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetListView.sizePolicy().hasHeightForWidth())
        self.assetListView.setSizePolicy(sizePolicy)
        self.assetListView.setMinimumSize(QSize(150, 150))
        font = QFont()
        font.setPointSize(12)
        self.assetListView.setFont(font)

        self.horizontalLayout.addWidget(self.assetListView)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.AssetsHistory = QPushButton(self.centralwidget)
        self.AssetsHistory.setObjectName(u"AssetsHistory")
        sizePolicy.setHeightForWidth(self.AssetsHistory.sizePolicy().hasHeightForWidth())
        self.AssetsHistory.setSizePolicy(sizePolicy)
        self.AssetsHistory.setMinimumSize(QSize(150, 150))
        self.AssetsHistory.setFont(font)

        self.horizontalLayout.addWidget(self.AssetsHistory)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.buyersBillView = QPushButton(self.centralwidget)
        self.buyersBillView.setObjectName(u"buyersBillView")
        sizePolicy.setHeightForWidth(self.buyersBillView.sizePolicy().hasHeightForWidth())
        self.buyersBillView.setSizePolicy(sizePolicy)
        self.buyersBillView.setMinimumSize(QSize(150, 150))
        self.buyersBillView.setFont(font)

        self.horizontalLayout.addWidget(self.buyersBillView)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.biddingRoom = QPushButton(self.centralwidget)
        self.biddingRoom.setObjectName(u"biddingRoom")
        sizePolicy.setHeightForWidth(self.biddingRoom.sizePolicy().hasHeightForWidth())
        self.biddingRoom.setSizePolicy(sizePolicy)
        self.biddingRoom.setMinimumSize(QSize(150, 150))
        self.biddingRoom.setFont(font)

        self.horizontalLayout.addWidget(self.biddingRoom)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(7, 50, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        ComissionerView.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ComissionerView)
        self.statusbar.setObjectName(u"statusbar")
        ComissionerView.setStatusBar(self.statusbar)

        self.retranslateUi(ComissionerView)

        QMetaObject.connectSlotsByName(ComissionerView)
    # setupUi

    def retranslateUi(self, ComissionerView):
        ComissionerView.setWindowTitle(QCoreApplication.translate("ComissionerView", u"Bid application - Comissione View", None))
        self.assetListView.setText(QCoreApplication.translate("ComissionerView", u"AssetListView", None))
        self.AssetsHistory.setText(QCoreApplication.translate("ComissionerView", u"AssetsHistory", None))
        self.buyersBillView.setText(QCoreApplication.translate("ComissionerView", u"BuyersBillView", None))
        self.biddingRoom.setText(QCoreApplication.translate("ComissionerView", u"BiddingRoom", None))
    # retranslateUi

