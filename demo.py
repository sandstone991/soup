import pygame
from player import Player
from sys import exit
# Starts & intiates pygame
pygame.init()
playerO = Player(500, 500)
player = pygame.sprite.GroupSingle()
player.add(playerO)
WIDTH = 1366
HEIGHT = 768
# def Game:
#     def __init__(self):

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Runner')
# You can also change the icon
clock = pygame.time.Clock()
floor_surface = pygame.image.load('Textures/frames/floor_1.png').convert()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # check for (W, A, S, D)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerO.left_pressed = True
            if event.key == pygame.K_d:
                playerO.right_pressed = True
            if event.key == pygame.K_w:
                playerO.up_pressed = True
            if event.key == pygame.K_s:
                playerO.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                playerO.left_pressed = False
            if event.key == pygame.K_d:
                playerO.right_pressed = False
            if event.key == pygame.K_w:
                playerO.up_pressed = False
            if event.key == pygame.K_s:
                playerO.down_pressed = False
    # draw all out elements
    # update everything
    # Updates the display
    for i in range(0, HEIGHT, 16):
        for k in range(0, WIDTH, 16):
            screen.blit(floor_surface, (k, i))
    player.draw(screen)
    player.update()
    pygame.display.update()
    # Locks the frame rate at 60 fps
    clock.tick(60)
