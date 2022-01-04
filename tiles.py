import pygame
from pygame import surface
from setting import scale
from tiles_data import floor

class Tile(pygame.sprite.Sprite):
    def __init__(self,size,x,y):
        super().__init__()
        self.image = pygame.Surface((size,size))
        
        self.rect =self.image.get_rect(topleft =(x,y))

    def update(self,x_shift,y_shift):
        self.rect.x += x_shift 
        self.rect.y -= y_shift

    
class StaticTile(Tile):
    def __init__(self, size, x, y,surface):
        super().__init__(size, x, y)
        self.image = surface


class Create (StaticTile):
    def __init__(self, size, x, y,type):
        # self.floor_type = floor[str(cell)]
      
        super().__init__(size,x,y, pygame.image.load(type).convert_alpha())
        offset_y = y +size 
        self.rect = self.image.get_rect(bottomleft = (x,offset_y))
        
        
       
         
