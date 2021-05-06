import turtle
import game
import time

game = game.Game()

STAMP_SIZE = 20

screen = turtle.Screen()
screen.title("pong by chuss")
screen.cv._rootwindow.resizable(False,False)
screen.bgcolor(0,0,0)
screen.setup(game.width,game.height)
screen.tracer(0)
ball = turtle.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.speed(1)


wall_a = turtle.Turtle()
wall_a.shape("square")
wall_a.color("red")
wall_a.penup()
wall_a.shapesize(game.wall_height/STAMP_SIZE, game.wall_width/STAMP_SIZE)

wall_b = turtle.Turtle()
wall_b.shape("square")
wall_b.color("red")
wall_b.penup()
wall_b.shapesize(game.wall_height/STAMP_SIZE, game.wall_width/STAMP_SIZE)

text = turtle.Turtle()
text.color("red")
text.penup()
text.goto(-game.width + 340, game.height - 290)
text.write(f"PLAYER A {game.points_a}  : {game.points_b} PLAYER B", align="left", font=("italics", 15, "normal"))
text.hideturtle()

def player_a_up():
    game.wall_a_up()

def player_a_down():
    game.wall_a_down()

def player_b_down():
    game.wall_b_down()

def player_b_up():
    game.wall_b_up()


screen.listen()
screen.onkeypress(player_a_up,"w")
screen.onkeypress(player_a_down,"s")
screen.onkeypress(player_b_down, "Down")
screen.onkeypress(player_b_up, "Up")

prev_points_a = None
prev_points_b = None


while True:
    game.tick()
    ball.goto(game.ball_position())
    wall_a.goto(game.wall_a_position)
    wall_b.goto(game.wall_b_position)
    if not prev_points_b == game.points_b or not prev_points_a == game.points_a:
        text.clear()
        text.write(f"PLAYER A {game.points_a} : {game.points_b} PLAYER B", align="left", font=("italics", 15, "normal"))
        prev_points_a = game.points_a
        prev_points_b = game.points_b
    screen.update()
    time.sleep(0.005)
