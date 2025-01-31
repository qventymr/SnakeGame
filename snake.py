import pygame
from config import *

class Snake:
    def __init__(self, color, grid_size):
        self.body = [[grid_size * 5, grid_size * 5]]
        self.direction = (grid_size, 0)
        self.color = color
        self.grid_size = grid_size

    def move(self):
        new_head = [self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1]]
        self.body.insert(0, new_head)
        self.body.pop()

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (*segment, self.grid_size, self.grid_size))


    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != (0, GRID_SIZE):
            self.direction = (0, -GRID_SIZE)
        elif key == pygame.K_DOWN and self.direction != (0, -GRID_SIZE):
            self.direction = (0, GRID_SIZE)
        elif key == pygame.K_LEFT and self.direction != (GRID_SIZE, 0):
            self.direction = (-GRID_SIZE, 0)
        elif key == pygame.K_RIGHT and self.direction != (-GRID_SIZE, 0):
            self.direction = (GRID_SIZE, 0)

    def check_collision(self):
        head = self.body[0]
        if head in self.body[1:]:
            return True
        if head[0] < 0 or head[1] < 0 or head[0] >= WIDTH or head[1] >= HEIGHT:
            return True
        return False

    def eat_food(self, food):
        if self.body[0] == food.position:
            self.body.append(self.body[-1])  # Увеличиваем змейку
            return True
        return False
