import pygame as pg
import controls 
import player
FPS = 25
pg.init()
Clock = pg.time.Clock()
screen = pg.display.set_mode((1024, 768))
background = pg.image.load("resources/bg.png")

me = player.init((256/4, 256/4), (512-40, 384-50), "resources\Sprites.png")

gameover = False
while not gameover:
    events = pg.event.get()
    for e in events:
        if e.type == pg.QUIT:
            gameover = True

    controls.update()
    screen.blit(background, (0, 0))
    screen.blit(me, player.my_position)
    pg.display.update()
    Clock.tick(FPS)