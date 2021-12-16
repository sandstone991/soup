from sys import platform
import pygame
import math
import time
import datetime

from pygame import Vector2, rect
from pygame import image
from pygame.mixer import Sound
from pygame.transform import rotate

# from player import Player
from generic_entity import GenericEntity

texture = pygame.image.load("Textures/frames/weapon_knight_sword.png")
sound = 'audio/weapon/mixkit-fast-sword-whoosh-2792.wav'


class Weapon(pygame.sprite.Sprite):
    """
    A class to represnt a weapon to be carried by the player
    future improvement may give other entites the ability to carry a weapon too
    ...

    Attributes
    ----------
    Texture : pygame.image -> the image of the weapon
    scale: tuple -> not implemented yet
    range: int   -> the range in which the weapon will move in a circle around the player in


    Methods
    -------
    getRotationAngle(): calculates the angle of rotation for the weapon depending on the players current position and the mouses position when the mouse is moving
    only runs if self.rotation is set to true. self.rotation can be set to true if the mouse is moving in the game event loop
    rotate():In a dire need for a better implementation but it kinda works basically rotates and moves the weapon in circle once its done it sets rotation to false
    draw():Overridden to work 
    """

    def __init__(self, texture=texture, scale=(3, 5), range=10, sound=sound):
        super().__init__()
        self.image = texture
        self.CurrentImage = texture
        self.angle = 0
        self.x = 0
        self.y = 0
        self.mx = 0
        self.my = 0
        self.rotation = False
        self.attackFlag = 0
        self.timerFlag = True
        self.direction= 'LEFT'
        self.pos = Vector2(0, 0)
        self.attackAngle = 0  # angle to be rotated to when attack is activated
        self.attackAnimationCounter = 0
        self.rect = self.CurrentImage.get_rect(center=(0, 0))
        self.listOfActions = [self.getRotationAngle,
                              self.rotateMove,self.mouseAntiHold,self.weaponAttack ]
        self.swordSound = pygame.mixer.Sound(sound)
        self.swordSound.set_volume(.4)
        self.timer_stop = datetime.datetime.utcnow() + datetime.timedelta(seconds=0)

    def getRotationAngle(self):
        if self.rotation:
            rel_x, rel_y = self.mx - self.x, self.my - self.y
            self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
    def rotateGeneral(self,angle):
        self.CurrentImage = pygame.transform.rotate(self.image, angle)
        # Starting position x
        x = self.x + 15 * math.cos(angle/60+1)+5
        # Starting position y
        y = self.y - 15 * math.sin(angle/60+1)+10
        self.rect = self.CurrentImage.get_rect(center=(x, y))


    def rotateMove(self):
        self.rotateGeneral(self.angle)
        self.rotation = False

    def applyActions(self):
        for i in range(len(self.listOfActions)):
            self.listOfActions[i]()

    def update(self):
        self.applyActions()

    def draw(self, screen):
        screen.blit(self.CurrentImage, self.rect)

    def attackAnimation(self):
        if self.attackAnimationCounter != 0:
            if self.direction == 'RIGHT':
                self.attackAngle -= 10
            else:
                self.attackAngle +=10
            self.rotateGeneral(self.attackAngle)
            self.attackAnimationCounter += 1
            if self.attackAnimationCounter == 6:
                self.attackAnimationCounter = 0
    
    def weaponAttack(self):
        if self.attackFlag and self.timerFlag:
            self.swordSound.play()
            self.attackAnimation()
            

    def attackDelay(self):
        self.timerFlag = False
        if datetime.datetime.utcnow() > self.timer_stop:
            self.attackAnimationCounter = 6
            self.attackAngle = self.angle
            self.resetDelay()
    def mouseAntiHold(self):
        if self.attackFlag!=0:
            self.attackFlag-=1
        else:
            self.attackFlag = 0
    def resetDelay(self):
        self.timer_stop = datetime.datetime.utcnow() + datetime.timedelta(seconds=.2)
        self.timerFlag = True
