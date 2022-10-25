from turtle import Turtle#, Screen

WIDTH = 5
HEIGHT = 1

UP = 90
DOWN = 270
IN_POS = [(350, 0), (-350, 0)]


class Paddle(Turtle):

    def __init__(self, tuple):
        super().__init__()
        #for position in IN_POS:
        self.create_paddle()
        self.goto(tuple)
        #IN_POS.remove(position)

    def create_paddle(self):
        self.color
        self.shape("square")
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT, outline=None)
        self.color("white")
        self.penup()
        #self.seth(UP)

    # def move(self):
    #     self.speed(3)
    #     self.fd(20)

    def up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)

    # def starting_positions(self, paddle):
    #     if paddle == "r_paddle":
    #         self.paddle.goto(IN_POS[0])
    #     elif paddle == "l_paddle":
    #         self.paddle.goto(IN_POS[1])




