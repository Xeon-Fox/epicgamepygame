import pygame as pg
from core.animatedsprite import AnimatedSprite

class Fireball(AnimatedSprite):
    size = (143, 143)
    total_frames = 5
    power = 10

    def __init__(self, layer, position, speed):
        super().__init__(layer, position, speed, colidable = True)
        self.sprites['solid'] = pg.image.load("resources/fireball.png")
        self.current_animation = 'solid'

    def move(self, dx, dy):
        super().move(dx, dy)
        if self.collided_object:
            self.layer.remove(self)
            self.collided_object.damage(self.power)