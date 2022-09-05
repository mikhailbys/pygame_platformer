import pyganim
from pygame import Color

from src.sprites.blocks import Platform

ANIMATION_PRINCESS = [
            'assets/princess/princess_l.png',
            'assets/princess/princess_r.png']
COLOR = "#888888"


class Princess(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color(COLOR))
        self.image.set_colorkey(Color(COLOR))
        bolt_anim = []
        for anim in ANIMATION_PRINCESS:
            bolt_anim.append((anim, 1.5))
        self.boltAnim = pyganim.PygAnimation(bolt_anim)
        self.boltAnim.play()

    def update(self):
        self.boltAnim.blit(self.image, (0, 0))
