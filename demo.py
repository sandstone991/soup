import pygame
from player import Player
from generic_enemy import GenericEnemy
from sys import exit
from weapon import Weapon
# Starts & intiates pygame
pygame.init()
weaponO = Weapon()
playerO = Player(weaponO)
enemyO = GenericEnemy(playerO)
enemy = pygame.sprite.Group()
enemy.add(enemyO)
player = pygame.sprite.Group()
player.add(playerO)
WIDTH = 1500
HEIGHT = 800
wall_left_rect=pygame.Rect(35,100,1,HEIGHT)
wall_left2_rect=pygame.Rect(240,160,1,60)
wall_left3_rect=pygame.Rect(560,130,1,110)
wall_left4_rect=pygame.Rect(580,300,1,190)
wall_left5_rect=pygame.Rect(580,560,1,140)
wall_left6_rect=pygame.Rect(1075,50,1,190)
wall_leftlast_rect=pygame.Rect(WIDTH-215,130,1,HEIGHT-50)
wall_right_rect=pygame.Rect(WIDTH-140,50,1,HEIGHT-130)
wall_right2_rect=pygame.Rect(WIDTH-345,130,1,HEIGHT-600)
wall_right3_rect=pygame.Rect(WIDTH-525,330,1,HEIGHT-410)
wall_right4_rect=pygame.Rect(290,100,1,140)
wall_right5_rect=pygame.Rect(160,560,1,140)
wall_right6_rect=pygame.Rect(130,310,1,140)
wall_right7_rect=pygame.Rect(110,50,1,50)
wall_right8_rect=pygame.Rect(WIDTH-540,130,1,100)
wall_right9_rect=pygame.Rect(1170,700,1,100)
wall_top_rect=pygame.Rect(0,46,WIDTH,1)
wall_top2_rect=pygame.Rect(115,110,200,1)
wall_top3_rect=pygame.Rect(290,240,270,1)
wall_top4_rect=pygame.Rect(550,126,500,1)
wall_top5_rect=pygame.Rect(35,224,210,1)
wall_top6_rect=pygame.Rect(35,495,540,1)
wall_top7_rect=pygame.Rect(160,700,420,1)
wall_top8_rect=pygame.Rect(960,240,110,1)
wall_top9_rect=pygame.Rect(980,720,190,1)
wall_top10_rect=pygame.Rect(1360,740,150,1)
wall_bottom_rect=pygame.Rect(0,HEIGHT-20,WIDTH,1)
wall_bottom2_rect=pygame.Rect(35,160,200,1)
wall_bottom3_rect=pygame.Rect(130,300,450,1)
wall_bottom4_rect=pygame.Rect(160,560,410,1)
wall_bottom5_rect=pygame.Rect(980,320,170,1)
wall_bottom6_rect=pygame.Rect(1155,125,130,1)
wall_bottom7_rect=pygame.Rect(35,445,100,1)


screen = pygame.display.set_mode((WIDTH, HEIGHT))

floor_surface = pygame.image.load('Textures/frames/floor_3.png').convert()

