import sys
import pygame
from settings import *
# Импорт уровня из файла
from level import Level

pygame.init()

clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Platformer')
# Создание экземпляра класса, с аргументами
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    # Физический вызов отрисовки всего
    level.run()

    pygame.display.update()
    clock.tick(60)