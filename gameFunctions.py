import pygame
import paddle as p
import sys


#   Displays dotted lines through center of screen. Visually represents AI side and User side.
def display_center(screen, settings):
    y = 0
    while y <= settings.get_screen_height():
        color = settings.get_ball_color()
        rect = pygame.Rect((settings.get_screen_width() / 2), y, 4, 12)
        pygame.draw.rect(screen, color, rect)
        y += 25


def update_paddles(ball, paddles):
    ball_rect = ball.get_rect()
    for paddle in paddles:
        if paddle.check_collision(ball_rect):
            paddle.hit_ball(ball_rect)
            ball.update_pos()
        paddle.update_pos()
        paddle.draw_paddle()


def update_ball(ball, scoreboard, settings):
    ball.update_pos()
    ball.check_out_of_bounds(scoreboard, settings)
    ball.draw_ball()


def update_screen(ball, paddles, scoreboard, screen, settings):
    screen.fill(settings.get_bg_color())
    display_center(screen, settings)
    scoreboard.show_scores()
    update_paddles(ball, paddles)
    update_ball(ball, scoreboard, settings)


#   Checks for key down events and sifts through them.
def check_keydown_events(event, settings):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_UP:
        settings.set_user_moving_up(True)
    elif event.key == pygame.K_DOWN:
        settings.set_user_moving_down(True)
    elif event.key == pygame.K_LEFT:
        settings.set_user_moving_left(True)
    elif event.key == pygame.K_RIGHT:
        settings.set_user_moving_right(True)


def check_keyup_events(event, settings):
    if event.key == pygame.K_UP:
        settings.set_user_moving_up(False)
    elif event.key == pygame.K_DOWN:
        settings.set_user_moving_down(False)
    elif event.key == pygame.K_LEFT:
        settings.set_user_moving_left(False)
    elif event.key == pygame.K_RIGHT:
        settings.set_user_moving_right(False)


#   Responds to key presses and mouse events
def check_events(settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, settings)


#   Creates and returns a list of all six paddles (3 AI Paddle Objects and 3 User Paddle Objects)
def create_paddles_list(ball, screen, settings):
    #   User Paddles
    paddle_one = p.HUPaddle(ball, screen, settings)
    paddle_one.set_pos(settings.get_screen_width() * 3/4, settings.get_paddle_offset())
    paddle_two = p.HUPaddle(ball, screen, settings)
    paddle_two.set_pos(settings.get_screen_width() * 3/4, settings.get_screen_height() - settings.get_paddle_offset())
    paddle_three = p.VUPaddle(ball, screen, settings)

    #   AI Paddles
    paddle_four = p.HAIPaddle(ball, screen, settings)
    paddle_four.set_pos(settings.get_screen_width() * 1/4, settings.get_paddle_offset())
    paddle_five = p.HAIPaddle(ball, screen, settings)
    paddle_five.set_pos(settings.get_screen_width() * 1/4, settings.get_screen_height() - settings.get_paddle_offset())
    paddle_six = p.VAIPaddle(ball, screen, settings)

    #   Create and return the list of paddle objects
    paddle_list = [paddle_one, paddle_two, paddle_three, paddle_four, paddle_five, paddle_six]
    return paddle_list


def user_win(ball, paddles, settings):
    level = settings.get_current_level() + 1
    settings.set_current_level(level)
    for paddle in paddles:
        paddle.update_dimensions()
    ball.update_rect(settings.get_ball_width() * settings.get_ball_reduction_rate(),
                     settings.get_ball_width() * settings.get_ball_reduction_rate())
    settings.increase_difficulty_parameters()


def ai_win(ball, paddles, settings, title_screen):
    settings.default_settings()
    for paddle in paddles:
        paddle.set_dimensions()
    ball.update_rect(settings.get_ball_width(), settings.get_ball_width())
    title_screen.display_title_screen()
