import pygame
from game import SnakeGame
from menu import MainMenu

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Snake Game")
    
    menu = MainMenu(screen)
    menu.run()

    game = SnakeGame(screen, menu.best_score)
    game.run()
