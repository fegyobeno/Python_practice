import json
import pygame
from games import pong, snake, block_breaker

class GameManager:
    def __init__(self):
        self.games = {
            "Pong": pong.PongGame(),
            "Snake": snake.SnakeGame(),
            "Block Breaker": block_breaker.BlockBreaker(),
        }
        self.current_game_name = "Pong"
        self.difficulty = "Medium"
        self.paused = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                self.paused = not self.paused
            elif event.key == pygame.K_q:
                self.save_game()
            elif event.key == pygame.K_e:
                self.load_game()
        if not self.paused:
            self.games[self.current_game_name].handle_event(event)

    def update(self):
        if not self.paused:
            self.games[self.current_game_name].update(self.difficulty)

    def draw(self, screen):
        self.games[self.current_game_name].draw(screen, self.difficulty)
        if self.paused:
            pygame.draw.polygon(screen, (255, 255, 255),
                                [(400, 260), (400, 340), (460, 300)])  # ▶ háromszög

    def switch_game(self, game_name):
        self.current_game_name = game_name
        # újraindul a kiválasztott játék
        self.games[game_name] = {
            "Pong": pong.PongGame(),
            "Snake": snake.SnakeGame(),
            "Block Breaker": block_breaker.BlockBreaker(),
        }[game_name]
        self.paused = False

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def check_resume_click(self, pos):
        if self.paused:
            triangle_area = pygame.Rect(400, 260, 60, 80)
            if triangle_area.collidepoint(pos):
                self.paused = False

    def save_game(self):
        state = self.games[self.current_game_name].get_state()
        with open(f"saves/{self.current_game_name.lower()}_save.json", "w") as f:
            json.dump(state, f)

    def load_game(self):
        try:
            with open(f"saves/{self.current_game_name.lower()}_save.json", "r") as f:
                state = json.load(f)
                self.games[self.current_game_name].load_state(state)
        except FileNotFoundError:
            print("Nincs mentett állapot.")
