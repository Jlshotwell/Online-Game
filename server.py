import socket
import pygame
from _thread import *
import pickle
import random
from player import Player
from level import Level
pygame.init()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('socket created!')

addr = '127.0.0.1'
port = 8080

s.bind((addr, port))

s.listen()

print('The Server is Listening!')

def player_thread(conn, id, level):
    conn.send(pickle.dumps(level.room[id])) #send starting info to client
    running = True
    while running:
        try:
            data = pickle.loads(conn.recv(2048)) #recieve updates from client about player position
            level.room[id] = data
            conn.sendall(pickle.dumps(level)) #send level info to client to be drawn on the screen
        except EOFError:
            handle_disconnect(id, level)
            running = False
        


def handle_disconnect(id, level):
    print(f"{level.room[id]} has disconnected")
    level.room[id] = None
    
    


def main():
    game_level = Level('TagBackground.jpg')
    player_id = 0
    while True:
        start_x = random.randint(10, 1190)
        start_y = random.randint(10, 700)
        start_info = [start_x, start_y]
        conn, addr = s.accept()
        print(f'{addr} has connected')
        player = Player(player_id, start_info, (30, 30), 0)
        game_level.room.append(player)
        start_new_thread(player_thread, (conn, player_id, game_level))
        player_id += 1

main()
