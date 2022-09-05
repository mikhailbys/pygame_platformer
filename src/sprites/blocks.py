import pyganim
from pygame import sprite, Surface, Color, Rect, image
from pygame.sprite import Sprite

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

ASSET_PATH = 'assets/platform/platform.png'
ASSET_GROUND_PATH = 'assets/ground/ground.png'
ANIMATION_BLOCK_TELEPORT = [
    'assets/portal/portal1.png',
    'assets/portal/portal2.png'
]


# class represent the Platform sprite
class Platform(Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = image.load(ASSET_PATH)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


# class represent the Platform sprite
class Ground(Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = image.load(ASSET_GROUND_PATH)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


# class represent the Teleport sprite
class Teleport(Platform):
    def __init__(self, x, y, go_x, go_y):
        Platform.__init__(self, x, y)
        # whereto destination coordinates
        self.goX = go_x
        self.goY = go_y
        # animation
        bolt_anim = []
        for anim in ANIMATION_BLOCK_TELEPORT:
            bolt_anim.append((anim, 1.1))
        self.boltAnim = pyganim.PygAnimation(bolt_anim)
        self.boltAnim.play()

    def update(self):
        self.image.fill(Color(PLATFORM_COLOR))
        self.boltAnim.blit(self.image, (0, 0))
