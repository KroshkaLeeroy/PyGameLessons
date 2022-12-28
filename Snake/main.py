import sys
import pygame
from pygame import Vector2
import random


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
        # 14 переменной которая это отслеживает
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), block_rect)

    def move_snake(self):
        # 15 и самой логики добавления блока
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    # 13 создание метода отвечающего за добавление
    def add_block(self):
        self.new_block = True



class FRUIT:
    def __init__(self):
        # 11 и вызов его соответственно
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

    # 10 создание метода размещения фрукта
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)

        self.pos = Vector2(self.x, self.y)


# 1 Создаем класс игры который будет в себе сдержать змею и фрукт
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    # 2 метод обновления движения змеи
    def update(self):
        self.snake.move_snake()
        # 8 Вызов проверки
        self.check_collision()

    # 3 метод отрисовки всех элементов
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    # 7 создание метода проверки пересечения позиций фрукта и позиций головы змеи
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # 9 В момент когда змея съедает фрукт, фрукт должен переместиться
            self.fruit.randomize()
            # 12 добавление змейке блок
            self.snake.add_block()


pygame.init()

clock = pygame.time.Clock()

cell_size = 40
cell_number = 20

screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption('Snake')

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# 4 Создание экземпляра класса
main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            # 5 обновление и передвижения
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)

    screen.fill((175, 215, 70))
    # 6 отрисовка
    main_game.draw_elements()

    pygame.display.update()
    clock.tick(60)
