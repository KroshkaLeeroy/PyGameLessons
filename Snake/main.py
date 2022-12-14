import sys
import pygame
from pygame import Vector2


# 2 Создание объекта фрукт, и размещение его на координатной сетке карты
class FRUIT:
    def __init__(self):
        self.x = 5
        self.y = 4
        # 3 Для более удобного контроля движения объекта используем векторы, так как они упрощают читаемость кода,
        # и работу с передвижением
        self.pos = Vector2(self.x, self.y)

    # 4 Создание метода для размещения фрукта по его координатным позиция
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x, self.pos.y, cell_size, cell_size)
        # 5 Физическая отрисовка объекта с цветом
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)


pygame.init()

clock = pygame.time.Clock()

# 1 Пересоздаем размеры окна, чтобы удобнее было составить сетку передвижения змеи
cell_size = 40
cell_number = 20

screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption('Snake')

# 6 Создание самого объекта фрукта
fruit = FRUIT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175, 215, 70))

    # 7 Использование метода для его размещения на экране
    fruit.draw_fruit()

    pygame.display.update()
    clock.tick(60)
