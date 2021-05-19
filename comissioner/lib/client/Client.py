from json.decoder import JSONDecodeError
from os import name
from threading import Thread, Semaphore, Lock
import socket, sys
from json import loads, dumps
from time import sleep


class Client:
    __HAS_SESSION =False
    __is_listening = False
    send_lock = None # To synchronize the semaphore  Send_signal_sem
    Send_signal_sem = None # To synchronize on connexion.send
    Response_signal_sem = None # To synchronize recievers on requests listening
    BroadCast_signal_sem = None # To synchronize recievers on broadcast msgs listening
    EMITTER = None
    RECIEVER = None
    request_to_send = None
    response_to_recieve = None
    broadCast_msg_to_recieve = None
    # temp just for debugging
    number = 0

    @classmethod
    def initialize(cls):
        # Resetting the semaphores and locks
        cls.send_lock = Semaphore(1) # cls.send_lock = ie Lock()
        cls.Send_signal_sem = Semaphore(0)
        cls.Response_signal_sem = Semaphore(0)
        cls.BroadCast_signal_sem = Semaphore(0)
        cls.__HAS_SESSION = False

    @classmethod
    def openSession(cls,host,port):
        cls.initialize()
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
            # print("EMITTER : ",cls.EMITTER.alive)
            if cls.EMITTER.alive:
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
            cls.Response_signal_sem.acquire()
            # print("RECIEVER : ",cls.RECIEVER.alive)
            if cls.RECIEVER.alive:
                response = cls.response_to_recieve
            return response
        except Exception as err:
            pass

    @classmethod
    def __send_then(cls,request):
        # Sending the response
        cls.__send(request)
        print("Sys>>>> request sent : ",request)
        # Wait for response
        var = cls.__wait_for_response()
        print("Sys>>>> response : ",var)
        return var

    @classmethod
    def get(cls,path):
        # sleep(0.5)
        if Client.__HAS_SESSION:
            request = Client.__Request(
                _type="GET",
                path=path,
                args=None
            )
            # Sending the response
            thread = cls.__Response(callable=cls.__send_then,name=f"getter {cls.number}",args=[request])
            cls.number += 1
            thread.start()
            return thread
        else:
            print("Sys>>>> Connot get, server is shutdown")

    @classmethod
    def post(cls,path,*args):
        # sleep(0.5)
        if Client.__HAS_SESSION:
            request = Client.__Request(
                _type="POST",
                path=path,
                args=args
            )
            # Sending the response
            thread = cls.__Response(callable=cls.__send_then,name=f"getter {cls.number}",args=[request])
            cls.number += 1
            thread.start()
        return thread

    @classmethod
    def set_listening_status(cls,isListening):
        cls.__is_listening = isListening
        if isListening:
            thread = cls.__Response(callable=cls.__listen_the_broadcast_channel,name=f"listener {cls.number}")
            cls.number += 1
            thread.start()
            return thread
        else:pass

    @classmethod
    def __listen_the_broadcast_channel(cls):
        while Client.__HAS_SESSION and cls.__is_listening:
            sleep(0.2)
            # Getting permission to read the ressource
            cls.BroadCast_signal_sem.acquire()
            if cls.__is_listening:
                decoded_msg = cls.broadCast_msg_to_recieve # Critical ressource
                cls.__Response.stream = decoded_msg['data']
                cls.__Response.streamLock.release()
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
                        self.stop()
                        print("Sys>>>> Emitter is shutdown")
                        break
                except Exception as err:
                    print("Sys>>>> Server is down!")
                    break

        def stop(self):
            # Releasing the thread before killing'em
            self.alive = False
            # Client.send_lock._value = 10000
            Client.Send_signal_sem.release()
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

        def recv(self):
            received_message = ""
            while 1:
                try:
                    # Recieve 1024 bytes
                    packet = self.connexion.recv(1024).decode("Utf8")
                    # Formatting the recieved bytes
                    packet = packet.replace("'",'"')
                    assert packet != ''
                    # Adding packet to received_message
                    received_message += packet
                    # Loading the json format
                    response = loads(received_message)
                    return response
                except JSONDecodeError:
                    pass

                    

        def run(self):
            print("Sys>>>> Reciever is on..")
            # Listening to the server
            while self.alive:
                try:
                    # Recieve the response
                    response = self.recv()
                    if response['status'] == 255: # The recieved message is a broadcast
                        Client.broadCast_msg_to_recieve = response
                        print('Broadcast msg : ',response)
                        # Releasing the next thread who is expecting a broadcast message
                        Client.BroadCast_signal_sem.release()
                    else: # If the recieved message is a response
                        Client.response_to_recieve = response
                        # Releasing the next thread who is expecting a response
                        Client.Response_signal_sem.release()
                     
                except Exception as err:
                    break
            self.th_E.stop()
            self.stop()
            print("Sys>>>> Reciever is shutdown")
            self.connexion.shutdown(socket.SHUT_RDWR)

        def stop(self):
            # Client.Response_signal_sem._value = 10000
            # Client.BroadCast_signal_sem._value = 10000
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

    class __Response(Thread):
        stream = None
        streamLock = Semaphore(0)
        def __init__(self,callable,args=None,name=None):
            Thread.__init__(self,name=name,args=args)
            self.callable = callable
            self.response = None

        def run(self):
            if self._args is None:
                self.response = self.callable()
            else:
                self.response = self.callable(*self._args)
            

        def then(self,callback):
            self.join()
            callback(self.response)
