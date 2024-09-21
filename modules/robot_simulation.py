# modules/robot_simulation.py

class RobotSimulation:
    def __init__(self, canvas, path):
        self.canvas = canvas
        self.path = path
        self.index = 0
        self.robot_icon = None

    def start_simulation(self):
        if self.path and len(self.path) > 1:
            self.move_robot()

    def move_robot(self):
        if self.index < len(self.path):
            x, y = self.path[self.index]
            if self.robot_icon:
                self.canvas.coords(self.robot_icon, x-5, y-5, x+5, y+5)
            else:
                self.robot_icon = self.canvas.create_oval(
                    x-5, y-5, x+5, y+5, fill='green'
                )
            self.index += 1
            self.canvas.after(100, self.move_robot)
