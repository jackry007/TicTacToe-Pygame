import pygame, sys

pygame.init()

WIDTH = 700
HEIGHT = 700
LINEWIDTH = 15
#rgb
RED = (255,0,0)
BGCOLOR = (28,170,156)
LINE_COLOR = (23,145,135)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BGCOLOR)

#pygame.draw.line(screen,RED,(10,10),(300,300),10)

def draw_lines():
    #Horizontal lines
    pygame.draw.line(screen,LINE_COLOR,(0,HEIGHT/3),(WIDTH,HEIGHT/3),LINEWIDTH)
    pygame.draw.line(screen,LINE_COLOR,(0,2*HEIGHT/3),(WIDTH,2*HEIGHT/3),LINEWIDTH)
    #Vertical lines
    pygame.draw.line(screen,LINE_COLOR,(WIDTH/3,0),(WIDTH/3,HEIGHT),LINEWIDTH)
    pygame.draw.line(screen,LINE_COLOR,(2*WIDTH/3,0),(2*WIDTH/3,HEIGHT),LINEWIDTH)

draw_lines() 
# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    pygame.display.update()
            