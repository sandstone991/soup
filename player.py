from os import X_OK
import pygame
from math import sqrt
from generic_entity import GenericEntity
from weapon import Weapon
# from generic_enemy import GenericEnemy
run = [pygame.image.load('Textures/frames/knight_m_run_anim_f0.png'), pygame.image.load('Textures/frames/knight_m_run_anim_f1.png'),
       pygame.image.load('Textures/frames/knight_m_run_anim_f2.png'), pygame.image.load('Textures/frames/knight_m_run_anim_f3.png')]
sound = 'audio/Player/player_walk.wav'
idle = [pygame.image.load('Textures/frames/knight_m_idle_anim_f0.png'), pygame.image.load('Textures/frames/knight_m_idle_anim_f1.png'),
        pygame.image.load('Textures/frames/knight_m_idle_anim_f2.png'), pygame.image.load('Textures/frames/knight_m_idle_anim_f3.png')]

class Player(GenericEntity):
    """
    A class to represent the player
    which inherits from the GenericEntity class
    ...
    Attributes
    ----------
    Check the generic_entity class
    Methods
    -------
    move():takes input and transfroms it to speed in y or x
    updateWeapons(): gives the weapon the current player coords
    """

    def __init__(self, weapon,screen, x=500, y=500, running=run, idiling=idle, sounds='audio/Player/player_walk.wav', scale=(25, 40), speed=3, health=100,healthFlag = False):
        super().__init__(x, y, running, idiling, sounds, scale, speed, health)
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.healthFlag = False
        self.health=health
        self.listOfActions = [self.move, self.applyMove,
                              self.updateWeapon, self.attack,self.healthBar]
        self.weapon = weapon
        self.screen = screen
        self.healthWidth = 370
        self.healthHeight = 100
        self.WIDTH = 1366
        self.HEIGHT = 768
        self.num_of_imgs = 36
        self.healthList = [
            pygame.image.load('Textures/imagesUi/health/health0.png'),
            pygame.image.load('Textures/imagesUi/health/health1.png'),
            pygame.image.load('Textures/imagesUi/health/health2.png'),
            pygame.image.load('Textures/imagesUi/health/health3.png'),
            pygame.image.load('Textures/imagesUi/health/health4.png'),
            pygame.image.load('Textures/imagesUi/health/health5.png'),
            pygame.image.load('Textures/imagesUi/health/health6.png'),
            pygame.image.load('Textures/imagesUi/health/health7.png'),
            pygame.image.load('Textures/imagesUi/health/health8.png'),
            pygame.image.load('Textures/imagesUi/health/health9.png'),
            pygame.image.load('Textures/imagesUi/health/health10.png'),
            pygame.image.load('Textures/imagesUi/health/health11.png'),
            pygame.image.load('Textures/imagesUi/health/health12.png'),
            pygame.image.load('Textures/imagesUi/health/health13.png'),
            pygame.image.load('Textures/imagesUi/health/health14.png'),
            pygame.image.load('Textures/imagesUi/health/health15.png'),
            pygame.image.load('Textures/imagesUi/health/health16.png'),
            pygame.image.load('Textures/imagesUi/health/health17.png'),
            pygame.image.load('Textures/imagesUi/health/health18.png'),
            pygame.image.load('Textures/imagesUi/health/health19.png'),
            pygame.image.load('Textures/imagesUi/health/health20.png'),
            pygame.image.load('Textures/imagesUi/health/health21.png'),
            pygame.image.load('Textures/imagesUi/health/health22.png'),
            pygame.image.load('Textures/imagesUi/health/health23.png'),
            pygame.image.load('Textures/imagesUi/health/health24.png'),
            pygame.image.load('Textures/imagesUi/health/health25.png'),
            pygame.image.load('Textures/imagesUi/health/health26.png'),
            pygame.image.load('Textures/imagesUi/health/health27.png'),
            pygame.image.load('Textures/imagesUi/health/health28.png'),
            pygame.image.load('Textures/imagesUi/health/health29.png'),
            pygame.image.load('Textures/imagesUi/health/health30.png'),
            pygame.image.load('Textures/imagesUi/health/health31.png'),
            pygame.image.load('Textures/imagesUi/health/health32.png'),
            pygame.image.load('Textures/imagesUi/health/health33.png'),
            pygame.image.load('Textures/imagesUi/health/health34.png'),
            pygame.image.load('Textures/imagesUi/health/health35.png')
            ]
        self.healthSurface = []
        self.healthRect = []
        
    
    def scaleImage(self, img_surf, w, h):
        return pygame.transform.scale(img_surf, (w, h))

    def setHealth(self):
        x = self.WIDTH/2
        y = -10
        w = self.healthWidth 
        h = self.healthHeight
        for i in range (0,self.num_of_imgs):
            img_Surf =  self.healthList[i]   
            image_rect = pygame.Rect(x-(w/2), y, w, h)
            image_surf = self.scaleImage(img_Surf, w, h)
            self.healthSurface.append(image_surf)
            self.healthRect.append(image_rect)

    def healthBar(self):
        self.setHealth()

        
        if self.health > 97.23:
            self.screen.blit(self.healthSurface[self.num_of_imgs - 1], self.healthRect[self.num_of_imgs - 1])
        elif self.health < 97.23 and self.health > 94.46: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 2], self.healthRect[self.num_of_imgs - 2])
        elif self.health < 94.46 and self.health > 91.69: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 3], self.healthRect[self.num_of_imgs - 3])
        elif self.health < 91.69 and self.health > 88.92: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 4], self.healthRect[self.num_of_imgs - 4])
        elif self.health < 88.92 and self.health > 86.15: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 5], self.healthRect[self.num_of_imgs - 5])
        elif self.health < 86.15 and self.health > 83.38: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 6], self.healthRect[self.num_of_imgs - 6])
        elif self.health < 83.38 and self.health > 80.61: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 7], self.healthRect[self.num_of_imgs - 7])
        elif self.health < 80.61 and self.health > 77.84: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 8], self.healthRect[self.num_of_imgs - 8])
        elif self.health < 77.84 and self.health > 75.07: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 9], self.healthRect[self.num_of_imgs - 9])
        elif self.health < 75.07 and self.health > 72.3: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 10], self.healthRect[self.num_of_imgs - 10])
        elif self.health < 72.3 and self.health > 69.53: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 11], self.healthRect[self.num_of_imgs - 11])
        elif self.health < 69.53 and self.health > 66.76: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 12], self.healthRect[self.num_of_imgs - 12])
        elif self.health < 66.76 and self.health > 63.99: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 13], self.healthRect[self.num_of_imgs - 13])
        elif self.health < 63.99 and self.health > 61.22: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 14], self.healthRect[self.num_of_imgs - 14])
        elif self.health < 61.22 and self.health > 58.45: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 15], self.healthRect[self.num_of_imgs - 15])
        elif self.health < 58.45 and self.health > 55.68: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 16], self.healthRect[self.num_of_imgs - 16])
        elif self.health < 55.68 and self.health > 52.91: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 17], self.healthRect[self.num_of_imgs - 17])




        elif self.health < 52.91 and self.health > 50.14: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 18], self.healthRect[self.num_of_imgs - 18])
        elif self.health < 50.14 and self.health > 47.37: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 19], self.healthRect[self.num_of_imgs - 19])
        elif self.health < 47.37 and self.health > 44.6: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 20], self.healthRect[self.num_of_imgs - 20])
        elif self.health < 44.6 and self.health > 41.83: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 21], self.healthRect[self.num_of_imgs - 21])
        elif self.health < 41.83 and self.health > 39.06: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 22], self.healthRect[self.num_of_imgs - 22])
        elif self.health < 39.06 and self.health > 36.29: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 23], self.healthRect[self.num_of_imgs - 23])
        elif self.health < 36.29 and self.health > 33.52: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 24], self.healthRect[self.num_of_imgs - 24])
        elif self.health < 33.52 and self.health > 30.75: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 25], self.healthRect[self.num_of_imgs - 25])
        elif self.health < 30.75 and self.health > 27.98: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 26], self.healthRect[self.num_of_imgs - 26])
        elif self.health < 27.98 and self.health > 25.21: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 27], self.healthRect[self.num_of_imgs - 27])
        elif self.health < 25.21 and self.health > 22.44: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 28], self.healthRect[self.num_of_imgs - 28])
        elif self.health < 22.44 and self.health > 19.67: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 29], self.healthRect[self.num_of_imgs - 29])
        elif self.health < 19.67 and self.health > 16.9: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 30], self.healthRect[self.num_of_imgs - 30])
        elif self.health < 16.9 and self.health > 14.13: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 31], self.healthRect[self.num_of_imgs - 31])
        elif self.health < 14.13 and self.health > 11.36: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 32], self.healthRect[self.num_of_imgs - 32])
        elif self.health < 11.36 and self.health > 8.59: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 33], self.healthRect[self.num_of_imgs - 33])

        elif self.health < 8.59 and self.health > 5.82: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 34], self.healthRect[self.num_of_imgs - 34])
        elif self.health < 5.82 and self.health > 3.05: 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 35], self.healthRect[self.num_of_imgs - 35])
        elif self.health < 3.05 : 
            self.screen.blit(self.healthSurface[self.num_of_imgs - 36], self.healthRect[self.num_of_imgs - 36])
        # elif self.health < 1.5: 
        #     self.screen.blit(self.healthSurface[self.num_of_imgs - 4], self.healthRect[self.num_of_imgs - 4])
        
    def dash(self):
        pass

    # def calculateDistance(self):
    #     self.distance = sqrt(
    #         (self.player.x-x)**2 + (self.player.y-y)**2)
    #     print(self.distance)

    # def attack(self):
    #     # attack func
    #     if self.weapon.attackFlag == 19:
    #         if pygame.Rect.colliderect(self.rect,self.rect):
    #             print('kk')

    def move(self):
        flagX = 1
        flagY = 1
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
            flagX = 0
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
            flagX = 0
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
            flagY = 0
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
            flagY = 0
        if flagX:
            self.velX = 0
        if flagY:
            self.velY = 0

    def updateWeapon(self):
        self.weapon.pos = self.rect.topright
        self.weapon.x = self.x
        self.weapon.y = self.y
        self.weapon.applyActions()
       
    def drawAdditions(self):
        # pygame.draw.rect(screen, (255,0,0),(1366/2 - 100,10,self.health * 5 ,75))
        pass
