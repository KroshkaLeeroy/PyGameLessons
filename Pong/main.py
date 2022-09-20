import pygame, sys


# Чтобы сделать код более читаемым и использовать цикл только для обновления игровой карты, перенесем проверки
# пересечения и движения шара в функцию и назовем еще ball_animation()

def ball_animation():
    # Объявляем переменные ball_speed_x и ball_speed_y глобальными из-за области видимости переменных.
    # Переменные созданные в основном коде не видны функциями и наоборот,
    # переменные функции не могут использоваться в основном коде.
    # Обойти это можно используя классы как мы поступили с мячом и его параметрами местоположения ball.x и ball.y
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

bg_color = pygame.Color('gray12')
light_gray = (200, 200, 200)

ball_speed_x = 7
ball_speed_y = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2) Тут же будем осуществлять только вызов функции движения мяча
    ball_animation()

    screen.fill(bg_color)
    pygame.draw.aaline(screen, light_gray, (screen_width / 2, 0), (screen_width / 2, screen_height))

    pygame.draw.rect(screen, light_gray, player)
    pygame.draw.rect(screen, light_gray, opponent)

    pygame.draw.ellipse(screen, light_gray, ball)

    pygame.display.flip()
    clock.tick(60)
