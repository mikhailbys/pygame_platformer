import time

import pygame

from src.config import DISPLAY


def render_text(fnt, what, color, where, screen):
    text_to_show = fnt.render(what, 0, pygame.Color(color))
    screen.blit(text_to_show, where)


def display_lives_counter(screen, lives_count):
    # todo with sprites
    string = ''
    for i in range(lives_count):
        string += '<3'

    render_text(
        pygame.font.SysFont("Arial", 32),
        string,
        "red",
        (DISPLAY[0] - 200, 50),
        screen
    )


def display_game_over(screen):
    time.sleep(300)
    render_text(
        pygame.font.SysFont("Arial", 64),
        'GAME OVER',
        "white",
        (DISPLAY[0] / 2, DISPLAY[1] / 2),
        screen
    )


def display_game_complete(screen):
    time.sleep(300)
    render_text(
        pygame.font.SysFont("Arial", 64),
        'COMPLETE',
        "white",
        (DISPLAY[0] / 2, DISPLAY[1] / 2),
        screen
    )
