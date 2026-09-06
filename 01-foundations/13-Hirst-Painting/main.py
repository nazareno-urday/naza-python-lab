from turtle import Turtle, Screen
import random

# Colors extracted from a Hirst painting using colorgram.py
all_colors = [(60, 96, 130), (219, 208, 118), (19, 34, 52), (50, 26, 18), (123, 73, 91),
              (132, 176, 154), (55, 25, 34), (176, 160, 40), (55, 121, 76), (198, 95, 76),
              (131, 27, 40), (147, 25, 17), (20, 46, 36), (182, 96, 113), (224, 170, 188),
              (42, 60, 98), (64, 163, 98), (223, 178, 170), (109, 119, 163), (24, 92, 57),
              (156, 210, 186), (12, 88, 103)]

# Pre-settings
pencil = Turtle()
screen = Screen()
screen.colormode(255)
pencil.hideturtle()
pencil.speed('fastest')


x = -330 # Starting position of the pencil
y = -270
pencil.teleport(x,y)

for i in range(10):
    for j in range(10):
        pencil.dot(35, random.choice(all_colors))
        pencil.penup()
        pencil.forward(70) # Exactly 10 dots per row
        pencil.pendown()

    y += 60
    pencil.teleport(x,y)

screen.exitonclick()