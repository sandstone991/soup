import pygame
from pygame import display
from player import Player
from tiles import Tile,StaticTile,Create
from setting import tile_size,scale
from support import import_csv_layout, import_cut_graphics
from tiles_data import *



class Level:
    x_scroll=0
    y_scroll=0
    def __init__(self,level_data,surface):
            #general setup
        self.display_surface = surface
        # #wall setup
        wall_layout = import_csv_layout(level_data['wall'])
        self.wall_sprites =self.create_tile_group(wall_layout,'wall')
        
        #floor setup
        floor_layout = import_csv_layout(level_data['floor'])
        self.floor_sprites =self.create_tile_group(floor_layout,'floor')
        
        
        # #tower setup
        tower_layout = import_csv_layout(level_data['tower'])
        self.tower_sprites =self.create_tile_group(tower_layout,'tower')
       
        # wall2_layout = import_csv_layout(level_data['wall2'])
        # self.wall2_sprites =self.create_tile_group(wall2_layout,'wall2')
            
           
    def create_tile_group(self,layout,type):
        sprite_group  = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index,cell in enumerate(row):
                if cell != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    print (cell)
                    
                    if type == 'wall':
                        if int(cell)<1000 and int(cell)>-1:
                            wall_tile_list = import_cut_graphics('levels/level_data/wall.png')
                            tile_surface = wall_tile_list[int(cell)]
                            sprite = StaticTile(tile_size,x,y,tile_surface)
                            sprite_group.add(sprite)

                    if type == 'tower':
                        if int(cell)<14:
                            tower_type = tower[cell]
                            sprite = Create(tile_size,x,y,tower_type)
                            sprite_group.add(sprite)
                    
                    if type == 'floor':
                        if int(cell)<14:
                            floor_type = floor[cell]
                            sprite = Create(tile_size,x,y,floor_type)
                    sprite_group.add(sprite)

        return sprite_group




    def run (self):
        self.wall_sprites.draw(self.display_surface)
        self.wall_sprites.update(self.x_scroll,self.y_scroll)
        self.floor_sprites.update(self.x_scroll,self.y_scroll)
        self.floor_sprites.draw(self.display_surface)
        self.tower_sprites.update(self.x_scroll,self.y_scroll)
        self.tower_sprites.draw(self.display_surface)
        


