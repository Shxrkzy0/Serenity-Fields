#To push changes to github:
#   git add . (Selects all files)
#   git commit -m "describe what you changed" (Keep the quotation)
#   git push (Updates all files)
#
#If you are switching devices:
#   git pull (Applies most recent changes to the current device)
import pygame
import sys

pygame.init()
size = (1280,720)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
