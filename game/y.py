import pygame as pg
from player import Player

FPS = 25
pg.init()
Clock = pg.time.Clock()
screen = pg.display.set_mode((1024, 768))
background = pg.image.load("resources/bg.png")

me = Player(screen, ( 256/4, 256/4), (512-40, 384-50),(
    {"key": pg.K_UP, "animation": "up"},
    {"key": pg.K_DOWN, "animation": "down"},
    {"key": pg.K_LEFT, "animation": "left"},
    {"key": pg.K_RIGHT, "animation": "right"}
))
bro = Player(screen, ( 256/4, 256/4), (112-40, 384-50),(
    {"key": pg.K_w, "animation": "up"},
    {"key": pg.K_s, "animation": "down"},
    {"key": pg.K_a, "animation": "left"},
    {"key": pg.K_d, "animation": "right"}
))

gameover = False
while not gameover:
    events = pg.event.get()
    for e in events:
        if e.type == pg.QUIT:
            gameover = True

    screen.blit(background, (0, 0))
    me.update()
    bro.update()
    pg.display.update()
    Clock.tick(FPS)