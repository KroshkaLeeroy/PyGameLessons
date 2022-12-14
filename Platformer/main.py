import sys
import pygame
from settings import *
# 1 Выносим настройки создания карты в отдельный файл settings.py.
# 2 Создаем tiles.py. Для создания блочной структуры 1 тайла
# 3 Прописываем импорт тайла
from tiles import Tile

pygame.init()

clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Platformer')

# 4 Создание тестовой плитки на экране
test_tile = pygame.sprite.Group(Tile((100, 100), 200))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    # 5 проверка работоспособности плитки
    test_tile.draw(screen)

    pygame.display.update()
    clock.tick(60)