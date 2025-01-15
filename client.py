from level import *
import pygame
from _thread import *
import pickle
import socket
pygame.init()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

x = 1200
y = 800
window = pygame.display.set_mode((x, y))

def draw_window(player1):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        clock = pygame.time.Clock()
        delta_time = clock.tick(60) / 1000.0
        client.send(pickle.dumps(player1))
        level = pickle.loads(client.recv(2048))
        window.blit(pygame.image.load(level.background).convert(), (0,0))
        player1.update(delta_time)
        for p in level.room:
            if p == None:
                continue
            else:
                p.draw(window)
        pygame.display.update()
        
             
def main():
    client.connect(('127.0.0.1', 8080))
    player1 = pickle.loads(client.recv(2048)) #recieves player specific data
    draw_window(player1)   

main()
