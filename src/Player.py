import pygame as pg
class Player:
    def __init__(self, name, pos, skin, score, foot):
        self.name = name
        self.pos = pos
        self.skin = skin
        self.foot = foot 
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            y += self.foot
        if keys[pg.K_DOWN]:
            y -= self.foot
        if keys[pg.K_RIGHT]:
            x += self.foot
        if keys[pg.K_LEFT]:
            x += self.foot