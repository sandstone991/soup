from os import X_OK
import pygame
from math import sqrt
from generic_entity import GenericEntity
from weapon import Weapon
from generic_enemy import GenericEnemy
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

    def __init__(self, weapon, x=500, y=500, running=run, idiling=idle, sounds='audio/Player/player_walk.wav', scale=(25, 40), speed=3, health=100):
        super().__init__(x, y, running, idiling, sounds, scale, speed, health)
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.listOfActions = [self.move, self.applyMove,
                              self.updateWeapon, self.attack]
        self.weapon = weapon

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
        pygame.draw.rect(self.screen, (255,0,0),(self.rect.x,self.rect.y,self.health,5))
