import pygame
from pygame import *

from src.config import DISPLAY, FPS
from src.utils.level_loader import load_level
from src.levels.level_select import level_dict
from src.utils.screen_render import display_lives_counter, display_game_over, display_game_complete, \
    display_level_complete


# check if hero still have lives
def is_alive(hero):
    return hero.lives_count > 0


def main():
    # Init PyGame
    pygame.init()
    # Create window
    screen = pygame.display.set_mode(DISPLAY)
    # Set window title
    pygame.display.set_caption("Mario Game")
    # apply background
    background_image = pygame.image.load('assets/background/background.jpeg')
    #
    is_win = False

    for lvl in level_dict:
        # set up in-game modules
        camera, timer, left, right, up, hero, entities, animated_entities, monsters, platforms \
            = load_level(lvl)

        # main game loop
        # todo change for while running
        while not hero.winner and is_alive(hero):

            # fps
            timer.tick(FPS)

            # handle input events
            for e in pygame.event.get():
                if e.type == QUIT:
                    raise SystemExit("QUIT")
                if e.type == KEYDOWN and e.key == K_LEFT:
                    left = True
                if e.type == KEYDOWN and e.key == K_RIGHT:
                    right = True
                if e.type == KEYUP and e.key == K_RIGHT:
                    right = False
                if e.type == KEYUP and e.key == K_LEFT:
                    left = False
                if e.type == KEYDOWN and e.key == K_UP:
                    up = True
                if e.type == KEYUP and e.key == K_UP:
                    up = False

            # sprite updates
            screen.blit(background_image, (0, 0))
            animated_entities.update()
            monsters.update(platforms)
            hero.update(left, right, up, platforms)
            camera.update(hero)

            # apply camera
            for e in entities:
                screen.blit(e.image, camera.apply(e))

            # render counter
            display_lives_counter(screen, hero.lives_count)

            # update all and output on screen
            pygame.display.update()

        # on level exit
        if is_alive(hero) > 0:
            # on level complete
            is_win = True
            display_level_complete(screen)
            time.wait(2000)
        else:
            is_win = False
            display_game_over(screen)
            time.wait(2000)
            break

    # on game end
    display_game_complete(screen, is_win)
    time.wait(3000)


if __name__ == "__main__":
    main()
