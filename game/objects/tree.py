import pygame as pg
from core.staticsprite import StaticSprite

class Tree(StaticSprite):
    size = (380/2, 480/2)

    def __init__(self, layer, position, colidable=False):
        super().__init__(layer, position, colidable)
        self.sprites["_"] = pg.image.load("resources/tree.png")
        self.sprites["_"] = pg.transform.scale(self.sprites["_"], self.size)
        self.show()

    def damage(self, power):
        self.layer.remove(self)