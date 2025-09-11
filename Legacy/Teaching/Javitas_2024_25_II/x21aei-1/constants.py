import pygame

pygame.init()

# --- Konstansok ---
WIDTH, HEIGHT = 1000, 600
MENU_WIDTH = 180
TOP_MENU_HEIGHT = 50
BOTTOM_MARGIN = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
BALL_SIZE = 15
FONT = pygame.font.SysFont(None, 36)
SMALL_FONT = pygame.font.SysFont(None, 24)