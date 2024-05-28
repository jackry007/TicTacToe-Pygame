import pygame

WIDTH = 700
HEIGHT = 700
LINEWIDTH = 15
LINE_COLOR = (23, 145, 135)

def draw_lines(screen):
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), LINEWIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * HEIGHT / 3), (WIDTH, 2 * HEIGHT / 3), LINEWIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), LINEWIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * WIDTH / 3, 0), (2 * WIDTH / 3, HEIGHT), LINEWIDTH)