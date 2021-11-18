from os import X_OK
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # player_walk_1 = pygame.image.load(
        #     'graphics/player/player_walk_1.png').convert_alpha()
        # player_walk_2 = pygame.image.load(
        #     'graphics/player/player_walk_2.png').convert_alpha()
        # self.player_walk = [player_walk_1, player_walk_2]
        # self.player_index = 0
        # self.image = self.player_walk[self.player_index]
        self.playerRun = [pygame.image.load('Textures/frames/knight_f_run_anim_f0.png'), pygame.image.load('Textures/frames/knight_f_run_anim_f1.png'),
                          pygame.image.load('Textures/frames/knight_f_run_anim_f2.png'), pygame.image.load('Textures/frames/knight_f_run_anim_f3.png')]
        self.playerRunIndex = 0

        self.playerIdle = pygame.image.load(
            'Textures/frames/knight_f_idle_anim_f0.png')
        self.image = self.playerIdle
        self.x = x
        self.y = y
        # temp
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.velX = 0
        self.velY = 0
        self.speed = 4
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def isRunning(self):
        if self.velX == 0 and self.velY == 0:
            return False
        return True

    def runAnimation(self):
        if self.playerRunIndex == 3:
            self.playerRunIndex = 0
        else:
            self.playerRunIndex += 1

    def animation_state(self):
        if self.isRunning():
            self.runAnimation()
            self.image = self.playerRun[self.playerRunIndex]
        else:
            self.image = self.playerIdle

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
        self.animation_state()
