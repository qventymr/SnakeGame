import pygame
from config import *

class Food:
    def __init__(self):
        self.color = FOOD_COLOR
        self.position = [GRID_SIZE * 7, GRID_SIZE * 7]
        self.is_food_on_screen = True

    def relocate(self, snake_body):
        while True:
            self.position = [GRID_SIZE * random.randrange(0, WIDTH // GRID_SIZE),
                             GRID_SIZE * random.randrange(0, HEIGHT // GRID_SIZE)]
            if self.position not in snake_body:
                break
        self.is_food_on_screen = True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))
