# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BillDetailsRNCgNj.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_BillDetails(object):
    def setupUi(self, BillDetails):
        if BillDetails.objectName():
            BillDetails.setObjectName(u"BillDetails")
        BillDetails.resize(500, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BillDetails.sizePolicy().hasHeightForWidth())
        BillDetails.setSizePolicy(sizePolicy)
        BillDetails.setMinimumSize(QSize(500, 400))
        BillDetails.setMaximumSize(QSize(500, 400))
        self.gridLayout = QGridLayout(BillDetails)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(BillDetails)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
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

        self.id = QLabel(self.groupBox)
        self.id.setObjectName(u"id")
        self.id.setFont(font)

        self.horizontalLayout.addWidget(self.id)

        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.foc = QLabel(self.groupBox)
        self.foc.setObjectName(u"foc")
        self.foc.setFont(font)

        self.horizontalLayout_7.addWidget(self.foc)

        self.horizontalSpacer_4 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_15)

        self.ac = QLabel(self.groupBox)
        self.ac.setObjectName(u"ac")
        self.ac.setFont(font)

        self.horizontalLayout_8.addWidget(self.ac)

        self.horizontalSpacer_6 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(BillDetails)

        QMetaObject.connectSlotsByName(BillDetails)
    # setupUi

    def retranslateUi(self, BillDetails):
        BillDetails.setWindowTitle(QCoreApplication.translate("BillDetails", u"Bill application - Bidder bill details", None))
        self.groupBox.setTitle(QCoreApplication.translate("BillDetails", u"Bidder's bill data", None))
        self.label.setText(QCoreApplication.translate("BillDetails", u"Bidder ID", None))
        self.id.setText(QCoreApplication.translate("BillDetails", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("BillDetails", u"Ammount FOC", None))
        self.foc.setText(QCoreApplication.translate("BillDetails", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("BillDetails", u"Ammount AC", None))
        self.ac.setText(QCoreApplication.translate("BillDetails", u"TextLabel", None))
    # retranslateUi

