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
        self.image = pygame.image.load(
            'Textures/frames/knight_f_idle_anim_f0.png')
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.velX = 0
        self.velY = 0
        self.speed = 4
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    # def player_input(self):
    #     # maybe a better approach is to put all events in the main game loop we'll see about that later
    #     for event in pygame.event.get():
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         self.left_pressed = True
        #     if event.key == pygame.K_d:
        #         self.right_pressed = True
        #     if event.key == pygame.K_w:
        #         self.up_pressed = True
        #     if event.key == pygame.K_s:
        #         self.down_pressed = True
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_a:
        #         self.left_pressed = False
        #     if event.key == pygame.K_d:
        #         self.right_pressed = False
        #     if event.key == pygame.K_w:
        #         self.up_pressed = False
        #     if event.key == pygame.K_s:
        #         self.down_pressed = False

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

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
