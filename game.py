import pygame
from player import Player
from generic_enemy import GenericEnemy
from sys import exit
from weapon import Weapon
from ui import Ui, Start
from ui import GameOver, Images


class Game:
    def __init__(self):
        pygame.init()
        self.currentWeapon = Weapon()
        self.playerObject = Player(self.currentWeapon)
        self.playerCoords = self.playerObject.getCoords()
        self.player = pygame.sprite.Group()
        self.player.add(self.playerObject)
        self.enemies = pygame.sprite.Group()
        self.WIDTH = 1366
        self.HEIGHT = 768
        self.floor_surface = pygame.image.load('Textures/frames/floor_1.png')
        self.started = True
        self.screen = None
        self.initEnemies()
        self.initScreen()
        # self.initUi()
        self.clock = pygame.time.Clock()

    def initUi(self):
        self.ui = Ui(self.screen, self.WIDTH, self.HEIGHT,
                     self.floor_surface, self.started)
        self.start = Start(self.screen, self.WIDTH, self.HEIGHT,
                           self.floor_surface, self.started)
        self.gameOver = GameOver(
            self.screen, self.WIDTH, self.HEIGHT, self.floor_surface, self.started)
        self.img = Images()

    def initEnemies(self):
        # This function is only temporary to be replaced with whatever function AWWAD comes up with
        for i in range(1):
            self.enemies.add(GenericEnemy())

    def initScreen(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Soup')

    def updateEnemies(self):
        # Static variable so all the objects would get the update at once
        GenericEnemy.playerCoords = self.playerCoords

    def updateData(self):
        self.playerCoords = self.playerObject.getCoords()
        self.currentWeapon.direction = self.playerObject.direction
        self.updateEnemies()

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            #     self.ui.paused()
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
            if event.type == pygame.MOUSEMOTION:
                self.currentWeapon.rotation = True
                self.currentWeapon.mx,  self.currentWeapon.my = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.currentWeapon.attackFlag = 20
                self.currentWeapon.attackDelay()
                #enemyO.damageFlag = 5

    def draw(self):
        for i in range(0, self.HEIGHT, 16):
            for k in range(0, self.WIDTH, 16):
                self.screen.blit(self.floor_surface, (k, i))
        # debug purposes
        # screen.blit(pygame.transform.scale(img.pause_surface,(50,50)),(WIDTH-50,0))
        # self.start.startUi()
        # self.ui.health()
        self.enemies.draw(self.screen)
        self.enemies.update()
        self.drawPlayer()
        pygame.display.update()
        # Locks the frame rate at 60 fps
        # not very clean code
        self.currentWeapon.direction = self.playerObject.direction
        self.clock.tick(60)

    def drawPlayer(self):
        self.player.draw(self.screen)
        self.player.update()
        self.currentWeapon.update()
        self.currentWeapon.draw(self.screen)

    def run(self):
        self.updateData()
        self.eventLoop()
        self.draw()
