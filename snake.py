import pygame
from config import *

class Snake:
    def __init__(self):
        self.body = [[GRID_SIZE * 5, GRID_SIZE * 5]]
        self.direction = (GRID_SIZE, 0)

    def move(self):
        new_head = [self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1]]
        self.body.insert(0, new_head)
        self.body.pop()

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
        if head in self.body[1:] or head[0] < 0 or head[1] < 0 or head[0] >= WIDTH or head[1] >= HEIGHT:
            return True
        return False

    def eat_food(self, food):
        if self.body[0] == food.position:
            self.body.append(self.body[-1])
            return True
        return False

    def draw(self, screen):
        for i, segment in enumerate(self.body):
            pygame.draw.rect(screen, SNAKE_COLOR, (*segment, GRID_SIZE, GRID_SIZE))
            if i == 0:
                eye_radius = GRID_SIZE // 6
                eye_offset = GRID_SIZE // 4
                eye_positions = [
                    (segment[0] + eye_offset, segment[1] + eye_offset),
                    (segment[0] + GRID_SIZE - eye_offset, segment[1] + eye_offset),
                ]
                for eye in eye_positions:
                    pygame.draw.circle(screen, FACE_COLOR, eye, eye_radius)