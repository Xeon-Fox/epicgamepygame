import pygame as pg
class Player:
    size = (0,0)
    position = (0,0)
    frame = 0
    sprite = None
    controls = ()
    layer: pg.Surface = None
    frame_lines = {
        "up": 3,
        "down": 0,
        "right": 1,
        "left": 2
    }
    current_animation = ""
    surface: pg.Surface = None

    def __init__(self, layer, size, position, controls):
        self.size = size
        self.position = position
        self.controls = controls
        self.layer = layer
        self.sprite = pg.image.load("resources\Sprites.png")
        self.surface = pg.Surface(size)
        self.surface.set_colorkey((0,0,0))
        self.current_animation = "down"
        self.show()

    def show(self):
        self.surface.fill((0,0,0))
        self.surface.blit(self.sprite, (0, 0), (self.frame *  self.size[0], self.frame_lines[self.current_animation] *  self.size[1],  self.size[0], self.size[1]))
    
    def next_frame(self):
        self.frame +=1
        if self.frame > 3:
            self.frame = 0
        self.show()

    def move(self, dx, dy):
        x, y = self.position
        self.position = (x + dx, y + dy)
        self.next_frame()

    def set_animation(self, name):
        if name in self.frame_lines:
            self.current_animation = name
        match name:
            case "up":
                self.move(0, -10)
            case "down":
                self.move(0, 10)
            case "left":
                self.move(-10, 0)
            case "right":
                self.move(10, 0)

    def update(self):
        keys = pg.key.get_pressed()
        for control in self.controls:
            code = control["key"]
            name = control["animation"]
            if keys[code]:
                self.set_animation(name)
        self.layer.blit(self.surface, self.position)