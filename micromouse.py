import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import time
import strategies.bfs as bfs
import strategies.dfs as dfs
import strategies.astar as astar
import maps.simple_map as simple_map
import maps.complex_map as complex_map
import modules.algorithm_animation as algorithm_animation
import modules.custom_maze_editor as custom_maze_editor
import modules.weighted_maze as weighted_maze
import modules.algorithm_comparison as algorithm_comparison
import modules.algorithm_parameters as algorithm_parameters
import modules.path_optimization as path_optimization
import modules.robot_simulation as robot_simulation
import modules.maze_generation as maze_generation
import modules.views_and_themes as views_and_themes
import modules.data_export as data_export
import modules.maze_import_export as maze_import_export
import modules.dynamic_obstacles as dynamic_obstacles
import modules.intelligent_assistance as intelligent_assistant

class MicroMouseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MicroMouse Maze Solver")

        # 初始化变量
        self.map_choice = tk.StringVar(value="Simple")
        self.algorithm = tk.StringVar(value="BFS")
        self.maze_lines = []
        self.maze = None
        self.start = None
        self.end = None
        self.paths = []
        self.selected = None
        self.canvas_width = 800
        self.canvas_height = 800
        self.num_paths = tk.IntVar(value=0)
        self.selection_history = []
        self.redo_stack = []
        self.step = 5  # 默认步长

        # 模块启用状态
        self.modules_enabled = {
            'Algorithm Animation': tk.BooleanVar(value=False),
            'Custom Maze Editor': tk.BooleanVar(value=False),
            'Weighted Maze': tk.BooleanVar(value=False),
            'Algorithm Comparison': tk.BooleanVar(value=False),
            'Algorithm Parameters': tk.BooleanVar(value=False),
            'Path Optimization': tk.BooleanVar(value=False),
            'Robot Simulation': tk.BooleanVar(value=False),
            'Maze Generation': tk.BooleanVar(value=False),
            'Views and Themes': tk.BooleanVar(value=False),
            'Data Export': tk.BooleanVar(value=False),
            'Maze Import/Export': tk.BooleanVar(value=False),
            'Dynamic Obstacles': tk.BooleanVar(value=False),
            'Intelligent Assistance': tk.BooleanVar(value=False),
        }

        # 初始化模块
        self.algorithm_animator = None
        self.maze_editor = None
        self.weighted_maze = None
        self.algorithm_comparator = None
        self.algorithm_params = {}
        self.path_optimizer = None
        self.robot_simulator = None
        self.maze_generator = None
        self.theme_manager = None
        self.data_exporter = None
        self.maze_io = None
        self.dynamic_obstacles = []
        self.intelligent_assistant = None

        self.init_gui()

    def init_gui(self):
        # 创建主框架
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=1)

        # 创建菜单
        self.create_menu()

        # 创建画布框架和滚动条
        canvas_frame = tk.Frame(main_frame)
        canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.h_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.v_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL)
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas = tk.Canvas(canvas_frame, bg="white",
                                scrollregion=(0, 0, self.canvas_width, self.canvas_height),
                                xscrollcommand=self.h_scrollbar.set,
                                yscrollcommand=self.v_scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.h_scrollbar.config(command=self.canvas.xview)
        self.v_scrollbar.config(command=self.canvas.yview)

        self.canvas.bind("<Button-1>", self.select_grid)
        self.root.bind("<space>", self.confirm_selection)

        # 控制面板
        control_frame = tk.Frame(main_frame)
        control_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # 地图选择
        tk.Label(control_frame, text="选择地图:").pack(pady=5)
        tk.OptionMenu(control_frame, self.map_choice, "Simple", "Complex").pack()

        # 算法选择
        tk.Label(control_frame, text="选择算法:").pack(pady=5)
        tk.OptionMenu(control_frame, self.algorithm, "BFS", "DFS", "A*").pack()

        # 路径点数量
        tk.Label(control_frame, text="设置路径点数量:").pack(pady=5)
        self.num_paths_spinbox = tk.Spinbox(control_frame, from_=0, to=10, textvariable=self.num_paths)
        self.num_paths_spinbox.pack()

        # 加载地图按钮
        tk.Button(control_frame, text="加载地图", command=self.load_map).pack(pady=5)

        # 解决迷宫按钮
        tk.Button(control_frame, text="Solve", command=self.solve_maze).pack(pady=5)

        # 撤回、重做和清除所有点的按钮
        button_frame = tk.Frame(control_frame)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="撤回", command=self.undo).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="重做", command=self.redo).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="清除所有点", command=self.clear_all).pack(side=tk.LEFT, padx=5)

        # 模块启用/禁用
        tk.Label(control_frame, text="模块启用/禁用:").pack(pady=5)
        for module_name, var in self.modules_enabled.items():
            tk.Checkbutton(control_frame, text=module_name, variable=var, command=self.toggle_module).pack(anchor='w')

        # 状态标签
        self.status_label = tk.Label(self.root, text="请加载地图并设置路径点数量")
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def create_menu(self):
        menubar = tk.Menu(self.root)

        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="加载地图", command=self.load_map)
        if self.modules_enabled['Maze Import/Export'].get():
            file_menu.add_command(label="导入迷宫", command=self.import_maze)
            file_menu.add_command(label="导出迷宫", command=self.export_maze)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.root.quit)
        menubar.add_cascade(label="文件", menu=file_menu)

        # 编辑菜单
        if self.modules_enabled['Custom Maze Editor'].get():
            edit_menu = tk.Menu(menubar, tearoff=0)
            edit_menu.add_command(label="进入编辑模式", command=self.enter_edit_mode)
            edit_menu.add_command(label="退出编辑模式", command=self.exit_edit_mode)
            menubar.add_cascade(label="编辑", menu=edit_menu)

        # 算法菜单
        if self.modules_enabled['Algorithm Parameters'].get():
            algorithm_menu = tk.Menu(menubar, tearoff=0)
            algorithm_menu.add_command(label="算法参数调节", command=self.apply_algorithm_parameters)
            menubar.add_cascade(label="算法", menu=algorithm_menu)

        # 视图菜单
        if self.modules_enabled['Views and Themes'].get():
            view_menu = tk.Menu(menubar, tearoff=0)
            theme_submenu = tk.Menu(view_menu, tearoff=0)
            if not self.theme_manager:
                self.theme_manager = views_and_themes.ThemeManager(self.canvas)
            for theme_name in self.theme_manager.themes.keys():
                theme_submenu.add_command(label=theme_name, command=lambda tn=theme_name: self.apply_theme(tn))
            view_menu.add_cascade(label="主题", menu=theme_submenu)
            menubar.add_cascade(label="视图", menu=view_menu)

        # 帮助菜单
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="关于", command=self.show_about)
        menubar.add_cascade(label="帮助", menu=help_menu)

        self.root.config(menu=menubar)

    def toggle_module(self):
        # 根据模块启用状态更新界面元素
        self.create_menu()
        self.draw_maze()

    def apply_theme(self, theme_name):
        if self.theme_manager:
            self.theme_manager.apply_theme(theme_name)
            self.draw_maze()

    def load_map(self):
        if self.modules_enabled['Maze Generation'].get():
            self.generate_maze()
        else:
            # 从预定义地图加载
            if self.map_choice.get() == "Simple":
                self.maze_lines = simple_map.get_map()
            elif self.map_choice.get() == "Complex":
                self.maze_lines = complex_map.get_map()

        # 重置点和历史记录
        self.start = None
        self.end = None
        self.paths = []
        self.selection_history = []
        self.redo_stack = []
        self.selected = None

        self.maze = self.generate_maze_array()
        self.adjust_canvas_size()
        self.draw_maze()
        self.status_label.config(text="地图已加载，请点击画布选择起点")

    def generate_maze(self):
        # 使用迷宫生成模块生成迷宫
        self.maze_generator = maze_generation.MazeGenerator(self.canvas_width, self.canvas_height)
        self.maze_lines = self.maze_generator.generate_maze()
        difficulty = self.maze_generator.assess_difficulty(self.maze_lines)
        messagebox.showinfo("Maze Generated", f"生成了难度为 {difficulty} 的迷宫")

    def generate_maze_array(self):
        # 创建空白迷宫数组
        maze_width = int(self.canvas_width)
        maze_height = int(self.canvas_height)
        maze = [[0] * maze_width for _ in range(maze_height)]

        # 将墙壁绘制到迷宫数组中
        for (x1, y1), (x2, y2) in self.maze_lines:
            self.draw_line_on_maze(maze, x1, y1, x2, y2)

        # 如果启用了加权迷宫模块，初始化权重
        if self.modules_enabled['Weighted Maze'].get():
            self.weighted_maze = weighted_maze.WeightedMaze(maze_width, maze_height)
            # 可以在界面上设置权重

        # 如果启用了智能辅助模块
        if self.modules_enabled['Intelligent Assistance'].get():
            self.intelligent_assistant = intelligent_assistant.IntelligentAssistant(maze)

        return maze

    def draw_line_on_maze(self, maze, x1, y1, x2, y2):
        # 使用 Bresenham 算法绘制线条到迷宫数组
        x1, y1 = int(x1), int(y1)
        x2, y2 = int(x2), int(y2)
        dx = abs(x2 - x1)
        dy = -abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx + dy
        while True:
            if 0 <= x1 < self.canvas_width and 0 <= y1 < self.canvas_height:
                maze[y1][x1] = 1
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x1 += sx
            if e2 <= dx:
                err += dx
                y1 += sy

    def adjust_canvas_size(self):
        if self.maze_lines:
            max_x = max(max(line[0][0], line[1][0]) for line in self.maze_lines) + 50
            max_y = max(max(line[0][1], line[1][1]) for line in self.maze_lines) + 50
        else:
            max_x = self.canvas_width
            max_y = self.canvas_height

        self.canvas_width = max(max_x, 800)
        self.canvas_height = max(max_y, 800)

        self.canvas.config(scrollregion=(0, 0, self.canvas_width, self.canvas_height))

    def draw_maze(self):
        self.canvas.delete("all")

        # 如果启用了主题模块，获取颜色
        if self.modules_enabled['Views and Themes'].get():
            if not self.theme_manager:
                self.theme_manager = views_and_themes.ThemeManager(self.canvas)
            wall_color = self.theme_manager.get_wall_color()
        else:
            wall_color = 'black'

        # 绘制墙壁
        for (x1, y1), (x2, y2) in self.maze_lines:
            self.canvas.create_line(x1, y1, x2, y2, fill=wall_color, width=3)

        # 绘制起点、路径点和终点
        if self.start:
            x, y = self.start
            self.canvas.create_text(x, y, text="🚀", font=("Arial", 24))
        if self.paths:
            for x, y in self.paths:
                self.canvas.create_text(x, y, text="⚪", font=("Arial", 24))
        if self.end:
            x, y = self.end
            self.canvas.create_text(x, y, text="🏁", font=("Arial", 24))

        # 如果有动态障碍物，绘制它们
        if self.modules_enabled['Dynamic Obstacles'].get():
            for obstacle in self.dynamic_obstacles:
                obstacle.draw(self.canvas)

        # 如果有选中的点，高亮显示
        if self.selected:
            x, y = self.selected
            self.canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, outline="red", width=2)

    def select_grid(self, event):
        x = int(self.canvas.canvasx(event.x))
        y = int(self.canvas.canvasy(event.y))
        self.selected = (x, y)
        self.draw_maze()

        total_points = 1 + self.num_paths.get() + 1
        current_selection = len(self.selection_history) + 1

        if current_selection == 1:
            status = f"选择的点: ({x}, {y})，按空格键确认作为起点"
        elif current_selection <= total_points - 1:
            idx = current_selection - 1
            status = f"选择的点: ({x}, {y})，按空格键确认作为路径点 {idx}"
        elif current_selection == total_points:
            status = f"选择的点: ({x}, {y})，按空格键确认作为终点"
        else:
            status = "所有点已设置完毕"

        self.status_label.config(text=status)

    def confirm_selection(self, event):
        if self.selected:
            x, y = self.selected
            x, y = int(x), int(y)

            if self.modules_enabled['Intelligent Assistance'].get() and self.intelligent_assistant:
                if not self.intelligent_assistant.is_valid_point(x, y):
                    messagebox.showwarning("Invalid Point", "选择的点在墙壁上或不可到达区域，请重新选择")
                    return

            total_points = 1 + self.num_paths.get() + 1
            if len(self.selection_history) < total_points:
                self.selection_history.append((x, y))
                self.redo_stack.clear()
                self.update_points()
                self.selected = None
                self.draw_maze()
                self.update_status()
            else:
                self.status_label.config(text="所有点已设置完毕，无法再添加")
        else:
            self.status_label.config(text="请先点击选择一个点")

    def update_points(self):
        total_points = 1 + self.num_paths.get() + 1
        points = self.selection_history[:total_points]

        if len(points) >= 1:
            self.start = points[0]
        if len(points) >= 2 + self.num_paths.get():
            self.end = points[-1]
        else:
            self.end = None

        self.paths = points[1:-1] if len(points) > 2 else []

    def update_status(self):
        total_points = 1 + self.num_paths.get() + 1
        current_selection = len(self.selection_history) + 1

        if current_selection == 1:
            status = "请点击选择起点"
        elif current_selection <= total_points - 1:
            idx = current_selection - 1
            status = f"请点击选择路径点 {idx}"
        elif current_selection == total_points:
            status = "请点击选择终点"
        else:
            status = "所有点已设置完毕"

        self.status_label.config(text=status)

    def solve_maze(self):
        if not self.start or not self.end:
            messagebox.showwarning("Input Error", "请设置起点和终点!")
            return

        # 检查点是否合法
        if self.maze[self.start[1]][self.start[0]] == 1:
            messagebox.showwarning("Input Error", "起点在墙壁上!")
            return
        if self.maze[self.end[1]][self.end[0]] == 1:
            messagebox.showwarning("Input Error", "终点在墙壁上!")
            return
        for idx, (x, y) in enumerate(self.paths):
            if self.maze[y][x] == 1:
                messagebox.showwarning("Input Error", f"路径点 {idx+1} 在墙壁上!")
                return

        # 对齐到步长网格
        def align_point(p):
            x = (p[0] // self.step) * self.step
            y = (p[1] // self.step) * self.step
            return (x, y)

        start_pos = align_point(self.start)
        end_pos = align_point(self.end)
        path_positions = [align_point(p) for p in self.paths]

        self.draw_maze()

        # 开始求解
        algo = self.algorithm.get()
        path = None

        # 算法参数
        params = {}
        if self.modules_enabled['Algorithm Parameters'].get():
            # 从用户输入获取参数
            params = self.algorithm_params.get(algo, {})

        # 如果启用了算法比较模块
        if self.modules_enabled['Algorithm Comparison'].get():
            self.algorithm_comparator = algorithm_comparison.AlgorithmComparison({
                'BFS': bfs.solve_with_waypoints,
                'DFS': dfs.solve_with_waypoints,
                'A*': astar.solve_with_waypoints
            })
            results = self.algorithm_comparator.compare(self.maze, start_pos, path_positions, end_pos, self.step)
            self.show_algorithm_comparison_results(results)
            return

        # 带动画的求解
        if self.modules_enabled['Algorithm Animation'].get():
            if algo == "BFS":
                generator = bfs.solve_with_animation(self.maze, start_pos, end_pos, self.step, **params)
            elif algo == "DFS":
                generator = dfs.solve_with_animation(self.maze, start_pos, end_pos, self.step, **params)
            elif algo == "A*":
                generator = astar.solve_with_animation(self.maze, start_pos, end_pos, self.step, **params)
            self.algorithm_animator = algorithm_animation.AlgorithmAnimation(self.canvas, self.maze)
            self.algorithm_animator.animate_algorithm(generator)
            return

        # 普通求解
        start_time = time.time()
        if algo == "BFS":
            path = bfs.solve_with_waypoints(self.maze, start_pos, path_positions, end_pos, self.step, **params)
        elif algo == "DFS":
            path = dfs.solve_with_waypoints(self.maze, start_pos, path_positions, end_pos, self.step, **params)
        elif algo == "A*":
            path = astar.solve_with_waypoints(self.maze, start_pos, path_positions, end_pos, self.step, **params)
        end_time = time.time()
        if path:
            if self.modules_enabled['Path Optimization'].get():
                self.path_optimizer = path_optimization.PathOptimization(self.maze)
                path = self.path_optimizer.optimize_path(path)
            self.draw_path(path)
            if self.modules_enabled['Robot Simulation'].get():
                self.start_robot_simulation(path)
            messagebox.showinfo("Result", f"使用 {algo} 算法解决迷宫，耗时 {round(end_time - start_time, 4)} 秒。")
            if self.modules_enabled['Data Export'].get():
                # 导出数据
                self.data_exporter = data_export.DataExporter()
                self.data_exporter.export_results({algo: {'path': path, 'time': end_time - start_time, 'length': len(path)}}, 'results.csv')
        else:
            messagebox.showinfo("Result", "未找到路径。")

    def draw_path(self, path):
        # 绘制路径
        if len(path) > 1:
            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

    # 其他模块的附加方法（如导入/导出迷宫，进入/退出编辑模式等）

    def import_maze(self):
        filename = filedialog.askopenfilename(title="导入迷宫", filetypes=[("JSON Files", "*.json")])
        if filename:
            self.maze_io = maze_import_export.MazeIO()
            self.maze_lines = self.maze_io.load_maze(filename)
            self.load_map_from_maze_lines()

    def export_maze(self):
        filename = filedialog.asksaveasfilename(title="导出迷宫", defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if filename:
            self.maze_io = maze_import_export.MazeIO()
            self.maze_io.save_maze(self.maze_lines, filename)
            messagebox.showinfo("导出成功", f"迷宫已导出到 {filename}")

    def load_map_from_maze_lines(self):
        # 重置起点、终点、路径等
        self.start = None
        self.end = None
        self.paths = []
        self.selection_history = []
        self.redo_stack = []
        self.selected = None

        self.maze = self.generate_maze_array()
        self.adjust_canvas_size()
        self.draw_maze()
        self.status_label.config(text="迷宫已加载，请点击画布选择起点")

    def enter_edit_mode(self):
        if not self.maze_editor:
            self.maze_editor = custom_maze_editor.CustomMazeEditor(self.canvas)
        self.maze_editor.toggle_edit_mode()
        self.status_label.config(text="进入编辑模式：在画布上绘制或删除墙壁")

    def exit_edit_mode(self):
        if self.maze_editor:
            self.maze_editor.toggle_edit_mode()
            self.maze_lines = self.maze_editor.get_maze_lines()
            self.maze = self.generate_maze_array()
            self.draw_maze()
            self.status_label.config(text="退出编辑模式")
            self.maze_editor = None

    # 添加撤回、重做、清除所有点的功能

    def undo(self):
        if self.selection_history:
            point = self.selection_history.pop()
            self.redo_stack.append(point)
            self.update_points()
            self.draw_maze()
            self.update_status()
        else:
            self.status_label.config(text="没有可撤回的操作")

    def redo(self):
        if self.redo_stack:
            point = self.redo_stack.pop()
            self.selection_history.append(point)
            self.update_points()
            self.draw_maze()
            self.update_status()
        else:
            self.status_label.config(text="没有可重做的操作")

    def clear_all(self):
        self.selection_history.clear()
        self.redo_stack.clear()
        self.start = None
        self.end = None
        self.paths = []
        self.selected = None
        self.draw_maze()
        self.status_label.config(text="所有点已清除，请重新选择起点")

    # 添加其他可能需要的方法

    def apply_algorithm_parameters(self):
        # 如果启用了算法参数调节模块
        if self.modules_enabled['Algorithm Parameters'].get():
            # 弹出一个窗口供用户设置参数
            params_window = tk.Toplevel(self.root)
            params_window.title("算法参数调节")

            tk.Label(params_window, text=f"设置 {self.algorithm.get()} 算法参数").pack(pady=5)

            if self.algorithm.get() == "A*":
                # A*算法的参数，如启发式函数
                heuristic_var = tk.StringVar(value="曼哈顿距离")
                tk.Label(params_window, text="启发式函数：").pack()
                heuristic_menu = tk.OptionMenu(params_window, heuristic_var, "曼哈顿距离", "欧几里得距离")
                heuristic_menu.pack()

                def save_params():
                    self.algorithm_params[self.algorithm.get()] = {'heuristic': heuristic_var.get()}
                    params_window.destroy()

                tk.Button(params_window, text="保存参数", command=save_params).pack(pady=10)
            else:
                tk.Label(params_window, text="该算法没有可调参数").pack(pady=10)
                tk.Button(params_window, text="关闭", command=params_window.destroy).pack(pady=5)

    def start_robot_simulation(self, path):
        if self.modules_enabled['Robot Simulation'].get():
            self.robot_simulator = robot_simulation.RobotSimulation(self.canvas, path)
            self.robot_simulator.start_simulation()

    def add_dynamic_obstacle(self):
        # 添加动态障碍物
        if self.modules_enabled['Dynamic Obstacles'].get():
            obstacle_path = [...]  # 定义障碍物的移动路径
            obstacle = dynamic_obstacles.DynamicObstacle(self.canvas, obstacle_path)
            self.dynamic_obstacles.append(obstacle)
            obstacle.start_moving()

    # 更新状态栏
    def update_status(self):
        total_points = 1 + self.num_paths.get() + 1  # 起点 + 路径点数量 + 终点
        current_selection = len(self.selection_history) + 1

        if current_selection == 1:
            status = "请点击选择起点"
        elif current_selection <= total_points - 1:
            idx = current_selection - 1
            status = f"请点击选择路径点 {idx}"
        elif current_selection == total_points:
            status = "请点击选择终点"
        else:
            status = "所有点已设置完毕"

        self.status_label.config(text=status)



    # 添加算法比较结果显示
    def show_algorithm_comparison_results(self, results):
        result_text = ""
        for alg, data in results.items():
            result_text += f"{alg} - Time: {data['time']:.4f}s, Path Length: {data['length']}\n"
        messagebox.showinfo("Algorithm Comparison Results", result_text)

    # 运行程序
if __name__ == "__main__":
    root = tk.Tk()
    app = MicroMouseApp(root)
    root.mainloop()
