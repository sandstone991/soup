import pygame
import math
import time,datetime

from pygame import Vector2, rect
from pygame import image
from pygame.mixer import Sound
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

    def __init__(self, texture=texture, scale=(12, 20), range=10):
        super().__init__()
        self.image = texture
        self.CurrentImage = texture
        self.angle = 0
        self.x = 0
        self.y = 0
        self.mx = 0
        self.my = 0
        self.rotation = False
        self.attackFlag = False
        self.timerFlag = True
        self.pos = Vector2(0, 0)
        self.rect = self.CurrentImage.get_rect(center=(0, 0))
        self.listOfActions = [self.getRotationAngle, self.rotate, self.weaponAttack]
        self.swordSound = pygame.mixer.Sound(sound)
        self.swordSound.set_volume(.1)
        self.timer_stop = datetime.datetime.utcnow() +datetime.timedelta(seconds=0)

    def getRotationAngle(self):
        if self.rotation:
            rel_x, rel_y = self.mx - self.x, self.my - self.y
            self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

    def rotate(self):
        self.CurrentImage = pygame.transform.rotate(self.image, self.angle)
        x = self.x + 15 * math.cos(self.angle/60+1)+5  # Starting position x
        y = self.y - 15 * math.sin(self.angle/60+1)+10  # Starting position y
        self.rect = self.CurrentImage.get_rect(center=(x, y))
        self.rotation = False

    def applyActions(self):
        for i in range(len(self.listOfActions)):
            self.listOfActions[i]()

    def update(self):
        self.applyActions()

    def draw(self, screen):
        screen.blit(self.CurrentImage, self.rect)
    
    def weaponAttack(self):
        if self.attackFlag and self.timerFlag:
            self.swordSound.play()
            self.CurrentImage = pygame.transform.rotate(self.image, -60+self.angle)
            x = self.x + 15 * math.cos((-60+self.angle)/60+1)+5  # Starting position x
            y = self.y - 15 * math.sin((-60+self.angle)/60+1)+10  # Starting position y
            self.rect = self.CurrentImage.get_rect(center=(x,y))
            self.rotation = False
    def attackDelay(self):
        self.timerFlag = False
        if datetime.datetime.utcnow() > self.timer_stop:
            self.resetDelay()
    def resetDelay(self):
        self.timer_stop = datetime.datetime.utcnow() +datetime.timedelta(seconds=1)
        self.timerFlag = True
