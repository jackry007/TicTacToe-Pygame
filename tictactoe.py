import pygame
import sys
from tictacHelpers import *

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

# MAINLOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Stop music and quit the game if the window is closed
            pygame.mixer.music.stop()
            sys.exit()

        if not game_started:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Start the game when SPACE key is pressed
                    game_started = True
                    screen.fill(BG_COLOR)
                    draw_lines(screen)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]  # x
                mouseY = event.pos[1]  # y

                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)

                if available_square(clicked_row, clicked_col):
                    # Mark the square if it's available
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player, screen):
                        # If a player wins, update the score, end the game, and display the end screen
                        score[player] += 1
                        game_over = True
                        screen.fill(BG_COLOR)
                        draw_end_screen(screen, player, score)
                    elif is_board_full():
                        # If the board is full and no one wins, end the game and display the end screen with a draw message
                        game_over = True
                        screen.fill(BG_COLOR)
                        draw_end_screen(screen, 0, score)
                    else:
                        # Switch player for the next turn
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
