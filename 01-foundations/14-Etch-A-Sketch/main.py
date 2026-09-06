from turtle import Turtle, Screen

pencil = Turtle()
screen = Screen()

def move_forward():
    pencil.forward(20)

def move_backward():
    pencil.backward(20)

def turn_right():
    pencil.right(15)

def turn_left():
    pencil.left(15)

def clear():
    screen.resetscreen()

screen.listen()

# Movements:
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear, "c")

screen.exitonclick()