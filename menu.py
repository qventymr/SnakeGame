import pygame
from config import *

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.best_score = 0
        self.running = True
        self.font = pygame.font.SysFont("Arial", 36)
        self.small_font = pygame.font.SysFont("Arial", 24)

        # Настройки по умолчанию
        self.selected_snake_color = SNAKE_COLOR
        self.selected_food_image = "image1.png"  # По умолчанию яблоко

    def draw_text(self, text, y, color=FACE_COLOR):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
        self.screen.blit(text_surface, text_rect)

    def draw_button(self, text, x, y, button_color, text_color):
        button_rect = pygame.Rect(x, y, 150, 50)
        pygame.draw.rect(self.screen, button_color, button_rect, border_radius=10)
        text_surface = self.small_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.screen.blit(text_surface, text_rect)
        return button_rect

    def show_settings(self):
        """Открывает меню настроек"""
        settings_running = True
        selected_snake = 0
        selected_food = 0

        snake_colors = [(0, 255, 0), (72, 118, 236), (255, 165, 0)]
        food_images = ["image1.png", "image2.png", "image3.png"]

        while settings_running:
            self.screen.fill(BG_COLOR)
            self.draw_text("Settings", HEIGHT // 10)

            # Выбор изображения еды
            self.draw_text("Food Type:", HEIGHT // 1.8)
            food_preview = pygame.image.load(food_images[selected_food])
            food_preview = pygame.transform.scale(food_preview, (50, 50))
            self.screen.blit(food_preview, (WIDTH // 2 - 25, HEIGHT // 1.8 + 40))

            left_food = self.draw_button("<", WIDTH // 3 - 50, HEIGHT // 1.8 + 90, SNAKE_COLOR, BG_COLOR)
            right_food = self.draw_button(">", WIDTH * 2 // 3 - 50, HEIGHT // 1.8 + 90, SNAKE_COLOR, BG_COLOR)

            # Кнопка выхода
            back_button = self.draw_button("Back", WIDTH // 2 - 75, HEIGHT - 100, SNAKE_COLOR, BG_COLOR)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settings_running = False
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if left_food.collidepoint(mouse_pos):
                        selected_food = (selected_food - 1) % len(food_images)
                    elif right_food.collidepoint(mouse_pos):
                        selected_food = (selected_food + 1) % len(food_images)

                    elif back_button.collidepoint(mouse_pos):
                        self.selected_food_image = food_images[selected_food]
                        settings_running = False

    def run(self):
        while self.running:
            self.screen.fill(BG_COLOR)

            self.draw_text("Snake Game", HEIGHT // 4)
            self.draw_text(f"Best Score: {self.best_score}", HEIGHT // 3)

            self.play_button = self.draw_button("Play", WIDTH // 2 - 75, HEIGHT // 2, SNAKE_COLOR, BG_COLOR)
            self.settings_button = self.draw_button("Settings", WIDTH // 2 - 75, HEIGHT // 2 + 100, SNAKE_COLOR, BG_COLOR)

            pygame.display.flip()
            self.handle_events()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.play_button.collidepoint(mouse_pos):
                    self.running = False  # Начать игру
                elif self.settings_button.collidepoint(mouse_pos):
                    self.show_settings()