wall_side= pygame.image.load('Textures/frames/wall_side_mid_right.png')
wall_top=pygame.image.load('Textures/frames/wall_inner_corner_t_top_left.png')
wall_corner_l=pygame.image.load('Textures/frames/wall_inner_corner_l_top_left.png')
wall_corner_7=pygame.image.load('Textures/frames/wall_inner_corner_l_top_left_mirrored.png')
wall_corner_c=pygame.image.load('Textures/frames/wall_inner_corner_l_top_rigth.png').convert()
wall_corner_m=pygame.image.load('Textures/frames/mirror.png').convert()
wall_side_top_left=pygame.image.load('Textures/frames/wall_side_top_right.png').convert()
door_closed=pygame.image.load('Textures/frames/doors_leaf_closed.png').convert()
door_opened=pygame.image.load('Textures/frames/doors_leaf_open.png')
wall=pygame.image.load('Textures/frames/wall_mid.png')
map1 ="""                             
                             
hhhhhhh                                                            hhhhhhhhhhhhhhhhhh
0000000v                                                           v00000000000000000v
0000000v                                                           v00000000000000000v
hh00000v                                                           v00000000000000000v
  v0000lhhhhhhhhhh                                                 v00000000000000000v
  v000000000000000v                hhhhhhhhhhhhhhhhhhhhhhhhh       v0000hhhhhhhh00000v
  v000000000000000v                v000000000000000000000000v      v0000v       v0000v
  lhhhhhhhhhhhh000v                v000000000000000000000000v      v0000v       v0000v
               v00v                v000000000000000000000000v      v0000v       v0000v
               v00v                v000000000000000000000000v      v0000v       v0000v
               v00v                v000000000000000000000000v      v0000v       v0000v
  hhhhhhhhhhhh7000v                v000000000000000000000000v      v0000v       v0000v
  v000000000000000lhhhhhhhhhhhhhhh7 000000000000000000000000lhhhhh700000v       v0000v
  v000000000000000000000000000000000000000000000000000000000000000000000v       v0000v
  v000000000000000000000000000000000000000000000000000000000000000000000v       v0000v
  v000000000000000000000000000000000000000000000000000000000000000000000v       v0000v   
  v00000hhhhhhhhhhhhhhhhhhhhhhhhhhhh000000000000000000000000000000000000v       v0000v
  v00000v                           v000000000000000000000000hhhhhhhhhh7        v0000v
  v00000v                           v000000000000000000000000v                  v0000v                 
  v00000v                           v000000000000000000000000v                  v0000v
  v00000v                           v000000000000000000000000v                  v0000v
  v00000v                           v000000000000000000000000v                  v0000v
  v00000v                           v000000000000000000000000v                  v0000v
  v00000v                           v000000000000000000000000v                  v0000v
  v00000v                           v000000000000000000000000v                  v0000v
  lhhhh7                            v000000000000000000000000v                  v0000v
                                    v000000000000000000000000v                  v0000v
                                    v000000000000000000000000v                  v0000v
  hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh7 000000000000000000000000v                  v0000v
  v0000000000000000000000000000000000000000000000000000000000v                  v0000v              
  v0000000000000000000000000000000000000000000000000000000000v                  v0000v
  v0000000000000000000000000000000000000000000000000000000000v                  v0000v
  v0000000hhhhhhhhhhhhhhhhhhhhhhhhhh0000000000000000000000000v                  v0000v
  v0000000v                         v000000000000000000000000v                  v0000v
  v0000000v                         v000000000000000000000000v                  v0000v
  v0000000v                         v000000000000000000000000v                  v0000v
  v0000000v                         v000000000000000000000000v                  v0000v
  v0000000v                         v000000000000000000000000v                  v0000v
  v0000000v                         v000000000000000000000000v                  v0000v
  v0000000v                         v000000000000000000000000v                  v0000v
  v0000000v                         v000000000000000000000000v                  v0010v
  v0000000lhhhhhhhhhhhhhhhhhhhhhhhhhv000000000000000000000000v                  v0000v
  v0000000000000000000000000000000000000000000000000000000000lhhhhhhhhhhh       v0000v
  v0000000000000000000000000000000000000000000000000000000000000000000000v      v0000lhhhhhhhh
  v0000000000000000000000000000000000000000000000000000000000000000000000v      v0000000000000
  v0000000000000000000000000000000000000000000000000000000000000000000000v      v0000000000000
  lhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh7       lhhhhhhhhhhhhh
      
"""    



def tiles(map1):
    global tile
    for y, line in enumerate(map1):
        for x, c in enumerate(line):
            if c== "0":
                screen.blit(floor_surface, (x*16, y*16))
            if c == "h":
                screen.blit(wall_top, (x * 16, y * 16))
            if c== "v":
                screen.blit(wall_side,(x * 16, y * 16))
            if c== "l":
                screen.blit(wall_corner_l,(x * 16, y * 16))
            if c== "7":
                screen.blit(wall_corner_7,(x * 16, y * 16))
            if c== "1":
                screen.blit(door_closed,(x * 16, y * 16))
            if c== "m":
                screen.blit(wall_corner_m,(x * 16, y * 16))
            if c== "c":
                screen.blit(wall_corner_c,(x * 16, y * 16))
           

