from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_AssetHistory(object):
    def setupUi(self, AssetHistory):
        if AssetHistory.objectName():
            AssetHistory.setObjectName(u"AssetHistory")
        AssetHistory.resize(700, 530)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AssetHistory.sizePolicy().hasHeightForWidth())
        AssetHistory.setSizePolicy(sizePolicy)
        AssetHistory.setMinimumSize(QSize(700, 530))
        AssetHistory.setMaximumSize(QSize(700, 530))
        self.gridLayout = QGridLayout(AssetHistory)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget = QTableWidget(AssetHistory)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(550, 0))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(120)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_5.addWidget(self.tableWidget)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(17)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.search = QPushButton(AssetHistory)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(11)
        self.search.setFont(font)

        self.horizontalLayout.addWidget(self.search)

        self.idInput = QSpinBox(AssetHistory)
        self.idInput.setObjectName(u"idInput")
        self.idInput.setMinimumSize(QSize(100, 30))
        self.idInput.setFont(font)
        self.idInput.setAcceptDrops(False)
        self.idInput.setFrame(True)
        self.idInput.setReadOnly(False)
        self.idInput.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.idInput.setMaximum(999999999)

        self.horizontalLayout.addWidget(self.idInput)

        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(AssetHistory)

        QMetaObject.connectSlotsByName(AssetHistory)
    # setupUi

    def retranslateUi(self, AssetHistory):
        AssetHistory.setWindowTitle(QCoreApplication.translate("AssetHistory", u"Bid application - Bidding History", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AssetHistory", u"Date & time", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AssetHistory", u"Bidder ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AssetHistory", u"Asset Ref", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AssetHistory", u"Proposition", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AssetHistory", u"Result", None));
        self.search.setText(QCoreApplication.translate("AssetHistory", u"Search", None))
    # retranslateUi

