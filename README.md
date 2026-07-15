# Pong Game

A simple implementation of the classic Pong game using Python and Pygame.

## Features

- Two-player gameplay
- Smooth paddle movement and ball physics
- Score tracking
- Ball spin mechanics based on paddle hit location
- Collision detection

## Requirements

- Python 3.7+
- Pygame 2.0.0+

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rishichitnis007/pong-game.git
   cd pong-game
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. Run the game:
   ```bash
   python pong.py
   ```

2. Controls:
   - **Left Paddle**: Use `W` (up) and `S` (down) keys
   - **Right Paddle**: Use `UP` and `DOWN` arrow keys

3. **Objective**: Keep the ball in play and score points by getting the ball past your opponent's paddle.

## Game Mechanics

- The ball bounces off the top and bottom walls
- The ball bounces off the paddles with added spin based on where it hits
- Each time the ball gets past a paddle, the other player scores a point
- The ball resets to the center after each score
- The game runs at 60 FPS for smooth gameplay

## License

MIT License - See LICENSE file for details
