import pygame
from player import Player
from generic_enemy import GenericEnemy
from sys import exit
from weapon import Weapon
from setting import*
from level import Level
from game_data import level_0
# Starts & intiates pygame
pygame.init()
weaponO = Weapon()
playerO = Player(weaponO)
enemyO = GenericEnemy(playerO)
enemy = pygame.sprite.Group()
enemy.add(enemyO)
player = pygame.sprite.Group()
player.add(playerO)
WIDTH = 1366
HEIGHT = 768
started = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Soup')
# You can also change the icon
clock = pygame.time.Clock()
floor_surface = pygame.image.load('Textures/frames/floor_1.png').convert()
ui0 = Ui(screen, WIDTH, HEIGHT, floor_surface, started)
start = Start(screen, WIDTH, HEIGHT, floor_surface, started)
over = GameOver(screen, WIDTH, HEIGHT, floor_surface, started)
img = Images()
level=Level(level_0,screen)
speed =5
#running = True
game_over = True

while True:
    # if game_over:
    #     over.gameOver()
    #     game_over = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # check for (W, A, S, D)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerO.left_pressed = True
                level.x_scroll+=speed
            if event.key == pygame.K_d:
                playerO.right_pressed = True
                level.x_scroll -= speed
            if event.key == pygame.K_w:
                playerO.up_pressed = True
                level.y_scroll -= speed
            if event.key == pygame.K_s:
                playerO.down_pressed = True
                level.y_scroll += speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                playerO.left_pressed = False
                level.x_scroll=0
            if event.key == pygame.K_d:
                playerO.right_pressed = False
                level.x_scroll=0
            if event.key == pygame.K_w:
                playerO.up_pressed = False
                level.y_scroll=0
            if event.key == pygame.K_s:
                playerO.down_pressed = False
                level.y_scroll=0
        # check for mouse movement and changes rotation true when moving as we don't want the weapon to follow the mouse when the mouse isn't moving
        if event.type == pygame.MOUSEMOTION:
            weaponO.rotation = True
            weaponO.mx, weaponO.my = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            weaponO.attackFlag = 20
            weaponO.attackDelay()
        if event.type == pygame.MOUSEBUTTONUP:
            weaponO.attackFlag = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            ui0.paused()
    # draw all out elements
    # Updates the display
   
    screen.fill('black')
    # debug purposes
    # screen.blit(pygame.transform.scale(img.pause_surface,(50,50)),(WIDTH-50,0))
    start.startUi()
    ui0.health()
    enemy.draw(screen)
    enemy.update()
    player.draw(screen)
    player.update()
    weaponO.update()
    weaponO.draw(screen)
    level.run()
    pygame.display.update()
    # Locks the frame rate at 60 fps
    # not very clean code
    weaponO.direction = playerO.direction
    clock.tick(60)
