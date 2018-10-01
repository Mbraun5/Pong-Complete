class Settings:
    def __init__(self):
        #   Screen Settings
        self.__screenWidth = 1800
        self.__screenHeight = 1000
        self.__bgColor = (0, 0, 0)

        #   Game Settings
        self.__gameTitle = "Pong Game"

        #   Ball Settings
        self.__ballColor = (255, 255, 255)
        self.__ballWidth = 25

        self.__maxXSpeedBall = 4
        self.__minXSpeedBall = 2
        self.__maxYSpeedBall = 4
        self.__minYSpeedBall = 2

        #   Ball Difficulty Settings
        self.__ballReductionRate = 0.95
        self.__ballSpeedRate = 1.05

        #   Paddle Settings
        self.__paddleColor = (255, 255, 255)
        self.__paddleHeight = 25
        self.__paddleWidth = 140
        self.__paddleOffset = 25

        self.__userPaddleSpeed = 3
        self.__maxAIPaddleSpeed = 3
        self.__minAIPaddleSpeed = 2

        #   Paddle Difficulty Settings
        self.__paddleReductionRate = 0.95

        #   Movement Flags
        self.__userMovingUp = False
        self.__userMovingDown = False
        self.__userMovingLeft = False
        self.__userMovingRight = False

        #   Difficulty Settings
        self.__easyMode = True
        self.__mediumMode = False
        self.__hardMode = False
        self.__currentLevel = 1

    #   #############################################
    #           Background FUNCTIONS                #
    #   #############################################
    def get_bg_color(self):
        return self.__bgColor

    def get_game_title(self):
        return self.__gameTitle

    def get_screen_width(self):
        return self.__screenWidth

    def get_screen_height(self):
        return self.__screenHeight

    #   #############################################
    #           BALL FUNCTIONS                      #
    #   #############################################
    def get_max_ball_x_speed(self):
        return self.__maxXSpeedBall

    def get_max_ball_y_speed(self):
        return self.__maxYSpeedBall

    def set_max_ball_x_speed(self, value):
        self.__maxXSpeedBall += value

    def set_max_ball_y_speed(self, value):
        self.__maxYSpeedBall += value

    def get_min_ball_x_speed(self):
        return self.__minXSpeedBall

    def get_min_ball_y_speed(self):
        return self.__minYSpeedBall

    def set_min_ball_x_speed(self, value):
        self.__minXSpeedBall += value

    def set_min_ball_y_speed(self, value):
        self.__minYSpeedBall += value

    def get_ball_color(self):
        return self.__ballColor

    def get_ball_width(self):
        return self.__ballWidth

    #   #############################################
    #           PADDLE FUNCTIONS                    #
    #   #############################################
    def get_paddle_color(self):
        return self.__paddleColor

    def get_paddle_height(self):
        return self.__paddleHeight

    def get_paddle_width(self):
        return self.__paddleWidth

    def get_paddle_offset(self):
        return self.__paddleOffset

    def get_user_paddle_speed(self):
        return self.__userPaddleSpeed

    def get_max_ai_paddle_speed(self):
        return self.__maxAIPaddleSpeed

    def get_min_ai_paddle_speed(self):
        return self.__minAIPaddleSpeed

    #   #############################################
    #           Movement FUNCTIONS                  #
    #   #############################################
    def get_user_moving_up(self):
        return self.__userMovingUp

    def set_user_moving_up(self, bool_var):
        self.__userMovingUp = bool_var

    def get_user_moving_down(self):
        return self.__userMovingDown

    def set_user_moving_down(self, bool_var):
        self.__userMovingDown = bool_var

    def get_user_moving_left(self):
        return self.__userMovingLeft

    def set_user_moving_left(self, bool_var):
        self.__userMovingLeft = bool_var

    def get_user_moving_right(self):
        return self.__userMovingRight

    def set_user_moving_right(self, bool_var):
        self.__userMovingRight = bool_var

    #   #############################################
    #           Difficulty FUNCTIONS                #
    #   #############################################
    def set_easy_mode(self, bool_var):
        self.__easyMode = bool_var
        if bool_var:
            self.set_easy_settings()

    def set_medium_mode(self, bool_var):
        self.__mediumMode = bool_var
        if bool_var:
            self.set_medium_settings()

    def set_hard_mode(self, bool_var):
        self.__hardMode = bool_var
        if bool_var:
            self.set_hard_settings()

    def set_easy_settings(self):
        self.__maxXSpeedBall = 3
        self.__minXSpeedBall = 1
        self.__maxYSpeedBall = 3
        self.__minYSpeedBall = 1

        self.__userPaddleSpeed = 3
        self.__maxAIPaddleSpeed = 3
        self.__minAIPaddleSpeed = 1

        self.__ballReductionRate = 0.80
        self.__ballSpeedRate = 1.05
        self.__paddleReductionRate = 0.80

    def set_medium_settings(self):
        self.__maxXSpeedBall = 4
        self.__minXSpeedBall = 2
        self.__maxYSpeedBall = 4
        self.__minYSpeedBall = 2

        self.__userPaddleSpeed = 4
        self.__maxAIPaddleSpeed = 3
        self.__minAIPaddleSpeed = 2

        self.__ballReductionRate = 0.75
        self.__ballSpeedRate = 1.10
        self.__paddleReductionRate = 0.75

    def set_hard_settings(self):
        self.__maxXSpeedBall = 5
        self.__minXSpeedBall = 3
        self.__maxYSpeedBall = 5
        self.__minYSpeedBall = 3

        self.__userPaddleSpeed = 5
        self.__maxAIPaddleSpeed = 4
        self.__minAIPaddleSpeed = 3

        self.__ballReductionRate = 0.70
        self.__ballSpeedRate = 1.15
        self.__paddleReductionRate = 0.70

    def get_current_level(self):
        return self.__currentLevel

    def set_current_level(self, value):
        self.__currentLevel = value

    def get_paddle_reduction_rate(self):
        return self.__paddleReductionRate

    def get_ball_reduction_rate(self):
        return self.__ballReductionRate

    def increase_difficulty_parameters(self):
        self.__maxXSpeedBall *= self.__ballSpeedRate
        self.__minXSpeedBall *= self.__ballSpeedRate
        self.__minYSpeedBall *= self.__ballSpeedRate
        self.__maxYSpeedBall *= self.__ballSpeedRate

    def default_settings(self):
        self.__ballWidth = 25
        self.__paddleHeight = 25
        self.__paddleWidth = 140
        self.__currentLevel = 1
