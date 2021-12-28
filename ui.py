import pygame
from pygame import mixer
import sys
import datetime



class Images:
    def __init__(self, *args, **kwargs) -> None:
        self.idle_enemy = [
        pygame.image.load('Textures/frames/big_demon_idle_anim_f0.png'), 
        pygame.image.load('Textures/frames/big_demon_idle_anim_f1.png'),
        pygame.image.load('Textures/frames/big_demon_idle_anim_f2.png'),
        pygame.image.load('Textures/frames/big_demon_idle_anim_f3.png')
        ]

        self.idle_player = [
        pygame.image.load('Textures/frames/knight_m_idle_anim_f0.png'), 
        pygame.image.load('Textures/frames/knight_m_idle_anim_f1.png'),
        pygame.image.load('Textures/frames/knight_m_idle_anim_f2.png'), 
        pygame.image.load('Textures/frames/knight_m_idle_anim_f3.png')
        ]
        
        self.start_surface = pygame.image.load(
            'Textures/imagesUi/start.png').convert()
        self.pause_surf = pygame.image.load(
            'Textures/imagesUi/pause.png').convert()
        self.menu_surface = pygame.image.load(
            'Textures/imagesUi/menu.png').convert()
        self.highScore_surf = pygame.image.load(
            'Textures/imagesUi/highScore.png').convert()
        self.play_surface = pygame.image.load(
            'Textures/imagesUi/play.png').convert()
        self.resume_surf = pygame.image.load(
            'Textures/imagesUi/resume.png').convert()
        self.quit_surface = pygame.image.load(
            'Textures/imagesUi/quit.png').convert()
        self.continue_surf = pygame.image.load(
            'Textures/imagesUi/continue.png').convert()
        self.pause_surface = pygame.image.load(
            'Textures/imagesUi/pause0.png').convert()
        self.exit_surface = pygame.image.load(
            'Textures/imagesUi/exit.png').convert()
        # self.healthList = [
        #     pygame.image.load('Textures/imagesUi/health0.png'),
        #     pygame.image.load('Textures/imagesUi/health1.png'),
        #     pygame.image.load('Textures/imagesUi/health2.png'),
        #     pygame.image.load('Textures/imagesUi/health3.png'),
        #     pygame.image.load('Textures/imagesUi/health4.png'),
        #     pygame.image.load('Textures/imagesUi/health5.png')
        #     ]
        # self.health0_surface = pygame.image.load(
        #     'Textures/imagesUi/health0.png').convert()
        # self.health1_surface = pygame.image.load(
        #     'Textures/imagesUi/health1.png').convert()
        # self.health2_surface = pygame.image.load(
        #     'Textures/imagesUi/health2.png').convert()
        # self.health3_surface = pygame.image.load(
        #     'Textures/imagesUi/health3.png').convert()
        # self.health4_surface = pygame.image.load(
        #     'Textures/imagesUi/health4.png').convert()
        # self.health5_surface = pygame.image.load(
        #     'Textures/imagesUi/heart.png')

        self.press_sound = mixer.Sound('audio/ui/press.wav')
        self.hover_sound = mixer.Sound('audio/ui/hover.wav')
        super(Images, self).__init__(*args, **kwargs)


class Colors:
    def __init__(self, *args, **kwargs) -> None:
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (99, 133, 206)
        self.green = (0, 200, 0)
        self.bright_red = (255, 0, 0)
        self.bright_green = (0, 255, 0)
        self.black = (0, 0, 0, 0)
        self.block_color = (53, 115, 255)
        self.gray = pygame.Color("gray30")
        super(Colors, self).__init__(*args, **kwargs)


