import pygame
import random
import tkinter as tk
from tkinter import messagebox
import json
from constants import *

# --- Pong játék ---
class PongGame:
    def __init__(self):
        self.ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_SIZE, BALL_SIZE)
        self.ball_speed = [4, 4]

        self.left_paddle = pygame.Rect(MENU_WIDTH + 30, TOP_MENU_HEIGHT + (HEIGHT - TOP_MENU_HEIGHT - BOTTOM_MARGIN)//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.right_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, TOP_MENU_HEIGHT + (HEIGHT - TOP_MENU_HEIGHT - BOTTOM_MARGIN)//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

        self.left_score = 0
        self.right_score = 0

        self.mode = "AI"
        self.difficulty = "közepes" 

        self.paused = False
        self.set_difficulty_params()

    def set_difficulty_params(self):
        if self.difficulty == 'könnyű':
            self.ai_speed = 3
            self.ai_error_chance = 0.5
        elif self.difficulty == 'nehéz':
            self.ai_speed = 6
            self.ai_error_chance = 0.1
        else:
            self.ai_speed = 4
            self.ai_error_chance = 0.3

    def reset_ball(self):
        self.ball.topleft = (WIDTH//2, HEIGHT//2)
        self.ball_speed = [4 if random.choice([True, False]) else -4, 4]

    def update(self, keys):
        if self.paused:
            return

        if keys[pygame.K_w] and self.left_paddle.top > TOP_MENU_HEIGHT:
            self.left_paddle.move_ip(0, -5)
        if keys[pygame.K_s] and self.left_paddle.bottom < HEIGHT - BOTTOM_MARGIN:
            self.left_paddle.move_ip(0, 5)

        if self.mode == "2P":
            if keys[pygame.K_UP] and self.right_paddle.top > TOP_MENU_HEIGHT:
                self.right_paddle.move_ip(0, -5)
            if keys[pygame.K_DOWN] and self.right_paddle.bottom < HEIGHT - BOTTOM_MARGIN:
                self.right_paddle.move_ip(0, 5)
        else:
            if random.random() > self.ai_error_chance:
                if self.right_paddle.centery < self.ball.centery and self.right_paddle.bottom < HEIGHT - BOTTOM_MARGIN:
                    self.right_paddle.move_ip(0, self.ai_speed)
                elif self.right_paddle.centery > self.ball.centery and self.right_paddle.top > TOP_MENU_HEIGHT:
                    self.right_paddle.move_ip(0, -self.ai_speed)

        self.ball.move_ip(*self.ball_speed)

        if self.ball.top <= TOP_MENU_HEIGHT or self.ball.bottom >= HEIGHT - BOTTOM_MARGIN:
            self.ball_speed[1] *= -1

        if self.ball.colliderect(self.left_paddle) or self.ball.colliderect(self.right_paddle):
            self.ball_speed[0] *= -1

        if self.ball.left <= MENU_WIDTH:
            self.right_score += 1
            self.check_winner()
            self.reset_ball()

        if self.ball.right >= WIDTH:
            self.left_score += 1
            self.check_winner()
            self.reset_ball()
            
    def reset(self):
        self.ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_SIZE, BALL_SIZE)
        self.ball_speed = [4, 4]

        self.left_paddle = pygame.Rect(MENU_WIDTH + 30, TOP_MENU_HEIGHT + (HEIGHT - TOP_MENU_HEIGHT - BOTTOM_MARGIN)//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.right_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, TOP_MENU_HEIGHT + (HEIGHT - TOP_MENU_HEIGHT - BOTTOM_MARGIN)//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

        self.left_score = 0
        self.right_score = 0

    def check_winner(self):
        winner = None
        if self.left_score >= 11:
            winner = "Bal oldali játékos"
            if self.mode == "AI":
                winner = "Játékos"
        elif self.right_score >= 11:
            winner = "Jobb oldali játékos"
            if self.mode == "AI":
                winner = "AI"

        if winner:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("Játék vége", f"{winner} nyert!")
            root.destroy()

            self.left_score = 0
            self.right_score = 0
            self.reset_ball()
            self.paused = False

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (MENU_WIDTH, TOP_MENU_HEIGHT, WIDTH - MENU_WIDTH, HEIGHT - TOP_MENU_HEIGHT - BOTTOM_MARGIN))
        pygame.draw.rect(screen, WHITE, self.left_paddle)
        pygame.draw.rect(screen, WHITE, self.right_paddle)
        pygame.draw.ellipse(screen, RED, self.ball)
        score_text = FONT.render(f"{self.left_score} - {self.right_score}", True, BLACK)
        screen.blit(score_text, (WIDTH//2 + 75 - score_text.get_width()//2, HEIGHT - BOTTOM_MARGIN + 10))

    def save_game(self, filename="pong_save.json"):
        data = {
            "mode": self.mode,
            "difficulty": self.difficulty,
            "left_score": self.left_score,
            "right_score": self.right_score,
            "ball_pos": [self.ball.x, self.ball.y],
            "ball_speed": self.ball_speed,
            "left_paddle_y": self.left_paddle.y,
            "right_paddle_y": self.right_paddle.y
        }
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_game(self, filename="pong_save.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            self.mode = data["mode"]
            self.difficulty = data["difficulty"]
            self.left_score = data["left_score"]
            self.right_score = data["right_score"]
            self.ball.x, self.ball.y = data["ball_pos"]
            self.ball_speed = data["ball_speed"]
            self.left_paddle.y = data["left_paddle_y"]
            self.right_paddle.y = data["right_paddle_y"]

            self.set_difficulty_params()
            self.paused = False
        except Exception as e:
            print(f"Hiba betöltéskor: {e}")