import socket
import os
from _thread import *
ServerSocket = socket.socket()
host = '10.0.0.13'
port = 8080
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error:
    print(str(error))
print('Waiting for a Connection..')
ServerSocket.listen(5)
sen = "0"
def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server'))
    while True:
        global sen
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        if(data.decode('utf-8')[:2] == "pi"):
           sen = data.decode('utf-8')[3:]
        connection.send(str.encode(str(sen)))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
