# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BillViewLmQxAa.ui'
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


class Ui_BillView(object):
    def setupUi(self, BillView):
        if BillView.objectName():
            BillView.setObjectName(u"BillView")
        BillView.resize(650, 450)
        BillView.setMaximumSize(QSize(650, 450))
        self.gridLayout = QGridLayout(BillView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(BillView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.payBtn = QPushButton(BillView)
        self.payBtn.setObjectName(u"payBtn")
        self.payBtn.setMinimumSize(QSize(100, 50))
        font = QFont()
        font.setPointSize(11)
        self.payBtn.setFont(font)

        self.horizontalLayout.addWidget(self.payBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.groupBox = QGroupBox(BillView)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 350))
        font1 = QFont()
        font1.setPointSize(12)
        self.groupBox.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.id = QLabel(self.groupBox)
        self.id.setObjectName(u"id")
        self.id.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.id)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.beforeTax = QLabel(self.groupBox)
        self.beforeTax.setObjectName(u"beforeTax")
        self.beforeTax.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.beforeTax)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.afterTax = QLabel(self.groupBox)
        self.afterTax.setObjectName(u"afterTax")
        self.afterTax.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.afterTax)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(BillView)

        QMetaObject.connectSlotsByName(BillView)
    # setupUi

    def retranslateUi(self, BillView):
        BillView.setWindowTitle(QCoreApplication.translate("BillView", u"Bid application - Bill View", None))
        self.payBtn.setText(QCoreApplication.translate("BillView", u"Pay", None))
        self.groupBox.setTitle(QCoreApplication.translate("BillView", u"Bill ", None))
        self.label.setText(QCoreApplication.translate("BillView", u"ID", None))
        self.id.setText(QCoreApplication.translate("BillView", u"0", None))
        self.label_2.setText(QCoreApplication.translate("BillView", u"Ammount", None))
        self.beforeTax.setText(QCoreApplication.translate("BillView", u"0", None))
        self.label_3.setText(QCoreApplication.translate("BillView", u"Charges", None))
        self.label_4.setText(QCoreApplication.translate("BillView", u"20%", None))
        self.label_5.setText(QCoreApplication.translate("BillView", u"All tax included", None))
        self.afterTax.setText(QCoreApplication.translate("BillView", u"0", None))
    # retranslateUi

