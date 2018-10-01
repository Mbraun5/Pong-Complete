import pygame
import time


class Title:
    def __init__(self, screen, settings):
        self.__screen = screen
        self.__settings = settings
        self.__screenRect = self.__screen.get_rect()
        self.__mouseX, self.__mouseY = pygame.mouse.get_pos()

        #   Center image to middle of screen and place it at the top.
        self.__titleImage = pygame.image.load('Images/title1.png')
        self.__titleRect = self.__titleImage.get_rect()
        self.__titleRect.centerx = self.__screenRect.centerx
        self.__titleRect.top = self.__screenRect.top - 35

        self.__difficultyImage = pygame.image.load('Images/Difficulty.png')
        self.__difficultyRect = self.__difficultyImage.get_rect()
        self.__difficultyRect.top = self.__titleRect.bottom
        self.__difficultyRect.left = settings.get_screen_width() / 5

        #   Start game with Easy mode selected.
        self.__easyImage = pygame.image.load('Images/EasyR.png')
        self.__easyRect = self.__easyImage.get_rect()
        self.__easyRect.top = self.__titleRect.bottom
        self.__easyRect.left = self.__difficultyRect.right

        self.__mediumImage = pygame.image.load('Images/MediumW.png')
        self.__mediumRect = self.__mediumImage.get_rect()
        self.__mediumRect.top = self.__titleRect.bottom
        self.__mediumRect.left = self.__easyRect.right

        self.__hardImage = pygame.image.load('Images/HardW.png')
        self.__hardRect = self.__hardImage.get_rect()
        self.__hardRect.top = self.__titleRect.bottom
        self.__hardRect.left = self.__mediumRect.right

        self.__titleImageCont = pygame.image.load('Images/Select Difficulty.png')
        self.__continueRect = self.__titleImageCont.get_rect()
        self.__continueRect.centerx = self.__screenRect.centerx
        self.__continueRect.bottom = self.__screenRect.bottom - 20

        self.__rulesImage = pygame.image.load('Images/Rules.png')
        self.__rulesRect = self.__rulesImage.get_rect()
        self.__rulesRect.centerx = self.__screenRect.centerx
        self.__rulesRect.top = self.__screenRect.top

        self.__rulesCont = pygame.image.load('Images/title continue.png')
        self.__rulesContRect = self.__rulesCont.get_rect()
        self.__rulesContRect.centerx = self.__screenRect.centerx
        self.__rulesContRect.bottom = self.__screenRect.bottom - 20

        self.display_title_screen()

    def display_title_screen(self):
        self.reset_screen()
        self.__screen.blit(self.__titleImage, self.__titleRect)
        self.__screen.blit(self.__difficultyImage, self.__difficultyRect)
        self.__screen.blit(self.__easyImage, self.__easyRect)
        self.__screen.blit(self.__mediumImage, self.__mediumRect)
        self.__screen.blit(self.__hardImage, self.__hardRect)
        self.__screen.blit(self.__titleImageCont, self.__continueRect)
        pygame.display.flip()

        while self.check_events(False):
            pass
        self.display_rule_screen()

    def display_rule_screen(self):
        self.reset_screen()
        self.__screen.blit(self.__rulesImage, self.__rulesRect)
        self.__screen.blit(self.__rulesCont, self.__rulesContRect)
        pygame.display.flip()

        while self.check_events(True):
            self.reset_screen()
            self.__screen.blit(self.__rulesImage, self.__rulesRect)
            pygame.display.flip()
            time.sleep(0.5)
            self.__screen.blit(self.__rulesCont, self.__rulesContRect)
            pygame.display.flip()
            time.sleep(0.5)

    def check_events(self, rule_bool):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if rule_bool:
                    return False
                elif event.key == pygame.K_RETURN:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__mouseX, self.__mouseY = pygame.mouse.get_pos()
                self.update_difficulty()
        return True

    def update_difficulty(self):
        easy_collide = self.__easyRect.collidepoint(self.__mouseX, self.__mouseY)
        medium_collide = self.__mediumRect.collidepoint(self.__mouseX, self.__mouseY)
        hard_collide = self.__hardRect.collidepoint(self.__mouseX, self.__mouseY)
        if easy_collide:
            self.__easyImage = pygame.image.load('Images/EasyR.png')
            self.__mediumImage = pygame.image.load('Images/MediumW.png')
            self.__hardImage = pygame.image.load('Images/HardW.png')
            self.__settings.set_medium_mode(False)
            self.__settings.set_hard_mode(False)
            self.__settings.set_easy_mode(True)
        if medium_collide:
            self.__easyImage = pygame.image.load('Images/EasyW.png')
            self.__mediumImage = pygame.image.load('Images/MediumR.png')
            self.__hardImage = pygame.image.load('Images/HardW.png')
            self.__settings.set_easy_mode(False)
            self.__settings.set_hard_mode(False)
            self.__settings.set_medium_mode(True)
        if hard_collide:
            self.__easyImage = pygame.image.load('Images/EasyW.png')
            self.__mediumImage = pygame.image.load('Images/MediumW.png')
            self.__hardImage = pygame.image.load('Images/HardR.png')
            self.__settings.set_easy_mode(False)
            self.__settings.set_medium_mode(False)
            self.__settings.set_hard_mode(True)

        self.__screen.blit(self.__easyImage, self.__easyRect)
        self.__screen.blit(self.__mediumImage, self.__mediumRect)
        self.__screen.blit(self.__hardImage, self.__hardRect)
        pygame.display.flip()

    def reset_screen(self):
        self.__screen.fill(self.__settings.get_bg_color())