map1 = map1.splitlines()
pygame.display.set_caption('Soup')
# You can also change the icon
clock = pygame.time.Clock()

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
        # check for mouse movement and changes rotation true when moving as we don't want the weapon to follow the mouse when the mouse isn't moving
        if event.type == pygame.MOUSEMOTION:
            weaponO.rotation = True
            weaponO.mx, weaponO.my = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            weaponO.attackFlag = True
            weaponO.attackDelay()
        if event.type == pygame.MOUSEBUTTONUP:
            weaponO.attackFlag = False

   
    # draw all out elements
    
    # Updates the display
    for i in range(0, HEIGHT, 16):
        for k in range(0, WIDTH, 16):
            screen.blit(floor_surface, (k, i))
            """screen.blit(wall_side, (0, i))
            screen.blit(wall_side, (WIDTH-5, i))
            screen.blit(wall_top, (k, -12))
            screen.blit(wall_top, (k, HEIGHT-18))"""
    #
    tiles(map1)
    # debug purposes
    if playerO.rect.colliderect(wall_right_rect) or playerO.rect.colliderect(wall_right2_rect) or playerO.rect.colliderect(wall_right3_rect)or playerO.rect.colliderect(wall_right4_rect)or playerO.rect.colliderect(wall_right5_rect) or playerO.rect.colliderect(wall_right6_rect) or playerO.rect.colliderect(wall_right7_rect) or playerO.rect.colliderect(wall_right8_rect) or playerO.rect.colliderect(wall_right9_rect):
        """pygame.draw.rect(screen,(0,255,0),wall_right_rect)
        pygame.draw.rect(screen,(0,255,0),wall_right2_rect)
        pygame.draw.rect(screen,(0,255,0),wall_right3_rect)
        pygame.draw.rect(screen,(0,255,0),wall_right4_rect)
        pygame.draw.rect(screen,(0,255,0),wall_right5_rect)
        pygame.draw.rect(screen,(0,255,0),wall_right6_rect)
        pygame.draw.rect(screen,(0,255,0),wall_right7_rect)
        pygame.draw.rect(screen,(0,255,0),wall_right8_rect)
        pygame.draw.rect(screen,(0,255,0),wall_right9_rect)"""
        playerO.stopr=1
    if playerO.rect.colliderect(wall_left_rect) or playerO.rect.colliderect(wall_left2_rect) or playerO.rect.colliderect(wall_left3_rect) or playerO.rect.colliderect(wall_left4_rect) or playerO.rect.colliderect(wall_left5_rect)or playerO.rect.colliderect(wall_left6_rect) or playerO.rect.colliderect(wall_leftlast_rect):
        """pygame.draw.rect(screen,(0,255,0),wall_left_rect)
        pygame.draw.rect(screen,(0,255,0),wall_left2_rect)
        pygame.draw.rect(screen,(0,255,0),wall_left3_rect)
        pygame.draw.rect(screen,(0,255,0),wall_left4_rect)
        pygame.draw.rect(screen,(0,255,0),wall_left5_rect)
        pygame.draw.rect(screen,(0,255,0),wall_left6_rect)
        pygame.draw.rect(screen,(0,255,0),wall_leftlast_rect)"""
        playerO.stopl=1
    if playerO.rect.colliderect(wall_top_rect) or playerO.rect.colliderect(wall_top2_rect) or playerO.rect.colliderect(wall_top3_rect) or playerO.rect.colliderect(wall_top4_rect) or playerO.rect.colliderect(wall_top4_rect) or playerO.rect.colliderect(wall_top6_rect) or playerO.rect.colliderect(wall_top7_rect)or playerO.rect.colliderect(wall_top8_rect) or playerO.rect.colliderect(wall_top9_rect)or playerO.rect.colliderect(wall_top10_rect):
        """pygame.draw.rect(screen,(255,0,0),wall_top_rect)
        pygame.draw.rect(screen,(0,255,0),wall_top2_rect)
        pygame.draw.rect(screen,(255,0,0),wall_top3_rect)
        pygame.draw.rect(screen,(0,255,0),wall_top4_rect)
        pygame.draw.rect(screen,(255,0,0),wall_top5_rect)
        pygame.draw.rect(screen,(0,255,0),wall_top6_rect)
        pygame.draw.rect(screen,(255,0,0),wall_top7_rect)
        pygame.draw.rect(screen,(255,0,0),wall_top8_rect)
        pygame.draw.rect(screen,(255,0,0),wall_top9_rect)
        pygame.draw.rect(screen,(255,0,0),wall_top10_rect)"""
        playerO.stopt=1
    if playerO.rect.colliderect(wall_bottom_rect) or playerO.rect.colliderect(wall_bottom2_rect) or playerO.rect.colliderect(wall_bottom3_rect) or playerO.rect.colliderect(wall_bottom4_rect) or playerO.rect.colliderect(wall_bottom5_rect) or playerO.rect.colliderect(wall_bottom6_rect) or playerO.rect.colliderect(wall_bottom7_rect):
        """pygame.draw.rect(screen,(255,0,0),wall_bottom_rect)
        pygame.draw.rect(screen,(0,255,0),wall_bottom2_rect)
        pygame.draw.rect(screen,(255,0,0),wall_bottom3_rect)
        pygame.draw.rect(screen,(0,255,0),wall_bottom4_rect)
        pygame.draw.rect(screen,(255,0,0),wall_bottom5_rect)
        pygame.draw.rect(screen,(255,0,0),wall_bottom6_rect)
        pygame.draw.rect(screen,(255,0,0),wall_bottom7_rect)"""
        playerO.stopd=1
    
    
    #pygame.draw.rect(screen,(0,255,0),wall_bottom7_rect)
    
   # pygame.draw.rect(screen, (255,0,0), pygame.Rect(30, 30, 60, 60))
    enemy.draw(screen)
    enemy.update()
    player.draw(screen)
    player.update()
    weaponO.update()
    weaponO.draw(screen)
    pygame.display.update()
    # Locks the frame rate at 60 fps
    clock.tick(60)
    