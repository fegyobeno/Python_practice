import pygame

WHITE = (255, 255, 255)
BALL_SPEED = 5
PADDLE_SPEED = 5

class Paddle:
    def __init__(self, x, controls=None):
        self.rect = pygame.Rect(x, 250, 10, 100)
        self.controls = controls or {}
    
    def move(self, keys):
        if self.controls.get("up") and keys[self.controls["up"]]:
            self.rect.y -= PADDLE_SPEED
        if self.controls.get("down") and keys[self.controls["down"]]:
            self.rect.y += PADDLE_SPEED
        self.rect.y = max(0, min(500, self.rect.y))

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(395, 295, 10, 10)
        self.vel = [BALL_SPEED, BALL_SPEED]

    def update(self, paddle1, paddle2):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.vel[1] *= -1
        if self.rect.colliderect(paddle1.rect) or self.rect.colliderect(paddle2.rect):
            self.vel[0] *= -1

class PongGame:
    def __init__(self):
        self.p1 = Paddle(20, {"up": pygame.K_w, "down": pygame.K_s})
        self.p2 = Paddle(770, {"up": pygame.K_UP, "down": pygame.K_DOWN})
        self.ball = Ball()
        self.is_ai = True
        self.difficulty = "Medium"
        self.scores = [0, 0]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                self.is_ai = not self.is_ai
                print("AI mód:", "bekapcsolva" if self.is_ai else "kikapcsolva")

    def update(self, difficulty):
        self.difficulty = difficulty
        keys = pygame.key.get_pressed()
        self.p1.move(keys)

        if self.is_ai:
            self.ai_move(self.p2, self.ball)
        else:
            self.p2.move(keys)

        self.ball.update(self.p1, self.p2)

        if self.ball.rect.left <= 0:
            self.scores[1] += 1
            self.ball = Ball()
        elif self.ball.rect.right >= 800:
            self.scores[0] += 1
            self.ball = Ball()

    def ai_move(self, paddle, ball):
        speed = {"Easy": 2, "Medium": 4, "Hard": 6}.get(self.difficulty, 4)
        if paddle.rect.centery < ball.rect.centery:
            paddle.rect.y += speed
        elif paddle.rect.centery > ball.rect.centery:
            paddle.rect.y -= speed
        paddle.rect.y = max(0, min(500, paddle.rect.y))

    def draw(self, screen, difficulty=None):
        pygame.draw.rect(screen, WHITE, self.p1.rect)
        pygame.draw.rect(screen, WHITE, self.p2.rect)
        pygame.draw.ellipse(screen, WHITE, self.ball.rect)
        font = pygame.font.SysFont(None, 40)
        score = font.render(f"{self.scores[0]} : {self.scores[1]}", True, WHITE)
        screen.blit(score, (370, 20))

    def get_state(self):
        return {
            "p1_y": self.p1.rect.y,
            "p2_y": self.p2.rect.y,
            "ball_pos": list(self.ball.rect.topleft),
            "ball_vel": self.ball.vel,
            "scores": self.scores,
            "is_ai": self.is_ai,
            "difficulty": self.difficulty
        }

    def load_state(self, state):
        self.p1.rect.y = state.get("p1_y", 250)
        self.p2.rect.y = state.get("p2_y", 250)
        self.ball.rect.topleft = state.get("ball_pos", [395, 295])
        self.ball.vel = state.get("ball_vel", [BALL_SPEED, BALL_SPEED])
        self.scores = state.get("scores", [0, 0])
        self.is_ai = state.get("is_ai", True)
        self.difficulty = state.get("difficulty", "Medium")

