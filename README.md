.
# Colliding Boxes Computing Pi

A Python program that visualizes the "colliding boxes computing pi" problem, famously demonstrated by 3Blue1Brown. This simulation shows how the number of elastic collisions between two boxes and a wall can be used to compute the digits of pi.

## About the Project 📐

This program simulates two boxes on a one-dimensional, frictionless surface. The small box is stationary at the beginning, while a massive box moves towards it. The boxes collide with each other and with a wall, and the program counts each collision. The number of collisions that occur is a direct approximation of pi, with the number of digits determined by the mass ratio of the boxes.

## How to Run the Program 🚀

### Prerequisites

  - Python 3.x
  - `pygame`
  - `numpy`

You can install the required libraries using pip:

```bash
pip install pygame numpy
```

### Execution

To start the simulation, run the Python script from your terminal:

```bash
python main.py
```

## Controls 🎮

  - **`SPACE`**: Press the spacebar to **pause** and **unpause** the simulation.

## Known Issues ⚠️

The simulation may not work correctly when the mass of the large box is set to an extremely high value. This is due to the discrete nature of the simulation's timestep, which can cause the boxes to "tunnel" through each other without a collision being detected.

## Inspiration ✨

This project was inspired by the fantastic video explanation by **3Blue1Brown** on the same topic.

Link -> https://youtu.be/HEfHFsfGXjs?si=tbKX71MOFnz6SrWp