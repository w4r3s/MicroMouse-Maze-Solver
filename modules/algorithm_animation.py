# modules/algorithm_animation.py

import tkinter as tk

class AlgorithmAnimation:
    def __init__(self, canvas, maze):
        self.canvas = canvas
        self.maze = maze
        self.visited_nodes = set()
        self.animation_delay = 50  # 动画延迟，单位毫秒

    def animate_algorithm(self, algorithm_generator):
        try:
            result = next(algorithm_generator)
            if result:
                path, visited = result
                # 绘制访问过的节点
                self.draw_visited(visited)
                # 如果找到路径，绘制路径
                if path:
                    self.draw_path(path)
                else:
                    # 继续动画
                    self.canvas.after(self.animation_delay, lambda: self.animate_algorithm(algorithm_generator))
            else:
                # 未找到路径，继续动画
                self.canvas.after(self.animation_delay, lambda: self.animate_algorithm(algorithm_generator))
        except StopIteration:
            pass  # 动画结束

    def draw_visited(self, visited):
        new_nodes = visited - self.visited_nodes
        for x, y in new_nodes:
            self.canvas.create_rectangle(x, y, x + 1, y + 1, fill='blue', outline='')
        self.visited_nodes.update(new_nodes)

    def draw_path(self, path):
        if len(path) > 1:
            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2)
