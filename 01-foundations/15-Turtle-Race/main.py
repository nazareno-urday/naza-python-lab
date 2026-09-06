from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color:"
)

colors = ["red", "green", "blue", "yellow", "orange", "purple"]
turtles = []

x = -200
y = 90

for color in colors:
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(color)
    racer.goto(x, y)
    turtles.append(racer)
    y -= 30

if user_bet:
    user_bet = user_bet.strip().lower()
    is_race_on = True

while is_race_on:
    for racer in turtles:
        random_distance = random.randint(0, 10)
        racer.forward(random_distance)

        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()

            if winning_color == user_bet:
                print(
                    f"Congratulations! The {winning_color} "
                    f"turtle is the winner!"
                )
            else:
                print(
                    f"You lost the race! The {winning_color} "
                    f"turtle is the winner!"
                )

            break

screen.exitonclick()