import pygame, sys

# 1)На текущем этапе можно приступать к отрисовки анимации и тут то и вступает экстра полезность прямоугольников
#  Для создания движения нам необходимы переменные в которых буде находиться скорость движения объектов


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

# 2) Горизонтальная скорость шара
ball_speed_x = 7
# Вертикальная скорость
ball_speed_y = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 3) В каждой итерации нашего цикла мяч будет перемещаться на количество указанных в переменной скорости пикселей
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # 4) На этом этапе можно запустить код, чтобы увидеть как мяч, стремительно уносится вниз и право.
    # Продолжаться это будет бесконечно, так как мы не указали ему никаких ограничений

    # 5) Задаем мячу ограничения
    # ball.top <= 0 Если верхняя часть мяча находится в нулевой Y координате (верхней части экрана)
    # ball.bottom >= screen_height или нижняя координата мяча больше или равна высоте экрана (нижней части экрана)
    if ball.top <= 0 or ball.bottom >= screen_height:
        # Меняем скорость движения мяча по Y строго на противоположное значение
        ball_speed_y *= -1
    # ball.left <= 0 Если левая часть мяча находится в нулевой X координате (левой части экрана)
    # ball.right >= screen_width или правая координата мяча больше или равна ширине экрана (правой части экрана)
    if ball.left <= 0 or ball.right >= screen_width:
        # Меняем скорость движения мяча по X строго на противоположное значение
        ball_speed_x *= -1
    # Именно по этой причине нам нужно 2 переменных для хранения скорости мяча, чтобы изменять их по отдельности.
    # Чтобы изменить скорость объекта, необходимо умножить его скорость на -1.
    # Использование >= обусловлено тем, что если частота обновления наших кадров пересечется со скоростью объекта, и он
    # окажется за краем дисплея хоть на пиксель, == дадут ему вылететь дальше за края дисплея и сломать игру
    # Однако >= полностью решает эту проблему.

    # 6) Теперь задача указать мячу, что от платформы тоже необходимо отскакивать
    # для этого будем использовать метод rect.colliderect(rect), он вызывается у прямоугольника и принимает в себя
    # аргументом другой прямоугольник с которым нужно проверить пересечение, если пересекается, вернет True, иначе False

    # ball.colliderect(player) Если мяч пересечется с игроком
    # ball.colliderect(opponent) или с оппонентом
    if ball.colliderect(player) or ball.colliderect(opponent):
        # Изменяем горизонтальную скорость мяча на противоположную
        ball_speed_x *= -1




    screen.fill(bg_color)
    pygame.draw.aaline(screen, light_gray, (screen_width / 2, 0), (screen_width / 2, screen_height))

    pygame.draw.rect(screen, light_gray, player)
    pygame.draw.rect(screen, light_gray, opponent)

    pygame.draw.ellipse(screen, light_gray, ball)

    pygame.display.flip()
    clock.tick(60)
