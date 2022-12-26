import pygame
from tiles import Tile

# подготовка к созданию классу уровня
class Level:
    def __init__(self, level_data, surface):
        # клас должен содержать поверхность (экран) и саму карту уровня
        self.display_surface = surface
        self.level_data = level_data

    def run(self):
        pass