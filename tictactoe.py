import pygame, sys
from tictacHelpers import *

# initializes pygame
pygame.init()

# Initialize the mixer
pygame.mixer.init()

# Load and play background music
pygame.mixer.music.load('background_music.mp3') 
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(start=60)  

# ------
# SCREEN
# ------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')

# Draw title screen initially
draw_title_screen(screen)

# ---------
# VARIABLES
# ---------
player = 1
game_over = False
game_started = False

# --------
# MAINLOOP
# --------
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
                mouseX = event.pos[0]  # x
                mouseY = event.pos[1]  # y

                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player, screen):
                        game_over = True
                        screen.fill(BG_COLOR)
                        draw_end_screen(screen, player)
                    elif is_board_full():
                        game_over = True
                        screen.fill(BG_COLOR)
                        draw_end_screen(screen, 0)
                    else:
                        player = player % 2 + 1
                    draw_figures(screen)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    restart(screen)
                    player = 1
                    game_over = False
                elif event.key == pygame.K_r and not game_started:
                    game_started = True
                    screen.fill(BG_COLOR)
                    draw_lines(screen)

    pygame.display.update()
