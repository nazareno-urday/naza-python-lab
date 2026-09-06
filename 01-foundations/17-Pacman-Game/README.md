<h1 align="center">🟡 Pac-Man Game</h1>

<p align="center">
  <strong>Clear the maze, use power pellets, and escape four unique ghosts.</strong><br>
  A complete object-oriented maze game built with Python and Pygame.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Library-Pygame-2E8B57?style=for-the-badge&logo=pygame&logoColor=white" alt="Pygame">
  <img src="https://img.shields.io/badge/Paradigm-OOP-8A2BE2?style=for-the-badge" alt="OOP">
</p>

---

## 🎮 About

This project recreates the core mechanics of the classic maze-chase game without external image or audio assets. Every character and maze element is rendered directly with Pygame.

Collect every pellet to win, activate power pellets to make ghosts vulnerable, and protect your three lives. Each ghost uses a different targeting personality inspired by the original arcade behavior.

## ✨ Features

- Smooth grid-based movement
- Pellets and animated power pellets
- Central ghost house with a player-blocking door
- Staggered ghost releases at different moments
- Four ghosts with different targeting strategies
- Eaten ghosts return to the house as eyes, regenerate, and leave again
- Chase, scatter, and frightened modes
- Increasing ghost combo rewards
- Score, session high score, and lives
- Side tunnel teleportation
- Pause, victory, game-over, and restart states
- Asset-free rendering
- Modular object-oriented architecture

## 🕹️ Controls

| Key | Action |
|:---:|---|
| <kbd>↑</kbd> / <kbd>W</kbd> | Move up |
| <kbd>↓</kbd> / <kbd>S</kbd> | Move down |
| <kbd>←</kbd> / <kbd>A</kbd> | Move left |
| <kbd>→</kbd> / <kbd>D</kbd> | Move right |
| <kbd>Space</kbd> | Start a round |
| <kbd>P</kbd> | Pause or resume |
| <kbd>R</kbd> | Restart after winning or losing |
| <kbd>Esc</kbd> | Exit |

## 👻 Ghost personalities

| Ghost | Behavior |
|---|---|
| Blinky | Directly targets the player's current tile |
| Pinky | Targets four tiles ahead of the player's direction |
| Inky | Combines the player's direction with Blinky's position |
| Clyde | Chases from far away and retreats when he gets close |

Ghosts alternate between `SCATTER` and `CHASE`. A power pellet changes active ghosts to `FRIGHTENED`; when eaten, they enter `EATEN`, return through the ghost-house door, wait inside, and leave the box again.

## 🧩 Project structure

```text
17-Pacman-Game/
├── main.py          # Application entry point
├── game.py          # Main loop, states, score, lives, and collisions
├── maze.py          # Maze, walls, pellets, and navigation rules
├── player.py        # Player movement and rendering
├── ghost.py         # Ghost AI, modes, collisions, and rendering
├── settings.py      # Shared constants, colors, and directions
├── requirements.txt # Pygame dependency
└── README.md         # Project documentation
```

## 🚀 Run locally

```bash
pip install -r requirements.txt
python main.py
```

## 🧠 Concepts practiced

`Object-oriented programming` · `Composition` · `Game loops` · `State management` · `Pathfinding heuristics` · `Collision detection` · `Event handling` · `Modular architecture` · `Pygame rendering`

---

<p align="center">
  <strong>Project 17 · Python Foundations</strong>
</p>
