from random import randint


class Game:
    def __init__(self):
        self.width = 600
        self.height = 500
        self.__ball_pos = (randint(-50,50),randint(-50,50))
        self.__ball_delta_x = 1
        self.__ball_delta_y = 1

        self.wall_a_position = (-self.width / 2 + 20,0)
        self.wall_b_position = (self.width / 2 - 25,0)
        self.wall_width = 20
        self.wall_height = self.height * 0.2

        self.points_a = 0
        self.points_b = 0

    def tick(self):
        self.__perform_wall_hit_checking()
        self.__perform_border_checking()
        x,y = self.__ball_pos
        self.__ball_pos = (x + self.__ball_delta_x, y + self.__ball_delta_y)

    def ball_position(self):
        return self.__ball_pos

    def __perform_wall_hit_checking(self):
        x,y = self.__ball_pos

        a_x, a_y = self.wall_a_position
        hit_wall_a = (a_x + 20) == x and ((a_y - self.wall_height /2 ) <= y <= (a_y + self.wall_height /2))

        b_x, b_y = self.wall_b_position
        hit_wall_b = (b_x - 20) == x and ((b_y - self.wall_height/2) <= y <= (b_y + self.wall_height /2))

        if hit_wall_a or hit_wall_b:
            self.__ball_delta_x *= -1


    def __perform_border_checking(self):
        x, y = self.__ball_pos
        if abs(y) >= self.height / 2:
            self.__ball_delta_y *= -1

        if x <= -(self.width/2):
            self.points_b += 1
            self.__ball_pos = (0, 0)

        if x >= self.width/2:
            self.points_a +=1
            self.__ball_pos = (0,0)

    def wall_a_up(self):
        x,y = self.wall_a_position
        self.wall_a_position = (x, y + 20)

    def wall_a_down(self):
        x,y = self.wall_a_position
        self.wall_a_position = (x, y - 20)

    def wall_b_down(self):
        x,y = self.wall_b_position
        self.wall_b_position = (x, y - 20)

    def wall_b_up(self):
        x,y = self.wall_b_position
        self.wall_b_position = (x,y+20)





