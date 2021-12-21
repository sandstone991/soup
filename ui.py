
import pygame
from pygame import mixer
import sys
import datetime



class Images:
    def __init__(self, *args, **kwargs) -> None:
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
        self.health0_surface = pygame.image.load(
            'Textures/imagesUi/health0.png').convert()
        self.health1_surface = pygame.image.load(
            'Textures/imagesUi/health1.png').convert()
        self.health2_surface = pygame.image.load(
            'Textures/imagesUi/health2.png').convert()
        self.health3_surface = pygame.image.load(
            'Textures/imagesUi/health3.png').convert()
        self.health4_surface = pygame.image.load(
            'Textures/imagesUi/health4.png').convert()
        self.health5_surface = pygame.image.load(
            'Textures/imagesUi/health5.png').convert()

        self.press_sound = mixer.Sound('audio/ui/press.wav')
        self.hover_sound = mixer.Sound('audio/ui/hover.wav')
        super(Images, self).__init__(*args, **kwargs)


class Colors:
    def __init__(self, *args, **kwargs) -> None:
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 179, 255)
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

        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.floor_surface = floor_surface
        self.started = started
        self.imgWidth = 250
        self.imgHeight = 70
        self.widthAdd = 80
        self.heightAdd = 25
        self.healthWidth = 300
        self.healthHeight = 100

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

    def health(self):
        health0_Surf, health0_Rect = self.setImage(
            self.health0_surface, self.WIDTH/2, 0, self.healthWidth, self.healthHeight)
        health1_Surf, health1_Rect = self.setImage(
            self.health1_surface, self.WIDTH/2, 0, self.healthWidth, self.healthHeight)
        health2_Surf, health2_Rect = self.setImage(
            self.health2_surface, self.WIDTH/2, 0, self.healthWidth, self.healthHeight)
        health3_Surf, health3_Rect = self.setImage(
            self.health3_surface, self.WIDTH/2, 0, self.healthWidth, self.healthHeight)
        health4_Surf, health4_Rect = self.setImage(
            self.health4_surface, self.WIDTH/2, 0, self.healthWidth, self.healthHeight)
        health5_Surf, health5_Rect = self.setImage(
            self.health5_surface, self.WIDTH/2, 0, self.healthWidth, self.healthHeight)

        self.screen.blit(health5_Surf, health5_Rect)

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
                        resumeSurf, resumeRect = self.setImage(
                            self.resume_surf, self.WIDTH/2, self.HEIGHT/2 - 100, self.imgWidth + self.widthAdd, self.imgHeight + self.heightAdd)
                    else:
                        self.handleImages()
                        resumeSurf, resumeRect = self.setImage(
                            self.resume_surf, self.WIDTH/2, self.HEIGHT/2 - 100, self.imgWidth, self.imgHeight)

                    if menuRect.collidepoint(pygame.mouse.get_pos()):
                        menuSurface, menuRect = self.setImage(
                            self.menu_surface, self.WIDTH/2, self.HEIGHT/2 + 25, self.imgWidth + self.widthAdd, self.imgHeight + self.heightAdd)

                    else:
                        self.handleImages()
                        menuSurface, menuRect = self.setImage(
                            self.menu_surface, self.WIDTH/2, self.HEIGHT/2 + 25, self.imgWidth, self.imgHeight)

                    if highRect.collidepoint(pygame.mouse.get_pos()):
                        highSurf, highRect = self.setImage(
                            self.highScore_surf, self.WIDTH/2, self.HEIGHT/2 + 150, self.imgWidth + self.widthAdd, self.imgHeight + self.heightAdd)
                    else:
                        self.handleImages()
                        highSurf, highRect = self.setImage(
                            self.highScore_surf, self.WIDTH/2, self.HEIGHT/2 + 150, self.imgWidth, self.imgHeight)

                    if quitRect.collidepoint(pygame.mouse.get_pos()):
                        quitSurface, quitRect = self.setImage(
                            self.quit_surface, self.WIDTH/2, self.HEIGHT/2 + 275, self.imgWidth + self.widthAdd, self.imgHeight + self.heightAdd)
                    else:
                        self.handleImages()
                        quitSurface, quitRect = self.setImage(
                            self.quit_surface, self.WIDTH/2, self.HEIGHT/2 + 275, self.imgWidth, self.imgHeight)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the buttons were clicked.
                    if resumeRect.collidepoint(event.pos): 
                        self.press_sound.play()
                        return  # Return to the main loop.

                    elif menuRect.collidepoint(event.pos):
                        self.press_sound.play()

                    elif highRect.collidepoint(event.pos):
                        self.press_sound.play()

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
            "Game Started", (self.WIDTH/2, self.HEIGHT/2), startText, self.white)
        textRect.center = ((self.WIDTH/2), 100)
        self.screen.blit(textSurf, textRect)

    def startUi(self):
        self.startHandle()
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
                        playSurf, playRect = self.setImage(
                            self.start_surface, self.WIDTH/2, self.HEIGHT/2 - 100, self.imgWidth + self.widthAdd, self.imgHeight + self.heightAdd)

                    else:
                        self.startHandle()
                        playSurf, playRect = self.setImage(
                            self.start_surface, self.WIDTH/2, self.HEIGHT/2 - 100, self.imgWidth, self.imgHeight)

                    if highRect.collidepoint(pygame.mouse.get_pos()):
                        highSurf, highRect = self.setImage(
                            self.highScore_surf, self.WIDTH/2, self.HEIGHT/2 + 25, self.imgWidth + self.widthAdd, self.imgHeight + self.heightAdd)
                    else:
                        self.startHandle()
                        highSurf, highRect = self.setImage(
                            self.highScore_surf, self.WIDTH/2, self.HEIGHT/2 + 25, self.imgWidth, self.imgHeight)

                    if quitRect.collidepoint(pygame.mouse.get_pos()):
                        quitSurf, quitRect = self.setImage(
                            self.quit_surface, self.WIDTH/2, self.HEIGHT/2 + 150, self.imgWidth + self.widthAdd, self.imgHeight + self.heightAdd)
                    else:
                        self.startHandle()
                        quitSurf, quitRect = self.setImage(
                            self.quit_surface, self.WIDTH/2, self.HEIGHT/2 + 150, self.imgWidth, self.imgHeight)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the buttons were clicked.
                    if playRect.collidepoint(event.pos):
                        self.press_sound.play()
                        self.newGame()  # Return to the main loop.
                    
                    elif highRect.collidepoint(event.pos):
                        self.press_sound.play()

                    elif quitRect.collidepoint(event.pos):
                        self.press_sound.play()
                        self.resetDelay()
                        pygame.quit()
                        sys.exit()
                    
            self.screen.blit(playSurf, playRect)
            self.screen.blit(highSurf, highRect)
            self.screen.blit(quitSurf, quitRect)

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
            "Press Enter to play again", (self.WIDTH/2, self.HEIGHT/2 + 200), newText, self.white)

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
            pygame.display.update()
