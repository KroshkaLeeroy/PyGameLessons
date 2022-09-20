import pygame, sys


def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

# 1) Теперь можно приступать к получению информации от пользователя, нажатию клавиш

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

# 3) Создаем переменную отвечающую за скорость перемещения героя в цикле.
# Будем изменять ее при нажатии на клавишу движения и за счет цикла игры и пользователь увидит движение
player_speed = 0

while True:
    # 2) У нас уже есть цикл проверяющий все нажатия клавиш пользователя, мы его расширим
    # Нам необходимо привязать клавиши стрелок вверх и вниз к движению платформы игрока соответственно.
    # Для этого нам нужно будет считывать 2 события
    # Нажатие кнопки для начала движения и отпускание кнопки для его прекращения
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Начинаем проверку нажатия какой-либо клавиши в игре в целом так как метод проверят нажатие всех клавиш в целом
        # pygame.KEYDOWN содержит информацию о том, что кнопка была нажата
        if event.type == pygame.KEYDOWN:
            # И вторая проверка на нажатие интересующей нас клавиши K_DOWN (стрелки вниз)
            if event.key == pygame.K_DOWN:
                # На этом этапе мы можем прописать движения игрока на какое-либо количество пикселей
                # Однако работать это не будет, по причине того, что событие считывает только единичное нажатие клавиши
                # и чтобы передвинуть игрока вниз, нужно будет множество раз нажать на клавишу движения, что не весело.
                # Для этого шаг 3)


                # 5)Устанавливаем скорость платформы на положительное значение для ее движения вниз
                player_speed += 7
            # 6) Если пользователь нажмет клавишу K_UP (стрелка вверх)
            if event.key == pygame.K_UP:
                # Изменяем скорость платформы в противоположную
                player_speed -= 7

        # 7) Дальше нам необходимо прописать сценарий в котором пользователь отпускает кнопку и программа считывает это
        # pygame.KEYUP содержит информацию о том, что кнопка была отжата
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                # И мы соответственно меняем скорость движения платформы вниз на обратную
                player_speed -= 7

            if event.key == pygame.K_UP:
                # И мы соответственно меняем скорость движения платформы вверх на обратную
                player_speed += 7

        # 8) На этом мы все, можем запускать программу и проверять движение платформы игрока,
        # но есть одна небольшая проблема, игрок выходит за края дисплея, чего быть не должно, чиним это

    ball_animation()
    # 4) Указываем, что координата Y платформы должна изменить на его текущую скорость
    player.y += player_speed

    # 9) Вся логика, что нам необходима это,
    # проверять пересечение верхней части платформы на превышение 0
    if player.top <= 0:
        # И ограничивать его этим порогом
        player.top = 0
    # И для нижней части платформы проверять, не вышла ли она за высоту экрана
    if player.bottom >= screen_height:
        # И ограничивать его этим порогом
        player.bottom = screen_height

    # Фактически мы телепортирует игрока настолько недалеко от его местоположения,
    # что это выглядит как будто движения нет вообще

    screen.fill(bg_color)
    pygame.draw.aaline(screen, light_gray, (screen_width / 2, 0), (screen_width / 2, screen_height))

    pygame.draw.rect(screen, light_gray, player)
    pygame.draw.rect(screen, light_gray, opponent)

    pygame.draw.ellipse(screen, light_gray, ball)

    pygame.display.flip()
    clock.tick(60)
