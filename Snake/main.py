import sys
import pygame
from pygame import Vector2
import random


# 3 создание класса змеи, для хранения информации о координатах ее тела
class SNAKE:
    def __init__(self):
        # 4 Создание 3х блоков тела змеи в начале игры
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]

    def draw_snake(self):
        # 5 по очереди отрисовываем блоки тела змеи
        for block in self.body:
            # 6 Повторяемся так же как и с отрисовкой фрукта
            block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (183,111,122), block_rect)


class FRUIT:
    def __init__(self):
        # 2 Используя рандом размещаем Х в случайной ячейке карты, -1 потому что 20 ячейка находится за экраном
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)

        self.pos = Vector2(self.x, self.y)

    # 1 Поправляем размещение фрукта, с созданием иллюзии сетки по которой все ставится и двигается
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)


pygame.init()

clock = pygame.time.Clock()


cell_size = 40
cell_number = 20

screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption('Snake')


fruit = FRUIT()
# 6 Создание объекта для класса змеи
snake = SNAKE()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175, 215, 70))


    fruit.draw_fruit()
    # 7 Физическая отрисовка змеи
    snake.draw_snake()

    pygame.display.update()
    clock.tick(60)
