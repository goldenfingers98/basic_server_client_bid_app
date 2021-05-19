from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_AssetDetails(object):
    def setupUi(self, AssetDetails):
        if AssetDetails.objectName():
            AssetDetails.setObjectName(u"AssetDetails")
        AssetDetails.resize(500, 415)
        AssetDetails.setMinimumSize(QSize(500, 415))
        AssetDetails.setMaximumSize(QSize(500, 415))
        self.gridLayout_2 = QGridLayout(AssetDetails)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(AssetDetails)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.ref = QLabel(self.groupBox)
        self.ref.setObjectName(u"ref")
        self.ref.setFont(font)

        self.horizontalLayout.addWidget(self.ref)

        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.startingPrice = QLabel(self.groupBox)
        self.startingPrice.setObjectName(u"startingPrice")
        self.startingPrice.setFont(font)

        self.horizontalLayout_7.addWidget(self.startingPrice)

        self.horizontalSpacer_4 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_15)

        self.lastPrice = QLabel(self.groupBox)
        self.lastPrice.setObjectName(u"lastPrice")
        self.lastPrice.setFont(font)

        self.horizontalLayout_8.addWidget(self.lastPrice)

        self.horizontalSpacer_6 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_7 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_17)

        self.state = QLabel(self.groupBox)
        self.state.setObjectName(u"state")
        self.state.setFont(font)

        self.horizontalLayout_9.addWidget(self.state)

        self.horizontalSpacer_8 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.gridLayout.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_9 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_19)

        self.owner = QLabel(self.groupBox)
        self.owner.setObjectName(u"owner")
        self.owner.setFont(font)

        self.horizontalLayout_10.addWidget(self.owner)

        self.horizontalSpacer_10 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.gridLayout.addLayout(self.horizontalLayout_10, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(AssetDetails)

        QMetaObject.connectSlotsByName(AssetDetails)
    # setupUi

    def retranslateUi(self, AssetDetails):
        AssetDetails.setWindowTitle(QCoreApplication.translate("AssetDetails", u"Bid application - Asset details", None))
        self.groupBox.setTitle(QCoreApplication.translate("AssetDetails", u"Asset data", None))
        self.label.setText(QCoreApplication.translate("AssetDetails", u"Asset Ref", None))
        self.ref.setText(QCoreApplication.translate("AssetDetails", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("AssetDetails", u"Starting price", None))
        self.startingPrice.setText(QCoreApplication.translate("AssetDetails", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("AssetDetails", u"Last price", None))
        self.lastPrice.setText(QCoreApplication.translate("AssetDetails", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("AssetDetails", u"State", None))
        self.state.setText(QCoreApplication.translate("AssetDetails", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("AssetDetails", u"Owner", None))
        self.owner.setText(QCoreApplication.translate("AssetDetails", u"TextLabel", None))
    # retranslateUi

