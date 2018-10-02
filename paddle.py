import pygame
import vector as v
import random
import math


#   ############################################
#           BASE CLASS PADDLE                  #
#   ############################################
class Paddle:
    def __init__(self, ball, screen, settings):
        self.ball = ball
        self.screen = screen
        self.settings = settings
        self.screenRect = self.screen.get_rect()
        self.speedVector = v.Vector(self.settings.get_user_paddle_speed(), self.settings.get_user_paddle_speed())

        self.__color = self.settings.get_paddle_color()
        self.rect = pygame.Rect(0, 0, 1, 1)
        self.ding_sound = pygame.mixer.Sound('Sounds/ding.wav')

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.__color, self.rect)

    def set_pos(self, xcoor, ycoor):
        self.rect.centerx = xcoor
        self.rect.centery = ycoor

    def check_collision(self, ball_rect):
        return self.rect.colliderect(ball_rect)

    def ball_speed_function(self, theta):
        amplitude = self.settings.get_max_ball_y_speed()
        omega = theta * (math.pi / self.settings.get_paddle_width())
        return amplitude * math.sin(omega)

    def hit_ball(self, ball_rect):
        pass

    def set_dimensions(self):
        pass

    def update_pos(self):
        pass

    def update_dimensions(self):
        self.rect.width *= self.settings.get_paddle_reduction_rate()
        self.rect.height *= self.settings.get_paddle_reduction_rate()


#   ######################################################
#               User Paddle Classes                      #
#   ######################################################
class UserPaddle(Paddle):
    def __init__(self, ball, screen, settings):
        Paddle.__init__(self, ball, screen, settings)


#   Horizontal Paddles Class
class HUPaddle(UserPaddle):
    def __init__(self, ball, screen, settings):
        UserPaddle.__init__(self, ball, screen, settings)
        self.set_dimensions()

    def set_dimensions(self):
        self.rect.width = self.settings.get_paddle_width()
        self.rect.height = self.settings.get_paddle_height()

    def update_pos(self):
        if self.settings.get_user_moving_right() and self.rect.right <= self.settings.get_screen_width():
            self.rect.x += self.speedVector.getx()
        elif self.settings.get_user_moving_left() and self.rect.left >= (self.settings.get_screen_width() / 2) + 5:
            self.rect.x -= self.speedVector.getx()

    def hit_ball(self, ball_rect):
        theta = ball_rect.centerx - self.rect.centerx
        self.ball.velocityVector.opposite_y()
        self.ball.velocityVector.setx(self.ball_speed_function(theta))
        pygame.mixer.Sound.play(self.ding_sound)


#   Vertical Paddles Class
class VUPaddle(UserPaddle):
    def __init__(self, ball, screen, settings):
        UserPaddle.__init__(self, ball, screen, settings)
        self.set_dimensions()
        self.set_pos(self.settings.get_screen_width() - self.settings.get_paddle_offset(),
                     self.settings.get_screen_height() / 2)

    def set_dimensions(self):
        self.rect.width = self.settings.get_paddle_height()
        self.rect.height = self.settings.get_paddle_width()

    #   y value grows down, so if user is moving up, subtract the y value speed vector.
    def update_pos(self):
        if self.settings.get_user_moving_up() and self.rect.top >= 2:
            self.rect.y -= self.speedVector.gety()
        elif self.settings.get_user_moving_down() and self.rect.bottom <= self.settings.get_screen_height() - 2:
            self.rect.y += self.speedVector.getx()

    def hit_ball(self, ball_rect):
        theta = ball_rect.centery - self.rect.centery
        self.ball.velocityVector.opposite_x()
        self.ball.velocityVector.sety(self.ball_speed_function(theta))
        pygame.mixer.Sound.play(self.ding_sound)


#   ######################################################
#               AI Paddle Classes                        #
#   ######################################################
class AIPaddle(Paddle):
    def __init__(self, ball, screen, settings):
        Paddle.__init__(self, ball, screen, settings)

    #   Horizontal and Vertical Paddles should move at the same speed for consistency. Thus, only one random
    #   integer needs to be created, and it can be given to both values.
    def change_speed(self):
        self.speedVector.setx(random.randint(self.settings.get_min_ai_paddle_speed(),
                                             self.settings.get_max_ai_paddle_speed()))
        self.speedVector.sety(self.speedVector.getx())


#   Horizontal AI Paddles
class HAIPaddle(AIPaddle):
    def __init__(self, ball, screen, settings):
        AIPaddle.__init__(self, ball, screen, settings)
        self.set_dimensions()

    def set_dimensions(self):
        self.rect.width = self.settings.get_paddle_width()
        self.rect.height = self.settings.get_paddle_height()

    def update_pos(self):
        if self.ball.get_x_pos() > self.rect.right and self.rect.right <= (self.settings.get_screen_width() / 2 - 5):
            self.rect.x += self.speedVector.getx()
        elif self.ball.get_x_pos() < self.rect.right and self.rect.left >= 3:
            self.rect.x -= self.speedVector.getx()

    def hit_ball(self, ball_rect):
        theta = ball_rect.centerx - self.rect.centerx
        self.ball.velocityVector.opposite_y()
        self.ball.velocityVector.setx(self.ball_speed_function(theta))
        self.change_speed()
        pygame.mixer.Sound.play(self.ding_sound)


#  ADD AI EPSILON LATER - abs(self.ball.get_x_pos() - self.rect.centerx) - epsilon > 0 ################

#   Vertical AI Paddles
class VAIPaddle(AIPaddle):
    def __init__(self, ball, screen, settings):
        AIPaddle.__init__(self, ball, screen, settings)
        self.set_dimensions()
        self.set_pos(self.settings.get_paddle_offset(),
                     self.settings.get_screen_height() / 2)

    def set_dimensions(self):
        self.rect.width = self.settings.get_paddle_height()
        self.rect.height = self.settings.get_paddle_width()

    def update_pos(self):
        if self.ball.get_y_pos() < self.rect.centery and self.rect.top > 1:
            self.rect.y -= self.speedVector.gety()
        elif self.ball.get_y_pos() > self.rect.centery and self.rect.bottom < self.settings.get_screen_height() - 3:
            self.rect.y += self.speedVector.gety()

    def hit_ball(self, ball_rect):
        theta = ball_rect.centery - self.rect.centery
        self.ball.velocityVector.opposite_x()
        self.ball.velocityVector.sety(self.ball_speed_function(theta))
        self.change_speed()
        pygame.mixer.Sound.play(self.ding_sound)
