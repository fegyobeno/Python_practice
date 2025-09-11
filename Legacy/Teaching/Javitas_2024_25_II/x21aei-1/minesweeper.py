import pygame
import random
import json
from constants import *

# --- MineSweeper játék ---
class MineSweeperGame:
    def __init__(self):
        self.grid_size = 10
        self.num_mines = 15
        self.cell_size = 30
        self.offset_x = MENU_WIDTH + 20
        self.offset_y = TOP_MENU_HEIGHT + 20
        self.paused = False
        self.difficulty = "közepes"

        self.flags = 0
        self.game_over = False
        self.win = False

        self.create_grid()

    def create_grid(self):
        self.grid = []
        self.revealed = []
        self.flags_positions = set()

        for y in range(self.grid_size):
            row = []
            revealed_row = []
            for x in range(self.grid_size):
                row.append(0)
                revealed_row.append(False)
            self.grid.append(row)
            self.revealed.append(revealed_row)

        mines_placed = 0
        while mines_placed < self.num_mines:
            rx = random.randint(0, self.grid_size - 1)
            ry = random.randint(0, self.grid_size - 1)
            if self.grid[ry][rx] == 0:
                self.grid[ry][rx] = -1
                mines_placed += 1

        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if self.grid[y][x] == -1:
                    continue
                count = 0
                for ny in range(max(0, y - 1), min(self.grid_size, y + 2)):
                    for nx in range(max(0, x - 1), min(self.grid_size, x + 2)):
                        if self.grid[ny][nx] == -1:
                            count += 1
                self.grid[y][x] = count

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (MENU_WIDTH, TOP_MENU_HEIGHT, WIDTH - MENU_WIDTH, HEIGHT - TOP_MENU_HEIGHT - BOTTOM_MARGIN))

        for y in range(self.grid_size):
            for x in range(self.grid_size):
                rect = pygame.Rect(self.offset_x + x*self.cell_size, self.offset_y + y*self.cell_size, self.cell_size, self.cell_size)
                if self.revealed[y][x]:
                    pygame.draw.rect(screen, GRAY, rect)
                    if self.grid[y][x] == -1:
                        pygame.draw.circle(screen, RED, rect.center, self.cell_size // 3)
                    elif self.grid[y][x] > 0:
                        num_surf = FONT.render(str(self.grid[y][x]), True, BLUE)
                        num_rect = num_surf.get_rect(center=rect.center)
                        screen.blit(num_surf, num_rect)
                else:
                    pygame.draw.rect(screen, DARK_GRAY, rect)
                    if (x, y) in self.flags_positions:
                        pygame.draw.circle(screen, YELLOW, rect.center, self.cell_size // 3)
                pygame.draw.rect(screen, BLACK, rect, 1)

        if self.game_over:
            text = FONT.render("Vesztettél!", True, RED)
            screen.blit(text, (WIDTH//2 + 75 - text.get_width()//2, HEIGHT - BOTTOM_MARGIN + 10))
        elif self.win:
            text = FONT.render("Nyertél!", True, GREEN)
            screen.blit(text, (WIDTH//2 + 75 - text.get_width()//2, HEIGHT - BOTTOM_MARGIN + 10))

    def reveal_cell(self, x, y):
        if self.paused or self.game_over or self.win:
            return

        if self.revealed[y][x] or (x, y) in self.flags_positions:
            return

        self.revealed[y][x] = True

        if self.grid[y][x] == -1:
            self.game_over = True
            self.reveal_all()
            return

        if self.grid[y][x] == 0:
            for ny in range(max(0, y - 1), min(self.grid_size, y + 2)):
                for nx in range(max(0, x - 1), min(self.grid_size, x + 2)):
                    if not self.revealed[ny][nx]:
                        self.reveal_cell(nx, ny)

        self.check_win()

    def reveal_all(self):
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                self.revealed[y][x] = True

    def toggle_flag(self, x, y):
        if self.paused or self.game_over or self.win:
            return

        if self.revealed[y][x]:
            return

        if (x, y) in self.flags_positions:
            self.flags_positions.remove((x, y))
            self.flags -= 1
        else:
            if self.flags < self.num_mines:
                self.flags_positions.add((x, y))
                self.flags += 1

    def check_win(self):
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if self.grid[y][x] != -1 and not self.revealed[y][x]:
                    return
        self.win = True
        self.reveal_all()

    def set_difficulty(self, level):
        if level == "könnyű":
            self.grid_size = 8
            self.num_mines = 10
        elif level == "nehéz":
            self.grid_size = 16
            self.num_mines = 40
        else:
            self.grid_size = 10
            self.num_mines = 15

        self.difficulty = level
        self.flags = 0
        self.game_over = False
        self.win = False
        self.paused = False
        self.create_grid()

    def save_game(self, filename="minesweeper_save.json"):
        data = {
            "grid_size": self.grid_size,
            "num_mines": self.num_mines,
            "flags_positions": list(self.flags_positions),
            "revealed": self.revealed,
            "grid": self.grid,
            "flags": self.flags,
            "game_over": self.game_over,
            "win": self.win,
            "difficulty": self.difficulty
        }
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_game(self, filename="minesweeper_save.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.grid_size = data["grid_size"]
            self.num_mines = data["num_mines"]
            self.flags_positions = set(tuple(pos) for pos in data["flags_positions"])
            self.revealed = data["revealed"]
            self.grid = data["grid"]
            self.flags = data["flags"]
            self.game_over = data["game_over"]
            self.win = data["win"]
            self.difficulty = data.get("difficulty", "közepes")
            self.paused = False
        except Exception as e:
            print(f"Hiba betöltéskor: {e}")