import pygame
from pygame import surface
from player import Player
from generic_enemy import GenericEnemy
from sys import exit
from weapon import Weapon
from ui import Ui,Start
WIDTH = 1366
HEIGHT = 768
# Starts & intiates pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

weaponO = Weapon()
playerO = Player(weaponO)
enemyO = GenericEnemy(player=playerO,screen=screen)
enemy = pygame.sprite.Group()
enemy.add(enemyO)
player = pygame.sprite.Group()
player.add(playerO)

#to control paused function in ui
started = True
pygame.display.set_caption('Soup')
# You can also change the icon
clock = pygame.time.Clock()
floor_surface = pygame.image.load('Textures/frames/floor_1.png').convert()
ui0 = Ui(screen,WIDTH,HEIGHT,floor_surface,started)
start = Start(screen,WIDTH,HEIGHT,floor_surface,started)
while True:
    start.startUi()
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
        # check for mouse movement and changes rotation true when moving as we don't want the weapon to follow the mouse when the mouse isn't moving
        if event.type == pygame.MOUSEMOTION:
            weaponO.rotation = True
            weaponO.mx, weaponO.my = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            weaponO.attackFlag = 20
            weaponO.attackDelay()
            enemyO.damageFlag = 5

        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                ui0.paused()

    # draw all out elements
    # Updates the display
    for i in range(0, HEIGHT, 16):
        for k in range(0, WIDTH, 16):
            screen.blit(floor_surface, (k, i))
    # debug purposes

    enemy.draw(screen)
    enemy.update()
    player.draw(screen)
    player.update()
    weaponO.update()
    weaponO.draw(screen)
    pygame.display.update()
    # Locks the frame rate at 60 fps
    #not very clean code
    weaponO.direction = playerO.direction
    clock.tick(60)
