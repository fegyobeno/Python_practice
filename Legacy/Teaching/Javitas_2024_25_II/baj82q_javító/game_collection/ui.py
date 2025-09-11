import pygame

def draw_sidebar(screen, manager):
    font = pygame.font.SysFont(None, 30)
    small_font = pygame.font.SysFont(None, 22)
    games = ["Pong", "Snake", "Block Breaker"]
    for i, name in enumerate(games):
        rect = pygame.Rect(0, 100 + i*60, 150, 50)
        pygame.draw.rect(screen, (80, 80, 80), rect)
        text = font.render(name, True, (255, 255, 255))
        screen.blit(text, (10, 110 + i*60))
        if pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos()):
            manager.switch_game(name)
    
    desc_y = 300
    desc_x = 10

    common_controls = [
        "Q: Mentés",
        "E: Betöltés",
        "P: Megállítás/Indítás"
    ]

    # Először az általános vezérlők
    for i, line in enumerate(common_controls):
        text = small_font.render(line, True, (200, 200, 200))
        screen.blit(text, (desc_x, desc_y + i * 22))

    # Most játék specifikus vezérlés
    desc_y += len(common_controls) * 22 + 20

    if manager.current_game_name == "Pong":
        pong_desc = [
            "Pong vezérlés:",
            "W/S: Player 1 fel/le",
            "Fel/Le nyíl: Player 2"
        ]
        for i, line in enumerate(pong_desc):
            text = small_font.render(line, True, (180, 255, 180))
            screen.blit(text, (desc_x, desc_y + i * 22))

    elif manager.current_game_name == "Snake":
        snake_desc = [
            "Snake vezérlés:",
            "W/A/S/D: Mozgás"
        ]
        for i, line in enumerate(snake_desc):
            text = small_font.render(line, True, (180, 255, 180))
            screen.blit(text, (desc_x, desc_y + i * 22))

    elif manager.current_game_name == "Block Breaker":
        block_desc = [
            "Block Breaker",
            "vezérlés:",
            "A/D: Balra/Jobbra"
        ]
        for i, line in enumerate(block_desc):
            text = small_font.render(line, True, (180, 255, 180))
            screen.blit(text, (desc_x, desc_y + i * 22))

def draw_topbar(screen, manager):
    font = pygame.font.SysFont(None, 30)
    difficulties = ["Easy", "Medium", "Hard"]
    for i, level in enumerate(difficulties):
        rect = pygame.Rect(160 + i*120, 10, 100, 40)
        pygame.draw.rect(screen, (50, 50, 50), rect)
        text = font.render(level, True, (255, 255, 255))
        screen.blit(text, (rect.x + 10, rect.y + 10))
        if pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos()):
            manager.set_difficulty(level)
    
    # Pong-specifikus AI vs Human gombok
    if manager.current_game_name == "Pong":
        modes = ["AI", "Human"]
        for i, mode in enumerate(modes):
            rect = pygame.Rect(540 + i * 110, 10, 100, 40)
            pygame.draw.rect(screen, (90, 90, 90), rect)
            text = font.render(mode, True, (255, 255, 255))
            screen.blit(text, (rect.x + 15, rect.y + 10))
            if pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos()):
                pong_game = manager.games["Pong"]
                pong_game.is_ai = (mode == "AI")
