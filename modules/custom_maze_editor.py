# modules/custom_maze_editor.py

class CustomMazeEditor:
    def __init__(self, canvas):
        self.canvas = canvas
        self.edit_mode = False
        self.walls = []
        self.current_line = None
        self.canvas.bind("<Button-1>", self.start_line)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.canvas.bind("<ButtonRelease-1>", self.end_line)

    def start_line(self, event):
        if self.edit_mode:
            x = self.canvas.canvasx(event.x)
            y = self.canvas.canvasy(event.y)
            self.current_line = [(x, y)]
            self.line_id = self.canvas.create_line(x, y, x, y, fill='black', width=3)

    def draw_line(self, event):
        if self.edit_mode and self.current_line:
            x = self.canvas.canvasx(event.x)
            y = self.canvas.canvasy(event.y)
            self.current_line.append((x, y))
            self.canvas.coords(self.line_id, *sum(self.current_line, ()))

    def end_line(self, event):
        if self.edit_mode and self.current_line:
            self.walls.append(self.current_line)
            self.current_line = None

    def toggle_edit_mode(self):
        self.edit_mode = not self.edit_mode

    def get_maze_lines(self):
        maze_lines = []
        for line in self.walls:
            for i in range(len(line)-1):
                maze_lines.append((line[i], line[i+1]))
        return maze_lines

    def clear(self):
        self.canvas.delete("all")
        self.walls.clear()
