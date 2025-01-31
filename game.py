import pygame
from snake import Snake
from food import Food
from config import *

class SnakeGame:
    def __init__(self, screen, grid_size, snake_color, food_image):
        self.screen = screen
        self.grid_size = grid_size
        self.snake = Snake(snake_color, grid_size)
        self.food = Food(food_image, grid_size)  # Теперь передаём путь к изображению еды
        self.running = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.score = 0

    def draw_grid(self):
        """Рисует шахматное поле фиксированного размера"""
        for row in range(HEIGHT // self.grid_size):
            for col in range(WIDTH // self.grid_size):
                color = COLOR_1 if (row + col) % 2 == 0 else COLOR_2
                pygame.draw.rect(self.screen, color, (col * self.grid_size, row * self.grid_size, self.grid_size, self.grid_size))

    def draw(self):
        self.draw_grid()
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()


    def update(self):
        self.snake.move()
        if self.snake.check_collision():
            self.running = False
        if self.snake.eat_food(self.food):
            self.food.relocate(self.snake.body)
            self.score += 1  # Теперь ошибки не будет


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


    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, FACE_COLOR)
        self.screen.blit(score_text, (10, 10))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()