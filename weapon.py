import pygame
import math
texture = pygame.image.load("Textures/frames/weapon_knight_sword.png")


class Weapon(pygame.sprite.Sprite):
    def __init__(self, texture=texture, scale=(12, 20), range=10):
        super().__init__()
        self.image = texture
        self.CurrentImage = texture
        self.angle = 0
        self.x = 0
        self.y = 0
        self.rect = self.CurrentImage.get_rect(center=(0, 0))
        self.listOfActions = [self.getRotationAngle, self.rotate, self.move]

    def getRotationAngle(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

    def rotate(self):
        self.CurrentImage = pygame.transform.rotate(self.image, self.angle)

    def move(self):
        self.rect = self.CurrentImage.get_rect(center=(self.x, self.y))

    def applyActions(self):
        for i in range(len(self.listOfActions)):
            self.listOfActions[i]()
