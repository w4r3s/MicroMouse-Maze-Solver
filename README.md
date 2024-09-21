### MicroMouse-Maze-Solver

<img width="1214" alt="Snipaste_2024-09-21_18-16-07" src="https://github.com/user-attachments/assets/b4cb13ca-5367-49c4-a00d-84fbef516ad9">

#### Languages

[中文](https://github.com/w4r3s/MicroMouse-Maze-Solver/blob/main/readme_cn.md)

#### Introduction

MicroMouse Maze Solver is an interactive application designed to solve maze problems. The program supports multiple algorithms and functional modules, allowing users to load or create mazes, set start points, end points, and waypoints, and find the optimal path using different algorithms. Users can also enable or disable various functional modules to customize the program's behavior.

#### Features
* Maze Loading and Generation: Supports loading predefined simple and complex mazes, as well as automatically generating mazes using the maze generator.

* Algorithm Selection: Provides BFS, DFS, and A* algorithms for selection.

* Waypoint Setting: Allows users to set multiple waypoints in the maze, and the algorithm will pass through these points in order.

* Modular Design: Supports enabling or disabling the following functional modules:

* Algorithm Animation: Animates the search process of the algorithm.

* Custom Maze Editor: A custom maze editor that allows users to draw or modify the maze.

* Weighted Maze: Supports weighted mazes, setting different weights for different areas.

* Algorithm Comparison: Compares the performance of different algorithms, including time and path length.

* Algorithm Parameters: Adjusts algorithm parameters, such as the heuristic function for the A* algorithm.

* Path Optimization: Optimizes the found path to reduce its length.

* Robot Simulation: Simulates a robot moving along the path in the maze.

* Maze Generation: Automatically generates mazes and evaluates their difficulty.

* Views and Themes: Changes the visual theme and style of the maze.

* Data Export: Exports algorithm results and path data to files.

* Maze Import/Export: Imports and exports maze data for easy sharing and saving.

* Dynamic Obstacles: Adds dynamic obstacles to the maze to increase challenge.

* Intelligent Assistance: Provides intelligent assistance to prevent selecting invalid start, end, or waypoint positions.


#### Usage

Launch the Program: Run the micromouse.py file to start the application.

**Select Map and Algorithm:**

In the control panel, select the predefined Simple or Complex map, or enable the Maze Generation module to generate a random maze.
Choose the algorithm to use: BFS, DFS, or A*.

Set the Number of Waypoints: Adjust the Set Number of Waypoints to determine how many waypoints to add in the maze.

**Load the Map:**

Click the Load Map button to load the selected maze onto the canvas.

**Select Start Point, Waypoints, and End Point:**

Click on the canvas to select points; the currently selected point is highlighted with a red box.
Press the spacebar to confirm the selection, and follow the prompts to set the start point, waypoints, and end point sequentially.

**Enable/Disable Modules:**

In the Module Enable/Disable section of the control panel, check or uncheck module names to enable or disable corresponding features.
Solve the Maze:

Click the Solve button, and the program will solve the maze using the selected algorithm and enabled modules.

If Algorithm Animation is enabled, the algorithm's search process will be displayed as an animation.

If Algorithm Comparison is enabled, the comparison results of different algorithms will be shown.

#### Other Features:

Undo/Redo/Clear: Use the Undo, Redo, and Clear All Points buttons to manage the selected points.

Custom Maze Editing: After enabling the Custom Maze Editor module, you can enter edit mode to manually draw or modify the maze.

Import/Export Maze: After enabling the Maze Import/Export module, you can import mazes from files or export the current maze.

#### Dependencies

Python 3.x
Tkinter library (usually comes with Python)

#### Run Example
```
python micromouse.py
```
