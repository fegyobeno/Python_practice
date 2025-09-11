import pygame

class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.buttons = ["Pong", "Tetris", "Snake"]
        self.difficulties = ["Easy", "Normal", "Hard"]
        self.selected_game = None
        self.selected_difficulty = 1
        self.top_buttons = ["Pause", "Save", "Load"]
        self.top_button_actions = {"Pause": "pause", "Save": "save", "Load": "load"}
        self.last_action = None

    def update(self, screen):
        font = pygame.font.SysFont(None, 30)
        pygame.draw.rect(screen, (50, 50, 50), (0, 0, 200, self.height))

        selected = None
        for i, text in enumerate(self.buttons):
            rect = pygame.Rect(10, 50 + i * 60, 180, 50)
            pygame.draw.rect(screen, (100, 100, 255), rect)
            screen.blit(font.render(text, True, (255, 255, 255)), (rect.x + 20, rect.y + 10))
            if pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos()):
                selected = text

        pygame.draw.rect(screen, (70, 70, 70), (200, 0, self.width - 200, 40))
        for i, diff in enumerate(self.difficulties):
            rect = pygame.Rect(220 + i * 100, 5, 90, 30)
            color = (255, 100, 100) if i == self.selected_difficulty else (100, 100, 100)
            pygame.draw.rect(screen, color, rect)
            screen.blit(font.render(diff, True, (255, 255, 255)), (rect.x + 10, rect.y + 5))
            if pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos()):
                self.selected_difficulty = i

        self.last_action = None
        for i, label in enumerate(self.top_buttons):
            rect = pygame.Rect(10 + i * 70, 5, 60, 30)
            pygame.draw.rect(screen, (90, 90, 90), rect)
            screen.blit(font.render(label, True, (255, 255, 255)), (rect.x + 5, rect.y + 5))
            if pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos()):
                self.last_action = self.top_button_actions[label]

        return selected

    def get_difficulty(self):
        return self.difficulties[self.selected_difficulty]

    def draw_overlay(self, screen, paused):
        font = pygame.font.SysFont(None, 36)
        if paused:
            text = font.render("PAUSED", True, (255, 255, 0))
            screen.blit(text, (self.width // 2 - 60, self.height // 2 - 20))
