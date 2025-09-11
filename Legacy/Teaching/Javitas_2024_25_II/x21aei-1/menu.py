import pygame
from constants import *

# --- Menü ---
class Button:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = GRAY
        self.hover_color = DARK_GRAY

    def draw(self, surface):
        font = pygame.font.SysFont(None, 30)
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

def create_menu():
    game_buttons = [
        Button("Pong - AI", 20, 100, 150, 40),
        Button("Pong - 2P", 20, 160, 150, 40),
        Button("MineSweeper", 20, 220, 150, 40),
        Button("Snake", 20, 280, 150, 40),
    ]

    menu_buttons = [
        Button("Mentés", 200, 20, 100, 35),
        Button("Betöltés", 310, 20, 100, 35),
        Button("Megállít / Folytat", 420, 20, 180, 35)
    ]

    difficulty_buttons = [
        Button("Könnyű", 620, 20, 80, 35),
        Button("Közepes", 710, 20, 100, 35),
        Button("Nehéz", 820, 20, 80, 35)
    ]

    return game_buttons, menu_buttons, difficulty_buttons