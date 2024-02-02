import pygame as pg
from .animatedsprite import AnimatedSprite

class ControllableSprite(AnimatedSprite):
    controls = ()

    def __init__(self, layer, position, speed, controls, colidable = False):
        super().__init__(layer, position, speed, colidable)
        self.controls = controls

    
    def update(self):
        keys = pg.key.get_pressed()
        for control in self.controls:
            code = control['key']
            name = control['animation']
            if keys[code]:
                self.set_animation(name)
        self.layer.blit(self.surface, self.position)


    def set_animation(self, name):
        if name in self.sprites:
            self.current_animation = name
