#To push changes to github:
#   git add . (Selects all files)
#   git commit -m "describe what you changed" (Keep the quotation)
#      if commit doesn't work, try:
#         git config --global user.name "Antoni Pantak"
#         git config --global user.email "antonipantk@gmail.com"
#   git push (Updates all files)
#
#If you are on a new device:
#   git clone https://github.com/Shxrkzy0/Serenity-Fields.git (Copies full repo onto device - For one time use)
#
#If you are switching devices:
#   git pull (Applies most recent changes to the current device)

import pygame
import sys
from grass import grassGrid

#Main window
pygame.init()
size = (1280,720) #720p minimum resolution, must be divisible by 16 for the grass tiles to fit properly
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Serenity Fields")
clock = pygame.time.Clock()

#Grass tiles
grass = grassGrid()

#Core game loop
while True:
    clock.tick(60) #Limits the game to 60 frames per second
    screen.fill((0,0,0))
    grass.draw(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Closes the game window
            sys.exit() #Exits the program