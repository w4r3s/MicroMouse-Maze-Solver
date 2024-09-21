# modules/path_optimization.py

class PathOptimization:
    def __init__(self, maze):
        self.maze = maze

    def optimize_path(self, path):
        optimized_path = [path[0]]
        for i in range(2, len(path)):
            if not self.has_line_of_sight(optimized_path[-1], path[i]):
                optimized_path.append(path[i - 1])
        optimized_path.append(path[-1])
        return optimized_path

    def has_line_of_sight(self, p1, p2):
        # 实现直线是否穿过墙壁的检测
        x1, y1 = p1
        x2, y2 = p2
        # 可使用 Bresenham 算法
        # 省略具体实现
        pass
