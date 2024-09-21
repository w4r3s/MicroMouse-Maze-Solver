# modules/dynamic_obstacles.py

class DynamicObstacle:
    def __init__(self, canvas, path):
        self.canvas = canvas
        self.path = path
        self.index = 0
        self.obstacle_icon = None

    def start_moving(self):
        self.move_obstacle()

    def move_obstacle(self):
        if self.index < len(self.path):
            x, y = self.path[self.index]
            if self.obstacle_icon:
                self.canvas.coords(self.obstacle_icon, x-5, y-5, x+5, y+5)
            else:
                self.obstacle_icon = self.canvas.create_rectangle(
                    x-5, y-5, x+5, y+5, fill='red'
                )
            self.index += 1
            self.canvas.after(200, self.move_obstacle)
