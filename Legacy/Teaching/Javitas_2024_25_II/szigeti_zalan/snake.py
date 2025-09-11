import pygame
import random

class SnakeGame:
    def __init__(self, difficulty):
        self.grid_size = 20
        self.snake = [(5, 5)]
        self.direction = (1, 0)
        self.spawn_food()
        self.score = 0
        self.speed = {"Easy": 5, "Normal": 10, "Hard": 15}[difficulty]
        self.counter = 0
        self.game_over = False

    def spawn_food(self):
        while True:
            self.food = (random.randint(0, 39), random.randint(0, 29))
            if self.food not in self.snake:
                break

    def update(self):
        if self.game_over:
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.direction != (0, 1):
            self.direction = (0, -1)
        elif keys[pygame.K_s] and self.direction != (0, -1):
            self.direction = (0, 1)
        elif keys[pygame.K_a] and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif keys[pygame.K_d] and self.direction != (-1, 0):
            self.direction = (1, 0)

        self.counter += 1
        if self.counter < 10 - self.speed:
            return
        self.counter = 0

        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])

        if (new_head in self.snake or
            not (0 <= new_head[0] < 40) or
            not (0 <= new_head[1] < 30)):
            self.game_over = True
            return

        self.snake = [new_head] + self.snake

        if new_head == self.food:
            self.score += 1
            self.spawn_food()
        else:
            self.snake.pop()

    def draw(self, screen):
        for segment in self.snake:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment[0]*20+200, segment[1]*20+40, 18, 18))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.food[0]*20+200, self.food[1]*20+40, 18, 18))

        if self.game_over:
            font = pygame.font.SysFont(None, 48)
            text = font.render("Game Over", True, (255, 255, 255))
            screen.blit(text, (400, 300))
