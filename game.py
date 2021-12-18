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
        self.playerCoords = self.playerObject.getCoords()
        self.player = pygame.sprite.Group()
        self.player.add(self.playerObject)
        self.enemies = pygame.sprite.Group()
        self.WIDTH = 1366
        self.HEIGHT = 768
        self.floor_surface = pygame.image.load(
            'Textures/frames/floor_1.png').convert()
        self.started = True
        self.screen = None
        self.initEnemies()
        self.initScreen()
        self.initUi()

    def initUi(self):
        self.ui = Ui(self.screen, self.WIDTH, self.HEIGHT,
                     self.floor_surface, self.started)
        self.start = Start(self.screen, self.WIDTH, self.HEIGHT,
                           self.floor_surface, self.started)

    def initEnemies(self):
        # This function is only temporary to be replaced with whatever function AWWAD comes up with
        for i in range(10):
            self.enemies.add(GenericEnemy())

    def initScreen(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Soup')

    def updateEnemies(self):
        # Static variable so all the objects would get the update at once
        GenericEnemy.playerCoords = self.playerCoords

    def updateData(self):
        self.playerCoords = self.playerObject.getCoords()
        self.updateEnemies()

    def eventLoop(self):
        for event in pygame.event.get():
            self.gameEvents(event)
            self.playerEvents(event)
            self.uiEvents(event)

    def gameEvents(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    def playerEvents(self, event):
        # check for (W, A, S, D)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.playerObject.left_pressed = True
            if event.key == pygame.K_d:
                self.playerObject.right_pressed = True
            if event.key == pygame.K_w:
                self.playerObject.up_pressed = True
            if event.key == pygame.K_s:
                self.playerObject.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.playerObject.left_pressed = False
            if event.key == pygame.K_d:
                self.playerObject.right_pressed = False
            if event.key == pygame.K_w:
                self.playerObject.up_pressed = False
            if event.key == pygame.K_s:
                self.playerObject.down_pressed = False
        self.playerAttackEvents(event)

    def playerAttackEvents(self, event):
        # check for mouse movement and changes rotation true when moving as we don't want the weapon to follow the mouse when the mouse isn't moving
        if event.type == pygame.MOUSEMOTION:
            self.currentWeapon.rotation = True
            self.currentWeapon.mx,  self.currentWeapon.my = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.currentWeapon.attackFlag = 20
            self.currentWeapon.attackDelay()
            #enemyO.damageFlag = 5

    def uiEvents(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.ui.paused()
