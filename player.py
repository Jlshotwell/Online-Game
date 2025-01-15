import pygame
pygame.init()

class Player():
    def __init__(self, player_id, co_ordinates, size, score):
        self.player_id = player_id
        self.image = 'Sprite Front.jpg'
        self.size = size
        self.score = score
        self.velocity = 400
        self.co_ordinates = co_ordinates
        self.timer = 0
        self.timer_max = 3
        self.current_image = 0
        self.position = pygame.math.Vector2()

    def update(self, delta_time):
        
        key = pygame.key.get_pressed()
        while True:
            if key[pygame.K_UP]:
                self.position.y = -1    
            elif key[pygame.K_DOWN]:
                self.position.y = 1 
            else:
                self.position.y = 0

            if key[pygame.K_LEFT]:
                self.position.x = -1 
            elif key[pygame.K_RIGHT]:
                self.position.x = 1
            else:
                self.position.x = 0
            
            if self.position.x == 1:
                self.co_ordinates[0] += self.velocity * delta_time
                self.animate(['Sprite Right.jpg', 'Sprite Right 2.jpg'])
            elif self.position.x == -1:
                self.co_ordinates[0] -= self.velocity * delta_time
                self.animate(['Sprite Left.jpg', 'Sprite Left 2.jpg'])
            else:
                self.co_ordinates[0] = self.co_ordinates[0]
            
            if self.position.y == 1:
                self.co_ordinates[1] += self.velocity * delta_time
                self.animate(['Sprite Front.jpg', 'Sprite Front 2.jpg'])
            elif self.position.y == -1:
                self.co_ordinates[1] -= self.velocity * delta_time
                self.animate(['Sprite Back.jpg', 'Sprite Back 2.jpg'])
            else:
                self.co_ordinates[1] = self.co_ordinates[1]

            player_info = [self.co_ordinates[0], self.co_ordinates[1]]

            #print(self.position.x, self.position.y, player_info)

            return player_info
        
        
    def draw(self, window):
        window.blit(pygame.image.load(self.image).convert(), self.co_ordinates)

    def animate(self, images= []):
        self.image = images[self.current_image]
        if self.timer > self.timer_max:
            if self.current_image == 0:
                self.current_image = 1
            else:
                self.current_image = 0
            self.timer = 0
        else:
            self.timer += 1