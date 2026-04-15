import pygame
import random
from animal import spawnAnimal
TILE = 32
COLS = 80
ROWS = 45


class animalSpawn:
    def __init__(self):
        self.animal = spawnAnimal()
        self.tile_x = random.randint(0, COLS - 1) #Random tile position
        self.tile_y = random.randint(0, ROWS - 1)
        self.x = self.tile_x * TILE + TILE // 2
        self.y = self.tile_y * TILE + TILE // 2
        self.colour = self.animal["colour"]
        self.font = pygame.font.SysFont(None, 20)

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), 10) #Draw the icon as a circle
        label = self.font.render("!", True, (0, 0, 0))
        screen.blit(label, (self.x - label.get_width() // 2, self.y - label.get_height() // 2)) 
        #blit draws the label over an existing display


#Checking for collision
    def collides_with_player(self, player):
        return (abs(self.x - (player.x + player.width // 2)) < TILE and
                abs(self.y - (player.y + player.height // 2)) < TILE)