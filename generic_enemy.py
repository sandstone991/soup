import pygame
import math

from generic_entity import GenericEntity


class GenericEnemy(GenericEntity):
    def __init__(self, x, y, running, idiling, sounds, scale, speed):
        super().__init__(x, y, running, idiling, sounds, scale, speed)
        self.dx = 0
        self.dy = 0

    def move(self, player):
        dx, dy = player.x-self.x, player.y-self.y
        dist = math.hypot(dx, dy)
        dx, dy = dx/dist, dy/dist
        self.x += dx*self.speed
        self.y += dy*self.speed
