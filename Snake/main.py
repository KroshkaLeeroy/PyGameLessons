import sys
import pygame

pygame.init()

clock = pygame.time.Clock()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')

# 1) Rectangles это просто прямоугольник в который можно использовать для рисования чего-либо, или обводки.
# И этот прямоугольник имеет большое количество точек, от которых мы можем отталкиваться.
# *---*---*     Предположим это наш прямоугольник
# |   |   |
# *---*---*
# |   |   |
# *---*---*     А это все точки в координатах от которых мы можем отталкиваться
#                             top
#                          _________
#                            midtop
#                              |
#           |    topleft - *---*---* - topright     |
#           |              |   | / | - center       |
#     left  |    midleft - *---*---* - midright     |  right
#           |              |   |   |                |
#           | bоttomleft - *---*---* - bottomright  |
#                              |
#                          midbоttom
#                          _________
#                           bоttom
# Эти точки чрезвычайно полезны не только для перемещения чего-то, но и для описания пересечения с другими объектами.
# Есть 2 способа создания Rectangles.
# pygame.Rect(x,y,w,h) Самостоятельное создание прямоугольника
# surface.get_rect(position) Создание прямоугольника вокруг какого либо объекта.
# И если у нас есть прямоугольник, мы можем делать с ним большое количество действий.

# test_rect = pygame.Rect(100, 200, 100, 100)

# 4) Создание поверхности
test_surface = pygame.Surface((100, 200))
test_rect = test_surface.get_rect(center=(300, 300))  # .get_rect() Создание прямоугольника вокруг поверхности.
# Выбрав точку прямоугольника указываем координаты на которых она будет размещаться .get_rect(center=(300, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175, 215, 70))

    # 6) Если нам необходимо передвинуть объект, мы двигаем какую либо сторону (left, right, top, buttom) прямоугольника
    test_rect.bottom += 1

    # 2) Физическое рисование прямоугольника
    # pygame.draw.rect(screen, (0, 0, 0), test_rect)

    # 3) Разница в Surface и Rectangle не только в удобстве перемещения, это еще и физически проще вычислять для компа.
    # Обычно мы не заполняем поверхность цветом, а располагаем в ней что-то еще.
    # screen.blit(test_surface, (200, 200))

    # 5) Фактическое размещение поверхности на экране, с указанием координат из прямоугольника
    screen.blit(test_surface,test_rect)

    pygame.display.update()  # Или .flip()
    clock.tick(60)
