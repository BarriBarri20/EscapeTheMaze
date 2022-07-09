import socket
from _thread import *
import sys



"""Enter here your local IPv4 address"""
server = ""
port = 3333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((server, port))

except socket.error as e:
    str(e)

s.listen(2)
print('Waiting for connection, Server Started !')

def threaded_client(conn):
    conn.send(str.encode("connected to "))
    reply = ''
    while True: 
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data: 
                print("Disconnected from the client")
                break
            else: 
                print("Recieved:", reply)
                print('Sending:', reply)
            conn.sendall(str.encode(reply))
        except: 
            break
    print("Connection is lost with clients")
    conn.close()
while True:
    conn, address = s.accept()
    print('connected to :', address)
    start_new_thread(threaded_client, (conn,))