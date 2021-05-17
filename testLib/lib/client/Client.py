from lib.server.Server import Server
from threading import Thread, Semaphore, Lock
import socket, sys
from json import loads, dumps
from time import sleep


class Client:
    __HAS_SESSION =False
    __is_listening = False
    send_lock = Lock() # To synchronize the semaphore  Send_signal_sem
    Send_signal_sem = Semaphore(0) # To synchronize on connexion.send
    Request_signal_sem = Semaphore(0) # To synchronize recievers on requests listening
    BroadCast_signal_sem = Semaphore(0) # To synchronize recievers on broadcast msgs listening
    EMITTER = None
    RECIEVER = None
    request_to_send = None
    response_to_recieve = None
    broadCast_msg_to_recieve = None

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
            cls.Send_signal_sem.release() # Critical ressource
        except Exception as err:
            pass
        # finally:
        #     cls.send_lock.release()

    @classmethod
    def __wait_for_response(cls):
        response = None
        try:
            cls.Request_signal_sem.acquire()
            response = cls.response_to_recieve
            return response
        except Exception as err:
            pass

    @classmethod
    def __send_then(cls,request,callback):
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
    def post(cls,path,callback,*args):
        # sleep(0.5)
        if Client.__HAS_SESSION:
            request = Client.__Request(
                _type="POST",
                path=path,
                args=args
            )
        # Sending the response and executing callback
        thread = Thread(target=cls.__send_then,args=[request,callback])
        thread.start()

    @classmethod
    def set_listening_status(cls,isListening):
        cls.__is_listening = isListening
        if isListening:
            thread = Thread(target=cls.__listen_the_broadcast_channel)
            thread.start()
        else:pass

    @classmethod
    def __listen_the_broadcast_channel(cls):
        while Client.__HAS_SESSION and cls.__is_listening:
            # Getting permission to read the ressource
            cls.BroadCast_signal_sem.acquire()
            if cls.__is_listening:
                decoded_msg = cls.broadCast_msg_to_recieve # Critical ressource
                print(decoded_msg['message'])
            else: # The Client isn't listening anymore
                break

    @classmethod
    def killSession(cls):
        # Giving a rest
        sleep(1)
        # Killing the threads
        cls.EMITTER.stop()
        cls.RECIEVER.stop()
        # Killing the broadcast channel listener
        cls.__is_listening = False
        cls.BroadCast_signal_sem.release()
        # Resetting the semaphores and locks
        cls.send_lock = Lock() 
        cls.Send_signal_sem = Semaphore(0)
        cls.Request_signal_sem = Semaphore(0)
        cls.BroadCast_signal_sem = Semaphore(0)
        cls.__HAS_SESSION = False
        print("Sys>>>> Client is shutdown.")
        

    class __Emitter(Thread):
        """
        Thread object that sends messages
        """
        def __init__(self,conn):
            Thread.__init__(self)
            print("Sys>>>> initializing the emitter.")
            self.connexion = conn
            self.alive = True

        def run(self):
            print("Sys>>>> Emitter is on..")
            while 1:
                try:
                    # Getting permission from Client class to send, ie, the appropiate message is ready
                    # Or the Reciever is blocked and cannot exit
                    Client.Send_signal_sem.acquire()
                    if self.alive: # Still alive and sending
                        self.connexion.send(Client.request_to_send)
                        # Take a rest
                        sleep(0.5)
                        # Release the next blocked emitter thread
                        Client.send_lock.release()
                    else: # Shutdown state
                        print("Sys>>>> Emitter is shutdown")
                        break
                except Exception as err:
                    print("Sys>>>> Server is down!")
                    break

        def stop(self):
            # Releasing the thread before killing'em
            Client.Send_signal_sem.release()
            self.alive = False
            # Closing the connexion even if the reciever is blocked on recieving
            self.connexion.shutdown(socket.SHUT_RDWR)

    class __Reciever(Thread):
        """
            Thread object that receives messages
        """
        def __init__(self,conn,emissionThread):
            print("Sys>>>> initializing the reciever.")
            Thread.__init__(self)
            self.connexion = conn
            self.th_E = emissionThread
            self.alive = True

        def run(self):
            print("Sys>>>> Reciever is on..")
            # Listening to the server
            while self.alive:
                received_message = ""
                try:
                    # Recieve the bytes
                    received_message = self.connexion.recv(1024).decode("Utf8")
                    # Formatting the recieved bytes
                    received_message = received_message.replace("'",'"')
                    assert received_message != ''
                    # Loading the json format
                    response = loads(received_message)
                    # If the recieved message is a response, ie code 200
                    if response['status'] == 200: 
                        Client.response_to_recieve = response
                        # Releasing the next thread who is expecting a response
                        Client.Request_signal_sem.release()
                    else: # The recieved message is a broadcast
                        Client.broadCast_msg_to_recieve = response
                        # Releasing the next thread who is expecting a broadcast message
                        Client.BroadCast_signal_sem.release()
                except Exception as err:
                    break
                if received_message.upper() == "END":
                    break
            self.th_E.stop()
            self.stop()
            print("Sys>>>> Reciever is shutdown")
            self.connexion.shutdown(socket.SHUT_RDWR)

        def stop(self):
            self.alive = False

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
