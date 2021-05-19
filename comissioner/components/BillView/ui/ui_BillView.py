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
        BillView.resize(800, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BillView.sizePolicy().hasHeightForWidth())
        BillView.setSizePolicy(sizePolicy)
        BillView.setMinimumSize(QSize(800, 500))
        BillView.setMaximumSize(QSize(800, 500))
        self.gridLayout = QGridLayout(BillView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget = QTableWidget(BillView)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(550, 0))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(160)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_5.addWidget(self.tableWidget)

        self.line_2 = QFrame(BillView)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(14)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.label = QLabel(BillView)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.bidderId = QSpinBox(BillView)
        self.bidderId.setObjectName(u"bidderId")
        self.bidderId.setMinimumSize(QSize(100, 25))
        self.bidderId.setMaximumSize(QSize(100, 25))
        font1 = QFont()
        font1.setPointSize(11)
        self.bidderId.setFont(font1)
        self.bidderId.setMaximum(999999999)

        self.horizontalLayout_2.addWidget(self.bidderId)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.addBtn = QPushButton(BillView)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setMinimumSize(QSize(100, 30))
        self.addBtn.setMaximumSize(QSize(16777215, 30))
        self.addBtn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.addBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(17)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.search = QPushButton(BillView)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(0, 30))
        self.search.setFont(font1)

        self.horizontalLayout.addWidget(self.search)

        self.idInput = QSpinBox(BillView)
        self.idInput.setObjectName(u"idInput")
        self.idInput.setMinimumSize(QSize(100, 30))
        self.idInput.setFont(font1)
        self.idInput.setAcceptDrops(False)
        self.idInput.setFrame(True)
        self.idInput.setReadOnly(False)
        self.idInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.idInput.setMaximum(999999999)

        self.horizontalLayout.addWidget(self.idInput)

        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(BillView)

        QMetaObject.connectSlotsByName(BillView)
    # setupUi

    def retranslateUi(self, BillView):
        BillView.setWindowTitle(QCoreApplication.translate("BillView", u"Bid application - Bill View", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("BillView", u"Bidder ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("BillView", u"Ammount free of charges", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("BillView", u"Full ammount", None));
        self.label.setText(QCoreApplication.translate("BillView", u"Bidder ID", None))
        self.addBtn.setText(QCoreApplication.translate("BillView", u"Add", None))
        self.search.setText(QCoreApplication.translate("BillView", u"Search", None))
    # retranslateUi

