import pygame

class Paddle:
    def __init__(self, x, keys=None):
        self.rect = pygame.Rect(x, 250, 10, 100)
        self.speed = 5
        self.keys = keys

    def move(self, keys):
        if self.keys:
            if keys[self.keys[0]]:
                self.rect.y -= self.speed
            if keys[self.keys[1]]:
                self.rect.y += self.speed

    def ai_move(self, ball, difficulty):
        if difficulty == "Easy": speed = 3
        elif difficulty == "Hard": speed = 7
        else: speed = 5

        if ball.centery > self.rect.centery:
            self.rect.y += speed
        elif ball.centery < self.rect.centery:
            self.rect.y -= speed

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(390, 290, 20, 20)
        self.vx = 4
        self.vy = 4

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.vy *= -1

class PongGame:
    def __init__(self, difficulty):
        self.left = Paddle(20, (pygame.K_w, pygame.K_s))
        self.right = Paddle(770)
        self.ball = Ball()
        self.difficulty = difficulty
        self.mode = "AI"  # Or "Human"

    def update(self):
        keys = pygame.key.get_pressed()
        self.left.move(keys)
        if self.mode == "Human":
            self.right.keys = (pygame.K_UP, pygame.K_DOWN)
            self.right.move(keys)
        else:
            self.right.ai_move(self.ball.rect, self.difficulty)

        self.ball.move()

        for paddle in [self.left, self.right]:
            if paddle.rect.colliderect(self.ball.rect):
                self.ball.vx *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.left.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.right.rect)
        pygame.draw.ellipse(screen, (255, 255, 255), self.ball.rect)

    def get_state(self):
        return {
            "ball": [self.ball.rect.x, self.ball.rect.y, self.ball.vx, self.ball.vy],
            "left": self.left.rect.y,
            "right": self.right.rect.y,
            "mode": self.mode
        }

    def set_state(self, state):
        self.ball.rect.x, self.ball.rect.y, self.ball.vx, self.ball.vy = state["ball"]
        self.left.rect.y = state["left"]
        self.right.rect.y = state["right"]
        self.mode = state.get("mode", "AI")