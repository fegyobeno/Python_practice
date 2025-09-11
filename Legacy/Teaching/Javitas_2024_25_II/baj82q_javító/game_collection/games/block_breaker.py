import pygame
import random

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

class BlockBreaker:
    def __init__(self, difficulty="Medium"):
        self.difficulty = difficulty  # tároljuk a nehézségi szintet
        self.paddle = pygame.Rect(350, 550, 100, 10)
        self.ball = pygame.Rect(390, 300, 10, 10)
        self.ball_speed = [4, -4]
        self.blocks = [pygame.Rect(x * 60 + 5, y * 30 + 5, 55, 25)
                       for y in range(5) for x in range(12)]
        self.score = 0

    def handle_event(self, event):
        pass

    def update(self, difficulty):
        # ha változott a nehézség, frissítjük a tárolt értéket
        if difficulty != self.difficulty:
            self.difficulty = difficulty

        keys = pygame.key.get_pressed()
        speed = {"Easy": 6, "Medium": 8, "Hard": 10}.get(self.difficulty, 8)

        if keys[pygame.K_a]:
            self.paddle.x -= speed
        if keys[pygame.K_d]:
            self.paddle.x += speed
        self.paddle.x = max(0, min(700, self.paddle.x))

        self.ball.x += self.ball_speed[0]
        self.ball.y += self.ball_speed[1]

        if self.ball.left <= 0 or self.ball.right >= 800:
            self.ball_speed[0] *= -1
        if self.ball.top <= 0:
            self.ball_speed[1] *= -1
        if self.ball.colliderect(self.paddle):
            self.ball_speed[1] *= -1

        hit_block = self.ball.collidelist(self.blocks)
        if hit_block != -1:
            del self.blocks[hit_block]
            self.ball_speed[1] *= -1
            self.score += 1

        if self.ball.bottom >= 600:
            self.__init__(self.difficulty)  # újraindítás a korábbi nehézségi szinttel

    def draw(self, screen, difficulty=None):
        pygame.draw.rect(screen, WHITE, self.paddle)
        pygame.draw.ellipse(screen, RED, self.ball)
        for block in self.blocks:
            pygame.draw.rect(screen, BLUE, block)
        font = pygame.font.SysFont(None, 30)
        score = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score, (650, 10))

    def get_state(self):
        return {
            "paddle_x": self.paddle.x,
            "ball_pos": list(self.ball.topleft),
            "ball_speed": self.ball_speed,
            "blocks": [list(b.topleft) for b in self.blocks],
            "score": self.score,
            "difficulty": self.difficulty
        }

    def load_state(self, state):
        self.paddle.x = state["paddle_x"]
        self.ball.topleft = state["ball_pos"]
        self.ball_speed = state["ball_speed"]
        self.blocks = [pygame.Rect(x, y, 55, 25) for x, y in state["blocks"]]
        self.score = state["score"]
        self.difficulty = state.get("difficulty", "Medium")