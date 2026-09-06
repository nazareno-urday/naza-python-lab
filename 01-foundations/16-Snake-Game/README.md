<h1 align="center">🐍 Snake Game</h1>

<p align="center">
  <strong>Eat. Grow. Survive.</strong><br>
  A classic Snake game built with Python and Turtle.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GUI-Turtle-2E8B57?style=for-the-badge" alt="Turtle">
  <img src="https://img.shields.io/badge/Style-OOP-8A2BE2?style=for-the-badge" alt="OOP">
</p>

---

## 🎮 About the game

A classic Snake game developed entirely with Python's standard-library `turtle` module.

Control the snake, collect the blue food, and grow one segment at a time. The game ends when the snake collides with a wall or its own body.

## 🕹️ Controls

| Key | Movement |
|:---:|:---|
| <kbd>↑</kbd> | Up |
| <kbd>↓</kbd> | Down |
| <kbd>←</kbd> | Left |
| <kbd>→</kbd> | Right |

Opposite-direction turns are blocked to prevent the snake from reversing into itself.

## ✨ Features

- Smooth continuous movement
- Keyboard direction controls
- Random food placement
- Snake growth after collecting food
- Live score tracking
- Wall collision detection
- Self-collision detection
- Game-over screen
- Modular object-oriented design

## 🧩 Project structure

```text
16-Snake-Game/
├── main.py        # Game loop, controls, and collision detection
├── snake.py       # Snake movement, direction, and growth
├── food.py        # Food creation and random positioning
├── scoreboard.py  # Score display and game-over message
└── README.md       # Project documentation
