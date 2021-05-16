from lib.server.Server import Server
from threading import Thread, Semaphore, Lock
import socket, sys
from json import loads, dumps
from time import sleep


class Client:
    __HAS_SESSION =False
    send_lock = Lock() # To synchronize the semaphore  Send_signal_sem
    # recieve_lock = Lock() # To synchronize the semaphore Recieve_signal_sem
    Send_signal_sem = Semaphore(0)
    Recieve_signal_sem = Semaphore(0)
    BroadCast_signal_sem = Semaphore(0)
    EMITTER = None
    RECIEVER = None
    request_to_send = None
    response_to_recieve = None
    BroadCast_response = None

    @classmethod
    def openSession(cls,host,port):
        connexion = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            connexion.connect((host,port))
        except socket.error:
            sys.exit()
        except Exception as err:
            pass
        cls.EMITTER = cls.__Emitter(connexion)
        cls.RECIEVER = cls.__Reciever(connexion,cls.EMITTER)
        cls.RECIEVER.start()
        cls.EMITTER.start()
        cls.__HAS_SESSION = True
        

    @classmethod
    def __send(cls,request):
        formatted_request = dumps(request).encode()
        try:
            cls.send_lock.acquire()
            cls.request_to_send = formatted_request
            cls.Send_signal_sem.release() # Cretical ressource
        except Exception as err:
            pass
        # finally:
        #     cls.send_lock.release()

    @classmethod
    def __wait_for_response(cls):
        response = None
        try:
            cls.Recieve_signal_sem.acquire()
            response = cls.response_to_recieve
            return response
        except Exception as err:
            pass


    @classmethod
    def __send_then(cls,request,callback,*args):
        # Sending the response
        cls.__send(request)
        # Wait for response
        var = cls.__wait_for_response()
        # Executing callback
        callback(var)

    @classmethod
    def get(cls,path,callback):
        # sleep(0.5)
        if Client.__HAS_SESSION:
            request = Client.__Request(
                _type="GET",
                path=path,
                args=None
            )
            # Sending the response and executing callback
            thread = Thread(target=cls.__send_then,args=[request,callback])
            thread.start()

    @classmethod
    def post(cls,path,request_args,callback,*args):
        # sleep(0.5)
        if Client.__HAS_SESSION:
            request = Client.__Request(
                _type="POST",
                path=path,
                args=request_args
            )
        # Sending the response and executing callback
        thread = Thread(target=cls.__send_then,args=[request,callback,args])
        thread.start()

    @classmethod
    def killSession(cls):
        cls.EMITTER.stop()
        cls.RECIEVER.stop()
        sys.exit()

    class __Emitter(Thread):
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
                    Client.Send_signal_sem.acquire()
                    # sleep(0.5)
                    self.connexion.send(Client.request_to_send)
                    Client.send_lock.release()
                except Exception as err:
                    print("Sys>>>> Server is down!")
                    break

        def stop(self):
            raise Exception("Quited")

    class __Reciever(Thread):
        """
            Thread object that receives messages
        """
        def __init__(self,conn,emissionThread):
            Thread.__init__(self)
            self.connexion = conn
            self.th_E = emissionThread
            self.alive = True

        def run(self):
            while self.isAlive():
                received_message = ""
                try:
                    # sleep(0.5)
                    received_message = self.connexion.recv(1024).decode("Utf8")
                    received_message = received_message.replace("'",'"')
                    if received_message != '':
                        response = loads(received_message)
                        if response['status'] == 200:
                            Client.response_to_recieve = response
                            Client.Recieve_signal_sem.release()
                        else:
                            Client.BroadCast_response = response
                            Client.BroadCast_signal_sem.release()
                except Exception as err:
                    break
                print(f"{received_message}")
                if received_message.upper() == "END":
                    break
            self.th_E.stop()
            print("\n>>>> Client is stoped. Interrupted connexion")
            self.connexion.close()

        def stop(self):
            raise Exception("Quited")

    class __Request(dict):
        def __init__(self,_type,path,args):
            super().__init__()
            self["type"] = _type
            self["path"] = path
            self["args"] = args

    # class __Response(dict):
    #     def __init__(self,status,data):
    #         super().__init__()
    #         self['status'] = status
    #         self['data'] = data
