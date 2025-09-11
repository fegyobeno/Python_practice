import pygame
import sys
from menu import *
from pong import *
from minesweeper import *
from snake import *
from constants import *

pygame.init()

# --- Fő program ---
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Játékgyűjtemény")

    clock = pygame.time.Clock()

    pong = PongGame()
    minesweeper = MineSweeperGame()
    snake = SnakeGame()

    game_buttons, menu_buttons, difficulty_buttons = create_menu()

    current_game = "Pong_AI" 

    running = True
    while running:
        screen.fill(WHITE)

        keys = pygame.key.get_pressed()

        pygame.draw.rect(screen, GRAY, (0, 0, MENU_WIDTH, HEIGHT))
        pygame.draw.rect(screen, GRAY, (MENU_WIDTH, 0, WIDTH - MENU_WIDTH, TOP_MENU_HEIGHT))
        pygame.draw.line(screen, BLACK, (MENU_WIDTH, 0), (MENU_WIDTH, HEIGHT), 3)
        pygame.draw.line(screen, BLACK, (0, TOP_MENU_HEIGHT), (WIDTH, TOP_MENU_HEIGHT), 3)
        pygame.draw.line(screen, BLACK, (MENU_WIDTH, HEIGHT - BOTTOM_MARGIN), (WIDTH, HEIGHT - BOTTOM_MARGIN), 3)

        for btn in game_buttons:
            btn.draw(screen)
        for btn in menu_buttons:
            btn.draw(screen)
        for btn in difficulty_buttons:
            btn.draw(screen)

        if current_game.startswith("Pong"):
            pong.update(keys)
            pong.draw(screen)
        elif current_game == "MineSweeper":
            minesweeper.draw(screen)
        elif current_game == "Snake":
            snake.update()
            snake.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if current_game == "Snake":
                    snake.handle_key(event.key)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                    
                for i, btn in enumerate(game_buttons):
                    if btn.rect.collidepoint(mx, my):
                        if i == 0:
                            current_game = "Pong_AI"
                            pong.mode = "AI"
                            pong.reset()
                        elif i == 1:
                            current_game = "Pong_2P"
                            pong.mode = "2P"
                            pong.reset()
                        elif i == 2:
                            current_game = "MineSweeper"
                        elif i == 3:
                            current_game = "Snake"

                for btn in menu_buttons:
                    if btn.rect.collidepoint(mx, my):
                        if btn.text == "Mentés":
                            if current_game.startswith("Pong"):
                                pong.save_game()
                            elif current_game == "MineSweeper":
                                minesweeper.save_game()
                            elif current_game == "Snake":
                                snake.save_game()

                        elif btn.text == "Betöltés":
                            if current_game.startswith("Pong"):
                                pong.load_game()
                            elif current_game == "MineSweeper":
                                minesweeper.load_game()
                            elif current_game == "Snake":
                                snake.load_game()

                        elif btn.text == "Megállít / Folytat":
                            if current_game.startswith("Pong"):
                                pong.paused = not pong.paused
                            elif current_game == "MineSweeper":
                                minesweeper.paused = not minesweeper.paused
                            elif current_game == "Snake":
                                snake.paused = not snake.paused

                for btn in difficulty_buttons:
                    if btn.rect.collidepoint(mx, my):
                        diff = btn.text.lower()
                        if current_game.startswith("Pong"):
                            pong.difficulty = diff
                            pong.set_difficulty_params()
                        elif current_game == "MineSweeper":
                            minesweeper.set_difficulty(diff)
                        elif current_game == "Snake":
                            snake.set_difficulty(diff)

                if current_game == "MineSweeper" and not minesweeper.paused:
                    grid_x = (mx - minesweeper.offset_x) // minesweeper.cell_size
                    grid_y = (my - minesweeper.offset_y) // minesweeper.cell_size

                    if 0 <= grid_x < minesweeper.grid_size and 0 <= grid_y < minesweeper.grid_size:
                        if event.button == 1:
                            minesweeper.reveal_cell(grid_x, grid_y)
                        elif event.button == 3:
                            minesweeper.toggle_flag(grid_x, grid_y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
