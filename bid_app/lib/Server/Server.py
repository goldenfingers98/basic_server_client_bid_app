from logging import error
import socket
import sys
import os
from threading import Thread,Lock
from time import sleep
import json


class Server:
    HOST = ''
    PORT = 0
    POOL_SIZE = 0
    CLIENT_POOL = {}
    GET_PATTERNS = {}
    POST_PATTERNS = {}
    __SOCKET = None
    CURRENT_CONNEXION = None
    MUTEX = Lock()

    @staticmethod
    def initialize(port, host=socket.gethostbyname(socket.gethostname()), pool_size=-1):
        Server.__SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Server.POOL_SIZE = pool_size
        Server.HOST = host
        Server.PORT = port
        try:
            Server.__SOCKET.bind((Server.HOST, Server.PORT))
        except socket.error as err:
            print(">>>> Socket connexion to the port has failed !\nReason : "+str(err))
            sys.exit()
        print(">>>> Server is ready to listen...")
        Server.__SOCKET.listen(Server.POOL_SIZE)

    @staticmethod
    def get(path, callable):
        Server.GET_PATTERNS[path] = callable

    @staticmethod
    def post(path, callable):
        Server.POST_PATTERNS[path] = callable

    @staticmethod
    def run_application():
        while 1:
            sleep(0.05)
            if(len(Server.CLIENT_POOL) < Server.POOL_SIZE):
                (connexion, address) = Server.__SOCKET.accept()
                # New client has come
                client = Server.__Client(connexion, address)
                # Reserving a place in the pool
                Server.CLIENT_POOL[client.getName()] = connexion
                client.start()
                # print(f">>>> {str(client)}")
                connexion.send(
                    "SERVER >>>>: You are connected. Ready to listen...".encode('Utf8'))

    @staticmethod
    def send(message):
        assert type(message) == type(dict())
        Server.CURRENT_CONNEXION.send(json.dumps(message).encode())

    class __Client(Thread):
        """
            Thread object for each client
        """

        def __init__(self, conn, address):
            Thread.__init__(self)
            self.connexion = conn
            self.isConnected = False
            self.address = address

        def recieve(self):
            request = self.connexion.recv(1024).decode("Utf8")
            try:
                serialized_request = json.loads(request)
                return serialized_request
            except:
                self.__sendERROR("Unsupported request format.")
                raise Exception("Unsupported format")

        def __sendERROR(self, message):
            self.connexion.send(f'SERVER error >>>> {message}'.encode())

        def __send(self, message):
            assert type(message) == type(dict())
            self.connexion.send(json.dumps(message).encode())

        def settingResponse(self):
            # Synchronization
            Server.MUTEX.acquire()
            Server.CURRENT_CONNEXION = self.connexion  # Cretical ressource
            Server.MUTEX.release()

        def run(self):
            # Client status : connected
            self.isConnected = True
            name = self.getName()  # Each client has a specific name
            # Listening requests from client
            while 1:
                try:
                    request = self.recieve()
                    if request["type"] == "GET":
                        if request["path"] in Server.GET_PATTERNS:
                            args = request["args"]
                            # Sending response setting
                            self.settingResponse()
                            # Executing callable
                            Server.GET_PATTERNS[request["path"]](*args)
                        else:
                            self.__sendERROR("path not defined.")
                    elif request["type"] == "POST":
                        if request["path"] in Server.POST_PATTERNS:
                            args = request["args"]
                            # Sending response setting
                            self.settingResponse()
                            # Executing callable
                            Server.GET_PATTERNS[request["path"]](*args)
                        else:
                            self.__sendERROR("path not defined.")
                    else:
                        self.__sendERROR("request type not defined")
                except Exception as err:
                    print(err)
                    break
                if not request or request['type'] == "EXIT":
                    break

                # message = f"{name} >>>> {request}"
                # print(message)
                # #Broadcast the message to the others
                # for key in Server.CLIENT_POOL:
                #     if key != name:
                #         Server.CLIENT_POOL[key].send(message.encode('Utf8'))

            # Closing the connexion
            try:
                self.connexion.close()
                self.isConnected = False
            except:
                pass
            # The client leaves the pool
            del Server.CLIENT_POOL[name]
            print(f">>>> Client {name} disconnected !")

        def __str__(self):
            if self.isConnected:
                return f"Client {self.getName()} is connected at port {Server.PORT} with address {self.address}."