class Ui(Colors, Images):

    def __init__(self, screen, WIDTH, HEIGHT, floor_surface, started, *args, **kwargs) -> None:
        super(Ui, self).__init__(*args, **kwargs)
        self.idiling_player = self.idle_player
        self.idiling_enemy = self.idle_enemy
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.floor_surface = floor_surface
        self.started = started
        self.imgWidth = 250
        self.imgHeight = 70
        self.widthAdd = 80
        self.heightAdd = 25
        self.healthWidth = 100
        self.healthHeight = 100
        self.soundFlag0 = True
        self.soundFlag1 = True
        self.soundFlag2 = True
        self.soundFlag3 = True
        self.soundFlag4 = True
        self.soundFlag5 = True
        self.soundFlag6 = True
        self.scale = (80,125)
        self.idleIndex = 0
        
        
        self.idleRight_player = [pygame.transform.scale(x, self.scale) for x in self.idiling_player]
        self.idleLeft_player = [pygame.transform.flip(
            x, True, False) for x in self.idleRight_player]
        
        self.idleRight_enemy = [pygame.transform.scale(x, self.scale) for x in self.idiling_enemy]
        self.idleLeft_enemy = [pygame.transform.flip(
            x, True, False) for x in self.idleRight_enemy]
        
        self.idleCurrent_enemy = self.idleLeft_enemy
        self.idleCurrent_player = self.idleRight_player
        self.image = self.idleCurrent_player[self.idleIndex]
        self.image_enemy = self.idleCurrent_enemy[self.idleIndex]    

    def idleAnimation(self,idleCurrent):
        if self.idleIndex >= 3.9:
            self.idleIndex = 0
        else:
            self.idleIndex += 0.01
        self.image = idleCurrent[int(self.idleIndex)]
        


    def scaleImage(self, img_surf, w, h):
        return pygame.transform.scale(img_surf, (w, h))

    def quitgame():
        pygame.quit()
        quit()

    def text_objects(self, text, pos, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect(center=pos)

    def button(self, msg, x, y, w, h, inactive_color, active_color):
        """Create a button dictionary with the images and a rect."""
        smallText = pygame.font.Font("8-BIT WONDER.TTF", 18)
        text_surf, text_rect = self.text_objects(
            msg, (w/2, h/2), smallText, self.black)
        # Create the normal and hover surfaces and blit the text onto them.
        surface = pygame.Surface((w, h))
        surface.fill(inactive_color)
        surface.blit(text_surf, text_rect)
        surface_hover = pygame.Surface((w, h))
        surface_hover.fill(active_color)
        surface_hover.blit(text_surf, text_rect)
        return {'active_surface': surface,
                'surface': surface,
                'surface_hover': surface_hover,
                'rect': pygame.Rect(x-(w/2), y, w, h),
                }

    def resetDelay(self):

        pygame.time.wait(200)
        

    def setImage(self, img_Surf, x, y, w, h):
        image_rect = pygame.Rect(x-(w/2), y, w, h)
        image_surf = self.scaleImage(img_Surf, w, h)
        return image_surf, image_rect

    def fillBack(self):
        for i in range(0, self.HEIGHT, 16):
            for k in range(0, self.WIDTH, 16):
                self.screen.blit(self.floor_surface, (k, i))

    def newGame(self):
        self.started = False

    def handleImages(self):
        self.fillBack()
        largeText = pygame.font.Font("8-BIT WONDER.TTF", 48)
        textSurf, textRect = self.text_objects(
            "Game Paused", (self.WIDTH/2, self.HEIGHT/2), largeText, self.blue)
        textRect.center = ((self.WIDTH/2), 100)
        self.screen.blit(textSurf, textRect)

    # def health(self):
    #     health0_Surf, health0_Rect = self.setImage(
    #         self.health0_surface, self.WIDTH/2 , 0, self.healthWidth, self.healthHeight)
    #     health1_Surf, health1_Rect = self.setImage(
    #         self.health1_surface, self.WIDTH/2, 0, self.healthWidth, self.healthHeight)
    #     health2_Surf, health2_Rect = self.setImage(
    #         self.health2_surface, self.WIDTH/2, 0, self.healthWidth, self.healthHeight)
    #     health3_Surf, health3_Rect = self.setImage(
    #         self.health3_surface, self.WIDTH/2, 0, self.healthWidth, self.healthHeight)
    #     health4_Surf, health4_Rect = self.setImage(
    #         self.health4_surface, self.WIDTH/2, 0, self.healthWidth, self.healthHeight)
    #     health5_Surf, health5_Rect = self.setImage(
    #         self.health5_surface, self.WIDTH/2 - 150, 0, self.healthWidth, self.healthHeight)

    #     # self.screen.blit(health5_Surf, health5_Rect)

    def paused(self):
        self.started = True
        self.handleImages()

        resumeSurf, resumeRect = self.setImage(
            self.resume_surf, self.WIDTH/2, self.HEIGHT/2 - 100, self.imgWidth, self.imgHeight)
        menuSurface, menuRect = self.setImage(
            self.menu_surface, self.WIDTH/2, self.HEIGHT/2 + 25, self.imgWidth, self.imgHeight)
        highSurf, highRect = self.setImage(
            self.highScore_surf, self.WIDTH/2, self.HEIGHT/2 + 150, self.imgWidth, self.imgHeight)
        quitSurface, quitRect = self.setImage(
            self.quit_surface, self.WIDTH/2, self.HEIGHT/2 + 275, self.imgWidth, self.imgHeight)

        while self.started:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEMOTION:
                    # Switch the active surface of the buttons
                    # if we're hovering over them.
                    if resumeRect.collidepoint(pygame.mouse.get_pos()):     
                        if self.soundFlag0:
                            self.soundFlag0 = False
                            self.hover_sound.play()
                                              
                        resumeSurf, resumeRect = self.setImage(
                            self.resume_surf, self.WIDTH/2, self.HEIGHT/2 - 100, self.imgWidth + self.widthAdd, self.imgHeight + self.heightAdd)
                    else:
                        self.handleImages()
                        self.soundFlag0 = True
                        resumeSurf, resumeRect = self.setImage(
                            self.resume_surf, self.WIDTH/2, self.HEIGHT/2 - 100, self.imgWidth, self.imgHeight)

                    if menuRect.collidepoint(pygame.mouse.get_pos()):
                        if self.soundFlag1:
                            self.soundFlag1 = False
                            self.hover_sound.play()
                        menuSurface, menuRect = self.setImage(
                            self.menu_surface, self.WIDTH/2, self.HEIGHT/2 + 25, self.imgWidth + self.widthAdd, self.imgHeight + self.heightAdd)

                    else:
                        self.handleImages()
                        self.soundFlag1 = True
                        menuSurface, menuRect = self.setImage(
                            self.menu_surface, self.WIDTH/2, self.HEIGHT/2 + 25, self.imgWidth, self.imgHeight)

                    if highRect.collidepoint(pygame.mouse.get_pos()):
                        if self.soundFlag2:
                            self.soundFlag2 = False
                            self.hover_sound.play()
                        highSurf, highRect = self.setImage(
                            self.highScore_surf, self.WIDTH/2, self.HEIGHT/2 + 150, self.imgWidth + self.widthAdd, self.imgHeight + self.heightAdd)
                    else:
                        self.handleImages()
                        self.soundFlag2 = True
                        highSurf, highRect = self.setImage(
                            self.highScore_surf, self.WIDTH/2, self.HEIGHT/2 + 150, self.imgWidth, self.imgHeight)

                    if quitRect.collidepoint(pygame.mouse.get_pos()):
                        if self.soundFlag3:
                            self.soundFlag3 = False
                            self.hover_sound.play()
                        quitSurface, quitRect = self.setImage(
                            self.quit_surface, self.WIDTH/2, self.HEIGHT/2 + 275, self.imgWidth + self.widthAdd, self.imgHeight + self.heightAdd)
                    else:
                        self.handleImages()
                        self.soundFlag3 = True
                        quitSurface, quitRect = self.setImage(
                            self.quit_surface, self.WIDTH/2, self.HEIGHT/2 + 275, self.imgWidth, self.imgHeight)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the buttons were clicked.
                    if resumeRect.collidepoint(event.pos): 
                        self.press_sound.play()
                        self.resetDelay()
                        return  # Return to the main loop.

                    elif menuRect.collidepoint(event.pos):
                        self.press_sound.play()
                        self.resetDelay()

                    elif highRect.collidepoint(event.pos):
                        self.press_sound.play()
                        self.resetDelay()

                    elif quitRect.collidepoint(event.pos):
                        self.press_sound.play()
                        
                        self.resetDelay()
                        pygame.quit()
                        sys.exit()
                            
                        
            self.screen.blit(resumeSurf, resumeRect)
            self.screen.blit(menuSurface, menuRect)
            self.screen.blit(highSurf, highRect)
            self.screen.blit(quitSurface, quitRect)
            pygame.display.update()


class Start(Ui):
    def __init__(self, screen, WIDTH, HEIGHT, floor_surface, started) -> None:
        super().__init__(screen, WIDTH, HEIGHT, floor_surface, started)

    def startHandle(self):
        Ui.fillBack(self)
        startText = pygame.font.Font("8-BIT WONDER.TTF", 48)
        textSurf, textRect = self.text_objects(
            "Soup", (self.WIDTH/2, self.HEIGHT/2), startText, self.blue)
        textRect.center = ((self.WIDTH/2), 100)
        self.screen.blit(textSurf, textRect)

    def startUi(self):
        self.startHandle()
        self.idleAnimation(self.idleCurrent_player)
        
        playSurf, playRect = self.setImage(
            self.start_surface, self.WIDTH/2, self.HEIGHT/2 - 100, self.imgWidth, self.imgHeight)
        highSurf, highRect = self.setImage(
            self.highScore_surf, self.WIDTH/2, self.HEIGHT/2 + 25, self.imgWidth, self.imgHeight)
        quitSurf, quitRect = self.setImage(
            self.quit_surface, self.WIDTH/2, self.HEIGHT/2 + 150, self.imgWidth, self.imgHeight)

        while self.started:
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEMOTION:
                    # Switch the active surface of the buttons
                    # if we're hovering over them.
                    if playRect.collidepoint(pygame.mouse.get_pos()):
                        if self.soundFlag4:
                            self.soundFlag4 = False
                            self.hover_sound.play()
                        playSurf, playRect = self.setImage(
                            self.start_surface, self.WIDTH/2, self.HEIGHT/2 - 100, self.imgWidth + self.widthAdd, self.imgHeight + self.heightAdd)

                    else:
                        self.startHandle()
                        self.soundFlag4 = True
                        playSurf, playRect = self.setImage(
                            self.start_surface, self.WIDTH/2, self.HEIGHT/2 - 100, self.imgWidth, self.imgHeight)

                    if highRect.collidepoint(pygame.mouse.get_pos()):
                        if self.soundFlag5:
                            self.soundFlag5 = False
                            self.hover_sound.play()
                        highSurf, highRect = self.setImage(
                            self.highScore_surf, self.WIDTH/2, self.HEIGHT/2 + 25, self.imgWidth + self.widthAdd, self.imgHeight + self.heightAdd)
                    else:
                        self.startHandle()
                        self.soundFlag5 = True
                        highSurf, highRect = self.setImage(
                            self.highScore_surf, self.WIDTH/2, self.HEIGHT/2 + 25, self.imgWidth, self.imgHeight)

                    if quitRect.collidepoint(pygame.mouse.get_pos()):
                        if self.soundFlag6:
                            self.soundFlag6 = False
                            self.hover_sound.play()
                        quitSurf, quitRect = self.setImage(
                            self.quit_surface, self.WIDTH/2, self.HEIGHT/2 + 150, self.imgWidth + self.widthAdd, self.imgHeight + self.heightAdd)
                    else:
                        self.startHandle()
                        self.soundFlag6 = True
                        quitSurf, quitRect = self.setImage(
                            self.quit_surface, self.WIDTH/2, self.HEIGHT/2 + 150, self.imgWidth, self.imgHeight)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the buttons were clicked.
                    if playRect.collidepoint(event.pos):
                        self.press_sound.play()
                        self.newGame()  # Return to the main loop.
                        self.resetDelay()

                    elif highRect.collidepoint(event.pos):
                        self.press_sound.play()
                        self.resetDelay()

                    elif quitRect.collidepoint(event.pos):
                        self.press_sound.play()
                        self.resetDelay()
                        pygame.quit()
                        sys.exit()
                    
            self.screen.blit(playSurf, playRect)
            self.screen.blit(highSurf, highRect)
            self.screen.blit(quitSurf, quitRect)
            self.screen.blit(self.image,(300,400))
            self.screen.blit(self.image_enemy,(self.WIDTH-300,400))

            pygame.display.update()


class GameOver(Ui):
    def __init__(self, screen, WIDTH, HEIGHT, floor_surface, started) -> None:
        super().__init__(screen, WIDTH, HEIGHT, floor_surface, started)

    def gameOver(self):
        Ui.fillBack(self)
        gameOverText = pygame.font.Font("8-BIT WONDER.TTF", 48)
        newText = pygame.font.Font("8-BIT WONDER.TTF", 24)

        toSurf, toRect = self.text_objects(
            "Game Over", (self.WIDTH/2, self.HEIGHT/2), gameOverText, (102, 76, 155))
        taSurf, taRect = self.text_objects(
            "Press Enter to exit game", (self.WIDTH/2, self.HEIGHT/2 + 200), newText, self.white)

        self.screen.blit(toSurf, toRect)
        self.screen.blit(taSurf, taRect)

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
                        pygame.quit()
                        exit()
            pygame.display.update()
