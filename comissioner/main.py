from PySide2.QtWidgets import QApplication
from components.ComissionerView.ComissionerView import ComissionerView
import sys
from lib.client.Client import Client
from dotenv import dotenv_values


# initializing host and port
CONFIG = dotenv_values('./.env')
HOST =  CONFIG["HOST"]
PORT = int(CONFIG["PORT"])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Open a session
    Client.openSession(HOST,PORT)
    # Start the application
    comissionerView = ComissionerView()
    app.exec_()
    # Quit the session
    Client.killSession()