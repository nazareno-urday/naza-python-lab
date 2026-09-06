<div align="center">

🐍 Snake Game

Eat, grow, and survive without hitting the walls or your own tail.






</div>

🎮 The game

A classic Snake game built entirely with Python's standard-library turtle module.

Guide the snake around the board, collect the blue food, and grow one segment at a time. The run ends when the snake collides with a wall or with its own body.

🕹️ Controls

Key

Action

↑

Move up

↓

Move down

←

Move left

→

Move right

The snake cannot instantly reverse into the opposite direction.

✨ Features

Continuous movement with keyboard-controlled direction changes

Random food placement inside the playable area

Snake growth after every collected food item

Live score tracking

Wall and self-collision detection

Game-over message when the run ends

Smooth screen updates using manual animation control

Modular object-oriented design

🧩 Project structure

15-Snake-Game/
├── main.py        # Creates the game window and runs the game loop
├── snake.py       # Handles snake creation, movement, growth, and direction
├── food.py        # Creates and randomly relocates the food
├── scoreboard.py  # Displays the score and game-over message
└── README.md

⚙️ How it works

The application is split into four focused modules:

main.py coordinates the screen, keyboard events, timing, and collision checks.

snake.py manages the snake's segments and prevents illegal 180-degree turns.

food.py extends Turtle to represent food and move it to a new random position.

scoreboard.py extends Turtle to render the current score and final message.

Every frame, the body segments move from tail to head before the head advances. This creates the effect of the entire snake following the path of its first segment.

🚀 Run locally

Requirements

Python 3.x

A desktop environment with Tk support for turtle

No third-party packages are required.

Start the game

git clone <your-repository-url>
cd python-lab/01-foundations/15-Snake-Game
python main.py

If your system uses python3 instead of python, run:

python3 main.py

🧠 Practiced here

Object-oriented programming · Classes and inheritance · Event listeners · Game loops · Collision detection · List slicing · Module organization · Turtle graphics

🌱 Possible next steps

Save and display a persistent high score

Add a restart option

Increase the speed as the score grows

Align food to the movement grid

Add difficulty levels and visual themes

<div align="center">

Project 15 — Python Foundations

</div>