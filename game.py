import pygame
from player import Player
from generic_enemy import GenericEnemy
from sys import exit
from weapon import Weapon
from ui import Ui, Start


class game:
    def __init__(self):
        self.currentWeapon = Weapon()
        self.playerObject = Player(self.currentWeapon)
        self.enemies = []
        self.player = pygame.sprite.Group()
        self.player.add(self.playerObject)
        self.enemies = pygame.sprite.Group()

    def initEnemies(self):
