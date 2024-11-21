# A* Maze Solver

## Project Description

This project implements the **A* algorithm** to solve a maze and find the shortest path from a starting point to the goal. The maze is visualized step-by-step as the algorithm searches for the optimal path. The implementation uses **matplotlib** for real-time display and the **PriorityQueue** to implement the A* search.

### Video Demonstration

You can watch the algorithm in action here:

[Watch the A* algorithm solving the maze](https://youtu.be/VWC7HKGGEQY)

### How It Works
- **Maze Representation**: The maze is represented as a 2D list, where `0` indicates a free space and `1` represents a wall.
- **A* Algorithm**: The algorithm finds the shortest path by evaluating the cost of each move and using the **Manhattan distance** as the heuristic for efficient pathfinding.
- **Visualization**: The `matplotlib` library is used to draw the maze, show the algorithm's progress, and display the found path.

### Key Functions:
- `draw_maze()`: Displays the initial maze.
- `highlight_rect()`: Highlights the current cell being explored by the algorithm.
- `astar()`: The core function that implements the A* search algorithm.
- `draw_path()`: Visualizes the final path found by the algorithm.

Feel free to modify the maze or experiment with different start and end points. Enjoy exploring the algorithm's pathfinding process!

---

The project demonstrates the **A* pathfinding algorithm** with a **dynamic visual display** of the maze-solving process.
