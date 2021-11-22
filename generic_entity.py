
import pygame
from pygame import transform


class GenericEntity (pygame.sprite.Sprite):
    """
    A class to represent any entity in the game
    this entity could be the player or an enemy
    Please note this is an interface and should not be instantied from
    ...

    Attributes
    ----------
    (can change in the future when new features are added)
    x       : int  -> representing the intital position of the entity on the x axis when spawned
    y       : int  -> representing the intital position of the entity on the y axis when spawned
    running : list -> containing all the running sprites
    idiling : list -> containing all the idling sprites 
    sounds  : str  -> containg the address of the walking sfx (still needs improvement/in the future it should contain a list of strings for all the sfx the entity should use not just walking)
    scale   : tuple-> containing the desired size of the sprite (width,height)
    speed   : int  -> speed of the entity

    Methods
    -------
    isRunning()      :Checks whether or not the entity is currently running or not return true if running and false otherwise
    handleDirection():Checks which way the sprite should be looking right or left no returns
    runAnimation()   :Loops in the array of running sprites to simulate running
    idleAnimation()  :loops in the array of idiling sprites to simulate idling
    handleAnimation():Calls the right type of animations (Still needs to handle other types of animations other than running an idling like attacking MUST be updated in the future)
    handleSound()    :Calls the right type of sound according to the action (Still not implemented)
    applyMove()      :Applies movement with values of x and y
    move()           :To be implemented in child classes
    update()         :Calls move() and handleAnimation() (Will be updated when new actions are added)
    """

    def __init__(self, x, y, running, idiling, sounds, scale, speed, health):
        super().__init__()
        # IMPORTING ALL SPRITES
        self.runRight = running
        self.runRight = [pygame.transform.scale(x, scale) for x in running]
        self.runLeft = [pygame.transform.flip(
            x, True, False) for x in self.runRight]

        self.runIndex = 0
        self.idleIndex = 0
        self.idleRight = [pygame.transform.scale(x, scale) for x in idiling]
        self.idleLeft = [pygame.transform.flip(
            x, True, False) for x in self.idleRight]
        self.runCurrent = self.runRight
        self.idleCurrent = self.idleRight
        self.image = self.idleCurrent[self.idleIndex]
        # need to implement better sounds system
        self.moveSound = pygame.mixer.Sound(sounds)
        self.moveSound.set_volume(.5)
        self.playSoundCnt = 5
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(x, y))
        self.velX = 0
        self.velY = 0
        self.speed = speed
        self.health = health
        self.isAlive = True

    def isRunning(self):
        if self.velX == 0 and self.velY == 0:
            return False
        self.idleIndex = 0
        return True

    def handleDirection(self):
        if self.velX < 0:
            self.runCurrent = self.runLeft
            self.idleCurrent = self.idleLeft
        elif self.velX > 0:
            self.runCurrent = self.runRight
            self.idleCurrent = self.idleRight

    def runAnimation(self):
        if self.runIndex > 3:
            self.runIndex = 0
        else:
            self.runIndex += 0.2

        self.image = self.runCurrent[int(self.runIndex)]

    def idleAnimation(self):
        if self.idleIndex > 3:
            self.idleIndex = 0
        else:
            self.idleIndex += 0.1
        self.image = self.idleCurrent[int(self.idleIndex)]

    def handleAnimation(self):
        self.handleDirection()
        if self.isRunning():
            # play sound
            self.handleSound()
            self.runAnimation()
        else:
            self.idleAnimation()

    def handleSound(self):
        if self.playSoundCnt >= 5:
            self.moveSound.play()
            self.playSoundCnt = 0
        else:
            self.playSoundCnt += 0.5

    def attack(self):
        pass

    def move(self):
        pass

    def applyActions(self):
        for i in range(len(self.listOfActions)):
            self.listOfActions[i]()

    def applyMove(self):
        self.move()
        self.x += self.velX
        self.y += self.velY
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def takeDamage(self, damage):
        self.health -= damage
        self.isEntityAlive()

    def isEntityAlive(self):
        if self.health <= 0:
            self.isAlive = False

    def update(self):
        self.applyActions()
        self.handleAnimation()
# Future changes -> make applyMove() apply actions an array of methods to be called
