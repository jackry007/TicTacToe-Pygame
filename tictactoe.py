import pygame  # type: ignore
import sys
import random
from tictacHelpers import *
import time

# initializes pygame
pygame.init()

# Initialize the mixer
pygame.mixer.init()

# Load and play background music, starting from 1:00 minute
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(start=60)

# SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')

# Draw title screen initially
draw_title_screen(screen)

# GAME STATES VARIABLES
player = 1
game_over = False
game_started = False
score = {1: 0, 2: 0}  # Dictionary to keep track of wins for each player

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            sys.exit()

        if not game_started:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_started = True
                    screen.fill(BG_COLOR)
                    draw_lines(screen)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)

                if available_square(board, clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player, screen):
                        score[player] += 1
                        game_over = True
                        screen.fill(BG_COLOR)
                        draw_end_screen(screen, player, score)
                    elif is_board_full():
                        game_over = True
                        screen.fill(BG_COLOR)
                        draw_end_screen(screen, 0, score)
                    else:
                        player = player % 2 + 1
                    draw_figures(screen)
            # AI's turn
            if not game_over and player == 2:
                ai_move = random_ai(board)
                if ai_move is not None:
                    ai_row, ai_col = ai_move
                    mark_square(ai_row, ai_col, player)
                    if check_win(player, screen):
                        score[player] += 1
                        game_over = True
                        screen.fill(BG_COLOR)
                        draw_end_screen(screen, player, score)
                    elif is_board_full():
                        game_over = True
                        screen.fill(BG_COLOR)
                        draw_end_screen(screen, 0, score)
                    else:
                        player = player % 2 + 1
                    draw_figures(screen)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    # Restart the game if it's over and 'R' key is pressed
                    restart(screen)
                    player = 1
                    game_over = False
                elif event.key == pygame.K_r and not game_started:
                    # If the game hasn't started and 'R' key is pressed, start the game again
                    game_started = True
                    screen.fill(BG_COLOR)
                    draw_lines(screen)
    pygame.display.update()
