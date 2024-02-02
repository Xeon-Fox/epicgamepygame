import pygame as pg

class Layer:
    objects = []
    surface:pg.Surface = None

    def __init__(self, surface):
        self.surface = surface
    
    def add(self, obj):
        self.objects.append(obj)
    
    def remove(self, obj):
        self.objects.remove(obj)
    
    def blit(self, surface, position):
        self.surface.blit(surface, position)
    
    def update(self):
        for x in self.objects:
            x.update()