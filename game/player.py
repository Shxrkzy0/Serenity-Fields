import pygame
speed = 5 #Picked a random speed for the player to move at

class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32 #Size of the player character
        self.height = 32 #This creates a square player, but we can change it later if we want
        self.color = (255, 0, 0)

    def move(self, keys):
        if keys[pygame.K_w]: #Move up
            self.y -= speed
            print("Moving up")
        if keys[pygame.K_s]: #Move down
            self.y += speed
            print("Moving down")
        if keys[pygame.K_a]: #Move left
            self.x -= speed
            print("Moving left")
        if keys[pygame.K_d]: #Move right
            self.x += speed
            print("Moving right")

        #Keep the player within the bounds of the screen
        self.x = max(0, min(self.x, 1280 - self.width))
        self.y = max(0, min(self.y, 720 - self.height))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))



