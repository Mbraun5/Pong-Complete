import pygame
import gameFunctions as gF
import time


class ScoreBoard:
    def __init__(self, ball, paddles, screen, settings, title_screen):
        self.settings = settings
        self.screen = screen
        self.ball = ball
        self.paddles = paddles
        self.title_screen = title_screen

        self.__leftScore = 0
        self.__rightScore = 0
        self.__leftScoreImage = None
        self.__rightScoreImage = None
        self.__leftScoreRect = None
        self.__rightScoreRect = None

        self.__farLeftScoreImage = None
        self.__farRightScoreImage = None
        self.__farLeftScoreRect = None
        self.__farRightScoreRect = None

        self.__winScreen = False
        self.__winImage = pygame.image.load('Images/Win.png')
        self.__winRect = self.__winImage.get_rect()

        self.__font = pygame.font.SysFont('Comic Sans MS', 14)
        self.__text = self.__font.render('Level: 1', False, self.settings.get_paddle_color())

        self.__playImage = None
        self.__playRect = None

        self.reset_score()
        self.show_scores()

    def reset_score(self):
        self.__leftScore = 0
        self.__rightScore = 0
        self.__text = self.__font.render('Level: {}'.format(self.settings.get_current_level()),
                                         False, self.settings.get_paddle_color())

        self.__leftScoreImage = pygame.image.load('Images/Zero.png')
        self.__leftScoreRect = self.__leftScoreImage.get_rect()
        self.__rightScoreImage = pygame.image.load('Images/Zero.png')
        self.__rightScoreRect = self.__rightScoreImage.get_rect()

        self.__farLeftScoreImage = None
        self.__farRightScoreImage = None

        self.__winScreen = False

        self.__leftScoreRect.top = 20
        self.__leftScoreRect.centerx = (self.settings.get_screen_width() / 2) - 125
        self.__rightScoreRect.top = 20
        self.__rightScoreRect.centerx = (self.settings.get_screen_width() / 2) + 125

    def show_scores(self):
        self.screen.blit(self.__leftScoreImage, self.__leftScoreRect)
        self.screen.blit(self.__rightScoreImage, self.__rightScoreRect)
        self.screen.blit(self.__text, (self.settings.get_screen_width() - 75, 0))

        if self.__farLeftScoreImage is not None:
            self.screen.blit(self.__farLeftScoreImage, self.__farLeftScoreRect)
        if self.__farRightScoreImage is not None:
            self.screen.blit(self.__farRightScoreImage, self.__farRightScoreRect)
        if self.__winScreen:
            self.screen.blit(self.__winImage, self.__winRect)

    def show_one(self, side):
        if side == "left":
            self.__leftScoreImage = pygame.image.load('Images/One.png')
        else:
            self.__rightScoreImage = pygame.image.load('Images/One.png')

    def show_two(self, side):
        if side == "left":
            self.__leftScoreImage = pygame.image.load('Images/Two.png')
        else:
            self.__rightScoreImage = pygame.image.load('Images/Two.png')

    def show_three(self, side):
        if side == "left":
            self.__leftScoreImage = pygame.image.load('Images/Three.png')
        else:
            self.__rightScoreImage = pygame.image.load('Images/Three.png')

    def show_four(self, side):
        if side == "left":
            self.__leftScoreImage = pygame.image.load('Images/Four.png')
        else:
            self.__rightScoreImage = pygame.image.load('Images/Four.png')

    def show_five(self, side):
        if side == "left":
            self.__leftScoreImage = pygame.image.load('Images/Five.png')
        else:
            self.__rightScoreImage = pygame.image.load('Images/Five.png')

    def show_six(self, side):
        if side == "left":
            self.__leftScoreImage = pygame.image.load('Images/Six.png')
        else:
            self.__rightScoreImage = pygame.image.load('Images/Six.png')

    def show_seven(self, side):
        if side == "left":
            self.__leftScoreImage = pygame.image.load('Images/Seven.png')
        else:
            self.__rightScoreImage = pygame.image.load('Images/Seven.png')

    def show_eight(self, side):
        if side == "left":
            self.__leftScoreImage = pygame.image.load('Images/Eight.png')
        else:
            self.__rightScoreImage = pygame.image.load('Images/Eight.png')

    def show_nine(self, side):
        if side == "left":
            self.__leftScoreImage = pygame.image.load('Images/Nine.png')
        else:
            self.__rightScoreImage = pygame.image.load('Images/Nine.png')

    def show_ten(self, side):
        if side == "left":
            self.__farLeftScoreImage = pygame.image.load('Images/One.png')
            self.__leftScoreImage = pygame.image.load('Images/Zero.png')
            self.__farLeftScoreRect = self.__farLeftScoreImage.get_rect()
            self.__farLeftScoreRect.top = 20
            self.__farLeftScoreRect.centerx = (self.settings.get_screen_width() / 2) - 245
            self.show_win("left")
            self.show_scores()
            pygame.display.flip()

            time.sleep(1)
            self.show_play_again()
            gF.ai_win(self.ball, self.paddles, self.settings, self.title_screen)
            self.reset_score()

        else:
            self.__farRightScoreImage = pygame.image.load('Images/Zero.png')
            self.__rightScoreImage = pygame.image.load('Images/One.png')
            self.__farRightScoreRect = self.__farRightScoreImage.get_rect()
            self.__farRightScoreRect.top = 20
            self.__farRightScoreRect.centerx = (self.settings.get_screen_width() / 2) + 245
            self.show_win("right")
            self.show_scores()
            pygame.display.flip()

            time.sleep(1)
            gF.user_win(self.ball, self.paddles, self.settings)
            self.update_text()
            self.reset_score()
            time.sleep(1)

    def update_text(self):
        self.__text = self.__font.render('Level: {}'.format(self.settings.get_current_level()),
                                         False, self.settings.get_paddle_color())

    def show_win(self, side):
        if side == "left":
            self.__winRect.centerx = (1/4) * self.settings.get_screen_width()
        else:
            self.__winRect.centerx = (3/4) * self.settings.get_screen_width()
        self.__winRect.centery = (1/2) * self.settings.get_screen_height()
        self.__winScreen = True

    def show_play_again(self):
        self.__playImage = pygame.image.load('Images/Play Again.png')
        self.__playRect = self.__playImage.get_rect()
        self.__playRect.centerx = self.__winRect.centerx
        self.__playRect.top = self.__winRect.bottom
        self.screen.blit(self.__playImage, self.__playRect)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return

    def update_left(self):
        self.__leftScore += 1
        if self.__leftScore == 1:
            self.show_one("left")
        elif self.__leftScore == 2:
            self.show_two("left")
        elif self.__leftScore == 3:
            self.show_three("left")
        elif self.__leftScore == 4:
            self.show_four("left")
        elif self.__leftScore == 5:
            self.show_five("left")
        elif self.__leftScore == 6:
            self.show_six("left")
        elif self.__leftScore == 7:
            self.show_seven("left")
        elif self.__leftScore == 8:
            self.show_eight("left")
        elif self.__leftScore == 9:
            self.show_nine("left")
        elif self.__leftScore == 10:
            self.show_ten("left")

    def update_right(self):
        self.__rightScore += 1
        if self.__rightScore == 1:
            self.show_one("right")
        elif self.__rightScore == 2:
            self.show_two("right")
        elif self.__rightScore == 3:
            self.show_three("right")
        elif self.__rightScore == 4:
            self.show_four("right")
        elif self.__rightScore == 5:
            self.show_five("right")
        elif self.__rightScore == 6:
            self.show_six("right")
        elif self.__rightScore == 7:
            self.show_seven("right")
        elif self.__rightScore == 8:
            self.show_eight("right")
        elif self.__rightScore == 9:
            self.show_nine("right")
        elif self.__rightScore == 10:
            self.show_ten("right")
