import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((500, 600))
pygame.display.set_caption('Space-Game')

icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

spaceship_x = 100
spaceship_y = 100

def display_spaceship(x, y):
    spaceship = pygame.image.load('spaceship.png')
    window.blit(spaceship, (x, y))

bg = pygame.image.load('skyy.png')

gameon = True
while gameon:
    window.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            gameon = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        spaceship_x -= 1
    if keys[K_RIGHT]:
        spaceship_x += 1
    if keys[K_UP]:
        spaceship_y -= 1
    if keys[K_DOWN]:
        spaceship_y += 1

    display_spaceship(spaceship_x, spaceship_y)

    pygame.display.update()

pygame.quit()
