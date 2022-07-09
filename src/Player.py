import pygame as pg
class Player:
    def __init__(self, name, pos, skin, score, foot, is_bot=True):
        self.name = name
        self.pos = pos
        self.skin = skin
        self.foot = foot
        self.is_bot = is_bot
    def move(self):
        if self.is_bot:
            
        else:
            keys = pg.key.get_pressed()
            if keys[pg.K_UP]:
                y += self.foot
            if keys[pg.K_DOWN]:
                y -= self.foot
            if keys[pg.K_RIGHT]:
                x += self.foot
            if keys[pg.K_LEFT]:
                x += self.foot  