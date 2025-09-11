import pygame
import random

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

class SnakeGame:
    def __init__(self):
        self.block_size = 20
        self.snake = [(100, 100)]
        self.direction = (1, 0)
        self.food = self.food = (200, 200)
        self.score = 0
        self.move_counter = 0
        self.move_delay = 10  # Alapérték, amit a difficulty felülír

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and self.direction != (0, 1):
                self.direction = (0, -1)
            elif event.key == pygame.K_s and self.direction != (0, -1):
                self.direction = (0, 1)
            elif event.key == pygame.K_a and self.direction != (1, 0):
                self.direction = (-1, 0)
            elif event.key == pygame.K_d and self.direction != (-1, 0):
                self.direction = (1, 0)

    def update(self, difficulty):
        delays = {"Easy": 15, "Medium": 8, "Hard": 4}
        self.move_delay = delays.get(difficulty, 8)

        self.move_counter += 1
        if self.move_counter < self.move_delay:
            return
        self.move_counter = 0

        head = (self.snake[0][0] + self.direction[0] * self.block_size,
                self.snake[0][1] + self.direction[1] * self.block_size)

        self.snake.insert(0, head)
        if head == self.food:
            self.food = self.spawn_food()
            self.score += 1
        else:
            self.snake.pop()

        # Game over: ütközés önmagával vagy a pálya szélével
        if head in self.snake[1:] or not (0 <= head[0] < 800 and 0 <= head[1] < 600):
            self.__init__()

    def draw(self, screen, difficulty=None):
        for block in self.snake:
            pygame.draw.rect(screen, GREEN, (*block, self.block_size, self.block_size))
        pygame.draw.rect(screen, RED, (*self.food, self.block_size, self.block_size))

        font = pygame.font.SysFont(None, 30)
        score = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score, (650, 10))

    def spawn_food(self):
        x = random.randint(0, 39) * self.block_size
        y = random.randint(0, 29) * self.block_size
        return (x, y)

    def get_state(self):
        return {
        "snake": self.snake,
        "direction": self.direction,
        "food": self.food,
        "score": self.score,
    }

    def load_state(self, state):
        self.snake = state["snake"]
        self.direction = tuple(state["direction"])
        self.food = tuple(state["food"])
        self.score = state["score"]
        self.move_counter = 0