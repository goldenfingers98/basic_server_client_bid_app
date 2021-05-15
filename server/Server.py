from logging import error
import socket, sys, os
from threading import Thread
from dotenv import dotenv_values
from time import sleep


# Changing current directory
os.chdir(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]))

CONFIG = dotenv_values('.env')
HOST = socket.gethostbyname(socket.gethostname())
PORT = int(CONFIG["PORT"])
POOL_SIZE = int(CONFIG["POOL_SIZE"])
CLIENT_POOL = {} #Client set

class ThreadingClient(Thread):
    """
        Thread object for each client
    """
    def __init__(self,conn,address):
        Thread.__init__(self)
        self.connexion = conn
        self.isConnected = False
        self.address = address

    def run(self):
        # Client status : connected
        self.isConnected = True
        #Listening requests from client
        name = self.getName() #Each client has a specific name
        while 1:
            try:
                msgClient = self.connexion.recv(1024)\
                                .decode("Utf8")
            except:
                break
            if not msgClient or msgClient.upper() == "END":
                break
            message = f"{name} >>>> {msgClient}"
            print(message)
            #Broadcast the message to the others
            for key in CLIENT_POOL:
                if key != name:
                    CLIENT_POOL[key].send(message.encode('Utf8'))
            
        #Closing the connexion
        try:
            self.connexion.close()
            self.isConnected = False
        except:pass
        #The client leaves the pool
        del CLIENT_POOL[name]
        print(f">>>> Client {name} disconnected !")

    
    def __str__(self):
        if self.isConnected:
            return f"Client {self.getName()} is connected at port {PORT} with address {self.address}."

######################################################################
##########################__Main program__############################
######################################################################
if __name__ == "__main__":
    # Server initialisation
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        _socket.bind((HOST,PORT))
    except socket.error:
        print(">>>> Socket connexion to the port has failed !")
        sys.exit()
    print(">>>> Server is ready to listen...")
    _socket.listen(POOL_SIZE)

    #Waiting for clients
    while 1:
        sleep(0.05)
        if(len(CLIENT_POOL) < POOL_SIZE):
            (connexion, address) = _socket.accept()
            # New client has come
            client = ThreadingClient(connexion,address)
            # Reserving a place in the pool
            CLIENT_POOL[client.getName()] = connexion
            client.start()
            print(f">>>> {client}")
            connexion.send("SERVER >>>>: You are connected. Ready to listen...".encode('Utf8'))
