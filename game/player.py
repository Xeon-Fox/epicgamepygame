import pygame as pg

my_size = (0,0)
my_position = (0,0)
my_frame = 0
my_sprite = None
my_frame_lines = {
    "up": 3,
    "down": 0,
    "right": 1,
    "left": 2
}
current_animation = ""
my_surface: pg.Surface = None

def init(size, position):
    global my_size, my_position, my_surface, my_sprite, current_animation
    my_size = size
    my_position = position
    my_sprite = pg.image.load("resources\Sprites.png")
    me = pg.Surface(my_size)
    me.set_colorkey((0,0,0))
    current_animation = "down"
    my_surface = me
    show()
    return me

def show():
    my_surface.fill((0,0,0))
    my_surface.blit(my_sprite, (0, 0), (my_frame * my_size[0], my_frame_lines[current_animation] * my_size[1], my_size[0], my_size[1]))

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

def set_animation(name):
    global current_animation
    if name in my_frame_lines:
        current_animation = name