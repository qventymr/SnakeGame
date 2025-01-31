import pygame
from game import SnakeGame
from menu import MainMenu
from config import *

if __name__ == "__main__":
    pygame.init()

    # Создаём окно фиксированного размера
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Показываем меню перед запуском игры
    menu = MainMenu(screen)
    menu.run()

    # Запускаем игру с выбранным изображением еды
    game = SnakeGame(screen, GRID_SIZE, menu.selected_snake_color, menu.selected_food_image)
    game.run()
