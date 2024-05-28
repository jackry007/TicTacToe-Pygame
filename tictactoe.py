import pygame, sys
from tictacHelpers import draw_lines

pygame.init()

WIDTH = 700
HEIGHT = 700
LINEWIDTH = 15
# rgb
RED = (255, 0, 0)
BGCOLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BGCOLOR)

draw_lines(screen) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    pygame.display.update()
