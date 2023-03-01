from functions import *


class Main:
    def __init__(self):
        self.cell_size = 20
        self.cell_number = 40

        self.screen = pygame.display.set_mode((self.cell_number * self.cell_size, self.cell_number * self.cell_size))
        pygame.display.set_caption("Game of Life")

        self.clock = pygame.time.Clock()

    def draw_map(self):



pygame.init()

main_game = Main()

while True:
    get_evenst()



    pygame.display.update()
    main_game.clock.tick(120)
