from os import X_OK
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # IMPORTING ALL SPRITES
        self.playerRunRight = [pygame.image.load('Textures/frames/knight_m_run_anim_f0.png'), pygame.image.load('Textures/frames/knight_m_run_anim_f1.png'),
                               pygame.image.load('Textures/frames/knight_m_run_anim_f2.png'), pygame.image.load('Textures/frames/knight_m_run_anim_f3.png')]
        self.playerRunLeft = [pygame.transform.flip(
            x, True, False) for x in self.playerRunRight]

        self.playerRunIndex = 0
        self.playerIdleIndex = 0
        self.playerIdleRight = [pygame.image.load('Textures/frames/knight_m_idle_anim_f0.png'), pygame.image.load('Textures/frames/knight_m_idle_anim_f1.png'),
                                pygame.image.load('Textures/frames/knight_m_idle_anim_f2.png'), pygame.image.load('Textures/frames/knight_m_idle_anim_f3.png')]
        self.playerIdleLeft = [pygame.transform.flip(
            x, True, False) for x in self.playerIdleRight]
        self.playerRunCurrent = self.playerRunRight
        self.playerIdleCurrent = self.playerIdleRight
        self.image = self.playerIdleCurrent[self.playerIdleIndex]
        self.x = x
        self.y = y
        # temp
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.velX = 0
        self.velY = 0
        self.speed = 3
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.latestDirection = 'RIGHT'

    def isRunning(self):
        if self.velX == 0 and self.velY == 0:
            return False
        self.playerIdleIndex = 0
        return True

    def handleDirection(self):
        if self.velX < 0:
            self.playerRunCurrent = self.playerRunLeft
            self.playerIdleCurrent = self.playerIdleLeft
        elif self.velX > 0:
            self.playerRunCurrent = self.playerRunRight
            self.playerIdleCurrent = self.playerIdleRight

    def runAnimation(self):
        if self.playerRunIndex > 3:
            self.playerRunIndex = 0
        else:
            self.playerRunIndex += 0.2
        self.image = self.playerRunCurrent[int(self.playerRunIndex)]

    def idleAnimation(self):
        if self.playerIdleIndex > 3:
            self.playerIdleIndex = 0
        else:
            self.playerIdleIndex += 0.1
        self.image = self.playerIdleCurrent[int(self.playerIdleIndex)]

    def handleAnimation(self):
        self.handleDirection()
        if self.isRunning():
            self.runAnimation()
        else:
            self.idleAnimation()

    def dash(self):
        pass

    def attack(self):
        pass

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

        self.x += self.velX
        self.y += self.velY
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.move()
        self.handleAnimation()
