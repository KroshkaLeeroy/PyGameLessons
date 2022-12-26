import sys
import pygame
from settings import *
from level import Level

pygame.init()

clock = pygame.time.Clock()

screen_width = 1280

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Platformer')
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')

    level.run()

    pygame.display.update()
    clock.tick(60)