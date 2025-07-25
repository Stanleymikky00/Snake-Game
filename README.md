## Snake Game (Python)

A classic Snake game built with the `turtle` graphics module in Python.

## How to Run

Make sure Python 3.x is installed, then run:

## Project Structure
main.py         # Game launcher
snake.py        # Snake class and logic
food.py         # Food spawning logic
scoreboard.py   # Score tracking

## Requirement 

Python 3.x
turtle (comes with Python standard libraey)

## Future AI Integration

I plan to implement an AI agent that plays the Snake game autonomously using:
- **Reinforcement Learning (Q-Learning or Deep Q-Learning)**
- State-action modeling of snake movement
- Reward system based on food, collisions, and survival time

This will be available in a separate file or branch (`ai_snake.py`).
-------------------------------------------------------------------------------------------------------------------
## New Feature: AI Agent Integrated

This Snake Game now includes an **AI agent** trained using a simple neural network and basic reinforcement principles.

### How the AI Works:
- The game collects data while a User plays.
- A TensorFlow model is trained to predict the best move.
- You can switch between User or AI control with the flag:

```python
USE_AI = True  # AI plays the game
USE_AI = False  # User plays the game


## Train AI Model:
python train_model.py
The trained model is saved as:
snake_model.keras.

##Play with AI Agent:
Simply run the game with AI enabled in main.py
python main.py
The agent will now make moves based on the trained neural network.


