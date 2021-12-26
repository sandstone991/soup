import pygame

class Particle():
    """
    A class that particles generated from
    
    Attributes:
    coordinates to start drawing from represnted by x,y
    random velocity in x and y directions that makes the circles drawn looks like mooving away
    random value of the radius of the generated circles 
    circles color 
    optional gravity attribute to make the particles drops down rather than flying 
    --------------------
    Methods:
    simple render() function that draw the particles on the surface
    this function just add the x and y velocity to the x,y coordinates
    then, checks if the optional gravity is given then makes the y velocity decreases
    and decrease the raduis of the circles to make it disappears
    
    """
    def __init__(self,x,y,xvel,yvel,radius,color,gravity=None) -> None:
        self.x=x
        self.y=y
        self.xvel=xvel
        self.yvel=yvel
        self.radius = radius
        self.color = color
        self.gravity = gravity

    def render(self,win):
        self.x += self.xvel
        self.y += self.yvel
        
        if self.gravity != None:
            self.yvel += self.gravity
        self.radius -= 0.3
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)