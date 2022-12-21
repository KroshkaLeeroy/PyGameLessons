import sys
import pygame
from pygame import Vector2
import random


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)

    # 1 Создаем функцию движения змеи.
    # Движение будет осуществляться путем смещения блоков тела змеи по вектору ее движения
    def move_snake(self):
        body_copy = self.body[:-1]  # Копируем все тело змеи за исключением последнего блока.
        body_copy.insert(0, body_copy[0] + self.direction)  # Вставляем в копию тела змеи, на место первого блока, блок
        # который будем изменять свои координаты отталкиваясь от вектора направления self.direction
        self.body = body_copy[:]


class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)

        self.pos = Vector2(self.x, self.y)

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
snake = SNAKE()
# 2 Для создания движение змеи нам необходимо передвигать ее блоки с равным промежутком времени
# для этого создаем кастомный ивент который будет вызываться каждые 150 миллисекунд по таймеру ниже
# в зависимости от цифры будет меняться скорость передвижения змеи
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 3 Теперь мы описываем, что нам необходимо делать в момент когда срабатывает наш таймер в списке событий
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        # 4 Теперь наконец можно прикручивать управление кнопками
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Изменяем вектор движения змеи
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)

    screen.fill((175, 215, 70))

    fruit.draw_fruit()
    snake.draw_snake()

    pygame.display.update()
    clock.tick(60)
