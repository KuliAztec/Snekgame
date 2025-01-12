# Snake Game

This is a simple Snake Game implemented using Python and Pygame.

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/KuliAztec/snake_game.git
    cd snake_game
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## How to Play

1. Run the game:
    ```sh
    python snake_game.py
    ```

2. Use the arrow keys to control the snake:
    - Up: Move up
    - Down: Move down
    - Left: Move left
    - Right: Move right

3. The objective is to eat the food (red block) to grow the snake and increase your score. Avoid hitting the walls or the snake's own body.

4. Special food (yellow block) appears occasionally and disappears after 3 seconds. Eating it will give you extra points based on the time left.

5. Rocks (white blocks) are scattered on the screen. Hitting a rock will end the game.

## Features

- Classic snake gameplay
- Special food with time-based scoring
- Randomly placed rocks that cause game over on collision
- High score tracking
