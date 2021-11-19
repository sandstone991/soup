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
    def __init__(self, player, x=700, y=700, running=run, idiling=idle, sounds=sound, scale=(50, 80), speed=2, range=100):
        super().__init__(x, y, running, idiling, sounds, scale, speed)
        self.player = player
        self.dx = 0
        self.dy = 0
        self.range = range

    def isInRange(self):
        distance = math.sqrt((self.player.x-self.x)**2 +
                             (self.player.y-self.y)**2)
        if distance <= self.range:
            return True
        else:
            return False

    def move(self):
        if self.isInRange():
            dx, dy = self.player.x-self.x, self.player.y-self.y
            dist = math.hypot(dx, dy)
            dx, dy = dx/dist, dy/dist
            self.velX = dx*self.speed
            self.velY = dy*self.speed
        else:
            self.velX = 0
            self.velY = 0
