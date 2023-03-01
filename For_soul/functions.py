import pygame
import sys

def get_evenst():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()





if __name__ == '__main__':

    pass