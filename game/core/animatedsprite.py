import pygame as pg
from .staticsprite import StaticSprite

class AnimatedSprite(StaticSprite):
    size = (1, 1)
    position = (0,0)
    frame = 0
    total_frames = 1
    sprites = {}
    current_animation = ''
    surface: pg.Surface = None
    layer: pg.Surface = None

    def __init__(self, layer, position, speed, colidable = False):
        super().__init__(layer, position, colidable)
        self.speed = speed

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
        new_position = (x + dx, y + dy)
        self.collided_object = self.is_collision(new_position)
        if self.collided_object is None:
            self.position = new_position
            self.next_frame()


    def update(self):
        dx, dy = self.speed
        self.move(dx, dy)
        self.layer.blit(self.surface, self.position)
    
    def is_collision(self, position):
        if not self.colidable:
            return None
        x1, y1 = position
        w1, h1 = self.size
        for obj in self.layer.objects:
            if obj.colidable and not obj is self:
                x2, y2 = obj.position
                w2, h2 = obj.size
                if x1 > x2:
                    collision_x = x1 - x2 < w2
                else:
                    collision_x = x2 - x1 < w1
                if y1 > y2:
                    collision_y = y1 - y2 < h2
                else:
                    collision_y = y2 - y1 < h1
                if collision_x and collision_y:
                    return obj
        return None
