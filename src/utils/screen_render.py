import time

import pygame

from src.config import DISPLAY


FONT = 'fonts/Super-Mario-World.ttf'

def render_text(fnt, what, color, where, screen):
    text_to_show = fnt.render(what, 0, pygame.Color(color))
    screen.blit(text_to_show, where)


def display_lives_counter(screen, lives_count):
    # todo with sprites
    string = ''
    for i in range(lives_count):
        string += '<3'

    render_text(
        pygame.font.Font(FONT, 32),
        string,
        "red",
        (DISPLAY[0] - 200, 50),
        screen
    )


def display_game_over(screen):
    background_image = pygame.image.load('assets/background/gameover.jpg')
    screen.blit(background_image, (0, 0))
    pygame.display.update()


def display_game_complete(screen, is_win):
    cur_font = pygame.font.Font(FONT, 32)
    text = cur_font.render(
        "Game Complete! Exit in 3 sec" if is_win else "Exit in 3 sec",
        True,
        (255, 255, 255),
        # todo background
    )
    screen.blit(text, (0, 0))
    pygame.display.update()


def display_level_complete(screen):
    cur_font = pygame.font.Font(FONT, 38)
    text = cur_font.render(
        "Level complete!",
        True,
        (255, 255, 255),
        # todo background
    )
    screen.blit(text, (400, 300))
    pygame.display.update()
