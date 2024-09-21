### MicroMouse Maze Solver

<img width="1214" alt="Snipaste_2024-09-21_18-16-07" src="https://github.com/user-attachments/assets/467c2c75-0892-4dc9-b664-beac99636742">


#### 简介
MicroMouse Maze Solver 是一个用于解决迷宫问题的交互式应用程序。该程序支持多种算法和功能模块，允许用户加载或创建迷宫，设置起点、终点和路径点，并通过不同的算法找到最优路径。用户还可以启用或禁用各种功能模块，以定制程序的行为。

#### 功能特性
* 迷宫加载和生成：支持加载预定义的简单和复杂迷宫，以及通过迷宫生成器自动生成迷宫。

* 算法选择：提供 BFS、DFS 和 A* 算法，可根据需要选择。

* 路径点设置：允许用户在迷宫中设置多个路径点，算法将按顺序经过这些点。

* 模块化设计：支持启用或禁用以下功能模块：

* - Algorithm Animation：动画展示算法的搜索过程。
* - Custom Maze Editor：自定义迷宫编辑器，允许用户绘制或修改迷宫。
* - Weighted Maze：支持加权迷宫，设置不同区域的权重。
* - Algorithm Comparison：比较不同算法的性能，包括时间和路径长度。
* - Algorithm Parameters：调整算法参数，如 A* 算法的启发式函数。
* - Path Optimization：对找到的路径进行优化，减少路径长度。
* - Robot Simulation：模拟机器人在迷宫中沿路径移动。
* - Maze Generation：自动生成迷宫，并评估其难度。
* - Views and Themes：更改迷宫的视觉主题和风格。
* - Data Export：将算法结果和路径数据导出为文件。
* - Maze Import/Export：导入和导出迷宫数据，方便共享和保存。
* - Dynamic Obstacles：在迷宫中添加动态障碍物，增加挑战性。
* - Intelligent Assistance：智能辅助，防止选择无效的起点、终点或路径点。
  - 
#### 使用方法
启动程序：运行 micromouse.py 文件启动应用程序。


**选择地图和算法：**

在控制面板中，选择预定义的 Simple 或 Complex 地图，或启用 Maze Generation 模块以生成随机迷宫。

选择要使用的算法：BFS、DFS 或 A*。

设置路径点数量：通过调整 设置路径点数量，确定要在迷宫中添加的路径点数目。


**加载地图：**

点击 加载地图 按钮，将所选迷宫加载到画布中。

**选择起点、路径点和终点：**

在画布上点击以选择点，当前选中的点会以红色方框高亮显示。

按下空格键确认选择，按照提示依次设置起点、路径点和终点。

**启用/禁用模块：**

在控制面板的 模块启用/禁用 部分，勾选或取消勾选模块名称以启用或禁用对应功能。
解决迷宫：

点击 Solve 按钮，程序将使用选定的算法和启用的模块来解决迷宫。

如果启用了 Algorithm Animation，将以动画形式展示算法的搜索过程。

如果启用了 Algorithm Comparison，将显示不同算法的比较结果。

#### 其他功能：

* 撤回/重做/清除：使用 撤回、重做 和 清除所有点 按钮来管理已选择的点。
* 自定义迷宫编辑：启用 Custom Maze Editor 模块后，可以进入编辑模式，手动绘制或修改迷宫。
* 导入/导出迷宫：启用 Maze Import/Export 模块后，可以从文件导入迷宫或将当前迷宫导出。

#### 依赖项
Python 3.x

Tkinter 库（通常随 Python 一起安装）

#### 运行示例
```
python micromouse.py
```
