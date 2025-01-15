import pygame
import time

pygame.init()

class Player():
    def __init__(self, player_id, co_ordinates, size, score):
        self.player_id = player_id
        self.image = 'Sprite Front.jpg'
        self.size = size
        self.score = score
        self.velocity = 1
        self.co_ordinates = co_ordinates
        self.position = pygame.math.Vector2()

    def update(self, delta_time):
        
        key = pygame.key.get_pressed()
        while True:
            if key[pygame.K_UP]:
                self.position.y -= self.velocity * delta_time
                self.image = 'Sprite Back.jpg'      
            elif key[pygame.K_DOWN]:
                self.position.y += self.velocity * delta_time
                self.image = 'Sprite Front.jpg'
            else:
                self.position.y = 0

            if key[pygame.K_LEFT]:
                self.position.x -= self.velocity * delta_time
                self.image = 'Sprite Right.jpg'
            elif key[pygame.K_RIGHT]:
                self.position.x += self.velocity * delta_time
                self.image = 'Sprite Right.jpg'
            else:
                self.position.x = 0

            self.co_ordinates[0] += self.position.x
            self.co_ordinates[1] += self.position.y
            player_info = [self.co_ordinates[0], self.co_ordinates[1]]
            return player_info
        
        
    def draw(self, window):
        window.blit(pygame.image.load(self.image).convert(), self.co_ordinates)

    def animate(self, image1, image2, image3):
        while True:
            current_image = 0
            images = [image1, image2, image3]
            self.image = images[current_image]
            if current_image >= 2:
                current_image = 0
            time.sleep(.5)


    


        

