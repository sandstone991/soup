import pygame
import sys

class Colors:
    def __init__(self) -> None:
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (200,0,0)
        self.green = (0,200,0)
        self.bright_red = (255,0,0)
        self.bright_green = (0,255,0)
        self.black = (0, 0, 0, 0)
        self.block_color = (53,115,255)
        self.gray = pygame.Color("gray30")

class Ui(Colors):


    def __init__(self,screen,WIDTH,HEIGHT,floor_surface,started) -> None:
        super().__init__()
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.floor_surface = floor_surface
        self.started = started
        


    def quitgame():
        pygame.quit()
        quit()

    def text_objects(self,text, pos, font,color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect(center=pos)

    def button(self,msg, x, y, w, h, inactive_color, active_color):
        """Create a button dictionary with the images and a rect."""
        smallText = pygame.font.Font("8-BIT WONDER.TTF",18)
        text_surf, text_rect = self.text_objects(msg, (w/2, h/2),smallText , self.black)
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

    def fillBack(self):
            for i in range(0, self.HEIGHT, 16):
                for k in range(0, self.WIDTH, 16):
                    self.screen.blit(self.floor_surface, (k, i))

    def newGame(self):
        self.started = False

    def paused(self):
        self.started = True
        self.fillBack()

        largeText = pygame.font.Font("8-BIT WONDER.TTF",48)
        textSurf, textRect = self.text_objects("Game Paused",(self.WIDTH/2, self.HEIGHT/2), largeText, self.white)
        textRect.center = ((self.WIDTH/2),100)
        self.screen.blit(textSurf, textRect)
        resume_button = self.button('Resume', self.WIDTH/2, self.HEIGHT/2, 200, 50, self.white, self.gray)
        newGame_button = self.button('New game', self.WIDTH/2, (self.HEIGHT/2)+100, 200, 50, self.white, self.gray)
        quit_button = self.button('Quit', self.WIDTH/2, (self.HEIGHT/2)+200, 200, 50, self.white, self.gray)
        while self.started:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEMOTION:
                    # Switch the active surface of the buttons
                    # if we're hovering over them.
                    for btn in (resume_button, quit_button,newGame_button):
                        if btn['rect'].collidepoint(event.pos):
                            btn['active_surface'] = btn['surface_hover']
                        else:
                            btn['active_surface'] = btn['surface']
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the buttons were clicked.
                    if resume_button['rect'].collidepoint(event.pos):
                        return  # Return to the main loop.
                    elif newGame_button['rect'].collidepoint(event.pos):
                        self.newGame()

                    elif quit_button['rect'].collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            self.screen.blit(resume_button['active_surface'], resume_button['rect'])
            self.screen.blit(newGame_button['active_surface'], newGame_button['rect'])
            self.screen.blit(quit_button['active_surface'], quit_button['rect'])
            
            pygame.display.update()



class Start(Ui):
    def __init__(self, screen, WIDTH, HEIGHT, floor_surface,started) -> None:
        super().__init__(screen,WIDTH,HEIGHT,floor_surface,started)

    
    def startUi(self):
        Ui.fillBack(self)
        startText = pygame.font.Font("8-BIT WONDER.TTF",48)
        textSurf, textRect = self.text_objects("Game Started",(self.WIDTH/2, self.HEIGHT/2), startText, self.white)
        textRect.center = ((self.WIDTH/2),100)
        self.screen.blit(textSurf, textRect)
        newGame_button = self.button('New game', self.WIDTH/2,self.HEIGHT/2, 200, 50, self.white, self.gray)
        quit_button = self.button('Quit', self.WIDTH/2, (self.HEIGHT/2)+100, 200, 50, self.white, self.gray)

        while self.started:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEMOTION:
                    # Switch the active surface of the buttons
                    # if we're hovering over them.
                    for btn in (newGame_button, quit_button):
                        if btn['rect'].collidepoint(event.pos):
                            btn['active_surface'] = btn['surface_hover']
                        else:
                            btn['active_surface'] = btn['surface']
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the buttons were clicked.
                    if newGame_button['rect'].collidepoint(event.pos):
                        self.newGame() # Return to the main loop.
                    elif quit_button['rect'].collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
            self.screen.blit(newGame_button['active_surface'], newGame_button['rect'])
            self.screen.blit(quit_button['active_surface'], quit_button['rect'])
            
            pygame.display.update()

