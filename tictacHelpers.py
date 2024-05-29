import pygame
import numpy as np

# ---------
# CONSTANTS
# ---------
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# -------------
# CONSOLE BOARD
# -------------
board = np.zeros((BOARD_ROWS, BOARD_COLS))


def draw_lines(screen):
    """Draws the horizontal and vertical lines on the screen to create the Tic Tac Toe board."""
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE),
                     (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE),
                     (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    # 1 vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0),
                     (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0),
                     (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_figures(screen):
    """Draws the X and O figures on the screen based on the current state of the board."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(
                    row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE -
                                 SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)


def mark_square(row, col, player):
    """Marks the square at the given row and column with the player's symbol."""
    board[row][col] = player


def available_square(row, col):
    """Checks if the square at the given row and column is available."""
    return board[row][col] == 0


def is_board_full():
    """Checks if the board is full."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


def check_win(player, screen):
    """Checks if the current player has won the game."""
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player, screen)
            return True

    # horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player, screen)
            return True

    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player, screen)
        return True

    # desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player, screen)
        return True

    return False


def draw_vertical_winning_line(col, player, screen):
    """Draws a vertical winning line on the screen."""
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, 15),
                     (posX, HEIGHT - 15), LINE_WIDTH)


def draw_horizontal_winning_line(row, player, screen):
    """Draws a horizontal winning line on the screen."""
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY),
                     (WIDTH - 15, posY), WIN_LINE_WIDTH)


def draw_asc_diagonal(player, screen):
    """Draws an ascending diagonal winning line on the screen."""
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT - 15),
                     (WIDTH - 15, 15), WIN_LINE_WIDTH)


def draw_desc_diagonal(player, screen):
    """Draws a descending diagonal winning line on the screen."""
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, 15),
                     (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)


def restart(screen):
    """Resets the game by clearing the board and redrawing the lines."""
    screen.fill(BG_COLOR)
    draw_lines(screen)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


def draw_title_screen(screen):
    """Draws the title screen with the game title and start instructions."""
    screen.fill(BG_COLOR)

    # Title text
    font_title = pygame.font.Font(None, 74)
    title_text = font_title.render('TIC TAC TOE', True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(title_text, title_rect)

    # Start instructions
    font_start = pygame.font.Font(None, 36)
    start_text = font_start.render(
        'Press SPACE to Start', True, (255, 255, 255))
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(start_text, start_rect)

    pygame.display.flip()


def draw_end_screen(screen, winner, score):
    """Draws the end screen with the game result, scoreboard, and restart instructions."""
    screen.fill(BG_COLOR)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

    font = pygame.font.Font(None, 74)

    if winner == 0:
        end_text = font.render('Draw!', True, (255, 255, 255))
    else:
        winner_text = 'Player 1 Wins!' if winner == 1 else 'Player 2 Wins!'
        end_text = font.render(winner_text, True, (255, 255, 255))

    screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 4))

    # Scoreboard
    font_score = pygame.font.Font(None, 36)
    score_text = font_score.render("Player 1: {}  Player 2: {}".format(
        score[1], score[2]), True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(score_text, score_rect)

    font_restart = pygame.font.Font(None, 36)
    restart_text = font_restart.render(
        'Press R to Restart', True, (255, 255, 255))
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4))
    screen.blit(restart_text, restart_rect)

    pygame.display.flip()
