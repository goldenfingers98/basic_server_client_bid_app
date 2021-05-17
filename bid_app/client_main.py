import sys ,time
from lib.client.Client import Client
import socket

HOST = socket.gethostbyname(socket.gethostname())
res = None

def callback(res):
    print(res['data'])

Client.openSession(HOST,3000)
Client.set_listening_status(True)
Client.get('/log',callback)
Client.post('/postTest',callback,"Hello world")
Client.killSession()