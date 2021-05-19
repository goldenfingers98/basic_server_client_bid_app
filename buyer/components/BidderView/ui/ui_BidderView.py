from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_BidderView(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 445)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 105, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 0, 3, 3, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 105, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(94, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.biddingRoomBtn = QPushButton(self.centralwidget)
        self.biddingRoomBtn.setObjectName(u"biddingRoomBtn")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.biddingRoomBtn.sizePolicy().hasHeightForWidth())
        self.biddingRoomBtn.setSizePolicy(sizePolicy)
        self.biddingRoomBtn.setMinimumSize(QSize(200, 200))
        font = QFont()
        font.setPointSize(14)
        self.biddingRoomBtn.setFont(font)

        self.gridLayout_3.addWidget(self.biddingRoomBtn, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(94, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(94, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.billViewBtn = QPushButton(self.centralwidget)
        self.billViewBtn.setObjectName(u"billViewBtn")
        sizePolicy.setHeightForWidth(self.billViewBtn.sizePolicy().hasHeightForWidth())
        self.billViewBtn.setSizePolicy(sizePolicy)
        self.billViewBtn.setMinimumSize(QSize(200, 200))
        self.billViewBtn.setFont(font)

        self.gridLayout_3.addWidget(self.billViewBtn, 1, 5, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(94, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 6, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 104, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 104, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 2, 5, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bid application - Bidder View", None))
        self.biddingRoomBtn.setText(QCoreApplication.translate("MainWindow", u"Bidding Room", None))
        self.billViewBtn.setText(QCoreApplication.translate("MainWindow", u"Bill View", None))
    # retranslateUi
