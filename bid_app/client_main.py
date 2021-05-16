from sys import path
import sys
from lib.client.Client import Client
import socket

HOST = socket.gethostbyname(socket.gethostname())
res = None

def callback(res):
    print(res['data'])

Client.openSession(HOST,3000)
Client.get('/log',callback)
Client.post('/postTest',["Hello world"],callback,res)
Client.killSession()