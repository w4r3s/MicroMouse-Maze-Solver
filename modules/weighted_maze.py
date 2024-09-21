# modules/weighted_maze.py

class WeightedMaze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.weights = [[1 for _ in range(width)] for _ in range(height)]

    def set_weight(self, x, y, weight):
        self.weights[y][x] = weight

    def get_weight(self, x, y):
        return self.weights[y][x]
