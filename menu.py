import pygame
from config import *

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.best_score = 0
        self.running = True
        self.font = pygame.font.SysFont("Arial", 36)
        self.small_font = pygame.font.SysFont("Arial", 24)

    def draw_text(self, text, y, color=FACE_COLOR):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
        self.screen.blit(text_surface, text_rect)

    def draw_button(self, text, y, button_color, text_color):
        button_rect = pygame.Rect(WIDTH // 2 - 100, y - 30, 200, 60)
        pygame.draw.rect(self.screen, button_color, button_rect, border_radius=10)
        text_surface = self.small_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.screen.blit(text_surface, text_rect)
        return button_rect

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

    def show_settings(self):
        print("Настройки пока не реализованы")

    def run(self):
        while self.running:
            self.screen.fill(BG_COLOR)

            self.draw_text("Snake Game", HEIGHT // 4)

            self.draw_text(f"Best Score: {self.best_score}", HEIGHT // 3)

            self.play_button = self.draw_button("Play", HEIGHT // 2, SNAKE_COLOR, BG_COLOR)
            self.settings_button = self.draw_button("Settings", HEIGHT // 2 + 100, SNAKE_COLOR, BG_COLOR)

            pygame.display.flip()
            self.handle_events()
