import pygame as pg

my_size = (0,0)
my_position = (0,0)
my_frame = 0
my_sprite = None
my_surface: pg.Surface = None

def init(size, position, filename):
    global my_size, my_position, my_surface, my_sprite
    my_size = size
    my_position = position
    my_sprite = pg.image.load(filename)
    me = pg.Surface(my_size)
    me.set_colorkey((0,0,0))
    my_surface = me
    show()
    return me

def show():
    my_surface.fill((0,0,0))
    my_surface.blit(my_sprite, (0, 0), (my_frame * my_size[0], 0, my_size[0], my_size[1]))



def next_frame():
    global my_frame
    my_frame +=1
    if my_frame > 3:
        my_frame = 0
    show()

def move(dx, dy):
    global my_position
    x, y = my_position
    my_position = (x + dx, y + dy)
    next_frame()