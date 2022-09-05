import pygame

from src.sprites.blocks import PLATFORM_WIDTH, PLATFORM_HEIGHT, Platform, Teleport
from src.camera import Camera, camera_configure
from src.levels.level_select import get_level
from src.sprites.Monster.monster import Monster
from src.sprites.Player.player import Player
from src.sprites.Princess.princess import Princess
from src.sprites.Spikes.spike import Spikes


def load_level(level_number):
    level, teleports, level_monsters, player_pos = get_level(level_number)

    # init entities groups
    entities = pygame.sprite.Group()  # Все объекты
    animated_entities = pygame.sprite.Group()
    monsters = pygame.sprite.Group()  # Все передвигающиеся объекты
    platforms = []  # то, во что мы будем врезаться или опираться

    # init hero
    hero = Player(player_pos[0], player_pos[1])  # создаем героя по (x,y) координатам
    # по умолчанию — стоим
    left = right = False
    up = False
    entities.add(hero)

    timer = pygame.time.Clock()

    # load level
    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "*":
                bd = Spikes(x, y)
                entities.add(bd)
                platforms.append(bd)
            if col == "P":
                pr = Princess(x, y)
                entities.add(pr)
                platforms.append(pr)
                animated_entities.add(pr)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нул

    # init entities
    for tp in teleports:
        tp = Teleport(tp[0], tp[1], tp[2], tp[3])
        entities.add(tp)
        platforms.append(tp)
        animated_entities.add(tp)

    for monster in level_monsters:
        if monster[0] == 'FIRE':  # todo dict
            mn = Monster(monster[1], monster[2], monster[3], monster[4], monster[5], monster[6])
            entities.add(mn)
            platforms.append(mn)
            monsters.add(mn)

    # init camera
    total_level_width = len(level[0]) * PLATFORM_WIDTH  # level fact width
    total_level_height = len(level) * PLATFORM_HEIGHT  # level fact height
    camera = Camera(camera_configure, total_level_width, total_level_height)

    return camera, timer, left, right, up, hero, entities, animated_entities, monsters, platforms
