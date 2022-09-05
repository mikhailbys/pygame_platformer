import pyganim as pyganim
from pygame import *
from pygame.sprite import Sprite

from src.sprites.Monster.monster import Monster
from src.sprites.Player.config import ANIMATION_LEFT, ANIMATION_RIGHT, ANIMATION_DELAY, ANIMATION_STAY, ANIMATION_JUMP_LEFT, \
    ANIMATION_JUMP_RIGHT, ANIMATION_JUMP
from src.sprites.Princess.princess import Princess
from src.sprites.Spikes.spike import Spikes
from src.sprites.blocks import Teleport

MOVE_SPEED = 6
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.35


# describes a main playable character's sprite
class Player(Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        # x/y moving speed, 0 - don't move
        self.x_vel = 0
        self.y_vel = 0
        # start position coordinates
        self.start_x = x
        self.start_y = y
        self.on_ground = False
        self.winner = False
        self.lives_count = 3

        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        # make background clear
        self.image.set_colorkey(Color(COLOR))

        # Animation
        # move to the right animation
        bolt_anim = []
        for anim in ANIMATION_RIGHT:
            bolt_anim.append((anim, ANIMATION_DELAY))
        self.bolt_anim_right = pyganim.PygAnimation(bolt_anim)
        self.bolt_anim_right.play()
        # move to the left animation
        bolt_anim = []
        for anim in ANIMATION_LEFT:
            bolt_anim.append((anim, ANIMATION_DELAY))
        self.bolt_anim_left = pyganim.PygAnimation(bolt_anim)
        self.bolt_anim_left.play()
        # don't move animation
        self.bolt_anim_stay = pyganim.PygAnimation(ANIMATION_STAY)
        self.bolt_anim_stay.play()
        # don't move by default
        self.bolt_anim_stay.blit(self.image, (0, 0))

        # jump to the right animation
        self.bolt_anim_jump_right = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.bolt_anim_jump_right.play()
        # jump to the left animation
        self.bolt_anim_jump_left = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.bolt_anim_jump_left.play()
        # jump animation
        self.bolt_anim_jump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.bolt_anim_jump.play()

    def update(self, left, right, up, platforms):
        if up:
            # jump only if on the ground
            if self.on_ground:
                self.y_vel = -JUMP_POWER
            self.image.fill(Color(COLOR))
            self.bolt_anim_jump.blit(self.image, (0, 0))

        if left:
            # Лево = x- n
            self.x_vel = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            if up:  # для прыжка влево есть отдельная анимация
                self.bolt_anim_jump_left.blit(self.image, (0, 0))
            else:
                self.bolt_anim_left.blit(self.image, (0, 0))

        if right:
            # Право = x + n
            self.x_vel = MOVE_SPEED
            self.image.fill(Color(COLOR))
            if up:
                self.bolt_anim_jump_right.blit(self.image, (0, 0))
            else:
                self.bolt_anim_right.blit(self.image, (0, 0))

        if not (left or right):  # stay, when no move input
            self.x_vel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.bolt_anim_stay.blit(self.image, (0, 0))

        if not self.on_ground:
            self.y_vel += GRAVITY

        # Мы не знаем, когда мы на земле((
        self.on_ground = False
        self.rect.y += self.y_vel
        self.collide(0, self.y_vel, platforms)

        # переносим свои положение на xvel
        self.rect.x += self.x_vel
        self.collide(self.x_vel, 0, platforms)

    def collide(self, x_vel, y_vel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):  # is player interact with Sprites
                if isinstance(p, Spikes) or isinstance(p, Monster):  # is Sprite is Spike/Monster
                    self.lives_count -= 1
                    if self.lives_count > 0:
                        self.restart()
                elif isinstance(p, Teleport):
                    self.teleporting(p.goX, p.goY)
                elif isinstance(p, Princess):  # is player interact with Princess
                    self.winner = True
                else:
                    if x_vel > 0:                      # если движется вправо
                        self.rect.right = p.rect.left # то не движется вправо

                    if x_vel < 0:                      # если движется влево
                        self.rect.left = p.rect.right # то не движется влево

                    if y_vel > 0:                      # если падает вниз
                        self.rect.bottom = p.rect.top  # то не падает вниз
                        self.on_ground = True          # и становится на что-то твердое
                        self.y_vel = 0                 # и энергия падения пропадает

                    if y_vel < 0:                      # если движется вверх
                        self.rect.top = p.rect.bottom  # то не движется вверх
                        self.y_vel = 0                 # и энергия прыжка пропадает

    def restart(self):
        time.wait(100)
        self.teleporting(self.start_x, self.start_y)  # перемещаемся в начальные координаты

    def teleporting(self, go_x, go_y):
        self.rect.x = go_x
        self.rect.y = go_y
