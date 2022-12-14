import pygame


# 1 Создаем класс 1 блока
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()  # 2 Наследуемся от класса спрайт.
        self.image = pygame.Surface((size, size))  # 3 Создаем объект поверхность с параметрами размера Х и У
        self.image.fill('gray')  # 4 Заполняем цветом
        self.rect = self.image.get_rect(topleft=pos)  # 5 Задаем место размещения.
        # 6 Возвращаемся в мейн файл и делаем импорт
