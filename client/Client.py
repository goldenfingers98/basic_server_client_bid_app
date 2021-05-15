import socket, sys, os
from threading import Thread
from dotenv import dotenv_values


# Changing current directory
os.chdir(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]))

# initializing host and port
CONFIG = dotenv_values('./.env')
HOST =  CONFIG["HOST"]
PORT = int(CONFIG["PORT"])

class ThreadReception(Thread):
    """
        Thread object that receives messages
    """
    def __init__(self,conn,emissionThread):
        Thread.__init__(self)
        self.connexion = conn
        self.th_E = emissionThread

    def run(self):
        while 1:
            received_message = ""
            try:
                received_message = self.connexion.recv(1024)\
                                        .decode("Utf8")
            except:
                break
            print(f"{received_message}")
            if received_message.upper() == "END":
                break
        self.th_E.stop()
        print("\n>>>> Client is stoped. Interrupted connexion")
        self.connexion.close()

class ThreadEmission(Thread):
    """
        Thread object that sends messages
    """
    def __init__(self,conn):
        Thread.__init__(self)
        self.connexion = conn
        self.alive = True

    def run(self):
        while self.alive:
            try:
                messageToSend = input("Sys>>>> Message to send: ")
                self.connexion.send(messageToSend.encode("Utf8"))
            except:
                print("Sys>>>> Server is down!")
                break

    def stop(self):
        self.alive = False

######################################################################
##########################__Main program__############################
######################################################################

if __name__ == "__main__":
    connexion = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        connexion.connect((HOST,PORT))
    except socket.error:
        print(">>>> Connexion failed !")
        sys.exit()
    else:
        print(">>>> Connected to the server !")
    
    th_E = ThreadEmission(connexion)
    th_R = ThreadReception(connexion,th_E)
    th_R.start()
    th_E.start()

    #{"type":"GET","path":"/log","args":["Hello"]}