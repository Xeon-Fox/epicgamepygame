import pygame as pg
import player
def update():
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player.set_animation("up")
        player.move(0, -10)
    if keys[pg.K_s]:
        player.set_animation("down")
        player.move(0, 10)
    if keys[pg.K_d]:
        player.set_animation("right")
        player.move(10, 0)
    if keys[pg.K_a]:
        player.set_animation("left")
        player.move(-10, 0)