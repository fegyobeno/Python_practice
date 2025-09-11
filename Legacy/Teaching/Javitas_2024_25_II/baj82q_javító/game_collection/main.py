import pygame
from game_manager import GameManager
from ui import draw_sidebar, draw_topbar

pygame.init()
WIDTH, HEIGHT = 960, 660
SIDEBAR_WIDTH = 160
TOPBAR_HEIGHT = 60
GAME_AREA = pygame.Rect(SIDEBAR_WIDTH, TOPBAR_HEIGHT, WIDTH - SIDEBAR_WIDTH, HEIGHT - TOPBAR_HEIGHT)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Játékgyűjtemény")
clock = pygame.time.Clock()

manager = GameManager()

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manager.handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            manager.check_resume_click(event.pos)

    draw_sidebar(screen, manager)
    draw_topbar(screen, manager)

    manager.update()
    manager.draw(screen.subsurface(GAME_AREA))

    pygame.draw.rect(screen, (200, 200, 200), GAME_AREA, 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
