import pygame
import random
import time
import json
from constants import *

# --- Snake játék ---
class SnakeGame:
    def __init__(self):
        self.cell_size = 20
        self.grid_width = (WIDTH - MENU_WIDTH) // self.cell_size
        self.grid_height = (HEIGHT - TOP_MENU_HEIGHT - BOTTOM_MARGIN) // self.cell_size
        self.offset_x = MENU_WIDTH
        self.offset_y = TOP_MENU_HEIGHT

        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = (1, 0)
        self.new_direction = (1, 0)
        self.food = self.spawn_food()
        self.paused = False
        self.difficulty = "közepes"
        self.speed = 10
        self.frame_counter = 0
        self.game_over = False
        self.game_won = False
        self.game_over_time = None

    def spawn_food(self):
        while True:
            pos = (random.randint(0, self.grid_width - 1), random.randint(0, self.grid_height - 1))
            if pos not in self.snake:
                return pos

    def update(self):
        if self.paused:
            return

        if self.game_won:
            if self.game_over_time and time.time() - self.game_over_time >= 2:
                self.reset_game()
            return
        
        if self.game_over:
            if self.game_over_time and time.time() - self.game_over_time >= 2:
                self.reset_game()
            return

        self.frame_counter += 1
        if self.frame_counter < (30 // self.speed):
            return
        self.frame_counter = 0

        self.direction = self.new_direction
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        if len(self.snake) == 100:
            self.game_won = True
            self.game_over_time = time.time()
            return
        
        if (new_head in self.snake or
            new_head[0] < 0 or new_head[1] < 0 or
            new_head[0] >= self.grid_width or new_head[1] >= self.grid_height):
            self.game_over = True
            self.game_over_time = time.time()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.spawn_food()
        else:
            self.snake.pop()
            
    def reset_game(self):
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = (1, 0)
        self.new_direction = (1, 0)
        self.food = self.spawn_food()
        self.frame_counter = 0
        self.game_won = False
        self.game_over = False
        self.game_over_time = None

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (MENU_WIDTH, TOP_MENU_HEIGHT, WIDTH - MENU_WIDTH, HEIGHT - TOP_MENU_HEIGHT - BOTTOM_MARGIN))
        for segment in self.snake:
            rect = pygame.Rect(self.offset_x + segment[0]*self.cell_size, self.offset_y + segment[1]*self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(screen, GREEN, rect)

        fx, fy = self.food
        food_rect = pygame.Rect(self.offset_x + fx*self.cell_size, self.offset_y + fy*self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(screen, RED, food_rect)

        if self.game_won:
            text = FONT.render("Nyertél!", True, GREEN)
            screen.blit(text, (WIDTH//2 + 75 - text.get_width()//2, HEIGHT - BOTTOM_MARGIN + 10))
        
        if self.game_over:
            text = FONT.render("Vesztettél!", True, RED)
            screen.blit(text, (WIDTH//2 + 75 - text.get_width()//2, HEIGHT - BOTTOM_MARGIN + 10))

    def set_difficulty(self, level):
        self.difficulty = level
        if level == "könnyű":
            self.speed = 5
        elif level == "nehéz":
            self.speed = 15
        else:
            self.speed = 10

    def handle_key(self, key):
        if self.paused or self.game_over:
            return
        if key == pygame.K_UP and self.direction != (0, 1):
            self.new_direction = (0, -1)
        elif key == pygame.K_DOWN and self.direction != (0, -1):
            self.new_direction = (0, 1)
        elif key == pygame.K_LEFT and self.direction != (1, 0):
            self.new_direction = (-1, 0)
        elif key == pygame.K_RIGHT and self.direction != (-1, 0):
            self.new_direction = (1, 0)

    def save_game(self, filename="snake_save.json"):
        data = {
            "snake": self.snake,
            "direction": self.direction,
            "new_direction": self.new_direction,
            "food": self.food,
            "difficulty": self.difficulty,
            "game_over": self.game_over
        }
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_game(self, filename="snake_save.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.snake = [tuple(p) for p in data["snake"]]
            self.direction = tuple(data["direction"])
            self.new_direction = tuple(data["new_direction"])
            self.food = tuple(data["food"])
            self.difficulty = data["difficulty"]
            self.game_over = data["game_over"]
            self.set_difficulty(self.difficulty)
            self.paused = False
        except Exception as e:
            print(f"Hiba betöltéskor: {e}")