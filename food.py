import pygame
import random
from config import *

class Food:
    def __init__(self, image_path, grid_size=GRID_SIZE):
        self.image = pygame.image.load(image_path)  # Загружаем изображение еды
        self.image = pygame.transform.scale(self.image, (grid_size, grid_size))  # Масштабируем под клетку
        self.grid_size = grid_size
        self.position = [grid_size * random.randint(0, (WIDTH // grid_size) - 1),
                         grid_size * random.randint(0, (HEIGHT // grid_size) - 1)]

    def relocate(self, snake_body):
        """Перемещает еду на случайную позицию, избегая тела змейки"""
        while True:
            self.position = [self.grid_size * random.randint(0, (WIDTH // self.grid_size) - 1),
                             self.grid_size * random.randint(0, (HEIGHT // self.grid_size) - 1)]
            if self.position not in snake_body:
                break

    def draw(self, screen):
        screen.blit(self.image, (self.position[0], self.position[1]))  # Отображаем изображение
