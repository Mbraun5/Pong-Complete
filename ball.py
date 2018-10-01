import pygame
import random
import math
import time
import vector as v


class Ball:
    def __init__(self, screen, settings):
        self.__screen = screen
        self.__settings = settings

        self.velocityVector = v.Vector()
        self.__color = self.__settings.get_ball_color()
        self.__rect = pygame.Rect(0, 0, self.__settings.get_ball_width(), self.__settings.get_ball_width())

        self.reset_ball()

    def draw_ball(self):
        pygame.draw.rect(self.__screen, self.__color, self.__rect)

    def update_pos(self):
        self.__rect.x += self.velocityVector.getx()
        self.__rect.y += self.velocityVector.gety()

    def reset_ball(self):
        #   Velocity of ball will be halfway between min and max speed
        self.velocityVector = v.Vector((self.__settings.get_max_ball_x_speed() +
                                        self.__settings.get_min_ball_x_speed()) / 2,
                                       (self.__settings.get_max_ball_y_speed() +
                                        self.__settings.get_min_ball_y_speed()) / 2)

        #   Randomizes the x and y direction so ball is not going same way every time.
        direction = random.randint(1, 10)
        if direction % 2 == 0:
            self.velocityVector.opposite_x()
        direction = random.randint(1, 10)
        if direction % 2 == 0:
            self.velocityVector.opposite_y()

        #   Centers ball on screen.
        self.__rect.centerx = self.__settings.get_screen_width() / 2
        self.__rect.centery = self.__settings.get_screen_height() / 2

    def get_x_pos(self):
        return self.__rect.centerx

    def get_y_pos(self):
        return self.__rect.centery

    def get_rect(self):
        return self.__rect

    def check_out_of_bounds(self, scoreboard, settings):
        if (self.__rect.left <= 5 or self.__rect.bottom >= self.__settings.get_screen_height() or
                self.__rect.top <= 5 or self.__rect.right >= self.__settings.get_screen_width()):
            time.sleep(0.5)
            if self.__rect.left < settings.get_screen_width() / 2:
                scoreboard.update_right()
            else:
                scoreboard.update_left()
            self.reset_ball()

    def update_rect(self, length, width):
        self.__rect = pygame.Rect(0, 0, length, width)

