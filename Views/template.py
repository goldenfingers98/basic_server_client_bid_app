import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from ui_Bidder_View import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
#
if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
