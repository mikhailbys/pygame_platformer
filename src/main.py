import pygame
from pygame import *

from src.config import DISPLAY, FPS
from src.utils.level_loader import load_level
from src.levels.level_select import level_dict
from src.utils.screen_render import display_lives_counter, display_game_over, display_game_complete


def main():
    pygame.init()  # Init PyGame
    screen = pygame.display.set_mode(DISPLAY)  # Create window
    pygame.display.set_caption("Mario Game")  # Set window title
    background_image = pygame.image.load('assets/background/background.jpeg')  # apply background

    for lvl in level_dict:
        # set up in-game modules
        timer, left, right, up, hero, entities, animated_entities, monsters, platforms \
            = load_level(lvl)
        running = True
        # main game loop
        while not hero.winner:  # change for while running

            if hero.lives_count == 0:
                running = False
                display_game_over(screen)

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

            # updates
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

        # когда заканчиваем уровень
        for e in entities:
            screen.blit(e.image, camera.apply(e))  # еще раз все перерисовываем
        cur_font = pygame.font.Font(None, 38)
        text = cur_font.render(("Level complete!"), True,
                                   (255, 255, 255))  # выводим надпись
        screen.blit(text, (10, 100))
        pygame.display.update()
        time.wait(10000)


if __name__ == "__main__":
    main()
