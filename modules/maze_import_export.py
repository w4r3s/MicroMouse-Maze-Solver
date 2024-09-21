# modules/maze_import_export.py

import json

class MazeIO:
    def save_maze(self, maze_lines, filename):
        with open(filename, 'w') as f:
            json.dump(maze_lines, f)

    def load_maze(self, filename):
        with open(filename, 'r') as f:
            maze_lines = json.load(f)
        return maze_lines
