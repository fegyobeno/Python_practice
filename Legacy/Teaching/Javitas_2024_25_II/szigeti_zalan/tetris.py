import pygame
import random

COLS, ROWS = 10, 20
CELL = 30

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]]
]

class TetrisGame:
    def __init__(self, difficulty):
        self.grid = [[0]*COLS for _ in range(ROWS)]
        self.shape = random.choice(SHAPES)
        self.x = 4
        self.y = 0
        self.tick = 0
        self.speed = 30 if difficulty == "Easy" else 15 if difficulty == "Hard" else 20

    def collide(self, x, y, shape):
        for i, row in enumerate(shape):
            for j, val in enumerate(row):
                if val:
                    if y+i >= ROWS or x+j < 0 or x+j >= COLS or self.grid[y+i][x+j]:
                        return True
        return False

    def place_shape(self):
        for i, row in enumerate(self.shape):
            for j, val in enumerate(row):
                if val:
                    self.grid[self.y+i][self.x+j] = 1
        self.shape = random.choice(SHAPES)
        self.x, self.y = 4, 0

    def clear_lines(self):
        self.grid = [row for row in self.grid if not all(row)]
        while len(self.grid) < ROWS:
            self.grid.insert(0, [0]*COLS)

    def update(self):
        self.tick += 1
        if self.tick >= self.speed:
            if not self.collide(self.x, self.y+1, self.shape):
                self.y += 1
            else:
                self.place_shape()
                self.clear_lines()
            self.tick = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not self.collide(self.x-1, self.y, self.shape):
            self.x -= 1
        if keys[pygame.K_RIGHT] and not self.collide(self.x+1, self.y, self.shape):
            self.x += 1
        if keys[pygame.K_DOWN] and not self.collide(self.x, self.y+1, self.shape):
            self.y += 1

    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, (0, 255, 0), (200 + x*CELL, y*CELL, CELL, CELL))
        for i, row in enumerate(self.shape):
            for j, val in enumerate(row):
                if val:
                    pygame.draw.rect(screen, (255, 0, 0), (200 + (self.x+j)*CELL, (self.y+i)*CELL, CELL, CELL))

    def get_state(self):
        return {
            "grid": self.grid,
            "x": self.x,
            "y": self.y,
            "shape": self.shape
        }

    def set_state(self, state):
        self.grid = state["grid"]
        self.x = state["x"]
        self.y = state["y"]
        self.shape = state["shape"]
