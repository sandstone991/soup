import pygame
import math
from random import randint
from ui import GameOver
from generic_entity import GenericEntity
from particles import Particle
# temporary spirtes for testing please DELETE
idle = [pygame.image.load('Textures/frames/big_demon_idle_anim_f0.png'), pygame.image.load('Textures/frames/big_demon_idle_anim_f1.png'),
        pygame.image.load('Textures/frames/big_demon_idle_anim_f2.png'), pygame.image.load('Textures/frames/big_demon_idle_anim_f3.png')]
run = [pygame.image.load('Textures/frames/big_demon_run_anim_f0.png'), pygame.image.load('Textures/frames/big_demon_run_anim_f1.png'),
       pygame.image.load('Textures/frames/big_demon_run_anim_f2.png'), pygame.image.load('Textures/frames/big_demon_run_anim_f3.png')]

sound = 'audio/Player/player_walk.wav'
hitSound = 'audio/weapon/audio_weapon_snd_player_hit.mp3'
enemyDie = 'audio/weapon/audio_weapon_snd_enemy_attack_03.ogg'
hitpSound= 'audio\weapon\Fire swoosh burning - Sound Effect.mp3'
phf=1
WIDTH = 1366
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
class GenericEnemy(GenericEntity):
    """
    A class for all kinds of enemies to inherit from
    maybe even instantiated from
    Inherits from the GenericEntity class
    ...
    Attributes
    ----------
    detectRange: int -> represnt the range from which the enemy can detect the player
    ----------
    Methods
    -------
    move()           :Checks if player in range if in range changes velX and velY with basic vector operations
    isInRange()      :Checks if player in range or not (Calculates euclidean distance and compares it with range)
    damageContol()   : to control the amount of damage done to the enemy
    drawAdditions()  : to draw the health bar of the enemy
    isStillAlive()   : checks if the enemy health is less than 5 to play dying sound
    createParticles(): create multiple objects of the particle with different parameters given randomly
    drawPartices()   : calling the render function of the particle by iterating over the list of the created objects
    cleanParticles() : clean the particles list to make a fresh one with fresh x,y valus -not used-

    -------
    """

    def __init__(self,screen,player, x=700, y=700, running=run, idiling=idle, sounds=sound, scale=(50, 80), speed=2, health=50, detectRange=100, attackRange=20, attackPower=0.3):
        super().__init__(x, y, running, idiling, sounds, scale, speed, health)
        self.player = player
        self.screen = screen
        self.dx = 0
        self.dy = 0
        self.attacking = False
        self.coolDownTimer = 1
        self.attackCoolDown = 100
        self.detectRange = detectRange
        self.attackRange = attackRange
        self.attackPower = attackPower
        self.hitSound = pygame.mixer.Sound(hitSound)
        self.hitpSound = pygame.mixer.Sound(hitpSound)
        self.hitSound.set_volume(.5)
        self.enemyDieSound = pygame.mixer.Sound(enemyDie)
        self.enemyDieSound.set_volume(.7)
        self.damageFlag = 0
        self.distance = 99999999
        self.particles =[]
        self.listOfActions = [self.calculateDistance,
                              self.isInAttackRange, self.move, self.applyMove, self.playerAttack, self.damageControl,self.drawAdditions,self.isStillAlive,self.attack]

    def calculateDistance(self):
        self.distance = math.sqrt(
            (self.player.x-self.x)**2 + (self.player.y-self.y)**2)

    def isInRange(self, range):
        if self.distance <= range:
            return True
        else:
            return False
    
    # check if the player attcks the enemy, in case of attacing -> do some damage to the enemy
    def playerAttack(self):
        if self.distance <= 20 and self.damageFlag:
            self.takeDamage(1)
            self.hitSound.play()
            print(self.health)
            self.createParticles()
            self.drawParticles()
            # self.cleanParticles()
    
    # holding the damage rate (to avoid some other bugs)
    def damageControl(self):
        if self.damageFlag!=0:
            self.damageFlag-=1
        else:
            self.damageFlag= 0
        """if self.player.damageFlag!=0:
            self.player.damageFlag-=1
        else:
            self.player.damageFlag= 0"""
       
    def isInAttackRange(self):
        if self.isInRange(self.attackRange):
            self.velX = 0
            self.velY = 0
            self.attacking = True
    def attack(self):
        if self.isInRange(self.attackRange)and self.player.health:
            self.player.takeDamage(self.attackPower)
            self.hitSound.play()
            self.hitpSound.play()
            circle=pygame.Surface((WIDTH*2,HEIGHT*2), pygame.SRCALPHA)
            #circle.set_alpha(128)
            pygame.draw.circle(circle, (255,0,0,128), (WIDTH/2,HEIGHT/2), HEIGHT+25,150)
            screen.blit(circle, (0, 0))
            print("phealth:",self.player.health)
        if (self.player.health == 0):
                self.player.healthFlag = True
                self.player.health = 100
                self.velX = 50
                self.velY = 50
                # print(phf)
    def move(self):
        if not self.attacking:
            if self.isInRange(self.detectRange):
                dx, dy = self.player.x-self.x, self.player.y-self.y
                dist = math.hypot(dx, dy)
                dx, dy = dx/dist, dy/dist
                self.velX = dx*self.speed
                self.velY = dy*self.speed
            else:
                self.velX = 0
                self.velY = 0
        else:
            if self.coolDownTimer > self.attackCoolDown:
                self.attacking = False
                self.coolDownTimer = 0
            else:
                self.coolDownTimer += 1

    def drawAdditions(self):
        pygame.draw.rect(self.screen, (255,0,0),(self.rect.x,self.rect.y,self.health,5))

    def isStillAlive(self):
        if self.health <= 5:
            self.enemyDieSound.play()
    
    def createParticles(self):
        for x in range(randint(15, 25)):
            particle = Particle(self.rect.x+20, self.rect.y+30, randint(0,50)/10, randint(-3, -1), randint(2, 5), (166,16,30),1.5)
            self.particles.append(particle)

    def drawParticles(self):
        for particle in self.particles:
            particle.render(self.screen)
            if particle.radius <= 0:
                self.particles.remove(particle)

    def cleanParticles(self):
        self.particles.clear()
