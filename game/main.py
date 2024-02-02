import pygame as pg
from objects.player import Player
from core.layer import Layer
from objects.tree import Tree

FPS = 25
pg.init()
Clock = pg.time.Clock()
screen = pg.display.set_mode((1024, 768))
layer = Layer(screen)
background = pg.image.load("resources/bg.png")

layer.add(Player(layer, (512-40, 384-50), (
    {"key": pg.K_UP, "animation": "up"},
    {"key": pg.K_DOWN, "animation": "down"},
    {"key": pg.K_LEFT, "animation": "left"},
    {"key": pg.K_RIGHT, "animation": "right"},
    {"key": pg.K_e, "animation": "attack"}
)))

layer.add(Tree(layer, (250, 400)))
layer.add(Tree(layer, (650, 400), True))

gameover = False
while not gameover:
    events = pg.event.get()
    for e in events:
        if e.type == pg.QUIT:
            gameover = True

    layer.blit(background, (0, 0))
    layer.update()
    pg.display.update()
    Clock.tick(FPS)