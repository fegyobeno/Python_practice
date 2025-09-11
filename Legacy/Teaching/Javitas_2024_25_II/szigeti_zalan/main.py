import pygame
import pickle
import os
from menu import Menu
from pong import PongGame
from tetris import TetrisGame
from snake import SnakeGame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
menu = Menu(800, 600)

current_game = None
paused = False
running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    selected = menu.update(screen)

    # Váltás új játékra
    if selected and selected != menu.selected_game:
        menu.selected_game = selected
        paused = False
        if selected == "Pong":
            current_game = PongGame(menu.get_difficulty())
        elif selected == "Tetris":
            current_game = TetrisGame(menu.get_difficulty())
        elif selected == "Snake":
            current_game = SnakeGame(menu.get_difficulty())

    if menu.last_action == "pause":
        paused = not paused
    elif menu.last_action == "save" and current_game and menu.selected_game:
        with open(f"save_{menu.selected_game.lower()}.pkl", "wb") as f:
            pickle.dump(current_game, f)
    elif menu.last_action == "load" and menu.selected_game:
        filename = f"save_{menu.selected_game.lower()}.pkl"
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                try:
                    current_game = pickle.load(f)
                    paused = False
                except Exception as e:
                    print(f"Error loading saved game: {e}")
        else:
            print("Save file does not exist.")

    if current_game and not paused:
        current_game.update()
        current_game.draw(screen)
    elif current_game and paused:
        current_game.draw(screen)
        menu.draw_overlay(screen, paused)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
