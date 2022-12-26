import pygame
from tiles import Tile
from settings import tile_size


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        # 1 Упрощение ввода карты
        self.setup_level(level_data)

    # 2 Создание функции которая будет отвечать за рисование клеток
    def setup_level(self, layout):
        # 3 Создание группы плиток
        self.tiles = pygame.sprite.Group()
        # 5 Итерируемся по всем элементам строкам
        for row_index, row in enumerate(layout):
            # 6 Итерируемся по всем ячейкам уровня
            for column_index, cell in enumerate(row):
                # 7 проверяем соответствие ячейки Х
                if cell == "X":
                    # Переводим в пиксели
                    x = column_index * tile_size
                    y = row_index * tile_size
                    # Создаем 1 ячейку
                    tile = Tile((x, y), tile_size)
                    # Добавляем ячейку в группу ячеек
                    self.tiles.add(tile)

    def run(self):
        # 8 Передвижение экрана на 1 пиксель под героя
        self.tiles.update(1)

        # 4 Отрисовка собираемой группы плиток
        self.tiles.draw(self.display_surface)
