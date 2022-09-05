from pygame import image

from src.sprites.blocks import Platform


class Spikes(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("assets/spikes/spikes.png")
