import pygame as pg
from core.layer import Layer

class StaticSprite:
    colidable = False
    size = (1, 1)
    position = (0,0)
    frame = 0
    sprites = {}
    current_animation = ''
    surface: pg.Surface = None
    layer: Layer = None

    def __init__(self, layer, position, colidable = False):
        self.colidable = colidable
        self.layer = layer
        self.position = position
        self.current_animation = '_'
        self.sprites['_'] = pg.Surface(self.size)
        self.surface = pg.Surface(self.size)
        self.surface.set_colorkey((0,0,0))


    def show(self):
        self.surface.fill((0,0,0))
        self.surface.blit(self.sprites[self.current_animation], (0,0), (
            self.frame * self.size[0], 
            0,
            self.size[0], 
            self.size[1]
        ))


    def next_frame(self):
        self.frame += 1
        if self.frame > self.total_frames - 1:
            self.frame = 0
        self.show()


    def move(self, dx, dy):
        x, y = self.position
        self.position = (x + dx, y + dy)
        self.next_frame()


    def update(self):
        self.layer.blit(self.surface, self.position)
    
    def damage(self, power):
        pass