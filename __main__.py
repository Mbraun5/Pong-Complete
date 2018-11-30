import ball as b
import gameFunctions as gF
import os
import pygame
import settings as s
import titleScreen as tS
import scoreboard as sb


class Main:
    def __init__(self):
        #   Provides consistent window positioning. These settings center pygame window for my computer.
        os.environ['SDL_VIDEO_WINDOW_POS'] = '60, 35'
        pygame.init()

        #   Sets up game window and local variables.
        self.settings = s.Settings()
        self.screen = pygame.display.set_mode((self.settings.get_screen_width(),
                                               self.settings.get_screen_height()))
        pygame.display.set_caption(self.settings.get_game_title())

        title_sequence = tS.Title(self.screen, self.settings)

        self.ball = b.Ball(self.screen, self.settings)
        self.paddles = gF.GameFunctions.create_paddles_list(self.ball, self.screen, self.settings)
        self.scoreboard = sb.ScoreBoard(self.ball, self.paddles, self.screen, self.settings, title_sequence)

    def play(self):
        while True:
            gF.GameFunctions.update_screen(self.ball, self.paddles, self.scoreboard, self.screen, self.settings)
            gF.GameFunctions.check_events(self.settings)
            pygame.display.flip()


if __name__ == '__main__':
    game = Main()
    game.play()
