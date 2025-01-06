# A* Maze Solver Project

## Overview

This project implements the A* algorithm to find the shortest path in a maze. The maze is represented by a grid where obstacles are denoted by `1` and open paths by `0`. The goal is to visualize how the A* algorithm works as it navigates through the maze from a start point to an end point, finding the most efficient route while avoiding obstacles.

This project demonstrates fundamental algorithmic thinking, problem-solving skills, and visualization techniques in Python, which are essential skills for data analysts.

### Video Demonstration

You can watch the video showing how the A* algorithm solves the maze here:

[Watch the Video](https://youtu.be/VWC7HKGGEQY?si=Xl3yh11YZoQ5jt6v)

## Project Details
## Research Paper
For a detailed explanation of the algorithm, methodology, and findings, refer to the research paper:
[CS6053 Artificial Intelligence.pdf](./CS6053%20Artificial%20Intelligence.pdf)


### Key Features

- **A* Algorithm**: Implements the A* search algorithm to find the shortest path between a start and end point in a maze grid.
- **Maze Visualization**: Uses `matplotlib` for real-time visualization of the maze-solving process, showing how the algorithm explores the maze and eventually finds the optimal path.
- **Interactive Mode**: The visualization updates in real-time to provide an engaging view of the algorithm's step-by-step solution.

### How It Works

1. **Maze Representation**: The maze is a 2D grid where:
   - `1` represents walls/obstacles.
   - `0` represents open paths.

2. **A* Search**: The A* algorithm finds the shortest path by:
   - Using the **Manhattan distance** as a heuristic to estimate the distance to the goal.
   - Considering all possible movements (up, down, left, right) while avoiding walls.
   - Expanding the search space in order of lowest cost, aiming for the optimal solution.

3. **Real-Time Visualization**: As the algorithm explores the maze, it highlights the cells being evaluated and shows the path it follows in real-time.

4. **Interactive Plot**: The project uses `matplotlib` to dynamically visualize the grid, with different colors representing various stages of the algorithm's process:
   - **Yellow** for the start.
   - **Green** for the end.
   - **Blue** for the path found.
   - **Black** for obstacles.

## Usage

### Requirements

To run this project, you need Python 3.x installed on your system, along with the following libraries:
- `matplotlib`
- `numpy`

You can install these libraries using `pip`:

```bash
pip install matplotlib numpy
