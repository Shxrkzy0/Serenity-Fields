#To push changes to github:
#   git add . (Selects all files)
#   git commit -m "describe what you changed" (Keep the quotation)
#   git push (Updates all files)
#
#If you are on a new device:
#   git clone https://github.com/Shxrkzy0/Serenity-Fields.git (Copies full repo onto device - For one time use)
#
#If you are switching devices:
#   git pull (Applies most recent changes to the current device)



import pygame
import sys

#Creates the main window
pygame.init()
size = (1280,720)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#Grass tiles
TILE = 16
grid = [[False] * 80 for _ in range (45)]

#Core game loop
while True:
    for y in range(45):
        for x in range(80):
            if grid[y][x] == False:
                pygame.draw.rect(screen, (48, 138, 57), (x*TILE,y*TILE,TILE,TILE))
            else:
                pygame.draw.rect(screen, (102, 252, 116), (x*TILE,y*TILE,TILE,TILE))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()