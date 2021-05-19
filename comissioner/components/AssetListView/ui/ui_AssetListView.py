from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_AssetListView(object):
    def setupUi(self, AssetListView):
        if AssetListView.objectName():
            AssetListView.setObjectName(u"AssetListView")
        AssetListView.resize(780, 500)
        AssetListView.setMinimumSize(QSize(780, 500))
        AssetListView.setMaximumSize(QSize(780, 500))
        self.gridLayout = QGridLayout(AssetListView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.assetTable = QTableWidget(AssetListView)
        if (self.assetTable.columnCount() < 5):
            self.assetTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.assetTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.assetTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.assetTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.assetTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.assetTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.assetTable.setObjectName(u"assetTable")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetTable.sizePolicy().hasHeightForWidth())
        self.assetTable.setSizePolicy(sizePolicy)
        self.assetTable.setMinimumSize(QSize(520, 0))
        self.assetTable.setMaximumSize(QSize(505, 16777215))
        self.assetTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.assetTable.setSortingEnabled(True)

        self.horizontalLayout_5.addWidget(self.assetTable)

        self.line_2 = QFrame(AssetListView)
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
        self.label = QLabel(AssetListView)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.assetRef = QSpinBox(AssetListView)
        self.assetRef.setObjectName(u"assetRef")
        self.assetRef.setMinimumSize(QSize(100, 25))
        self.assetRef.setMaximumSize(QSize(100, 25))
        font1 = QFont()
        font1.setPointSize(11)
        self.assetRef.setFont(font1)
        self.assetRef.setMaximum(999999999)

        self.horizontalLayout_2.addWidget(self.assetRef)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetFixedSize)
        self.label_2 = QLabel(AssetListView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.startingPrice = QDoubleSpinBox(AssetListView)
        self.startingPrice.setObjectName(u"startingPrice")
        self.startingPrice.setMinimumSize(QSize(100, 25))
        self.startingPrice.setMaximumSize(QSize(100, 25))
        self.startingPrice.setFont(font1)
        self.startingPrice.setMaximum(99999999999.000000000000000)

        self.horizontalLayout_4.addWidget(self.startingPrice)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.addBtn = QPushButton(AssetListView)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setMinimumSize(QSize(100, 30))
        self.addBtn.setMaximumSize(QSize(16777215, 30))
        self.addBtn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.addBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.line = QFrame(AssetListView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.searchBtn = QPushButton(AssetListView)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setMinimumSize(QSize(100, 30))
        self.searchBtn.setMaximumSize(QSize(100, 30))
        self.searchBtn.setFont(font1)

        self.horizontalLayout.addWidget(self.searchBtn)

        self.idInput = QSpinBox(AssetListView)
        self.idInput.setObjectName(u"idInput")
        self.idInput.setMinimumSize(QSize(100, 25))
        self.idInput.setMaximumSize(QSize(100, 25))
        self.idInput.setFont(font1)
        self.idInput.setMaximum(999999999)

        self.horizontalLayout.addWidget(self.idInput)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(AssetListView)

        QMetaObject.connectSlotsByName(AssetListView)
    # setupUi

    def retranslateUi(self, AssetListView):
        AssetListView.setWindowTitle(QCoreApplication.translate("AssetListView", u"Bid application - Asset list view", None))
        ___qtablewidgetitem = self.assetTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AssetListView", u"Asset reference", None));
        ___qtablewidgetitem1 = self.assetTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AssetListView", u"Starting price", None));
        ___qtablewidgetitem2 = self.assetTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AssetListView", u"Last price", None));
        ___qtablewidgetitem3 = self.assetTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AssetListView", u"State", None));
        ___qtablewidgetitem4 = self.assetTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AssetListView", u"Buyer", None));
        self.label.setText(QCoreApplication.translate("AssetListView", u"Asset ref", None))
        self.label_2.setText(QCoreApplication.translate("AssetListView", u"Starting price", None))
        self.addBtn.setText(QCoreApplication.translate("AssetListView", u"Add", None))
        self.searchBtn.setText(QCoreApplication.translate("AssetListView", u"Search", None))
    # retranslateUi

