import pygame
TILE = 16
COLS = 80
ROWS = 45

#Creating a grid of grass tiles represented as a 2D list using True and False
class grassGrid:
    def __init__(self):
        self.grid = [[False] * COLS for _ in range(ROWS)] # False = uncut, True = cut

    def cut(self, x, y):
        if 0 <= x < COLS and 0 <= y < ROWS: #Checking bounds
            self.grid[y][x] = True

    def draw(self, screen):
        for y in range(ROWS):
            for x in range(COLS):
                colour = (48, 138, 57) if self.grid[y][x] == False else (102, 252, 116)
                pygame.draw.rect(screen, colour, (x*TILE, y*TILE, TILE, TILE)) #Draw the grass tile