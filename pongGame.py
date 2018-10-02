import ball as b
import gameFunctions as gF
import os
import pygame
import settings as s
import titleScreen as tS
import scoreboard as sb


def run_game():
    #   Provides consistent window positioning. These settings center pygame window for my computer.
    os.environ['SDL_VIDEO_WINDOW_POS'] = '60, 35'
    pygame.init()

    #   Sets up game window and local variables.
    settings = s.Settings()
    screen = pygame.display.set_mode((settings.get_screen_width(),
                                     settings.get_screen_height()))
    pygame.display.set_caption(settings.get_game_title())

    title_sequence = tS.Title(screen, settings)

    ball = b.Ball(screen, settings)
    paddles = gF.create_paddles_list(ball, screen, settings)
    scoreboard = sb.ScoreBoard(ball, paddles, screen, settings, title_sequence)

    while True:
        gF.update_screen(ball, paddles, scoreboard, screen, settings)
        gF.check_events(settings)
        pygame.display.flip()


run_game()
