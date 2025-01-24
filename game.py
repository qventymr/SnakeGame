import pygame
from snake import Snake
from food import Food
from config import *

class SnakeGame:
    def __init__(self, screen, best_score):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.running = True
        self.score = 0
        self.best_score = best_score
        self.font = pygame.font.SysFont("Arial", 24)

    def update(self):
        self.snake.move()
        if self.snake.check_collision():
            self.running = False
        if self.snake.eat_food(self.food):
            self.food.relocate(self.snake.body)
            self.score += 1
            if self.score > self.best_score:
                self.best_score = self.score


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.snake.change_direction(event.key)

    def update(self):
        self.snake.move()
        if self.snake.check_collision():
            self.running = False
        if self.snake.eat_food(self.food):
            self.food.relocate(self.snake.body)
            self.score += 1

    def draw_grid(self):
        for row in range(HEIGHT // GRID_SIZE):
            for col in range(WIDTH // GRID_SIZE):
                color = COLOR_1 if (row + col) % 2 == 0 else COLOR_2
                pygame.draw.rect(self.screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, FACE_COLOR)
        self.screen.blit(score_text, (10, 10))

    def draw(self):
        self.draw_grid()
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.draw_score()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()