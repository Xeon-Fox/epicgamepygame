import pygame as pg
from .fireball import Fireball
from core.controllablesprite import ControllableSprite

class Player(ControllableSprite):
    size = (64,64)
    total_frames = 4
    
    def __init__(self, layer, position, controls):
        super().__init__(layer, position, (0,0), controls, colidable = True)
        self.sprites['up'] = pg.image.load("resources/Sprite_Up.png")
        self.sprites['down'] = pg.image.load("resources/Sprite_Down.png")
        self.sprites['left'] = pg.image.load("resources/Sprite_Left.png")
        self.sprites['right'] = pg.image.load("resources/Sprite_Right.png")
        self.current_animation = 'right'
        self.show()


    def set_animation(self, name):
        super().set_animation(name)
        match name:
            case 'up':
                self.move(0, -10)
            case 'down':
                self.move(0, 10)  
            case 'left':
                self.move(-10, 0) 
            case 'right':
                self.move(10, 0)   
            case 'attack':
                self.new_fireball()
        

    def new_fireball(self):
        match self.current_animation:
            case 'left':
                fireball_x = self.position[0] - Fireball.size[0]
                fireball_y = self.position[1] + (self.size[1] - Fireball.size[1])/2
                fireball_speed = (-20, 0)
            case 'right':
                fireball_x = self.position[0] + self.size[0]
                fireball_y = self.position[1] + (self.size[1] - Fireball.size[1])/2
                fireball_speed = (+20, 0)
            case _:
                return
        newfire = Fireball(self.layer, (fireball_x,fireball_y), fireball_speed)
        self.layer.add(newfire)