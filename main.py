import socket
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket Created')

host = '127.0.0.1'
port = 8080

s.bind((host, port))

print('socket binded')

s.listen(2)

print('server is listening')

clients = []

def clientthread(conn):
    conn.send('Hello from the server'.encode('utf-8'))

    while True:
        try:
            message = conn.recv(2048)
            if message:
                print(message)
                broadcast(message)
            else:
                remove(conn)
        except:
            continue

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message)
            except:
                client.close()
                remove(client)

def remove(connection):
    if connection not in clients:
        clients.remove(connection)

running = True
while running:
    c,addr = s.accept()
    clients.append(c)
    start_new_thread(clientthread, (c, ))

c.close()
s.close()
    


