import pygame
import math

from generic_entity import GenericEntity
# temporary spirtes for testing please DELETE
run = [pygame.image.load('Textures/frames/knight_m_run_anim_f0.png'), pygame.image.load('Textures/frames/knight_m_run_anim_f1.png'),
       pygame.image.load('Textures/frames/knight_m_run_anim_f2.png'), pygame.image.load('Textures/frames/knight_m_run_anim_f3.png')]
sound = 'audio/Player/player_walk.wav'
idle = [pygame.image.load('Textures/frames/knight_m_idle_anim_f0.png'), pygame.image.load('Textures/frames/knight_m_idle_anim_f1.png'),
        pygame.image.load('Textures/frames/knight_m_idle_anim_f2.png'), pygame.image.load('Textures/frames/knight_m_idle_anim_f3.png')]


class GenericEnemy(GenericEntity):
    """
    A class for all kinds of enemies to inherit from
    maybe even instantiated from
    Inherits from the GenericEntity class
    ...

    Attributes
    ----------
    detectRange: int -> represnt the range from which the enemy can detect the player
    ----------

    Methods
    -------
    move()     :Checks if player in range if in range changes velX and velY with basic vector operations
    isInRange():Checks if player in range or not (Calculates euclidean distance and compares it with range)
    -------
    """

    def __init__(self, player, x=700, y=700, running=run, idiling=idle, sounds=sound, scale=(50, 80), speed=2, health=100, detectRange=100, attackRange=20, attackPower=5):
        super().__init__(x, y, running, idiling, sounds, scale, speed, health)
        self.player = player
        self.dx = 0
        self.dy = 0
        self.detectRange = detectRange
        self.attackRange = attackRange
        self.attackPower = attackPower
        self.distance = 99999999

    def calculateDistance(self):
        self.distance = math.sqrt(
            (self.player.x-self.x)**2 + (self.player.y-self.y)**2)

    def isInRange(self, range):
        if self.distance <= range:
            return True
        else:
            return False

    def attack(self):
        if self.isInRange(self.attackRange):
            self.player.takeDamage(self.attackPower)

    def move(self):
        self.calculateDistance()
        self.attack()
        if self.isInRange(self.detectRange):
            dx, dy = self.player.x-self.x, self.player.y-self.y
            dist = math.hypot(dx, dy)
            dx, dy = dx/dist, dy/dist
            self.velX = dx*self.speed
            self.velY = dy*self.speed
        else:
            self.velX = 0
            self.velY = 0
